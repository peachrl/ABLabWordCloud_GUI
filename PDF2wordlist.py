# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 17:25:26 2021

@author: peachrl
"""
import re
import jieba
import jieba.analyse
import os


def PDF2conventionalwordlist(file_dict):
    if not os.path.exists('tmp/'):
        os.mkdir('tmp/')
    object_list = []
    from pdfminer.pdfparser import PDFParser, PDFDocument
    from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
    
    from pdfminer.converter import PDFPageAggregator
    from pdfminer.layout import LTTextBoxHorizontal, LAParams
    
    for (dir_pdf,file_pdf) in file_dict.items():
        pdf_file = dir_pdf
        txt_file = 'tmp/'+file_pdf+'.txt'
        print('\n'+file_pdf+'.pdf：')
    
        device = PDFPageAggregator(PDFResourceManager(), laparams=LAParams())
        interpreter = PDFPageInterpreter(PDFResourceManager(), device)
        
        document = PDFDocument()
        parser = PDFParser(open(pdf_file, 'rb'))
        parser.set_document(document)
        document.set_parser(parser)
        document.initialize()
        
        with open(txt_file, 'w', encoding='utf-8') as f:
            page_list = list(document.get_pages())
            page_list_length = len(page_list)
            print('The page number of this PDF is: ', page_list_length)
                
            for page in document.get_pages():  
                # 接受LTPage对象
                interpreter.process_page(page)               
                # 获取LTPage对象的text文本属性
                layout = device.get_result()
                for x in layout:
                    if isinstance(x, LTTextBoxHorizontal):
                        results = x.get_text()
                        f.write(results)

        data_txt = open(txt_file,'r',encoding='utf-8').read()
        pattern = re.compile(u'\'|\t|\n|\.|=|-|:|;|\)|\(|\?|\"|\d')
        data_txt = re.sub(pattern, '', data_txt)
        #cut_txt = jieba.cut(data_txt, cut_all=False)
        cut_txt = jieba.analyse.extract_tags(data_txt, topK=1000)
        remove_words = [u"的",u'对',u'和',u'等',u'能',u'都',u'。',u' ',u'、',u'中',u'在',u'了',u'，',u'（',u'）',u'“',u'”',u'一个',u'是',u'：']
        for word in cut_txt:
            if word not in remove_words:
                object_list.append(word)
            #object_list.append(word)
        os.remove(txt_file)
    return object_list

# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords

def PDF2professionalwordlist(file_dict):
    if not os.path.exists('tmp/'):
        os.mkdir('tmp/')
    object_list = []
    from pdfminer.pdfparser import PDFParser, PDFDocument
    from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
    
    from pdfminer.converter import PDFPageAggregator
    from pdfminer.layout import LTTextBoxHorizontal, LAParams
    
    for (dir_pdf,file_pdf) in file_dict.items():
        pdf_file = dir_pdf
        txt_file = 'tmp/'+file_pdf+'.txt'
        print('\n'+file_pdf+'.pdf：')
    
        device = PDFPageAggregator(PDFResourceManager(), laparams=LAParams())
        interpreter = PDFPageInterpreter(PDFResourceManager(), device)
        
        document = PDFDocument()
        parser = PDFParser(open(pdf_file, 'rb'))
        parser.set_document(document)
        document.set_parser(parser)
        document.initialize()
        
        with open(txt_file, 'w', encoding='utf-8') as f:
            page_list = list(document.get_pages())
            page_list_length = len(page_list)
            print('The page number of this PDF is: ', page_list_length)
                
            for page in document.get_pages():  
                # 接受LTPage对象
                interpreter.process_page(page)               
                # 获取LTPage对象的text文本属性
                layout = device.get_result()
                for x in layout:
                    if isinstance(x, LTTextBoxHorizontal):
                        results = x.get_text()
                        f.write(results)

        data_txt = open(txt_file,'r',encoding='utf-8').read()
        pattern = re.compile(u'\'|\t|\n|\.|=|-|:|;|\)|\(|\?|\"|\d')
        data_txt = re.sub(pattern, '', data_txt)
        remove_words = stopwordslist("dict/stopwords.txt")
        cut_txt = jieba.cut(data_txt, cut_all=False)
        #cut_txt = jieba.analyse.extract_tags(data_txt, topK=1000)
        #remove_words = [u"的",u'对',u'和',u'等',u'能',u'都',u'。',u' ',u'、',u'中',u'在',u'了',u'，',u'（',u'）',u'“',u'”',u'一个',u'是',u'：']
        for word in cut_txt:
            if word not in remove_words:
                object_list.append(word)
            #object_list.append(word)
        os.remove(txt_file)
    return object_list