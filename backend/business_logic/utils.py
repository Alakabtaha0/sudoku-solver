import numpy as np
import cv2 as cv
import tensorflow as tf
# tensorflow == 2.15 && keras == 2.15
# If not working properly make sure tensorflow and keras versions are compatible

# Function to get the biggest contour in the image of the sudoku grid
def biggest_contour(contours):
    biggest = np.array([])
    maxArea = 0
    for contour in contours:
        area = cv.contourArea(contour)
        if area > 50:
            peri = cv.arcLength(contour, True)
            approx = cv.approxPolyDP(contour, 0.02 * peri, True)
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
    return biggest, maxArea

# Function to reorder the points
# The points are in the order of [top-left, top-right, bottom-left, bottom-right]
def reorder(points):
    points = points.reshape((4, 2))
    new_points = np.zeros((4, 1, 2), dtype=np.int32)
    add = points.sum(1)
    new_points[0] = points[np.argmin(add)]
    new_points[3] = points[np.argmax(add)]
    diff = np.diff(points, axis=1)
    new_points[1] = points[np.argmin(diff)]
    new_points[2] = points[np.argmax(diff)]
    return new_points

# Function to split the sudoku grid into 81 cells
def split_cells(img):
    # Split the image into 9 rows
    rows = np.vsplit(img, 9)
    cells = []
    for row in rows:
        # Split each row into 9 columns -> creating 9 cells from each row
        cols = np.hsplit(row, 9)
        for col in cols:
            # Append the individual cells to the cells list
            cells.append(col)
    return cells

# Function to load the prediction model
def init_model(model):
    # Load TFLite model and allocate tensors.
    # interpreter = tf.lite.Interpreter(model_path="models/2.tflite")
    # interpreter.allocate_tensors()
    # return interpreter
    # model = load_model('models/model.h5')
    model = tf.keras.models.load_model(model)
    return model

# Function to predict the number in the cell
def predict_cell(cells, model):
    result = []
    for image in cells:
        ## PREPARE IMAGE
        img = np.asarray(image)
        img = img[4:img.shape[0] - 4, 4:img.shape[1] -4]
        img = cv.resize(img, (28, 28))
        img = img / 255
        img = img.reshape(1, 28, 28, 1)
        ## GET PREDICTION
        predictions = model.predict(img)
        classIndex = np.argmax(predictions, axis=-1)
        probabilityValue = np.amax(predictions)
        ## SAVE TO RESULT
        if probabilityValue > 0.8:
            result.append(classIndex[0])
        else:
            result.append(0)
    return result