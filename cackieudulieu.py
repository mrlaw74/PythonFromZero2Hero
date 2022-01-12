# Python cũng giống như một số các ngôn ngữ bậc cao khác, khi ta khai báo biến thì 
# kiểu dữ liệu của nó sẽ tự động được detect. 
# Vì vậy nên chúng ta cũng không phải quá vất vả khi khai báo 1 biến

#Kiem tra kieu du lieu type()

name = "Vũ Thanh Tài"
#string

age = 22
#integer

point = 8.9
#float

option = [1,2,3,4,5]
#lists

tuple = ('Vũ Thanh Tài', 22 , True)
#Tuple

dictionary = {"name": "Vu Thanh Tai", "age": 22, "male": True}
#Dictionary

#Ep kieu du lieu: 
age = 10

# ép sang float
floatAge = float(age)
print(type(floatAge))

#ép sang integer.
intAge = int(age)
print(type(intAge))

#ép sang chuỗi.
strAge = str(age)
print(type(strAge))