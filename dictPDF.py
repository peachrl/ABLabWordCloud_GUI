# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 16:54:14 2021

@author: peachrl
"""

import os

# 切换到pdf文件所在目录
#os.chdir(input_dir);
# 回到当前脚本所在目录
#os.chdir(os.path.abspath(os.path.dirname(sys.argv[0])))
#input_dir = "E:/Python/ABLab_WordCloud/pdf"
def dictPDF(input_dir):
    # 筛选pdf文件
    filter = [".pdf"]  # 设置过滤后的文件类型 当然可以设置多个类型
    def all_path(dirname):
        result = []
        for maindir, subdir, file_name_list in os.walk(dirname):
            for filename in file_name_list:
                apath = os.path.join(maindir, filename)  # 合并成一个完整路径
                ext = os.path.splitext(apath)[1]  # 获取文件后缀；[0]获取的是除了文件名以外的内容
    
                if ext in filter:
                    result.append(apath)
            #break
        return result
    
    # 提取pdf文件的路径与文件名
    data_path = all_path(".")
    file_dict = {}
    for file_path in data_path:
        file_name = file_path[file_path.rindex('\\') + 1:len(file_path)]
        file_name = file_name[:file_name.index(".pdf")]
        file_dict[file_path] = file_name
    return file_dict