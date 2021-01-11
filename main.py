# list1=[1,1,1,1,1,1,1,6,6,6,6,6,6,3,3,'n','n','n','n','n','s','a','a','a','a','w','w',1,6,7,10]
# list2=set(list1)
# print(list2,len(list2))
# dict1={i:list1.count(i) for i in list1}
# print(dict1)
#
#
# list1=[1,1,1,1,1,1,1,1,1,14,4,4,4,4,4,4,4,4,7,7,7,7,7,7,7,7,7,7,7,7,7,9,9,9,9,9,9,9,9,9,9,9,5,5,5,5,5,5,5,5,5,5,5,5,5,5,10,10,10,10,3,3,3,12,12,12,12,12,12,12,12,18,18]
# dict1=set(list1)
# print(list(dict1))
# dict1_1=[]
# for i in range(len(dict1)+1):
#     if i!=0:
#         dict1_1.append(i)
# print(dict1_1)
# dict1_2=dict(zip(dict1_1, dict1))
# print(dict1_2)
# dict2={i:list1.count(i) for i in list1}
# print(dict2)
# for key, val in dict1_2.items():
#     for i in dict2:
#         if i == val:
#             print(key, ":", val, ",", dict2[i])
#
#
# dict1={"age":'13', "name": "sofi", "town": "krasnodar"}
# dict2={'street': 'promishlennaya', 'cat': "Tima"}
# # dict3=dict1.update(dict2)
# # print(dict1)
# def sumdict(dict1, dict2):
#     dict3=dict1.update(dict2)
#     return dict1
# print(sumdict(dict1,dict2))
#
#
# str1="Привет, как, твои, дела, сегодня"
# def magic(str1):
#     list1=str1.split(',')
#     return list1
# print(magic(str1))
#
#
# a='345'
# def summ(a):
#     s=str(a)
#     l=list(s)
#     for i in range(len(l)):
#         l[i]=int(l[i])
#     suml=sum(l)
#     return suml
# print(summ(a))
#
#
# dict1={"age":'13', "name": "sofi", "town": "krasnodar"}
# dict2={'street': 'promishlennaya', 'cat': "Tima"}
# def aboutme(dict1,dict2):
#     print('\033[35m {}'.format(dict1))
#     print('\033[36m {}'.format(dict2))
# print(aboutme(dict1,dict2))
#
#
# dict1={"age":'13', "name": "sofi", "town": "krasnodar"}
# def change(dict1):
#     dict2={v:k for k,v in dict1.items()}
#     return dict2
# print(change(dict1))
#
#
# list1=[11,45,11,56,78,34,45,893]
# def tuple1(list1):
#     listsum=[]
#     for i in list1:
#         if i not in listsum:
#             listsum.append(i)
#             listsumrev=listsum[::-1]
#             a=tuple(listsumrev)
#     return(a)
# print(tuple1(list1))
#
#
# list1=[33, 15, 1000, 67, 78, 45, 67, 98, 57]
# list2=[8, 15, 1000, 92, 78, 45, 56, 98, 75]
# listnew=[]
# for i in list1:
#     for j in list2:
#         if i==j:
#             listnew.append(i)
# listsorted=sorted(listnew)
# print(listsorted)
#
#
# list1=[1, 2, 3, 4, 5, 5, 5, 3, 2, 3, 7, 8, 10]
# list2=[]
# for i in list1:
#     if i not in list2:
#         list2.append(i)
#         print('No')
#     else:
#         print("Yes")
#
#
# list1=[1, 2, 3, 4, 5, 5, 5, 3, 2, 3, 7, 8, 10]
# def summalist(list1):
#     sum1=sum(list1)
#     aver=sum1/len(list1)
#     return aver
# print(summalist(list1))
#
#
# a=34555
# def razryd(a):
#     a1=len(str(a))
#     return a1
# print(razryd(a))
#
#
# a=345667
# def summa(a):
#     a1=str(a)
#     a2=list(a1)
#     b=[]
#     for i in a2:
#         i=int(i)
#         b.append(i)
#     sum1=sum(b)
#     return sum1
# print(summa(a))
#
#
#
# i = int(input('Веедите номер месяца  '))
# def month_to_season(i):
#     if 1 <= i <=2 or i == 12:
#         print("зима")
#     elif 3 <= i <= 5:
#         print("весна")
#     elif 6 <= i <= 8:
#         print("лето")
#     elif 9 <= i <= 11:
#         print('осень')
#     else:
#         print('недопустимый диапазон')
#     return
# print (month_to_season(i))
#
#
# list1=[1, 2, 3, 4, 5, 5, 5, 3, 2, 3, 7, 8, 10]
# def dubl(list1):
#     if len(list1)>len(set(list1)):
#         i=print("Дубликаты имеются")
#         return(i)
# dubl(list1)
#
#
# list1=[1, 2, 3, 4, 5, 5, 5, 3, 2, 3, 7, 139, 8, 9, 10]
# def listN(list1):
#     list2=[]
#     for i in list1:
#         if i%2!=0:
#             list2.append(i)
#         if i==139:
#             break
#     return (list2)
# print(listN(list1))
#
#
# a = int(input('Введите первое число A '))
# b = int(input('Введите второе число B '))
# operation = str(input('Введите операцию '))
# def calc(a,b, operation):
#
#     if operation == "+":
#         result = a+b
#     elif operation == "-":
#         result = a-b
#     elif operation == "*":
#         result = a*b
#     elif operation == "/":
#         result = a/b
#     else:
#         result="Операция не поддерживается"
#     return result
# print(calc(a,b, operation))

# from PIL import Image, ImageDraw      - посмотреть не получилось
#
# canvas = Image.new("RGB", (1000, 1000), (255, 0, 0))
# paint_brush = ImageDraw.Draw(canvas)
# paint_brush.line((0, 0, 1000, 1000), fill=(255, 0, 255), width=10)
# paint_brush.ellipse((0, 0, 1000, 1000), (0, 255, 0))
# paint_brush.rectangle((0, 0, 1000, 1000), (0, 0, 255))
# canvas.save('canvas.png')






