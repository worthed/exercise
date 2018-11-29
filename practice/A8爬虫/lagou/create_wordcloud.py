# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/11/24 下午8:21
IDE：PyCharm
描述：制作词云
"""
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from support.common.connect.connect_db.ConnectDB import localhost_query
import jieba

#work_duty = "充分参与整个开发流程，从制定测试计划到产品上线最后一道关卡的把控，在此基础上，配合相关人员，提供针对于产品结构及功能的指导意见主要参与测试app和we应用/对新鲜事物有兴趣且能够踏下心来去做，在有资源有条件的情况下，愿意接触自动化测试/"
#work_requirement = "熟悉黑白盒测试的流程及过程管理，（编写测试用例 bug跟踪 搭建测试环境 编写缺陷等）/实际项目中用过至少二种较为流行的自动化测试工具，如Selenium/熟悉linux，能够编写基本的shell脚本/熟悉基本的网络协议，对udp，tcp协议有基础的理解，对应用层的协议有基本理解/熟悉SQL及常用数据库，如nosql：redis，mongo对批量导入测试数据，或者编写测试数据脚本有过了解/知悉如何使用jmeter（RoadRunner）进行性能方面的测试/年以上web测试经验，年以上app测试经验/熟练掌握Docker，jenkins以及公有云的使用者优先/"

def create_wordcloud(info):
    wordlist = jieba.cut(info,cut_all=False)  # 采用精确模式
    # 设置停止词
    stopwords = set('')
    stopwords.update(['测试','进行','参与','工作','根据','完成','熟悉','优先','以上学历',
                      '具备','常用','掌握','熟练使用','了解','以上','一定','能够','基本',
                      '良好','相关'])
    text = " ".join(wordlist)

    wordcloud = WordCloud(
        width=400,
        height=200,
        background_color = "black", # 背景颜色
        max_words = 50, # 最多词个数
        stopwords = stopwords, #设置停用词
        font_path = "/Users/wangyuxiang/Library/Fonts/msyh.ttf", # 中文字体
        max_font_size = 60,  # 字体最大值
        random_state = 30, # 配色方案

    ).generate(text)

    process_word = WordCloud.process_text(wordcloud,text)

    # 获取文本词频最高的前10个词
    sort = sorted(process_word.items(),key=lambda e:e[1],reverse=True)
    print(sort[:10])

    # 存储和展示
    wordcloud.to_file('cloud.jpg')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


if __name__ == '__main__':
    get_info_sql = "select jobs_lagou_info_work_duty,jobs_lagou_info_work_requirement from jobs_lagou_info " \
                   "inner join jobs_lagou_position on jobs_lagou_position_positionId = jobs_lagou_info_positionId " \
                   "where jobs_lagou_position_positionType = '测试';"

    get_work_requirement_sql = "select jobs_lagou_info_work_requirement from jobs_lagou_info " \
                               "inner join jobs_lagou_position on jobs_lagou_position_positionId = jobs_lagou_info_positionId " \
                               "where jobs_lagou_position_positionType = '测试';"

    all_work_duty = localhost_query(get_info_sql)
    work_duty = ""
    work_requirement = ""

    for i in all_work_duty:
        work_duty = "".join([work_duty,i[0]])
        work_requirement = "".join([work_requirement,i[1]])

    # 去掉空格
    work_duty.replace(' ','')
    work_requirement.replace(' ', '')

    create_wordcloud(work_duty)
    create_wordcloud(work_requirement)


