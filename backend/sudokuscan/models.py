from django.db import models
from django.utils import timezone as tz
import datetime as dt


# Create your models here.
# This is where you define the database schema for the Django app.
# The class is the table name
# The variables are what the column name would be
# The variable values are the column types
# They need to be imported from django.db.models and is like the data types in SQL
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

# python3 manage.py migrate creates new tables in the database
# python3 manage.py makemigrations creates new migrations based on the changes you made to the models

class Sudoku(models.Model):
    # Creating a custom method to return accurate string representation of the model
    def __str__(self):
        return self.name
    
    def was_published_recently(self):
        return self.date_created >= tz.now() - dt.timedelta(days=1)

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')
    puzzle = models.JSONField(max_length=81, default=dict)
    solution = models.JSONField(max_length=81, default=dict)
    date_created = models.DateTimeField(auto_now_add=True, editable=False, blank=False, null=False)
    date_modified = models.DateTimeField(auto_now=True, editable=False, blank=False, null=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
