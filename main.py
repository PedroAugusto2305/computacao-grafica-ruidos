import cv2
from adicionar_ruido import ruido_sal_pimenta, ruido_gaussiano
from filtros import (
    filtro_gaussiano, 
    filtro_mediana, 
    filtro_bilateral
)
from utils import show_images

# Carrega a imagem em escala de cinza
img = cv2.imread('./images/cavalo.webp', cv2.IMREAD_GRAYSCALE)
if img is None:
    raise ValueError("Imagem não encontrada ou não pôde ser carregada.")

# Aplica os dois tipos de ruído
img_sp_noise = ruido_sal_pimenta(img, prob=0.05)
img_gauss_noise = ruido_gaussiano(img)

# Aplica filtros de suavização nos ruídos
gaussian_blur_sp = filtro_gaussiano(img_sp_noise)
gaussian_blur_gauss = filtro_gaussiano(img_gauss_noise)

median_blur_sp = filtro_mediana(img_sp_noise)
median_blur_gauss = filtro_mediana(img_gauss_noise)

bilateral_sp = filtro_bilateral(img_sp_noise)
bilateral_gauss = filtro_bilateral(img_gauss_noise)

# Lista de títulos e imagens para visualização
titles = [
    'Imagem Original', 'Ruído Sal e Pimenta', 'Ruído Gaussiano',
    'Filtro Gaussiano (S&P)', 'Filtro Gaussiano (Gauss)',
    'Filtro da Mediana (S&P)', 'Filtro da Mediana (Gauss)',
    'Filtro Bilateral (S&P)', 'Filtro Bilateral (Gauss)'
]
images = [
    img, img_sp_noise, img_gauss_noise,
    gaussian_blur_sp, gaussian_blur_gauss,
    median_blur_sp, median_blur_gauss,
    bilateral_sp, bilateral_gauss
]

# Exibe as imagens
show_images(titles, images, 3, 3)
