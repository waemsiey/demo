from django.db import models

# Create your models here.
#This is a model name TodoItems | This acts as entity for a table in the database
class TodoItems(models.Model):

    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

#If I plan to saves the csv/uploaded file in a db i should declare its attr
# class CSVUploadedFiles(models.Model):
    