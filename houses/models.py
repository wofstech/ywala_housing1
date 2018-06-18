from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime

  

class Myhouses(models.Model):
    
    Available = 'A'
    Not_Available = 'NA'
    Availability = (
        (Available, 'Available'),
        (Not_Available, 'Not_Available'),
    )

    Flat = 'Flat'
    Self_contained = 'Self Contain'
    Bungalow = 'Bungalow'
    Mini_flat = 'Mini Flat'
    Duplex = 'Duplex'
    Room = (
        (Flat, 'Flat'),
        (Self_contained, 'Self_contained'),
        (Bungalow, 'Bungalow'),
        (Mini_flat, 'Mini_flat'),
        (Duplex, 'Duplex'),
    )

    time = models.DateTimeField(default = datetime.now, blank = True)
    name_of_accomodation = models.CharField(max_length=20)
    type_of_apartment = models.CharField(max_length=20, choices=Room, )
    Number_of_rooms = house_rent = models.IntegerField()
    house_rent = models.IntegerField()
    availability = models.CharField(max_length=2, choices=Availability, default=Available,)
    location = models.CharField(max_length=200)
    nearest_institution = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    house_image = models.ImageField()
    house_image2 = models.ImageField()
    house_image3 = models.ImageField()
    house_image4 = models.ImageField()
    house_image5 = models.ImageField()
    house_image6 = models.ImageField()
    house_image7 = models.ImageField( null=True, blank=True,)
    house_image8 = models.ImageField( null=True, blank=True,)
    house_image9 = models.ImageField( null=True, blank=True,)
    house_image10 = models.ImageField( null=True, blank=True,)
    house_image11 = models.ImageField( null=True, blank=True,)
    house_image12 = models.ImageField( null=True, blank=True,)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='author')

    def __str__(self):
        return self.name_of_accomodation

    def get_absolute_url(self):
        return reverse('search-detail', args=[str(self.id)])

    class Meta:
        ordering = ["-time"]


    