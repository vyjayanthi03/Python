# def welcome(name):
#     print(name)
# welcome('python')

def value(num,num1):
    return num+num1
print(value(1,3))


def evenodd(no):
    if(no % 2==0):
        print ("even no")
    else:
        print ("odd")

evenodd(8)
evenodd(87)

def valu(nos):
    for i in nos:
        print(i)
lis=[1,2,3]
valu(lis)


def funcc(value="parameter ?t"):
    print(value)
funcc()
funcc(1)

def funcc(value="parameter ?t"):
    pass

def fun(*num1):
    print(num1)
fun(1,2,3,4)


def fun1(*num1):
    print(num1)
fun1(num1=1)

