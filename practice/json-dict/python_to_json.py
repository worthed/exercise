# -*- coding:utf-8 -*-

'''


Skipkeys：默认值是False，如果dict的keys内的数据不是python的基本类型(str,unicode,int,long,float,bool,None)，设置为False时，就会报TypeError的错误。此时设置成True，则会跳过这类key

ensure_ascii：默认值True，如果dict内含有non-ASCII的字符，则会类似'\ u XXXX'的显示数据，设置成False后，就能正常显示

indent：应该是一个非负的整型，如果是0，或者为空，则一行显示数据，否则会换行且按照indent的数量显示前面的空白，这样打印出来的json数据也叫pretty-printed json

separators：分隔符，实际上是(item_separator, dict_separator)的一个元组，默认的就是(',',':')；这表示dictionary内keys之间用“,”隔开，而KEY和value之间用“：”隔开。

encoding：默认是UTF-8，设置json数据的编码方式。  -- 已失效

# sort_keys：将数据根据keys的值进行排序。

\\'''

import json

data = {"spam" : "foo", "parrot" : 42} # Encode the data  把python对象转换成json对象

python_to_json = json.dumps(data)
print(python_to_json)

json_to_python = json.loads(python_to_json) # Decode into a Python object
print(json_to_python)


dic1 = {'type':'dic1','username':None,'age':16}
json_dic1 = json.dumps(dic1)
print(json_dic1)
json_dic2 = json.dumps(dic1, sort_keys=True, indent=4, separators=(',',':'), ensure_ascii=False, skipkeys=False)
print(json_dic2)

