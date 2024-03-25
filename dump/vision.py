import numpy as np
import cv2 as cv
from utils import *
import sys

# Storing image in variable
IMAGE = 'assets/2.JPG'
HEIGHT = 450
WIDTH = 450

# Initialize the model
model = init_model() 

# Get the image
img = cv.imread(IMAGE)
# Check if the image is not None
assert img is not None, "file could not be read, check with os.path.exists()"
# Resize the image to a smaller size
img = cv.resize(img, (WIDTH, HEIGHT))

def pre_process(img):
    # Convert the image to grayscale
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Create a new image to work on (Gaussian Blur reduces noise and helps identify the sudoku grid)
    blur_img = cv.GaussianBlur(img, (5, 5), 1)
    # Edge detection using Canny Edge Detector to find the edges
    # New edge detection using adaptiveThreshold (Gave better results)
    # edges = cv.Canny(blur_img, 200, 300)
    edges = cv.adaptiveThreshold(blur_img, 255, 1, 1, 11, 2)
    return edges

edges = pre_process(img)
# Find contours to find the shapes
contours, hierarchy = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)


# Get the corners of the sudoku grid
biggest, maxArea = biggest_contour(contours)
if biggest.size != 0:
    # Reorder the points to get the corners in the correct order
    biggest = reorder(biggest)

    # Warp the image to get a top-down view of the sudoku grid
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [WIDTH, 0], [0, HEIGHT], [WIDTH, HEIGHT]])

    # Warp the image to get a top-down view of the sudoku grid
    matrix = cv.getPerspectiveTransform(pts1, pts2)
    img_warped = cv.warpPerspective(img, matrix, (WIDTH, HEIGHT))
    img_warped = cv.cvtColor(img_warped, cv.COLOR_BGR2GRAY)

    # Get each cell and create image from them (81 images in total)
    # Each box can be either empty or contain a number
    cells = split_cells(img_warped)

    # Predict the number in the cell
    prediction = predict_cell(cells, model)
    print(prediction)


# Delete the window upon key press
# cv.waitKey(0)
# cv.destroyAllWindows()
# sys.exit(0)
