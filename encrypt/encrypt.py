import random
'''take input sentence'''
print("Enter message to be encrypted:")
message=input()
encrypt=list(message)
'''form a dictionary for all aphabet values'''
alpha1=list('abcdefghijklmnopqrstuvwxyz')    
alpha2=alpha1[:]
dictionary={}
for i in alpha1:
    dictionary[i]=random.choice(alpha2)
    alpha2.remove(dictionary[i])
for i in range(len(encrypt)):
    if message[i]==' ':
        continue
    else:
        encrypt[i]=dictionary[encrypt[i]]
encrypt=''.join(encrypt)
print("The encrypted message is: "+encrypt) #encrypted message
'''getting back the real message'''
decrypt = {v: k for k, v in dictionary.items()}   #creating an inverse dictionary
real=''
for i in encrypt:
    if i==' ':
        real+=' '
    else:
        real+=decrypt[i]
print("Real message is: "+real)
