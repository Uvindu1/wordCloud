import sys #Python runtime environment thiyana vivida kotas hesiravima pahasu karai
import numpy as np
from PIL import Image # Image kiyana eken image ekata cl karano,open karano, image eke nama pass karano
import wikipedia # wikipedia eken pahasuwenma data ganna puluwan
from wordcloud import wordcloud,STOPWORDS
# mema STOPWORDS eka bavitha karanne commen words ain karanna

a = str(input("Enter the name of whice you want to make word cloud :"))
title = wikipedia.search(a)[0] #wikipedia eken titel eka soyai
page = wikipedia.page(title) #titel ekata adala body eka wikipedia eken soyai
text = page.content # topic ekata adala karunutika gannawa
print(text)

bg = np.array(Image.open("abcd.jpeg")) # apita word print karanna black ground ekaka on
unwated_word = set(STOPWORDS) # samanya podu wachana ewath kara(ex : the, to , a,....)
wordclo = wordcloud(background_color = 'black', max_words = 400, mask = bg, stopwords = unwated_word)
wordclo.generate(text)
wordclo.to_file("sample.png")  # save karana nama































