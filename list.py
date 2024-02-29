List= [1,11,111,111.11,"hello world"]
print(List)
print(List[0]) 
print(List[-1]) #Negetive Index

List2=[[1,2,3],[4,5,6]] #Multidimentional List
print(List2)
print(List2[0])
print(List2[1])

List2.append(List) #Append Lists
print(List2)

List2.remove(List2[1])
print(List2)


tpl=("Hi","This is a tuple")
print(tpl)

#Dictionary
Dict={"Name":"Shafiq","Language":"Python"}
print(Dict)
print(Dict["Name"])
print(Dict["Language"])