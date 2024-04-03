from django.urls import path
from . import views

# View simply means the function that receives a web request and returns a web response.
# Another name for view is a request handler.

# Need to add app_name to differentiate between the same name of the view in different apps.
# You could have the same view name in different apps.
app_name='sudokuscan'
urlpatterns = [
    path('', views.read_puzzle, name='read_puzzle'),
]