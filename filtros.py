import cv2

def filtro_gaussiano(img, kernel_size=(5, 5), sigma=1):
    return cv2.GaussianBlur(img, kernel_size, sigma)

def filtro_mediana(img, kernel_size=5):
    return cv2.medianBlur(img, kernel_size)

def filtro_bilateral(img, d=9, sigma_color=75, sigma_space=75):
    return cv2.bilateralFilter(img, d, sigma_color, sigma_space)
