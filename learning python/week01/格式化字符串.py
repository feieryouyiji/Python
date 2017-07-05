name = input("请输入姓名:")
age = input("请输入年龄:")
job = input("请输入职业:")
print(type(age))
info1 ='''
你的信息如下:
name : %s 
age : %s 
job : %s
''' % (name,age,job)

info2 ='''
你的信息如下:
name : {_name}
age : {_age} 
job : {_job}
'''.format(_name=name,_age=age,_job=job)
print(info1)
print("------------------")
print(info2)
