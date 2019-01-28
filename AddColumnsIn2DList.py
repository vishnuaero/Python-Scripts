#Add columns in a row
def add_columns(sample_list):
    # Solution type 1:
    # return [max(col) for col in zip(*sample_list)]
    # Alternative Solution
    cols = len(sample_list[0])
    mylist = []
    for c in range(cols):
        column_sum = 0
        for row in sample_list:
            column_sum += row[c]
        mylist.append(column_sum)
    print(mylist)
    
sample_list=[[34,23,45,56],[33,12,103,24],[45,-37,37-45]]
add_columns(sample_list)
