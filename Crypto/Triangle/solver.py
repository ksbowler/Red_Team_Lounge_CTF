enc = "133f29027034094a33253126395b3704"
key = []
flag = "RTL{"
for i in range(0,8,2):
	key.append(int(enc[i:i+2],16)^ord(flag[i//2]))
print(key)
for i in range(0,len(enc),2):
	x = int(enc[i:i+2],16)^key[(i//2)%4]
	print(chr(x),end="")
print()
