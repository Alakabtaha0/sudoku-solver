# from django.shortcuts import render
from django.http import HttpResponse
from .models import Sudoku
from business_logic.process_image import process_image
import json

# Create your views here. AKA Routes
# CRUD operations

# Create i.e. read info from the data provided (image processing)
def read_puzzle(request):
    if request.method == 'POST':
        # Get the image file from the request
        image = request.FILES.get('image')

        if image is None:
            return HttpResponse(content='No image provided', status=400)
        # Create a new Sudoku object
        sudoku = Sudoku(image=image)

        # Save the object to the database
        sudoku.save()

        # process the image and save the returned class to an object
        processed_image = process_image(sudoku.image.path)

        # Get the grid from the processed image
        grid = processed_image.return_grid()

        # Return the puzzle to the user
        return HttpResponse(content=grid, status=201)    


# Implement the asynchronous request-reply pattern.
# The below is a simple example of this, implement a more complex version of this.
    
# def start_task(request):
#     # Start the long-running task in a separate thread
#     Thread(target=long_running_task).start()
#     # Respond with a 202 Accepted status code and the status URL
#     return JsonResponse({'status_url': '/status/'}, status=202)

# def long_running_task():
#     # This function does the long-running task
#     pass

# def check_status(request):
#     # This view returns the status of the long-running task
#     if task_is_complete():
#         return JsonResponse({'status': 'complete'}, status=200)
#     else:
#         return JsonResponse({'status': 'in progress'}, status=202)