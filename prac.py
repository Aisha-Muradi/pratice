
# print(type(int("22")))
# print( "Happy", "Friday")
# print(7%2 + 1.0)

# row = ""
# for i in range(3):
#     row = row + str(i)
#     print(row)

# row = 0
# for i in range(3):
#     row = row + i
#     print(row)

# for i in range(3):
#     print(i, end="")

# s = ""
# for a in range(2):
#     for b in range(3):
#         s = s + "b"
#     for c in range(2):    
#         s = s + "c"
# print (s)

# x = ""
# for n in range(5,1,-1):
#     x = x + (n*"@") + "" 
#     print (x)


# for n in range(5,1,-1):
#     x= n*"@"
#     print (x)
# n = 5
# r = " "
# for i in range (n):
#     r =  r + "*" 
#     print  (r)

# n = 5
# for r in range(1,n+1):
#     print((n-r)*" " + (2*r-1)*"*")
# n = 5
# for r in range(1,n+1):
#     print((2*r-1)*" " + (n-r)*"*")
# n = 5
# for r in range(n):
#     print((n-r)*" " + (2*r-1)*"*")

# year = 2021
# is_CSCI_major = True
# print(year >= 2022)
# print(is_CSCI_major or year >= 2022)
# print(is_CSCI_major and year >= 2022)

# desc = "Good morning! #HelloWorld #OberlinCSCI"
# count = 0
# for char in desc:
#     if char == "#":
#         count = count + 1
# print("Hashtag Count:", count)


# desc = "Good morning! #HelloWorld #OberlinCSCI"
# count = 0
# for char in desc:
#     if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
#         count = count + 1
# print("??? Count:", count)

# iClicker = {'Molly': [1,0,1], 'Adam':[1,1,1],'Sam':[0,1,1]}
# for k in iClicker.keys():
#     print( k )

year = 2021 
is_CSCI_major = True 
print(year >= 2022) 
print(is_CSCI_major or year >= 2022) #why this prints true however if we compare is_CSCI_major to the 2022 it should be false ?
print(is_CSCI_major and year >= 2022)


def silly_voice(s):
    temp = ""
    i = 0
    #Why do we have i i here if the value does not change throughout the loop 
    for c in s:
        if (i%2) == 0:
    #for any string s, calling s.upper() returns a version of s where all
    # the letters are upper-case
            temp = temp + c.upper() # c is every capital of string and it will do the capital 
        else:
            temp = temp + c
        i = i+1 # instead of i we could have len to see the length and i here it is keeping track of where we are in string
    return temp