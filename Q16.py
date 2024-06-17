'''Write a program in python that counts the frequency of each character in
a string'''
str1=input("enter string")
keys=[]
vals=[]
for i in range(len(str1)):
    if(str1[i] not in keys):
        key=str1[i]

        keys.append(key)

        val=str1.count(str1[i])
        vals.append(val)
dict1=dict(zip(keys,vals))
print(dict1)