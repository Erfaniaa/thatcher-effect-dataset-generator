import pandas as pd
from os import listdir, mkdir
from os.path import isfile, join
import cv2

INPUT_IMAGES_DIRECTORY_PATH = "input_images"
OUTPUT_IMAGES_DIRECTORY_PATH = "output_images"
ATTRIBUTES_CSV_PATH = "attributes.csv"
ATTRIBUTES_CSV_DELIMITER = ","
ATTRIBUTES_CSV_MAX_ROWS = 1000
PRINT_LOG = True
PRINT_LOG_PERIOD = 10

def flip_subimage_vertically(image, x1, y1, x2, y2):
        mid_x = (x1 + x2) // 2
        for x in range(x1, mid_x):
                for y in range(y1, y2):
                        image[x][y], image[2 * mid_x - x][y] = image[2 * mid_x - x][y].copy(), image[x][y].copy()


def gradient_subimage(image, x1, y1, x2, y2):
        final_distance = (x2 - x1) ** 2 + (y2 - y1) ** 2
        start_color = image[x1][y1].copy()
        final_color = image[x2][y2].copy()
        for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                        current_distance = (x - x1) ** 2 + (y - y1) ** 2
                        k = current_distance / final_distance
                        current_color = start_color * (1 - k) + final_color * k
                        image[x][y] = current_color


def blur_orthogonal_border(image, x1, y1, x2, y2, border_size):
        if x1 == x2:
                x = x1
                for y in range(y1, y2 + 1):
                        gradient_subimage(image, x - border_size, y, x + border_size, y)
        if y1 == y2:
                y = y1
                for x in range(x1, x2 + 1):
                        gradient_subimage(image, x, y - border_size, x, y + border_size)


def blur_rectangle_border(image, x1, y1, x2, y2, border_size=3):
        blur_orthogonal_border(image, x1, y1, x1, y2, border_size)
        blur_orthogonal_border(image, x2, y1, x2, y2, border_size)
        blur_orthogonal_border(image, x1, y1, x2, y1, border_size)
        blur_orthogonal_border(image, x1, y2, x2, y2, border_size)


def flip_subimage_vertically_with_border_softening(image, x1, y1, x2, y2):
        flip_subimage_vertically(image, x1, y1, x2, y2)
        blur_rectangle_border(image, x1, y1, x2, y2)


def apply_thatcher_effect_on_image(input_image_path, output_image_path, left_eye_pos, right_eye_pos, mouth_pos1, mouth_pos2):
        image = cv2.imread(input_image_path)
        flip_subimage_vertically_with_border_softening(image, left_eye_pos[1] - 6, left_eye_pos[0] - 13, left_eye_pos[1] + 8, left_eye_pos[0] + 13)
        flip_subimage_vertically_with_border_softening(image, right_eye_pos[1] - 6, right_eye_pos[0] - 13, right_eye_pos[1] + 8, right_eye_pos[0] + 13)
        flip_subimage_vertically_with_border_softening(image, mouth_pos1[1] - 6, mouth_pos1[0] - 2, mouth_pos2[1] + 16, mouth_pos2[0] + 2)
        image = cv2.flip(image, 0)
        cv2.imwrite(output_image_path, image)


def read_attributes_csv(csv_file_path, csv_file_delimiter):
        global attributes_csv
        global attributes_csv_rows_count
        global attributes_csv_cols_count
        attributes_csv = pd.read_csv(csv_file_path, delimiter=csv_file_delimiter)
        attributes_csv_rows_count = len(attributes_csv)
        attributes_csv_cols_count = len(attributes_csv.iloc[0])


def main():
        read_attributes_csv(ATTRIBUTES_CSV_PATH, ATTRIBUTES_CSV_DELIMITER)
        for i in range(min(attributes_csv_rows_count, ATTRIBUTES_CSV_MAX_ROWS)):
                filename = attributes_csv.iloc[i]["image_id"]
                if PRINT_LOG and i % PRINT_LOG_PERIOD == 0:
                        print("Filename:", filename)
                input_file_path = join(INPUT_IMAGES_DIRECTORY_PATH, filename)
                if not isfile(input_file_path):
                        if PRINT_LOG and i % PRINT_LOG_PERIOD == 0:
                                print("Not found")
                        continue
                output_file_path = join(OUTPUT_IMAGES_DIRECTORY_PATH, filename)
                left_eye_pos = attributes_csv.iloc[i]["lefteye_x"], attributes_csv.iloc[i]["lefteye_y"]
                right_eye_pos = attributes_csv.iloc[i]["righteye_x"], attributes_csv.iloc[i]["righteye_y"]
                mouth_pos1 = attributes_csv.iloc[i]["leftmouth_x"], attributes_csv.iloc[i]["leftmouth_y"]
                mouth_pos2 = attributes_csv.iloc[i]["rightmouth_x"], attributes_csv.iloc[i]["rightmouth_y"]
                apply_thatcher_effect_on_image(input_file_path, output_file_path, left_eye_pos, right_eye_pos, mouth_pos1, mouth_pos2)
                if PRINT_LOG and i % PRINT_LOG_PERIOD == 0:
                        print("Done")


if __name__ == "__main__":
        main()
