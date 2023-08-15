import math 

def diagonal(a, b):
    x=a*a
    y=b*b
    h=173
    k=x*h
    return (math.sqrt(x+y), k)

znach = diagonal(2, 4)

print(znach[0] + diagonal(2, 8)[0] - znach[1])

# day 2

print(" <==== day 2 ====>")

times = 0


while times != 5:
    print("work")
    times = times+1



print ("after work")

# sdhjcsjhcgs
print("vdgygwsyuu")

x=input('x = ')
x=int(x)

def fakt(x):
    # 1 * 2 * ... * x
    i = 0
    result = 1
    if x<=i:
        # print("invalid")
        #return "invalid"
        raise ValueError(f"{x} is invalid number")
    while i!=x:
        i = i+1
        result = result*i
    return result

print(fakt(x))

#correctans=[1,2,6]
x=1
i=0
while i<3:
    if fakt(x)==math.factorial(x):
        print ("correct")
    else:
        print ("byaka tu")
    assert math.factorial(x)==fakt(x)
    i = i+1
    x=x+1



i = 0
while i < 3:
    i = i + 1
