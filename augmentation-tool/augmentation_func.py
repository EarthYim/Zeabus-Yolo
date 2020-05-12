import cv2 as cv
import numpy as np
import random
from skimage.util import random_noise, img_as_float


debug = False
# debug = True


def normalize(image, max=255, input_max=None, input_min=None):
    if input_max is not None:
        result = 255.*(image - input_min)/(input_max-input_min)
    else:
        # print(image.max(),image.min())
        result = 255.*(image - image.min())/(image.max()-image.min())
    result = np.uint8(result)
    return result


def median_blur(img):
    rand = random.randint(2, 5)

    if not rand % 2:
        rand += 1
    result = cv.medianBlur(img, rand)
    if debug:
        cv.imshow("blurring", result)
        cv.waitKey(-1)
    return result


def blurring(img):
    rand = random.randint(2, 5)
    if not rand % 2:
        rand += 1
    result = cv.blur(img, (rand, rand))
    if debug:
        cv.imshow("blurring", result)
        cv.waitKey(-1)
    return result


def add_sun_light(img):
    result = cv.cvtColor(img, cv.COLOR_BGR2LAB)
    avg_a = np.average(result[:, :, 1])
    avg_b = np.average(result[:, :, 2])
    rand = random.randint(150, 170)
    result[:, :, 1] = result[:, :, 1] - \
        ((avg_a - 128) * (result[:, :, 0] / 255.0) * 0.6)
    result[:, :, 2] = result[:, :, 2] - \
        ((avg_b - rand) * (result[:, :, 0] / 255.0) * 0.6)
    result = cv.cvtColor(result, cv.COLOR_LAB2BGR)

    if debug:
        cv.imshow("add_sun_light", result)
        cv.waitKey(-1)
    return result


def remove_sun_light(img):
    result = cv.cvtColor(img, cv.COLOR_BGR2LAB)
    avg_a = np.average(result[:, :, 1])
    avg_b = np.average(result[:, :, 2])
    rand = random.randint(110, 120)
    result[:, :, 1] = result[:, :, 1] - \
        ((avg_a - 128) * (result[:, :, 0] / 255.0) * 0.6)
    result[:, :, 2] = result[:, :, 2] - \
        ((avg_b - rand) * (result[:, :, 0] / 255.0) * 0.6)
    result = cv.cvtColor(result, cv.COLOR_LAB2BGR)

    if debug:
        cv.imshow("add_sun_light", result)
        cv.waitKey(-1)
    return result


def increase_brightness(img):
    """
        Overexpose
    """
    rand = random.uniform(1.2, 1.5)
    result = cv.cvtColor(img, cv.COLOR_BGR2LAB)
    result[:, :, 0] = np.clip(np.int16(result[:, :, 0]) * rand, 0, 255)
    result = cv.cvtColor(result, cv.COLOR_LAB2BGR)

    if debug:
        cv.imshow("overexpose", result)
        cv.waitKey(-1)
    return result


def decrease_brightness(img):
    """
        Underexpose
    """
    rand = random.uniform(0.55, 0.75)
    result = cv.cvtColor(img, cv.COLOR_BGR2LAB)
    result[:, :, 0] = np.clip(np.int16(result[:, :, 0]) * 0.7, 0, 255)
    result = cv.cvtColor(result, cv.COLOR_LAB2BGR)

    if debug:
        cv.imshow("underexpose", result)
        cv.waitKey(-1)
    return result


def add_gaussian_noise(img):
    img = random_noise(img, mode='gaussian',
                       mean=random.random()/100., var=random.random()/100.)
    result = normalize(img)
    if debug:
        cv.imshow("gaussian_noise", result)
        cv.waitKey(-1)
    return result


def add_salt_paper(img):
    img = random_noise(img, mode='s&p', amount=random.random()/10.)
    result = normalize(img)
    if debug:
        cv.imshow("s&p_noise", result)
        cv.waitKey(-1)
    return result
