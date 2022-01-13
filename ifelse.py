a =int(input("Enter a number: "))
if (a%3==0):
    print("Divisible by 3")
else:
    print("Not divisible by 3")

a = 'hai'
dic = {
    'mot': 1,
    'hai': 2,
    'ba': 3,
}
print(dic.get(a,'khong ro')) # get() method, if not have a in dic, will print "khong ro"
# Ket Qua: 2