from PIL import Image, ImageFilter
import os 

# Caminho relativo das pastas de entrada e saída de imagens
INPUT_DIR = os.path.join('data', 'input')
OUTPUT_DIR = os.path.join('data', 'output')


def in_file(filename):
    '''Retorna o caminho de um arquivo de entrada'''

    return os.path.join(INPUT_DIR, filename)

def out_file(filename):
    '''Retorna o caminho de um arquivo de saída'''

    return os.path.join(OUTPUT_DIR, filename)

 
# img.show()
# filtered_img.show() 

# A função recebe dois parâmetros, img1 e img2, que são assumidos como objetos de imagem.  

# Uma nova imagem (new_img) é criada usando Image.new('RGB', (img1.width + img2.width, img1.height)). 
# Essa nova imagem tem largura igual à soma das larguras das duas imagens de entrada (img1 e img2) e 
# a mesma altura da imagem img1. A cor padrão para a nova imagem é RGB.

# A imagem img1 é colada na nova imagem (new_img) na posição (0, 0) usando o método paste.
# A imagem img2 é colada na nova imagem (new_img) ao lado da imagem img1, 
# começando na posição (img1.width, 0). Isso significa que a imagem img2 é colada à direita da imagem img1.
# A nova imagem resultante, que agora contém ambas as imagens lado a lado, é exibida usando o método show().
# Em resumo, a função cria uma nova imagem combinando duas imagens de entrada horizontalmente e a exibe.
def show_vertical(img1, img2):
#     '''Retorna as imagens concatenadas na vertical'''
    new_img = Image.new('RGB', (img1.width + img2.width, img1.height))
    new_img.paste(img1, (0,0))
    new_img.paste(img2, (img1.width, 0))
    new_img.show()
    return new_img

def show_horizontal(img1, img2):
#     '''Retorna as imagens concatenadas na horizontal'''
    new_img = Image.new('RGB', (img1.width, img1.height + img2.height))
    new_img.paste(img1, (0,0))
    new_img.paste(img2, (0, img1.height))
    new_img.show()
    return new_img

