# use of Map built-in function
My_tuple=(3,2,1,7,8,9)
ans=map(lambda n:n**3,My_tuple)
print("The cube of elements of the tuple in tuple format is : ",tuple(ans))

#Use of filter built-in function
My_list=[3,4,1,2,9]
def fun(n):
    return n>1
res=filter(fun,My_list)
print("The  elements of the list in list format which are greater than 1 are : ",list(res))

# Nested-dictionary and accessing it's Keys - Values pairs serially
a={
    "name":"Pradip",
    "age":19,
    "Address":"KTM"
}
b={
    "name":"Prabin",
    "age":17,
    "Address":"Pyuthan"
}
c={
    "name":"Pratyush",
    "age":20,
    "Address":"Dang"
}
info={
    "1st":a,
    "2nd":b,
    "3rd":c
}
for i,obj in info.items():
      print(i,"Person",":",obj)
      for j in obj:
         print(j,":",obj[j]);