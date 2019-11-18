

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
A7 = ''

print('A0=', A0,
    '\nA1=', A1,
    '\nA2=', A2, 
    '\nA3=', A3, 
    '\nA4=', A4, 
    '\nA5=', A5, 
    '\nA6=', A6,
    '\nA7=', A7)
    
# OUTPUT: 
# A0= {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
# A1= range(0, 10)
# A2= []
# A3= [1, 2, 3, 4, 5]
# A4= [1, 2, 3, 4, 5]
# A5= {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
# A6= [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]
# A7=



###############################################################################
###### *ARGS and **KWARGS

# *args = when we aren't sure how many arguments are going to be passed to a 
# function, or if we want to pass a stored list or tuple of arg to a function. 
# **kwargs = when we dont know how many keyword arguments will be passed to a 
# function, or it can be used to pass the values of a dictionary as keyword arg

def f(*args,**kwargs): print(args, kwargs)

l = [1,2,3]
t = (4,5,6)
d = {'a':7,'b':8,'c':9}

f()
f(1,2,3)                    
f(1,2,3,"groovy")           
f(a=1,b=2,c=3)              
f(a=1,b=2,c=3,zzz="hi")     

f(1,2,3,a=1,b=2,c=3)        
f(*t,**d)                   
f(1,2,*t)                   
f(q="winning",**d)          
f(1,2,*t,q="winning",**d)   

# OUTPUT:
# () {}
# (1, 2, 3) {}
# (1, 2, 3, 'groovy') {}
# () {'a': 1, 'b': 2, 'c': 3}
# () {'a': 1, 'b': 2, 'c': 3, 'zzz': 'hi'}

# (1, 2, 3) {'a': 1, 'b': 2, 'c': 3}
# (1, 2, 3) {'a': 7, 'b': 8, 'c': 9}
# (4, 5, 6) {'a': 7, 'b': 8, 'c': 9}
# (1, 2, 4, 5, 6) {}
# () {'q': 'winning', 'a': 7, 'b': 8, 'c': 9}
# (1, 2, 4, 5, 6) {'q': 'winning', 'a': 7, 'b': 8, 'c': 9}

def f2(arg1,arg2,*args,**kwargs): print(arg1,arg2, args, kwargs)

f2(1,2,3)                       
f2(1,2,3,"groovy")              
f2(arg1=1,arg2=2,c=3)           
f2(arg1=1,arg2=2,c=3,zzz="hi")  
f2(1,2,3,a=1,b=2,c=3)           

f2(*l,**d)                   
f2(*t,**d)                   
f2(1,2,*t)                   
f2(1,1,q="winning",**d)      
f2(1,2,*t,q="winning",**d)   

# OUTPUT:
# 1 2 (3,) {}
# 1 2 (3, 'groovy') {}
# 1 2 () {'c': 3}
# 1 2 () {'c': 3, 'zzz': 'hi'}
# 1 2 (3,) {'a': 1, 'b': 2, 'c': 3}

# 1 2 (3,) {'a': 7, 'b': 8, 'c': 9}
# 4 5 (6,) {'a': 7, 'b': 8, 'c': 9}
# 1 2 (4, 5, 6) {}
# 1 1 () {'q': 'winning', 'a': 7, 'b': 8, 'c': 9}
# 1 2 (4, 5, 6) {'q': 'winning', 'a': 7, 'b': 8, 'c': 9}