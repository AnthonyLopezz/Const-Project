from django.db import models

# Create your models here.


class Cover(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to="Cover")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "cover"
        verbose_name_plural = "covers"