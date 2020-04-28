from imutils import face_utils
import numpy as np
import imutils
import dlib
import cv2
import matplotlib.pyplot as plt

SHAPE_DETECTOR_PATH = "shape_predictor_68_face_landmarks.dat"

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(SHAPE_DETECTOR_PATH)

def get_image_facial_landmarks(image_path):
	ret = []

	image = plt.imread(image_path)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	rects = detector(gray, 1)

	for (i, rect) in enumerate(rects):
		shape = predictor(gray, rect)
		shape = face_utils.shape_to_np(shape)

		for (x, y) in shape:
			ret.append((x, y))

	return ret
