from django.db import models
from core import models as core_models
from django_countries.fields import CountryField
from users import models as user_models

# Create your models here.


class AbstractItem(core_models.TimeStampedModel):
    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Amenity(AbstractItem):
    """ Amenity Object Definition """

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    """ Facility Model Definition """

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    """ HouseRule Model Definition """

    class Meta:
        verbose_name = "House Rule"


class RoomType(AbstractItem):
    """ RoomType Object Definition """

    class Meta:
        verbose_name = "Room Type"
        ordering = ["created"]


class Photo(core_models.TimeStampedModel):
    """ Photo Model Definition """

    caption = models.CharField(max_length=140)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):

    """ Room Model Definition """

    name = models.CharField(max_length=40)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    adress = models.CharField(max_length=140)
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    instant_book = models.BooleanField(default=False)

    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    # host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room_type = models.ForeignKey(
        "RoomType", blank=True, on_delete=models.SET_NULL, null=True
    )
    amenities = models.ManyToManyField("Amenity", blank=True)
    facilities = models.ManyToManyField("Facility", blank=True)
    house_rules = models.ManyToManyField("HouseRule", blank=True)
