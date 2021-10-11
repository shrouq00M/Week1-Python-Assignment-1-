

#1. Basic 

for x in range(1,151):
    print(x)

#2. Multiples of Five 

for x in range(5,1001):
    print(5*x)
    


#3. Counting, the Dojo Way 

for x in range (1,101,1):
    if x % 5 == 0:
        print('Coding')
    if x % 10 == 0:
        print  ('Dojo')


#4. Whoa. That Sucker's Huge 

sum = 0
for x in range(0,500001):
    if x % 2 != 0:
        sum = sum + x
        
print("the sum of all odd number from 0 to 50000 is {}".format(sum))


#5. Countdown by Fours 

for x in range(2018,0,-4):
    print(x)

#6. Flexible Counter (optional) 

lowNum = 2
highNum = 9
mult = 3

for i in range (lowNum,highNum+1,1):
    if i % mult == 0 :
        print(i)

 
