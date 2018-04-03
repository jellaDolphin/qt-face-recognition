import numpy as np
import cv2


class ImageNotFoundException(Exception):
    def __init__(self, message):
        super(ImageNotFoundException, self).__init__(message)


class Histogram(object):
    bins = [8, 8, 8]

    def __init__(self, image_location, histogram_type='rgb'):
        self.image_location = image_location
        self.histogram_type = histogram_type

    @property
    def image(self):
        return cv2.imread(self.image_location)

    def generate(self):
        # b 0 , g 1, r 2
        # mask is None
        # bins are 128 by default
        hist_list = np.array([])
        for channel in range(3):
            _hist = cv2.calcHist([self.image], [channel], None, [8], [0, 256])
            hist = cv2.normalize(_hist)

        # return out 3D histogram as a flattened array
        return hist.flatten()

    def show_image(self):
        cv2.imshow('My Image', self.image)
        cv2.waitKey(0) & 0xFF
        cv2.destroyAllWindows()


class HaarCascadeFaceDetection(object):
    _line_thickness = 2
    _blue = (255, 0, 0)
    _green = (0, 255, 0)
    _red = (0, 0, 255)
    face_classifier_cascade_file = "haarcascades/haarcascade_frontalface_default.xml"

    def __init__(self, image_location):
        self.image_location = image_location

    @property
    def image(self):
        """
        Reads the image from the given location in the constructor
        :return: ``numpy.nd``
        """
        img = cv2.imread(self.image_location, cv2.IMREAD_COLOR)
        if img is None:
            raise ImageNotFoundException("Unable to find image in location")
        return img

    @property
    def get_classifier(self):
        """
        Returns the cascade classifier with the currently selected classifier training data
        :return: ``cv2.CascadeClassifier``
        """
        return cv2.CascadeClassifier(self.face_classifier_cascade_file)

    @property
    def gray(self):
        """
        Color the picture gray
        :return: ``numpy.nd``
        """
        return cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def _detect_faces(self):
        """
        Find all features in a given image and return coordinates for bounding boxes as numpy array
        :return: ``numpy.nd``
        """
        return self.get_classifier.detectMultiScale(self.gray, 1.5, 5)

    def detect(self):
        """
        Function detects faces according to given
        :return: ``numpy.ndarray``
        """
        return self._detect_faces()

    def show_classified_image(self):
        """
        Method shows the image after detection with bounding box
        :return:
        """
        image = self.image
        for (x, y, w, h) in self._detect_faces():
            point1 = (x, y)
            point2 = (x + w, y + h)
            # draw the rectangle on all possible faces
            cv2.rectangle(image, point1, point2, self._red, self._line_thickness)

        cv2.imshow('Face Detection Debug', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()