from django.db import models

class Person(models.Model):
  name = models.CharField(max_length=100)

class Gift(models.Model):
  gift = models.CharField(max_length=100)

class GiftToPerson(models.Model):
  person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
  gift_id = models.ForeignKey(Gift, on_delete=models.CASCADE)
  purchased = models.BooleanField(default = False)