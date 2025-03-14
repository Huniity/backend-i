def cenas(a:str, b:int, c:bool = False):
    print(a,b,c)

def cenas2(a,b,c=None,*args):
    print(type(args))
    print(a,b,c,*args)


a = "ola"
b = 3.14
c = True

cenas2(a,b,c,1,2,3,4,5,6)
cenas2(1,2,3,4,5,c=a, a=b, b=c)


