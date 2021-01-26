# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 17:55:50 2021

@author: peachrl
"""
#msyh.ttc微软雅黑    simsun.ttc宋体    simfang.ttf仿宋

import numpy as np
from PIL import Image
import collections
import matplotlib.pyplot as plt           
from wordcloud import WordCloud

def conventional(final_list, image_file, counts, pic_scale, font_size, prefer):
    if image_file=='':
        background_image = None
    else:
        background_image = np.array(Image.open(image_file))
    word_counts = collections.Counter(final_list)

    mycloud1 = WordCloud(scale=pic_scale, prefer_horizontal=prefer, font_path = 'C:\\Windows\\Fonts\\simsun.ttc', max_font_size=font_size, relative_scaling=0.5, max_words=int(counts), background_color=None, mode="RGBA", mask=background_image).generate_from_frequencies(word_counts)
    plt.imshow(mycloud1)
    plt.axis('off')   # 关闭词云图坐标显示
    plt.savefig('ABLab_WordCloud_conventional.svg',dpi=3000, edgecolor='blue', bbox_inches='tight', transparent = True)
    plt.show()


def professional(final_list, image_file, counts, pic_scale, font_size, prefer):
    if image_file=='':
        background_image = None
    else:
        background_image = np.array(Image.open(image_file))
    word_counts = collections.Counter(final_list)

    mycloud2 = WordCloud(scale=pic_scale, prefer_horizontal=prefer, font_path = 'C:\\Windows\\Fonts\\simsun.ttc', max_font_size=font_size, relative_scaling=0.5, max_words=int(counts), background_color=None, mode="RGBA", mask=background_image).generate_from_frequencies(word_counts)
    plt.imshow(mycloud2)
    plt.axis('off')   # 关闭词云图坐标显示
    plt.savefig('ABLab_WordCloud_professional.svg',dpi=3000, edgecolor='blue', bbox_inches='tight', transparent = True)
    plt.show()