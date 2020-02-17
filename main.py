import pandas as pd
from os import listdir
from os.path import isfile, join

INPUT_IMAGES_DIRECTORY_PATH = "input_images"
LANDMARKS_CSV_FILE_PATH = "landmarks.csv"
LANDMARKS_CSV_FILE_DELIMITER = ","

dataset_directory_filenames = listdir(IMAGE_DATASET_DIRECTORY_PATH)
dataset_directory_filenames.sort()

for f in dataset_directory_filenames:
    if isfile(join(IMAGE_DATASET_DIRECTORY_PATH, f)):
        file_path = join(IMAGE_DATASET_DIRECTORY_PATH, f)

csv_contents = pd.read_csv(IMAGE_ATTRIBUTES_CSV_FILE_PATH, delimiter=IMAGE_ATTRIBUTES_CSV_FILE_DELIMITER)
rows = len(csv_contents)
cols = len(csv_contents.iloc[0])
print(csv_contents.iloc[0]["image_id"])
