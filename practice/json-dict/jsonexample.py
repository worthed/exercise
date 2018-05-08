# -*- coding:utf-8 -*-
'''

'''

import json

data = {"order_id":"201832455731316621","loan_type":7,"user_id":1715454,"consignee_id":None,"loan_product":{"borrower_money":2000.00,"pay_way":1,"borrower_term":30,"behead_amount":0,"total_service_fee":50.83},"loan_basic_information":{"user_name":"张文俊","certificate_type":1,"certificate_number":"362233199601233014","bank_card":"6236682120001309694","phone_number":"18172969867","id_card_front_picture":"http://paydayloan-10000035.file.myqcloud.com/2017/04/02/170402_161751_897","id_card_after_picture":"http://paydayloan-10000035.file.myqcloud.com/2017/04/02/170402_161810_445","sex":1,"education":4,"marriage_status":1,"contact_phone":"18172969867","emergency_contact":[{"emergency_contact_name":"张龙","emergency_contact_relation":"父母","emergency_contact_phone":"15909463518"}],"loan_compact":"","loan_purpose":3,"company_name":"赣州鼎力房地产咨询代理有限公司","company_address":"江西省赣州市信丰县府东路41号","company_phone":"0797-3388890","profession":"服务业/其他"},"partner_fields":{}}
#json_to_python = json.loads(data)
#print(data)
#print(data.get("order_id"))


print(k)  # 遍历字典的key
print(data.get(k))  # 遍历字典的value
print(type(k))
print(data["loan_product"]["pay_way"])  # 字典里的字典取值
print(data["loan_basic_information"]["emergency_contact"][0]["emergency_contact_relation"])  # 字典中的字典取值






