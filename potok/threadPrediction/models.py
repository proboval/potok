from django.db import models


class Research(models.Model):
    Name = models.CharField(
        max_length=50
    )
    Description = models.TextField()
    Verdict = models.BooleanField(
        null=True
    )


class HeadMRI(models.Model):
    Name = models.CharField(
        max_length=50
    )
    Image = models.ImageField(
        upload_to='images/MRI/'
    )
    research = models.ForeignKey(
        'Research',
        on_delete=models.CASCADE,
        related_name='MRIs'
    )

    def __str__(self):
        return self.Name


class MRIMask(models.Model):
    Name = models.CharField(
        max_length=50
    )
    Image = models.ImageField(
        upload_to='images/Masks/'
    )
    headMRI = models.OneToOneField(
        'HeadMRI',
        on_delete=models.CASCADE,
        related_name='Mask',
        blank=True
    )

    def __str__(self):
        return self.Name
