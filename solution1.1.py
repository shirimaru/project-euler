x = 0 #this creates a bucket starting from zero
for i in range(1000): #this checks every number from 0 to 999
  if(i%3==0 or i%5==0): #this finds all the i which are multiples of 3 or 5
    x = x+i #this adds each i in the previous step to x i.e. 0 
    print(x) #this prints each x=0 added with each i in step 3
