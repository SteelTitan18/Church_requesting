from django.db import models
from datetime import *
from taggit.managers import TaggableManager


class Church (models.Model):
    name = models.fields.CharField(verbose_name="Nom ", max_length=100)
    status = models.fields.CharField(verbose_name="Status", max_length=30, choices=[('top', 'Paroisse'),
    ('second', 'Station secondaire')])
    archdiocese = models.fields.CharField(verbose_name="Archidiocèse ", max_length=30)
    priest = models.fields.CharField(verbose_name="Curé ", max_length=100)
    mother_parish = models.fields.CharField(verbose_name="Curé ", max_length=100, blank=True, null=True)

class Church_request(models.Model):
    customer = models.fields.CharField(verbose_name="Demandée par " ,max_length=30)
    request = models.fields.TextField(verbose_name="Intention (Veuillez être clair, précis et bref)\n", max_length=200)
    type_choices = models.fields.CharField(verbose_name="Type de messe ", max_length=30, choices=[('solo', 'Unique'),
                                                    ('trio', 'Tridium'),
                                                    ('nine', 'Neuvaine'),
                                                    ('month', 'Trentaine')])
    hours = models.fields.CharField(verbose_name="Horaires ", max_length=255)
    start_date = models.fields.DateField(verbose_name="Date de début ", default=date.today)
    end_date = models.fields.DateField(verbose_name="Date de fin ", blank=True, null=True)
    church = models.ForeignKey(Church, on_delete=models.CASCADE, related_name="church")

    def __str__(self):
        return f'{self.content}'

class Suggestion(models.Model):
    content = models.fields.CharField(verbose_name="Contenu ", max_length=200)
    church = models.ForeignKey(Church, on_delete=models.CASCADE, related_name="request.Suggestion.church+")
    tags = TaggableManager()

class Announcement(models.Model):
    title = models.fields.CharField(verbose_name="Contenu ", max_length=50)
    content = models.fields.CharField(verbose_name="Contenu ", max_length=200)
    illustration = models.ImageField(default=None, blank=True, null=True, upload_to='images/illustrations/%Y/%m/%d/')
    church = models.ForeignKey(Church, on_delete=models.CASCADE, related_name="request.Announcement.church+")
