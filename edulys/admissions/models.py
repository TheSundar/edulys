from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Address(models.Model):
    address1 = models.CharField(max_length=1000)
    address2 = models.CharField(max_length=1000, null=True, blank=True)
    city = models.CharField(max_length=1000)
    state = models.CharField(max_length=1000)
    pincode = models.CharField(max_length=1000)

    def __str__(self):
        return self.address1 + ',' + self.city


class AllImages(models.Model):
    image = models.ImageField(upload_to='static/images')


class School(models.Model):
    name = models.CharField(max_length=1000)
    school_pricipal = models.CharField(max_length=1000)
    address = models.ForeignKey(Address)
    logo = models.ImageField(upload_to='static/images',null=True, blank=True)
    images = models.ManyToManyField(AllImages, null=True, blank=True)

    def __str__(self):
        return self.name + ' ,' + self.address.__str__()


class Sylabuss(models.Model):
    name = models.CharField(max_length=100)
    school = models.ForeignKey(School)
    def __str__(self):
        return  self.name


class SchoolClass(models.Model):
    name = models.CharField(max_length=100)
    school = models.ForeignKey(School)

    def __str__(self):
        return  self.name


class ClassFee(models.Model):
    from_class = models.ForeignKey(SchoolClass, related_name='From')
    to_class = models.ForeignKey(SchoolClass, related_name='to', null=True, blank=True)
    amount = models.PositiveIntegerField()
    sylabus = models.ForeignKey(Sylabuss)

