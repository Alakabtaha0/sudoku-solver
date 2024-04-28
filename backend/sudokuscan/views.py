# from django.shortcuts import render
from django.http import HttpResponse
from .models import Sudoku
from business_logic.process_image import process_image
import json
import base64
from PIL import Image
from io import BytesIO
import os
import numpy as np

# Create your views here. AKA Routes
# CRUD operations

# Create i.e. read info from the data provided (image processing)
# Need to go through the docs again to see how to save the image to the sql database
def read_puzzle(request):
    if request.method == 'POST':

        # with open('information.txt', 'w') as f:
        #     f.write(request.POST.get('image'))

        image_data = request.POST.get('image')

        if image_data is None:
            return HttpResponse(content='No image provided', status=400)
        
        # Convert the image data (base64) to an image (JPG)
        image_data = base64.b64decode(image_data)
        image = Image.open(BytesIO(image_data))

        # Save the image to a file path
        image_path = 'images/image.jpg'
        image.save(image_path)
        # Run the image processing logic and get the grid values
        grid = process_image(image_path).return_grid()
        # Delete the temporary image after processing
        os.remove(image_path)

        # Save the grid information to the database
        # The image_data is saved as base64 string to make it easier to work with
        # Important thing is that we have the grid values
        sudoku = Sudoku(image_data=request.POST.get('image'), name='test2', description='test2', puzzle=grid)
        sudoku.save()

        # Return the grid values to the user
        return HttpResponse(content=grid, status=200)
        # # Get the base64 string from the request
        # base_string = request.POST.get('image')
        
        # # Decode the base64 string
        # image_data = base64.b64decode(base_string)
        # # Convert the image data to an image
        # image = Image.open(BytesIO(image_data), mode='r')

        # if image is None:
        #     return HttpResponse(content='No image provided', status=400)

    
        # # Create a new Sudoku object
        # sudoku = Sudoku(image=image)
        # sudoku.image = image

        # # Save the object to the database
        # sudoku.save()

        # # process the image and save the returned class to an object
        # processed_image = process_image(sudoku.image.path)

        # # Get the grid from the processed image
        # grid = processed_image.return_grid()

        # # Return the puzzle to the user
        # return HttpResponse(content=grid, status=201)    


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