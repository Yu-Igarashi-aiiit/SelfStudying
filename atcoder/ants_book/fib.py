
#フィボナッチ数列
#遅い
def fact(n):
    if(n==0):
        return
    return n*fact(n-1)

#メモ探索
memo = [0]*(MAX_N+1)
def fib(n):
    if n<=1:
        return n
    if memo[n] != 0 :
        return memo[n]
    return memo[n] = fib(n-1) + fib(n-2)
