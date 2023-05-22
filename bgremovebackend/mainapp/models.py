from django.db import models

class imageStorageModel(models.Model):
    name = models.CharField(max_length=10000)
    uploaded_image = models.ImageField(upload_to='uploads/')
    downloaded_image = models.ImageField(upload_to='downloads/')
