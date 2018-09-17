def reverseStr(str):
	if len(str) == 0:
		return str
	else:
		return reverseStr(str[1:])+ str[0]

print(reverseStr("jklhgf"))

a= "ka"
print (a[1:]+a[0])