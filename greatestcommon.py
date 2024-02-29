print("Enter two string to calculate greatest common...")
str1=str(input("Enter first string :"))
str2=str(input("Enter second string :"))
i,j=0,0
stack=[]
while i<len(str1) and j<len(str2):
    if str1[i]==str2[j]:
        stack.append(str1[i])
        i+=1
    else:
        j+=1

print(set(stack))