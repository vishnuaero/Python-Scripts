#montypython provlem
count1=0
count2=0
count3=0
count4=0
count_no_of_times=1    #no of times the program is executed
def monty_python():
    import random
    import time
    global count1
    global count2
    global count3
    global count4
    global count_no_of_times
    
    door_list=[1,2,3]
    yes_list=['y','Y','yes','ys','Yes','ya',""," "]
    no_list=['n','no','No','NO','N','na']

    while True:
        try:    
            player_guess=int(input("Choose from one of the Doors 1, 2 or 3: "))
            break
        except:
            print("Please enter one of the following numbers: 1, 2 or 3")
    door_w_car=random.randint(1,3)
    #print("door w car",door_w_car)
    
    if player_guess not in door_list:
        print("Please choose from the doors 1, 2 or 3")
        monty_python()
    else:
        for door in door_list:
            if door!=player_guess and door!=door_w_car:
                door_with_goat=door
        print("Now the host will open this door :",door_with_goat)
        time.sleep(2.0)
        print("...See this door is empty")
        time.sleep(1.5)
        second_response=input("do you wan to change the selection?y or no : ")

        if second_response not in no_list:
            for door in door_list:
                if door!= player_guess and door!=door_with_goat:
                    player_second_guess=door
            if door_w_car==player_second_guess:
                print("congrats u have won the car X")
                time.sleep(1.5)
                print("door",door_w_car," had the car  X")
                count1=count1+1
            else:
                 print("sorry u lose XX")
                 time.sleep(1.0)
                 print("door",door_w_car," had the car XX")
                 count2=count2+1

        elif second_response in no_list:
                if player_guess==door_w_car:
                    print("congrats u have won the car XXX")
                    time.sleep(2.0)
                    print("door",door_w_car," had the carXXX")
                    count3=count3+1
                else:
                    print("sorry u loseXXXX")
                    time.sleep(2.0)
                    print("door",door_w_car," had the carXXXX")
                    count4=count4+1
        print("___")
        print("times player changed and guessed corect 2ndtime:",count1,'/',count_no_of_times)
        print("times player changed and lost:", count2,'/',count_no_of_times)
        print("times player went w his first guess and won: ",count3,'/',count_no_of_times)
        print("times player wnt w his first guess and LOST: ", count4,'/',count_no_of_times)
        time.sleep(1.0)
        restart=input("Do u wanna start again?: y or n?: ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        count_no_of_times=count_no_of_times+1

        if restart not in no_list:
            monty_python()
        elif restart in no_list:
            #count1 and 4 are similar;count 2 and 3 are similar
            #p1,probily of winning by changing guess is the same as losing by sticking w intial guess
            #p2,probabilty of winning by stickn w inital guess is same as losing whn u change the door
            p1=(count1+count4)/(count_no_of_times-1)
            p2=(count2+count3)/(count_no_of_times-1)
            print("By changing your first guess u won",p1,"times")           
            print("By sticking w ur first guess u won",p2,"times")
            #exit()
        
    
monty_python()
