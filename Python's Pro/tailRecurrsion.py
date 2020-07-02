# 꼬리제귀 공부 꼬리 제귀의 경우에는 stack의 활용을 극적으로 낮출수 있다.
def FactorialTail(n , acc) :
    if n == 1 :
        return acc
    return  FactorialTail(n - 1 , acc * n)

def Factorial(n):
    return FactorialTail(n , 1)
