from django.contrib import admin
from .models import Sudoku


# Register your models here.
# This is where you register the models you created in the models.py file so that they can be viewed in the admin page.
admin.site.register(Sudoku)