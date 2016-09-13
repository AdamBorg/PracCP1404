x=1
y=2

print(x==y)
print(x != y and x == y)
print(y<x or x>y)
print(x==y or x<y and y>x)

print("abc" in "abcdefg")

text = "one two three"
print(text[0:1] + text[0:2] + text[0:2])

print(text[0:3])

print(7-11)
print(7*11)
print(7%11)
print(11//7)


name = str(input('get name'))
while name == '':
    print("invalid name")
    name = str(input('get name'))
print("done")