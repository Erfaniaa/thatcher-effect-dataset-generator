import pandas as pd
from os import listdir
from os.path import isfile, join
import cv2
from matplotlib import pyplot as plt

INPUT_IMAGES_DIRECTORY_PATH = "input_images"
ATTRIBUTES_CSV_PATH = "attributes.csv"
ATTRIBUTES_CSV_DELIMITER = ","

def flip_subrectangle(image, x1, y1, x2, y2):
        mid_x = (x1 + x2) // 2
        for x in range(x1, mid_x):
                for y in range(y1, y2):
                        image[x][y], image[2 * mid_x - x][y] = image[2 * mid_x - x][y].copy(), image[x][y].copy()

dataset_directory_filenames = listdir(INPUT_IMAGES_DIRECTORY_PATH)
dataset_directory_filenames.sort()

for image_id in range(1, 80):

        filename = dataset_directory_filenames[image_id]

        file_path = join(INPUT_IMAGES_DIRECTORY_PATH, filename)
        print(file_path)
        image = cv2.imread(file_path)

        image_id += 99

        # for f in dataset_directory_filenames:
        #     if isfile(join(INPUT_IMAGES_DIRECTORY_PATH, f)):
        #         file_path = join(INPUT_IMAGES_DIRECTORY_PATH, f)
        #         print(file_path)
        #         image = cv2.imread(file_path)
        #         break

        csv_contents = pd.read_csv(ATTRIBUTES_CSV_PATH, delimiter=ATTRIBUTES_CSV_DELIMITER)
        rows = len(csv_contents)
        cols = len(csv_contents.iloc[0])

        x, y = csv_contents.iloc[image_id]["lefteye_x"], csv_contents.iloc[image_id]["lefteye_y"]
        flip_subrectangle(image, y - 6, x - 13, y + 8, x + 13)
        x, y = csv_contents.iloc[image_id]["righteye_x"], csv_contents.iloc[image_id]["righteye_y"]
        flip_subrectangle(image, y - 6, x - 13, y + 8, x + 13)
        x1, y1 = csv_contents.iloc[image_id]["leftmouth_x"], csv_contents.iloc[image_id]["leftmouth_y"]
        x2, y2 = csv_contents.iloc[image_id]["rightmouth_x"], csv_contents.iloc[image_id]["rightmouth_y"]
        flip_subrectangle(image, y1 - 6, x1 - 2, y2 + 16, x2 + 2)
        image = cv2.flip(image, 0)
        cv2.imshow("image " + str(image_id), image)

cv2.waitKey(0)
cv2.destroyAllWindows()
