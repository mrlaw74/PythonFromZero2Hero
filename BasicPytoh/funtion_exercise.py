def highest_even(li):
    try:
        highest = li[0]
        for i in range(len(li)):
            if li[i] > highest and li[i]%2 == 0:
                highest = li[i]
        return highest
    except:
        print("No element in list")
a = highest_even([1, 2, 3, 4, 5, 6, 7, 8])
# a = highest_even([])
print(a)