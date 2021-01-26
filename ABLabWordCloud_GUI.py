# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 11:45:52 2021

@author: peachrl
"""
from dictPDF import dictPDF
import PDF2wordlist
import generatewordcloud
import PySimpleGUI as sg

##############################################################################
sg.theme('DefaultNoMoreNagging')

layout = [
    [sg.Frame(layout=[
    [
        sg.Text("请选择所需批量处理的pdf文件所在文件夹："),
        sg.In(size=(27, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse('浏览文件夹'),],
    [
        sg.Text("请选择所需生成的文字云形状（白底jpg图片，可不选）："),
        sg.In(size=(20, 1), enable_events=True, key="-IMAGE-"),
        sg.FileBrowse('浏览文件'),],    
    [
        sg.Text("词语数量（50~5000）："),
        sg.Slider(size=(44, 20), range=(50,5000), default_value=200, orientation='h', enable_events=True, key="-COUNTS-"),],    
    [
        sg.Text("画布大小（0.1~10）："),
        sg.Slider(size=(45, 20), range=(0.1,4), resolution=.1, default_value=1, orientation='h', enable_events=True, key="-SCALE-"),],    
    [
        sg.Text("最大字号（4~1024）："),
        sg.Slider(size=(44.5, 20), range=(4,1024), default_value=768, orientation='h', enable_events=True, key="-FONTSIZE-"),],    
    [
        sg.Text("横排文字概率（0~1）："),
        sg.Slider(size=(44, 20), range=(0,1), resolution=.1, default_value=0.9, orientation='h', enable_events=True, key="-PREFER-"),],    
    ], 
    title='Options', title_color='black', relief=sg.RELIEF_SUNKEN, tooltip='ABLab随手出品：批量pdf生成文字云')],
    [
        sg.Button('开始 - 普通版', enable_events=True, key="-PROCESSINGCONVENIONTAL-"),
        sg.Button('开始 - 专业版', enable_events=True, key="-PROCESSINGPROFESSIONAL-"),
        sg.Text(size=(37, 1), key="-TOUT-"),
        sg.Button('退出', enable_events=True, key="-EXIT-")],
    [sg.Output(size=(77,5))]
    ]
window = sg.Window('【批量pdf->文字云】生成器', layout)

##############################################################################
while True:
    event, values = window.read()
    print(event, values)
    if event == "-EXIT-" or event == None:
        break
    else:
        if event == "-FOLDER-":
            window["-TOUT-"].update("已获取pdf文件所在目录"+" √")
        if event == "-IMAGE-":
            window["-TOUT-"].update("已更改文字云形状"+" √")
        if event == "-COUNTS-":
            window["-TOUT-"].update("已更改文字云偏好"+" √")
        if event == "-SCALE-":
            window["-TOUT-"].update("已更改文字云偏好"+" √")
        if event == "-FONTSIZE-":
            window["-TOUT-"].update("已更改文字云偏好"+" √")
        if event == "-PREFER-":
            window["-TOUT-"].update("已更改文字云偏好"+" √")
        if event == "-PROCESSINGCONVENIONTAL-":
            if values['-FOLDER-']=='':
                window["-TOUT-"].update("似乎发生了什么奇怪的错误。。")
            else:
                window["-TOUT-"].update("正在努力生成文字云，请稍等昂~~")
                # for i in range(100):
                #     sg.OneLineProgressMeter('正在努力生成文字云，请稍等昂~~', i+1, 100, '-DINGDINGDINGDING-')
                #----------------------------------------------------------
                dir_dict = dictPDF(values['-FOLDER-'])
                final_list = PDF2wordlist.PDF2conventionalwordlist(dir_dict)
                image_file = values['-IMAGE-']
                word_counts = values['-COUNTS-']
                pic_scale = values['-SCALE-']
                font_size = values['-FONTSIZE-']
                prefer_horizontal = values['-PREFER-']
                generatewordcloud.conventional(final_list, image_file, word_counts, pic_scale, font_size, prefer_horizontal)
                window["-TOUT-"].update("文字云已生成 √")
        if event == "-PROCESSINGPROFESSIONAL-":
            if values['-FOLDER-']=='':
                window["-TOUT-"].update("似乎发生了什么奇怪的错误。。")
            else:
                window["-TOUT-"].update("正在努力生成文字云，请稍等昂~~")
                dir_dict = dictPDF(values['-FOLDER-'])
                final_list = PDF2wordlist.PDF2professionalwordlist(dir_dict)
                image_file = values['-IMAGE-']
                word_counts = values['-COUNTS-']
                pic_scale = values['-SCALE-']
                font_size = values['-FONTSIZE-']
                prefer_horizontal = values['-PREFER-']
                generatewordcloud.professional(final_list, image_file, word_counts, pic_scale, font_size, prefer_horizontal)
                window["-TOUT-"].update("文字云已生成 √")

window.close()
##############################################################################
