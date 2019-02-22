#My name is Vishnu->mY nAmE iS vIsHnU
def spongebob_meme(string):
    a=''
    b=""
    d="..!#$!"
    e=""
    #c=""
    for i in range(len(string)):
        #print(string[i])
            if i%2==0:
                b=b+string[i].lower() #letters at even positioned are lower cased
            #print(b)        
            else:
            #print(string[i])
            #string[i].upper()
                b=b+string[i].upper()   # letters at odd places are upper cased
            #print(a)
            c=''.join(b)
    e="".join((c,d))
        
    print(e) 
    
string=input("Enter something:")
spongebob_meme(string)
