def check_length(num):
    count=0
    while num!=0:
        num=num//10
        count+=1
    return count

    

    

num=int(input(":Enter a number: "))    
print(f"Length of number is: {check_length(num)} ")
