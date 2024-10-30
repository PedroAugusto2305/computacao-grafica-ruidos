import random
import numpy as np
import cv2

def ruido_sal_pimenta(img, prob):
    noisy_img = img.copy()
    row, col = img.shape
    num_salt = int(prob * row * col / 2)
    num_pepper = int(prob * row * col / 2)

    for _ in range(num_salt):
        y_coord = random.randint(0, row - 1)
        x_coord = random.randint(0, col - 1)
        noisy_img[y_coord, x_coord] = 255

    for _ in range(num_pepper):
        y_coord = random.randint(0, row - 1)
        x_coord = random.randint(0, col - 1)
        noisy_img[y_coord, x_coord] = 0

    return noisy_img

def ruido_gaussiano(img, mean=0, sigma=25):
    gaussian = np.random.normal(mean, sigma, img.shape).astype(np.uint8)
    noisy_img = cv2.add(img, gaussian)
    return noisy_img
