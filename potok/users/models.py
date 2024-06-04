from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from threadPrediction.models import Research
from django.contrib.auth.hashers import make_password


class DoctorManager(BaseUserManager):
    def create_user(self, email, lastName, firstName, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        doctor = self.model(email=email, lastName=lastName, firstName=firstName, **extra_fields)
        doctor.set_password(password)
        doctor.save(using=self._db)
        return doctor


class Doctor(AbstractBaseUser):
    email = models.EmailField(unique=True)
    lastName = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    research = models.ManyToManyField(Research, blank=True)

    is_active = models.BooleanField(default=True)

    objects = DoctorManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['lastName', 'firstName']

    def __str__(self):
        return f'{self.lastName} {self.firstName}'

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)


class ExpertManager(BaseUserManager):
    def create_user(self, email, lastName, firstName, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        expert = self.model(email=email, lastName=lastName, firstName=firstName, **extra_fields)
        expert.set_password(password)
        expert.save(using=self._db)
        return expert


class Expert(AbstractBaseUser):
    email = models.EmailField(unique=True)
    lastName = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)

    objects = ExpertManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['lastName', 'firstName']

    def __str__(self):
        return f'{self.lastName} {self.firstName}'

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
