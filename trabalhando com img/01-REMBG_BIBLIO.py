#projeto para remover qualquer fundo de fotos em elaboração

from rembg import remove
from PIL import Image

input_path = '/Users/HP Workstation/OneDrive/Área de Trabalho/Python/trabalhando com img/images.jpg'
output_path = 'semfund.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)
print("foto salva...")