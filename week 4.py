def invword():
    Userlist = input("Enter what you want to reverse: ")
    reverse = ""
    for i in range(len(Userlist)):
        reverse += Userlist [len(Userlist) -1 -i]
    print (reverse)


invword()