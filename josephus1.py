nprisoners=int(input("How many prisoners are there?"))
step=int(input("each prisoner kills how many per turn?: (default 2)"))
lprisoners=list(range(1, nprisoners+1)) #creates the list of prisoners
index=0
def solve(index,prisoners): 
    if len(prisoners)<=1:      #checks whether there is only one prisoner left
        return(prisoners[0]) 
    survivors=[] 
    while index<len(prisoners):   #adds all survivors of current round
        survivors.append(prisoners[index])
        index+=step
        
    index%=len(prisoners) #handles index overflow

    print(survivors)
    return(solve(index,survivors))
        

    
print(solve(index,lprisoners))
    
    
    
