# ------Basic---------
for i in range(0,151):
    print(i)
    # ------multiple of 5--------
for v in range(5,1001,5):
    print(v)
# Counting, the Dojo Way -
for n in range (1,101):
    if n%5==0:
        print("coding")
    elif n%10==0 :
        print("coding dojo")
    else :
        print(n)
# Countdown by Fours -
for i in range(2018,0,-4):
    print(i)      
# Flexible Counter - 
lowNUM = 1
highNUM = 10
mult = 2
for num in range(lowNUM,highNUM + 1) : 
    if num%mult==0:
        print(num)