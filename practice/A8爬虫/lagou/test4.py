# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/11/24 下午8:21
IDE：PyCharm
描述：
"""
import matplotlib.pyplot as plt
from wordcloud import WordCloud

import jieba

work_duty = "充分参与整个开发流程，从制定测试计划到产品上线最后一道关卡的把控，在此基础上，配合相关人员，提供针对于产品结构及功能的指导意见主要参与测试app和we应用/对新鲜事物有兴趣且能够踏下心来去做，在有资源有条件的情况下，愿意接触自动化测试/"
work_requirement = "熟悉黑白盒测试的流程及过程管理，（编写测试用例 bug跟踪 搭建测试环境 编写缺陷等）/实际项目中用过至少二种较为流行的自动化测试工具，如Selenium/熟悉linux，能够编写基本的shell脚本/熟悉基本的网络协议，对udp，tcp协议有基础的理解，对应用层的协议有基本理解/熟悉SQL及常用数据库，如nosql：redis，mongo对批量导入测试数据，或者编写测试数据脚本有过了解/知悉如何使用jmeter（RoadRunner）进行性能方面的测试/年以上web测试经验，年以上app测试经验/熟练掌握Docker，jenkins以及公有云的使用者优先/"



wordlist = jieba.cut(work_duty,cut_all=True)
wl = " ".join(wordlist)
print(wl)
wordcloud = WordCloud(background_color = "black", #设置背景颜色
               #mask = "图片",  #设置背景图片
               max_words = 2000, #设置最大显示的字数
               #stopwords = "", #设置停用词
               font_path = "/Users/wangyuxiang/Library/Fonts/msyh.ttf",
        #设置中文字体，使得词云可以显示（词云默认字体是“DroidSansMono.ttf字体库”，不支持中文）
               max_font_size = 50,  #设置字体最大值
               random_state = 30, #设置有多少种随机生成状态，即有多少种配色方案
).generate(wl)

wordcloud.to_file('cloud.jpg')

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

plt.show()