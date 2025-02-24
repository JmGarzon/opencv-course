import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    # Works for images, video and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def read_cat():
    # Looks for an image's path and returns its matrix of pixels
    img = cv.imread('./Resources/Photos/cat_large.jpg')
    cv.imshow('Cat', img)

    img_resized = rescaleFrame(img)
    cv.imshow('Resized Cat', img_resized)
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

        # To show a resized video
        resized_frame = rescaleFrame(frame)
        cv.imshow('Resized video', resized_frame)

        # To stop reproducing the video if the d key is pressed
        if cv.waitKey(20) & 0xFF == ord('d'):
            break

    capture.release()
    cv.destroyAllWindows()


def record_me():
    """
        cv.VideoCapture receives as parameters either an integer if using the computer peripherals is intended,
        or a path to a video.
        """

    def changeRes(width, height):
        # Only works for live video
        capture.set(3, width)
        capture.set(4, height)

    capture = cv.VideoCapture(0)
    if not capture.isOpened():
        raise Exception("Could not open video device")
    changeRes(200, 120)

    while True:
        isTrue, frame = capture.read()

        # To prevent an error with the last frame
        if isTrue is False:
            break
        # To show the video frame by frame
        cv.imshow('Video', frame)

        # To stop reproducing the video if the d key is pressed
        if cv.waitKey(20) & 0xFF == ord('d'):
            break

    capture.release()
    cv.destroyAllWindows()
