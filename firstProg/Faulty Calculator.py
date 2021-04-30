print ("faulty calculator")
# correct all the calculation accept this
# { 54*34 =32143 , 66+55 = 43534 , 78 *3 54367 , 56-56 = 12234, 25/5= 50}
print("your first digit")
x = int(input())
print("your second digit")
y = int(input())
print("write the  type of calculation +, *, -,/  ")
q = str(input())

#78 *3 54367    54*34 =32143

if q == ('*'):

    if x==54 and y==34 or x==34and y==54 :
        print("your answer is 32143")
    if x==78 and y==3 or x==3 or y==78:
        print("your answer is 54367")
    else:
        print("your anwer is")
        print(x*y)

#66+55 = 43534
if q==('+'):
    if x==66 and y==55 or x==55 and y==66:
        print('your answer is 43534')
    else:
        print('your answer is')
        print(x+y)
#56-56 = 12234
if q==('-'):
    if x==56 and y==56 or x==56 and y==56:
        print("your answer is 12234")
    else:
        print("your answer is")
        print(x-y)
if q==('/'):
    if x==25 and y==5:
        print("your answer is 50")
    else:
        print("your answer is ")
        print(x/y)

print("thank you")