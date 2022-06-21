'''
Trickiest problem, hehehe..!!
Accept two strings, variable1 and variable2 create a new string variable3 made of the first char of variable1, then the last char of variable2,
Next, the second char of variable1 and second last char of variable2, and so on.
Eg: a = "Japan"
b = "china"
O/p:- c = "Jaanpiahnc" 

'''
'''
a = "Japan"
b = "china"
c = " "

def string1_both_ends(a):
    if len(a) < 2:
        return ''
    return a[0:2] + a[-2:]

print("c:" ,string1_both_ends(a))

def string2_both_ends(b):
    if len(b) < 2:
        return ''
    return b[0:2] + b[-2:]

print(string1_both_ends(a) + string2_both_ends(b))

'''

a = "japan"
b = "china"
c = str(a[0]+a[1]+a[3]+a[4]+a[2]+b[2]+b[4]+b[1]+b[3]+b[0])

print("c:"+c)

