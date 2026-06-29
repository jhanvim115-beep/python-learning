def show(): 
        print("Hello World") 
        show() 
        show()

        def show(): 
            print("Hello World") 
            for i in range(5): 
                show()

                def sum(): 
                    n1 = 10 
                    n2 = 20 
                    ans = n1+n2 
                    print("Sum is ", ans) 
                    sum()

                    def sum(n1, n2): 
                        ans = n1+n2 
                        print("Sum is ", ans) 
                        sum(10, 20)

                        def sum(n1, n2): 
                            ans = n1+n2 
                            return ans 
                        a1 = sum(10, 20) 
                        print("Sum is ", a1)

                        def sum(): 
                            n1 = 10 
                            n2 = 20 
                            ans = n1+n2 
                            return ans 
                        ans = sum() 
                        print("Sum is ", ans)

def sum(): 
    n1 = 10 
    n2 = 20 
    ans = n1+n2 
    return ans, n1, n2 
ans, n1, n2 = sum() 
print("n1 is ", n1) 
print("n2 is ", n2) 
print("Sum is ", ans)

def doSum(a,b): 
    ans= a+b 
    return ans 
def doSub(a,b): 
     ans= a-b
     return ans 
sum1 = doSum(20,10) 
print("Sum is ",sum1) 
sub1 = doSub(20,10) 
print("Sub is ",sub1)                        

def sum(n1=5, n2=7): 
        ans = n1+n2 
        print("Sum is ", ans) 
        sum(10, 20) 
        sum(10) 
        sum()

def show(n1, n2): 
        print("n1 is ", n1) 
        print("n2 is ", n2) 
        show(10, 20) 
        show(n2=200, n1=100)

def show(*num): 
        print(num) 
        show(10) 
        show(10, 20)
        show(10, 20, 30)

def show(*num): 
        sum = 0 
        for i in num: 
         sum = sum+i 
        print("Sum is ", sum) 
        show(10, 20) 
        show(10, 20, 30)

        def show(**num): 
         print(num) 
        show(n1=10) 
        show(n1=10,n2=20) 
        show(n1=10,n2=20,n3=30)

def show(**num): 
     for i, j in num.items(): 
      print(i, j) 
show(n1=10, n2=20)
def show(**num): 
    sum = 0 
    for i, j in num.items(): 
     sum = sum+j 
    print("Sum is ", sum) 
    show(n1=10, n2=20)

def countNumber(x): 
    if x < 5:
     x = x +1 
    print(x) 
    countNumber(x) 
    countNumber(0)