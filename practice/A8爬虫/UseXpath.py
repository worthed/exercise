# -*- coding:utf-8 -*-
'''

'''
'''
1、导入
'''

from lxml import etree

'''
2、基本使用
'''
wb_data = """
        <div>
            <ul>
                 <li class="item-0"><a href="link1.html">first item</a></li>
                 <li class="item-1"><a href="link2.html">second item</a></li>
                 <li class="item-inactive"><a href="link3.html">third item</a></li>
                 <li class="item-1"><a href="link4.html">fourth item</a></li>
                 <li class="item-0"><a href="link5.html">fifth item</a>
             </ul>
         </div>
        """

print("\n例2-----------------------------------------------:")
html = etree.HTML(wb_data)
print(html)
result = etree.tostring(html)
print(result.decode("utf-8"))
# 打印html其实就是一个打印python对象，etree.tostring(html)则补全了缺胳膊少腿的标签


'''
3、获取某个标签的内容(基本使用)，注意，获取a标签的所有内容，a后面就不用再加正斜杠，否则报错
'''
# 方法一
print("\n例3-a-----------------------------------------------:")
html = etree.HTML(wb_data)
html_data = html.xpath('/html/body/div/ul/li/a')
print (html)
for i in  html_data:
    print(i.text)

# 方法二  直接在需要查找内容的标签后面加一个/text()就行）
print("\n例3-b-----------------------------------------------:")
html = etree.HTML(wb_data)
html_data = html.xpath('/html/body/div/ul/li/a/text()')
print(html)
for i in html_data:
    print(i)

'''
4、打印指定路径下a标签的属性（可以通过遍历拿到某个属性的值，查找标签的内容）
'''
print("\n例4-----------------------------------------------:")
html = etree.HTML(wb_data)
html_data = html.xpath('/html/body/div/ul/li/a/@href')
for i in html_data:
    print(i)

'''
5、使用xpath拿到得都是一个个的ElementTree对象，所以如果需要查找内容的话，还需要遍历拿到数据的列表。查到绝对路径下a标签属性等于link2.html的内容
'''
print("\n例5-----------------------------------------------:")
html = etree.HTML(wb_data)
html_data = html.xpath('/html/body/div/ul/li/a[@href="link2.html"]/text()')
print(html_data)
for i in html_data:
    print(i)

'''
6、上面我们找到全部都是绝对路径（每一个都是从根开始查找），下面我们查找相对路径，例如，查找所有li标签下的a标签内容
'''
print("\n例6-----------------------------------------------:")
html = etree.HTML(wb_data)
html_data = html.xpath('//li/a/text()')
print(html_data)
for i in html_data:
    print(i)

'''
7、上面我们找到全部都是绝对路径（每一个都是从根开始查找），下面我们查找相对路径，例如，查找所有li标签下的a标签内容
'''
print("\n例7-----------------------------------------------:")
html = etree.HTML(wb_data)
html_data = html.xpath('//li/a//@href')
print(html_data)
for i in html_data:
    print(i)

'''
8、相对路径下跟绝对路径下查特定属性的方法类似，也可以说相同
'''
print("\n例8-----------------------------------------------:")
html = etree.HTML(wb_data)
html_data = html.xpath('//li/a[@href="link2.html"]')
print(html_data)
for i in html_data:
    print(i.text)

'''
9、相对路径下跟绝对路径下查特定属性的方法类似，也可以说相同
'''
print("\n例9-----------------------------------------------:")
html = etree.HTML(wb_data)
html_data = html.xpath('//li[last()]/a/text()')
print(html_data)
for i in html_data:
    print(i)

'''
10、相对路径下跟绝对路径下查特定属性的方法类似，也可以说相同
'''
print("\n例10-----------------------------------------------:")
html = etree.HTML(wb_data)
html_data = html.xpath('//li[last()-1]/a/text()')
print(html_data)
for i in html_data:
    print(i)






