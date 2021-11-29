list=[1,-2,4,6,-8,3,-3,9]
re=[num for num in list if num>=0]
print(re)

n=int(input("enter the limit:"))
squarelist=[i**2 for i in range(1,n+1)]
print("sqaure",squarelist)

word=str(input("enter the string:"))
print("the actual string is",word)
print("vowels are:",end=" ")
for i in word:
    if i in "aeiou,AEIOU":
        print(i,end=" ")