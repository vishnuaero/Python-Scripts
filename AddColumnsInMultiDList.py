#Add coluns in a mutli D list
def add_cols(sample_list):
    my_list2=[]
    my_list3=[]
    q=len(sample_list)
    for inner_list in sample_list:
        k=len(inner_list)
    for j in range(k):
        for i in range(len(sample_list)):
               my_list2.append(sample_list[i][j])
               print(my_list2)
    for p in range(0,len(my_list2),q):
        chunk=my_list2[p:p+q]
        #print(p,p+q)                #this will splicethe list into chunks of q
        print(chunk)           #q should be the no of inner lists
        my_max=max(chunk)
        my_list3.append(my_max)
    print(my_list3)
    #max_val=sum(my_list2)
    #return(max_val)

        
        







sample_list=[[34,23,4235,56],[33,612,103,24],[405,607,812,333],[-11,0,3,-1]]
add_cols(sample_list)






    
