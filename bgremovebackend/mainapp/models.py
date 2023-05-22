from django.db import models

class imageStorageModel(models.Model):

    uploaded_image = models.ImageField(upload_to='uploads/')
    downloaded_image = models.ImageField(upload_to='downloads/', blank=True)
