from django.db import models

# Create your models here.

class Options(models.Model):
    server_url = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "options"
