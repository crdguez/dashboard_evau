# Ejecutar el código en jupyterlite. Para descargar la imagen concatenada desde jupyterlite, abrir la imagen y sobre ella botón derecho del ratón y descargar.

from PIL import Image

def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst


im1 = Image.open('entrada1.png')
im2 = Image.open('entrada2.png')
get_concat_v(im1, im2).save('salida.png')

# Si son 3 imágenes

# from PIL import Image

# def get_concat_v(im1, im2, im3):
#     dst = Image.new('RGB', (im1.width, im1.height + im2.height + im3.height))
#     dst.paste(im1, (0, 0))
#     dst.paste(im2, (0, im1.height))
#     dst.paste(im3, (0, im1.height + im2.height))
#     return dst


# im1 = Image.open('entrada1.png')
# im2 = Image.open('entrada2.png')
# im3 = Image.open('entrada3.png')
# get_concat_v(im1, im2,im3).save('salida.png')
