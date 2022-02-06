#Q-1
count =1
while count<=30:
    if (count%3==0 ):
        print(count,end=" ")
    elif count%5==0:
        print(count,end=" ")
    elif (count%3==0 and count%5==0):
        print(count,end=" ")
    count+=1
    