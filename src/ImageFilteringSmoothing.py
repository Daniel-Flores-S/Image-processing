import cv2

# Ler a imagem
img = cv2.imread('filters/lena.png')

# Aplicar um filtro de suavização (por exemplo, média)
smoothed_img = cv2.blur(img, (5, 5))

# Exibir as imagens original e suavizada
cv2.imshow('Imagem Original', img)
cv2.imshow('Imagem Suavizada', smoothed_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
