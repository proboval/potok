import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from users.models import *
from .models import *
from django.db.models import Q
from PIL import Image
import pydicom
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import numpy as np


def researchsShowView(request):
    user = request.user

    try:
        reserchs = user.research.filter(Q(Verdict=False) | Q(Description=''))
        user_type = 'Doctor'
    except AttributeError:
        reserchs = Research.objects.filter(~Q(Verdict=False) & ~Q(Description=''))
        user_type = 'Expert'

    print(reserchs)
    context = {'user': user, 'reserchs': reserchs, 'user_type': user_type}

    return render(request, 'threadPrediction/researchsShow.html', context=context)


def dicom2png(dicom_file):
    dicom_data = pydicom.dcmread(dicom_file)
    pixel_array = dicom_data.pixel_array

    # Normalize pixel array to range 0-255
    pixel_array = ((pixel_array - np.min(pixel_array)) / (np.max(pixel_array) - np.min(pixel_array)) * 255).astype(np.uint8)

    image = Image.fromarray(pixel_array)
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    buffered.seek(0)
    return buffered


def addResearch(request):
    if request.method == 'POST':
        researchId = Research.objects.all().count() + 1
        research = Research(Name=f'Исследование{researchId}')
        research.save()

        doctor = request.user

        doctor.research.add(research)

        files = request.FILES.getlist('file')

        for file in files:
            imageName = file.name.replace('.dcm', '.png')

            img_buffer = dicom2png(file)
            img_file = InMemoryUploadedFile(img_buffer, None, imageName, 'image/png', img_buffer.getbuffer().nbytes,
                                            None)

            newImage = HeadMRI(Name=imageName, Image=img_file, research=research)
            newImage.save()

        return redirect(reverse('threadPrediction:research'))

    return render(request, 'threadPrediction/addResearch.html')


@csrf_exempt
def showResearch(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        role = data.get('role')

        researchId = data.get('researchPk')
        research = Research.objects.get(pk=researchId)

        if role == 'Doctor':
            description = data.get('text')
            print()
            research.Description = description
            research.Verdict = None
            research.save()
        else:
            verdict = data.get('verdict')

            research.Verdict = verdict
            research.save()

        return redirect(reverse('threadPrediction:research'))
    elif request.method == 'GET':
        researchPk = request.GET.get('researchId')
        role = request.GET.get('role')
        research = Research.objects.get(pk=researchPk)
        headMRIs = research.MRIs.all()
        description = ('Поступил в диагностику с жалобами на ___.\n' + '\n' +
                       'При проведении магнитно-резонансной томографии ГМ было выявлено * патологических изменения: ___.\n' + '\n' +
                        'Данные патологические изменения могут быть проявлением следующих патологических процессов: MP-картина образования в ___, сопровождающегося ___ выраженным перифокальным отёком' +
                        'органической патологии.\n' + '\n' +
                        'Морфология образования в ___ характерна для осложнения ___ в виде ___  (на момент исследования в ___ фазе).\n' + '\n' +
                        'Анамнез: ___.')
        context = {'research': research, 'headMRIs': headMRIs, 'role': role, 'description': description}

        return render(request, 'threadPrediction/showResearch.html', context=context)
