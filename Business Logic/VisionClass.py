import numpy as np
import cv2 as cv
from utils import *


class Vision:

    def __init__(self, image_path, model_path):
        self.image_path = image_path
        self.model_path = model_path
        self.height = 450
        self.width = 450
        self.model = init_model()
    
    def pre_process(self, img):
        # Convert the image to grayscale
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # Create a new image to work on (Gaussian Blur reduces noise and helps identify the sudoku grid)
        blur_img = cv.GaussianBlur(img, (5, 5), 1)
        # Edge detection using Canny Edge Detector to find the edges
        # New edge detection using adaptiveThreshold (Gave better results)
        # edges = cv.Canny(blur_img, 200, 300)
        edges = cv.adaptiveThreshold(blur_img, 255, 1, 1, 11, 2)
        return edges
    
    def process_image(self):
        # Get the image
        self.img = cv.imread(self.image_path)
        # Check if the image is not None
        assert self.img is not None, "file could not be read, check with os.path.exists()"
        # Resize the image to a smaller size
        self.img = cv.resize(self.img, (self.width, self.height))
        edges = self.pre_process(self.img)

        # Find contours to find the shapes
        contours, hierarchy = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        # Get the corners of the sudoku grid
        biggest, maxArea = biggest_contour(contours)
        if biggest.size != 0:
            # Reorder the points to get the corners in the correct order
            biggest = reorder(biggest)

            # Warp the image to get a top-down view of the sudoku grid
            pts1 = np.float32(biggest)
            pts2 = np.float32([[0, 0], [self.width, 0], [0, self.height], [self.width, self.height]])

            # Warp the image to get a top-down view of the sudoku grid
            matrix = cv.getPerspectiveTransform(pts1, pts2)
            img_warped = cv.warpPerspective(self.img, matrix, (self.width, self.height))
            img_warped = cv.cvtColor(img_warped, cv.COLOR_BGR2GRAY)

            # Get each cell and create image from them (81 images in total)
            # Each box can be either empty or contain a number
            cells = split_cells(img_warped)

            # Predict the number in the cell
            prediction = predict_cell(cells, self.model)
            return prediction
        else:
            return None