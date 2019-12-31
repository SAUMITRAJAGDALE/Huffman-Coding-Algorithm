import os
import sys
import numpy as np

text=input('Enter the text:')
print(text)
unique_char=[]
for x in text:
    if x not in unique_char :
        unique_char.append(x)

freq=[]

for i in range(0,len(unique_char)):
    freq.append(text.count(unique_char[i]))

print(unique_char)
print(freq)
tot=sum(freq)
prob=[]

for i in range(0,len(freq)):
    prob.append(freq[i]/tot)

print(prob)

dprob=prob

for i in range(0,len(dprob)+1):
    for j in range(0,len(dprob)-i-1):
        if dprob[j]>dprob[j+1]:
            temp=dprob[j]
            dprob[j]=dprob[j+1]
            dprob[j+1]=temp
            tmp=unique_char[j]
            unique_char[j]=unique_char[j+1]
            unique_char[j+1]=tmp
        
print(dprob)
print(unique_char)
codeword=[]
for i in range(0,len(unique_char)):
    codeword.append('')
huffman=list(zip(dprob,unique_char,codeword))

for i in range(0,len(unique_char)):
    huffman[i]=list(huffman[i])
print(huffman)
n=len(unique_char)


'''
for i in range(0,len(unique_char)-2):

    
    a[i+1][len(a[i])-i-2][1]=a[i][len(a[i])-i-1][1]+a[i][len(a[i])-i-2][1]
    a[i+1]=sorted(a[i+1],reverse=True)
    a[i+1].pop()
    print(a)
'''
print(min(huffman))
a=[[''],['']]
for i in range(0,len(unique_char)):
    huffman.append(a)
print(huffman)

'''
for i in range(0,len(unique_char)-1):
    huffman[0][]
    
   ''' 









    



    




    









'''a=sorted(prob,reverse=True)
print(a)
'''