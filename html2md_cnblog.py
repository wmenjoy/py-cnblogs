import os
import sys
import re
import getopt
import html2text
from bs4 import BeautifulSoup
# 将CNBLOGS上的HTML格式的博客文章转换为Markdown格式
# Author: Wang shiqiang
# Email: cocowool@qq.com

# 入口函数，支持输入文件名和输入目录两种方式进行文件转换
def main(argv):
    try :
        opts,args = getopt.getopt(argv,"hf:d:",["file=","diretory="])
    except getopt.GetoptError:
        print("Usage: python html2md_cnblog.py -file <filename> -folder <folder_path>")

    for opt, arg in opts:
        if opt in ("-f", "--file"):
            html2md(arg)
            pass
        elif opt in ("-d", "--directory"):
            print(arg)
            pass
        else:
            print("Usage: python html2md_cnblog.py -file <filename> -folder <folder_path>")



# 将HTML文件转换为MD文件
def html2md(income_file, outcome_file = ""):
    # 打开文档
    file = open(income_file, 'r')
    article = file.read()


    h2md = html2text.HTML2Text()
    h2md.ignore_links = False
    article = h2md.handle(article)

    with open("./output.md", "w", encoding='utf8') as f:
        lines = article.splitlines()
        for line in lines:
            if line.endswith('-'):
                f.write(line)
            else:
                f.write(line+"\n")

if __name__ == "__main__":
    # print(__name__)
    main(sys.argv[1:])