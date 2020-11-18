from django.db import models

# Create your models here.

class Ocr712(models.Model):
    # description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/',blank=True, null=True)
    # uploaded_at = models.DateTimeField(auto_now_add=True)