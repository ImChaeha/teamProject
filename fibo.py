!#usr/bin/python

def fibo(n):
    n= int(input("fibonacci number: "))
    a, b = 1, 1
    for i in range(n):
        print(a, end = ' ')
        if i==n-1:
          print("\nF",n, "=",a)
        a, b = b, a+b
if__name=="__main__":
  print()
