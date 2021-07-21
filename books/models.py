from django.db import models

class PublishingHouse(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ManyToManyField(to=Author, related_name='author')
    publishing_year =models.DateField()
    publushing_house = models.ForeignKey(to='PublishingHouse', on_delete=models.PROTECT)
    pages = models.IntegerField()

    def __str__(self):
        return self.title