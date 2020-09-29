from django.db import models

# Create your models here.
class example_models(models.Model):
    img = models.ImageField(upload_to='pics')
    photo_choice = (
        ('wed', 'wedding'),
        ('Fash', 'fashion'),
         ('mag', 'magazine'),
        ('pot', 'potrait'),
    )
    pho_type = models.CharField(max_length=10 ,choices = photo_choice)
