a = 6
b = 6
c = 6
if(a is b):
 print("1) a 与 b 相同")
else:
 print("1) a 与 b 不同")
if(id(a) == id(c)):
 print("2) a 与 c 相同")
else:
 print("2) a 与 c 不同")

print("That's all")