a = "LTR"
b = "0D"
c = "S1"
 
inp = input("> ")
 
if len(inp) != 17:
    print("Wrong size.")
    exit()
 
if (inp[0] == a[2] and inp[1] == a[1] and inp[2] == a[0]) and inp[3] == "{" and \
   ((inp[4] + inp[5]) == b[::-1]) and (inp[6] == "N" and inp[7] == "T" and inp[8] == chr(95)) and \
   (inp[9] + inp[10] == b[::-1]) and (inp[11] + inp[12] + inp[13] == "_TH") and (inp[14] + inp[15] == c[::-1]) and \
   (inp[16] == "}"):
    print("Good job.")
else:
    print("Flag is incorrect.")
