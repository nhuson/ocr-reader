import click
import logging
from PIL import Image
from pdf2image import convert_from_path
from pytesseract import image_to_string
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

extentions = ['png', 'jpeg', 'jpg', 'pdf']

def validInput(inputFile):
  strArr = inputFile.split('.')
  strArr = strArr[::-1]
  if strArr[0] not in extentions:
    raise Exception('Incorrect format of input file.')

  return True

def pdfToImage(pdfFile):
  return convert_from_path(pdfFile)

def convertImgToText(input, output):
  inputArr = input.split('.')
  inputArr = inputArr[::-1]
  file = pdfToImage(input) if inputArr[0] == 'pdf' else Image.open(input)
  text = image_to_string(file)
  logger.debug(f"Text scanned from image: {text}")
  with open(output, 'w') as outFile:
    outFile.write(text)

@click.command()
@click.option('--input', default="./test.jpg", help='Image text file.')
@click.option('--output', default="output.text", help='Text scan output.')
def scanText(input, output):
  try:
    if validInput(input):
      convertImgToText(input, output)
  except Exception as error  :
    logger.error(str(error))

if __name__ == '__main__':
  scanText()