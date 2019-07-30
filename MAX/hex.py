
s = ""

with open("SNIFFED") as f:
    for line in f:
        s += line

res = ""

cur = "\\x"

i = 0

while i < len(s):
    if(s[i].isalpha() or s[i].isdigit()):
        cur += s[i] + s[i+1]
        i+=1
        res += cur
        cur = "\\x"
    i+=1

print (res)
