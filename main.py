def fact_num(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact_num(n-1)
number=int(input("Enter the value:"))
res=fact_num(number)
print("The factorial of{}is{}".format(number,res))