story befor i aske you any qustion
give him 3 choices
1:
2:
3:
 """

user_input = input(
    "chouse one from this three options: \n 1: \n 2: \n 3: \n right here type : 1 or 2 or 3 : ")


def first():
    #text 
    #2 choices
    first_disition = input("chouse one from this tow options : \n 1: \n 2: \n right here type : )
    if first_disition == "1":
        #text 
        #2 choices
        pass
    elif first_disition == "2":
        #text 
        #2 choices
        secund_choice = input("chouse one from this tow options : \n 1: \n \ ")
        if secund_choice == "1":
            second()

        pass
    else:
        print("you have to chouse 1 or 2 or 3 to begin the story")
    pass

def second():
    #text 
    #3 choices
    pass

def third():
    #text 
    #2 choices
    pass

if user_input == "1":
    first()
elif user_input == "2":
    second()
elif user_input == "3":
    third
else:
    print("you have to chouse 1 or 2 or 3 to begin the story")