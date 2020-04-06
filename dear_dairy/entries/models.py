from django.db import models

# Create your models here.

class Entries(models.Model):
    title=models.CharField(max_length=50)
    text=models.TextField(max_length=500)
    name=models.CharField(max_length=20)
    date=models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural='entries'
