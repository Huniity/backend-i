def sum_args(*args):
    return sum(args)

print(sum_args(1, 2, 3, 4,5,6,7,8,7,6,4,3,32,4,56,7,8)) 


def dict_kwargs(*arg, **kwargs):
    for key,value in kwargs.items():
        print(value)
    

dict_kwargs(3,a=1, b=2, c= 3, d= "Hello", e= "World", f= False)


##################### CHALLENGE ##################### 


def example_function(*args, **kwargs):
    print(kwargs[args])
example_function("aluno", "Web Dev",name='Alice', age=30, pw="ahsuahsq837123tgeud")