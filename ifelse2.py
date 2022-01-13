score = float(input("Enter Score: "))
if (score>=0 and score <= 10):
    if(score < 5):
        print("HS yeu")
    elif (score >= 5 and score < 6.5):
        print("HS trung binh")
    elif (score >= 6.5 and score < 8):
        print ("HS kha")
    else:
        print("HS gioi")
else:
    print("Score out of range")