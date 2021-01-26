# ReadMe File

[![standard-readme compliant](https://img.shields.io/badge/ABLabPickME-v2021.01.16-brightgreen.svg?style=flat-square)](https://github.com/peachRL/ABLabWordCloud_GUI)

- [ReadMe File](#readme-file)
  - [背景](#背景)
  - [安装](#安装)
  - [使用说明](#使用说明)
    - [环境](#环境)
    - [使用](#使用)
    - [界面和ico](#界面和ico)
  - [维护者](#维护者)
  - [使用许可](#使用许可)

## 背景

ABLabWordCloud小程序为ABLab实验室2020年终报告合集提供了文字云图。

## 安装

该项目使用Python编写，有图形化界面但无exe版本。请在windows系统中运行ABLabWordCloud_GUI.py使用。

## 使用说明

### 环境

**首先进入requirements文件夹，将requirements.txt中的包都装上。**

```shell
pip install -r requirements.txt
```

### 使用

按照程序的条目依次输入，然后点“开始”即可。“开始”分为**普通版**和**专业版**，区别在于专业版去除了一些生活词，两者的输出文件分别为“ABLab_WordCloud_conventional”和“ABLab_WordCloud_professional”。

### 界面和ico

界面由PySimpleGUI生成，没有ico。

<img src="https://img.imgdb.cn/item/600e87503ffa7d37b3f79806.png" alt="界面" style="zoom:50%;" />

## 维护者

[@peachRL](https://github.com/peachrl)


## 使用许可

[MIT](LICENSE) © peachRL

