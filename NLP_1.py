from wordcloud import WordCloud, STOPWORDS
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import platform
from matplotlib import font_manager, rc
from konlpy.tag import Kkma
import csv
kkma = Kkma()


# text = open("write.csv",'r',encoding='UTF-8').read()
r = open("write.csv",'r')
text = csv.reader(r)

text_kkma = kkma.morphs(text)

r.close()

rabbit_img = np.array(Image.open("images.png"))

stop_word = ["!","?","~","이"]




path = "C:/Users/user/Desktop/workspace/vscode/python/font/SUITE-Bold.ttf"

if platform.system() == "Darwin":
    rc("font",family = "AppleGothic") 
elif platform.system() == "Windows":
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc("font",family = font_name)
else:
    print("Unknown")
# %matplotlib inline

# plt.figure(figsize=(8,8))
# plt.imshow(rabbit_img,cmap = plt.cm.gray, interpolation='bilinear')
# plt.axis('off')
# plt.show()
wc = WordCloud(font_path="C:/Users/user/Desktop/workspace/vscode/python/font/SUITE-Bold.ttf",background_color = 'black',max_font_size=60, max_words = 2000, mask = rabbit_img,stopwords = stop_word)
wc = wc.generate(str(text_kkma))
wc.words_

# print(wc.words_)

plt.figure(figsize=(12,12))
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
plt.show()

r.close()


