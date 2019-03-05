from PIL import Image
import pytesseract
from pytesseract import Output
import glob
import pandas as pd
import numpy as np


class ocr_pytesseract:
    def __init__(self, im_list):
        self.im_list = sorted(glob.glob('*.jpg'))
    
    def jpg2text(self):
        lst_text = []
        for i in self.im_list:
            imjpg = Image.open(i) # Opening the image with PIL
            print('Transcribing text for,' i)
            text = pytesseract.image_to_string(imjpg) # Uses trained model from Tesseract to convert JPG image to a string of text
            scores = pytesseract.image_to_data(imjpg, output_type=pytesseract.Output.DATAFRAME) # scores for each word transcribed
            # text_conf = scores[['text','conf']] # Extracting only the text and associated scores dataframe
            mean1 = scores.conf.replace(-1,np.NaN).mean() # Taking the mean confidence value over each word in the transcription
            print('The mean confidence value of', i, 'is', mean1,'. Transcription complete!')
            lst_text.append(text)