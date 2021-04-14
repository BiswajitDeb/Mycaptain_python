n = int(input("Enter the number upto which you want the series : "))
a = 0
b = 1
sum = 0
c = 1
print("Fibonacci Series: ", end = " ")
while(c <= n):
    c += 1
    a = b
    b = sum
    sum = a + b
    print(sum, end = " ")
  