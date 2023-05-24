import cv2 as cv


def read_cat():
    # Looks for an image's path and returns its matrix of pixels
    img = cv.imread('./Resources/Photos/cat_large.jpg')
    cv.imshow('Cat', img)
    # Waits for a key to be pressed
    cv.waitKey(0)

def read_dog_video():
    """
    cv.VideoCapture receives as parameters either an integer if using the computer peripherals is intended,
    or a path to a video.
    """
    capture = cv.VideoCapture('./Resources/Videos/dog.mp4')

    # We read every frame of the video
    while True:
        isTrue, frame = capture.read()

        # To prevent an error with the last frame
        if isTrue is False:
            break
        # To show the video frame by frame
        cv.imshow('Video', frame)

        # To stop reproducing the video if the d key is pressed
        if cv.waitKey(20) & 0xFF==ord('d'):
            break

    capture.release()
    cv.destroyAllWindows()

