# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Sudoku
from business_logic.process_image import process_image
import base64
from PIL import Image
from io import BytesIO
import os
import datetime as dt
import json

# Create your views here. AKA Routes
# CRUD operations


# Create i.e. read info from the data provided (image processing)
# Need to go through the docs again to see how to save the image to the sql database
def sudoku(request):

    # Get all sudoku objects and send them back to the user
    if request.method == "GET":
        sudokus = Sudoku.objects.all()
        return JsonResponse(
            [
                {
                    "id": sudoku.id,
                    "name": sudoku.name,
                    "description": sudoku.description,
                    "puzzle": sudoku.puzzle,
                    "solution": sudoku.solution,
                    "date_created": sudoku.date_created,
                    "date_modified": sudoku.date_modified,
                }
                for sudoku in sudokus
            ],
            safe=False,
            status=200,
        )
    # Create new sudoku object
    elif request.method == "POST":

        image_data = request.POST.get("image")
        name = request.POST.get("name")
        description = request.POST.get("description")

        if image_data is None or name is None or description is None:
            return HttpResponse(content="Please fill in all of the fields", status=400)

        # Convert the image data (base64) to an image (JPG)
        image_data = base64.b64decode(image_data)
        image = Image.open(BytesIO(image_data))

        # Save the image to a file path
        image_path = "images/image.jpg"
        image.save(image_path)
        # Run the image processing logic and get the grid values
        grid = process_image(image_path).return_grid()
        # Delete the temporary image after processing
        os.remove(image_path)

        # Save the grid information to the database
        # The image_data is saved as base64 string to make it easier to work with
        # Important thing is that we have the grid values
        sudoku = Sudoku(
            image_data=request.POST.get("image"),
            name=name,
            description=description,
            puzzle=grid,
        )
        sudoku.save()

        # Return the grid values to the user
        return JsonResponse(
            {
                "id": sudoku.id,
                "name": sudoku.name,
                "description": sudoku.description,
                "puzzle": sudoku.puzzle,
                "solution": sudoku.solution,
                "date_created": sudoku.date_created,
                "date_modified": sudoku.date_modified,
            },
            status=201,
        )


# Read, Update, Delete operations
def one_sudoku(request, sudoku_id):

    # Get the sudoku object from the database
    if request.method == "GET":
        try:
            sudoku = Sudoku.objects.get(pk=sudoku_id)
            return JsonResponse(
                {
                    "id": sudoku.id,
                    "name": sudoku.name,
                    "description": sudoku.description,
                    "puzzle": sudoku.puzzle,
                    "solution": sudoku.solution,
                    "date_created": sudoku.date_created,
                    "date_modified": sudoku.date_modified,
                },
                status=200,
            )
        except Sudoku.DoesNotExist:
            return HttpResponse(content="Sudoku not found", status=404)

    # Update the sudoku object
    elif request.method == "PATCH":
        try:
          
            data = json.loads(request.body)
            
            fields = {
                "name": data.get("name"),
                "description": data.get("description"),
                "puzzle": data.get("puzzle"),
            }

            # Get the sudoku object from the database
            sudoku = Sudoku.objects.get(pk=sudoku_id)

            # Update the sudoku object
            for field, value in fields.items():
                if value is not None:
                    setattr(sudoku, field, value)
            
            sudoku.date_modified = dt.datetime.now()

            sudoku.save()

            # Return a success message
            return HttpResponse(content=[
                {
                    "id": sudoku.id,
                    "name": sudoku.name,
                    "description": sudoku.description,
                    "puzzle": sudoku.puzzle,
                    "solution": sudoku.solution,
                    "date_created": sudoku.date_created,
                    "date_modified": sudoku.date_modified,
                }
            ], status=200)
        except Sudoku.DoesNotExist:
            return HttpResponse(content="Sudoku not found", status=404)

    # Delete a sudoku object
    elif request.method == "DELETE":
        try:
            sudoku = Sudoku.objects.get(pk=sudoku_id)
            sudoku.delete()
            return HttpResponse(content="Sudoku deleted", status=204)
        except Sudoku.DoesNotExist:
            return HttpResponse(content="Sudoku not found", status=404)


