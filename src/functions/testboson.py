# encoding: utf-8
"""
@author: peng_an
@time: 2016/5/7 14:49
"""
from __future__ import print_function, unicode_literals
import os
import sys

from bosonnlp import BosonNLP


# info=os.getcwd()
# listfile=os.listdir(os.getcwd())
# print listfile,
# out=open(listfile,'r')


# 使用波森语义分析api token
def emotion_analysis(context):
    nlp = BosonNLP('GrrNaeVG.6417.dsK_xHt0qE6-')
    return nlp.sentiment(context, model='weibo')


# print(nlp.sentiment(text1))
if __name__ == '__main__':
    # index = '中欧班列'
    # listfile = os.listdir(index)
    # titles = []
    # allcontext = []

    # for line in listfile:  # 把目录下的文件都赋值给line这个参数
    #     if line.startswith("index"):
    #         print("目录")
    #     elif line[-4:] == '.txt':
    #         print(line)
    #         try:
    #             file = open(index + '/' + line, 'r')
    #             context = file.read()
    #             context = context.strip()
    #             titles.append(line[0:-4])
    #             allcontext.append(context)
    #         except IOError as err:
    #             print(err)
    #         finally:
    #             file.close()
    #     else:
    #         print("非文本文件，无法分析")
    test="""
看在两个教练一边卧槽怎么还有一个远的……一边用自己家的专车把我送到校门口的份上……我就不生气了……等了一天吹了一天……头痛死了……
    """
    print(emotion_analysis(test))
    # outcomes = emotion_analysis(allcontext)
    # i = 0
    # for outcome in outcomes:
    #     print(titles[i])
    #     i += 1
    #     print('%.6f' % outcome[0], '%.6f' % outcome[1])
    #     print("")