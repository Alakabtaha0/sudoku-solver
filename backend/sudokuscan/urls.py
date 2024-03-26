from django.urls import path
from . import views

# View simply means the function that receives a web request and returns a web response.
# Another name for view is a request handler.
urlpatterns = [
    path('', views.index, name='index'),
]