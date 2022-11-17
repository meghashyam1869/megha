import pdb

def addition(a,b):
    answer = a * b
    return answer

pdb.set_trace()
x = input("enter first number: ")
y = input("enter second number: ")
sum=addition(x,y)
print(sum)
