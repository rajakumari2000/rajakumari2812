

def read_data():

    f=open("aug22.txt","r")
    data=f.read()
    x=data.split(",")
    #y=x.count("unpaid")
    #print(y)
    paid=[]
    unpaid=[] 
    for i in x:
        if i=="paid":
            paid.append(i)
        else:
            unpaid.append(i)
    print(f"paid data's->{len(paid)}") 
    print(f"unpaid data's->{len(unpaid)}")  
read_data()          
             


