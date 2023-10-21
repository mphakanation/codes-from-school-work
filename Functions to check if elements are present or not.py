# function to check if all elements are present or not
 
string ="The quick brown fox jumps over the lazy dog"
string=string.replace(" ","")
string=string.lower()
x=list(set(string))
x.sort()
x="".join(x)
alphabets="abcdefghijklmnopqrstuvwxyz"
if(x==alphabets):
    print("The string is a pangram")
else:
    print("The string isn't a pangram")
