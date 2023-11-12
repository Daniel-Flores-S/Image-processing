from PIL import Image 

 
image  = Image.open('filtros/lena.png')

print(image.getpixel((500,500)) ) 

image .show()
