f = lambda : 1
g = lambda x , y : x * y
increase = lambda  x, inc = 1 : x + inc
vargs = lambda x, *args : args
kwords = lambda x , *args, **kw : kw


print(kwords(1 , 2 , 3 , a = 4 ,b = 5))