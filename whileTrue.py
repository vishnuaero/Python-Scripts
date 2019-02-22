def max_of_list():
    my_list=[]
    while True:
        try:
            i=int(input("ENter a number, just press enter when done:"))
            my_list.append(i)
        except ValueError:
            j=max(my_list)
            print(my_list,j)
max_of_list()
              
