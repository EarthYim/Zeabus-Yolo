import numpy as np
import cv2 as cv
from skimage.util import random_noise, img_as_float
import random
from augmentation_func import *
import os 
import time
import csv 
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", type=str, default="./",
                help="path")
ap.add_argument("-f", "--filename", type=str, default="./",
                help="Original dataset")
args = vars(ap.parse_args())

print("this is path", args["path"])

dataset_dir = args["path"]
csv_name = args["filename"]
augment_with_two_func = 0.3

images_augmentation_dir = os.path.join(dataset_dir, "images_augmentation")

if not os.path.exists(images_augmentation_dir):
    os.mkdir(images_augmentation_dir)


augment_1 = [blurring, median_blur, increase_brightness, decrease_brightness, add_sun_light, remove_sun_light, add_gaussian_noise, add_salt_paper]
# augment_1 = 0 1
augment_2 = [add_sun_light, remove_sun_light, add_gaussian_noise, add_salt_paper]
# augment_1 = 2 3 4 5
augment_3 = [blurring, median_blur,  add_gaussian_noise, add_salt_paper]
# augment_1 = 6 7
augment_4 = [blurring, median_blur, increase_brightness, decrease_brightness, add_sun_light, remove_sun_light]

def get_file_name(img_path, filter=[]):
    if "\\" in img_path:
        name = img_path.split('\\')[-1]
    else:
        name = img_path.split('/')[-1]

    for f in filter:
        name = name.replace(f, '') 
    return name


def augmentation(img):
    rand1 = random.randint(0, 7)
    img_augmented = augment_1[rand1](img)

    if random.random() < augment_with_two_func:
        if rand1 < 2:
            rand2 = random.randint(0, 3)
            img_augmented = augment_2[rand2](img_augmented)
        elif rand1 < 6:
            rand2 = random.randint(0, 3)
            img_augmented = augment_3[rand2](img_augmented)
        else:
            rand2 = random.randint(0, 5)
            img_augmented = augment_4[rand2](img_augmented)
    return img_augmented

def main():
    csv_aug_path = os.path.join(dataset_dir, "dataset-augmentation.csv") 
    csv_aug_file = open(csv_aug_path, 'w', newline='' )
    writer = csv.writer(csv_aug_file, delimiter=',')

    csv_path = os.path.join(dataset_dir, csv_name) 
    img_dir = os.path.join(dataset_dir, "images") 

    csv_file = open(csv_path)
    csv_reader = csv.reader(csv_file, delimiter=',')

    prev_name = ''
    name_img_aug_list = []
    count = 0
    start_time = time.time()
    for row in csv_reader:
        name = row[0]
        name = get_file_name(name)
        if name == prev_name:
            for n in name_img_aug_list:
                data = [n] + row[1:]
                # print(data)
                writer.writerow(data)
            continue
        else:
            count += 1
            name_img_aug_list = []

        #img_path = "%s/%s" % (img_dir,name)
        img_path = os.path.join(img_dir, name)
        print(img_path)
        img = cv.imread(img_path, 1)

        number_of_augment = 2


        for i in range(0, number_of_augment):
            img_augmented = augmentation(img)

            img_aug_name = str(time.time()).replace(".","")
            img_aug_name += ".png"
            img_aug_path = os.path.join(images_augmentation_dir,img_aug_name)

            name_img_aug_list.append("images/%s"%img_aug_name)

            cv.imwrite(img_aug_path, img_augmented)
            data = ["images/%s"%img_aug_name] + row[1:]
            # print(data)
            writer.writerow(data)

        prev_name = name
        print("number of augmented: %d time: %.2f minutes"%(count, (time.time() - start_time)/60.))
if __name__ == "__main__":
    main()
