import time                     #importing time module to find time taken


arr=[[0]*25 for _ in range(25)]     #2 D array for storing known(already calculated) nCr values
                                    #size should be specified according to the domain ,here 25

count =0  
def com_dp(n,r):        #function for finding nCr using DP
    global arr
    global count
    count+=1
    if arr[n][r]!=0:        #check if already found
        return arr[n][r]
    else:               # checking base contitions for recurence
        if n==r:            
            arr[n][r]= 1
        elif r<=1:
            arr[n][r]= n
        else:       #calling recursivly
            arr[n][r]= com_dp(n-1,r-1)+com_dp(n-1,r)  
    return arr[n][r] 

n=(int(input("enter the number in order (n, r):")))
r=int(input())
print (n,r)
start=time.time()   #calculate start time
p=com_dp(n,r)
end=time.time()     #calculate end time

print "time taken for finding nCr=%f"%(end-start)   
print "number of recursive call done: %d"%count     
print "**************************"
print "\n       nCr =%d\n"%p
print "**************************"
print "\n\n\n"
for i in range(7):          #see how elemens are stored.
    print arr[i]
    