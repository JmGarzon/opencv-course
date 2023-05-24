import cv2 as cv
import numpy as np

# Create a blank image:
blank = np.zeros((500, 500, 3), dtype='uint8')


def draw_rectangles():
    cv.imshow("Blank", blank)

    # 1. Point the image a certain color
    blank[:] = (0, 255, 0)
    cv.imshow("Green", blank)

    # Get a subsection of the picture
    blank[200:300, 300:400] = 0, 0, 255
    cv.imshow("Color in a color", blank)

    # 2. Draw a rectangle shape
    cv.rectangle(blank, (0, 0), (250, 250), (0, 0, 255), thickness=2)
    cv.imshow("Rectangle shape", blank)

    # 3. Draw a filled rectangle
    cv.rectangle(blank, (0, 0), (250, 250), (0, 0, 255), thickness=cv.FILLED)
    cv.imshow("Rectangle filled", blank)

    # 4. Draw a rectangle defined from the image size
    cv.rectangle(blank, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2), (0, 0, 255), thickness=cv.FILLED)
    cv.imshow("Rectangle perc", blank)

    cv.waitKey(0)
    cv.destroyAllWindows()


def draw_circle():
    # 5. Draw a circle
    cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 40, (0, 0, 255), thickness=3)
    cv.imshow("Circle", blank)
    cv.waitKey(0)


def draw_line():
    # 6. Draw lines
    cv.line(blank, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2), (255, 255, 255), thickness=2)
    cv.imshow("Line", blank)
    cv.waitKey(0)


def write_text():
    cv.putText(blank, "Testing testing", (0, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 255))
    cv.imshow("Text", blank)
    cv.waitKey(0)