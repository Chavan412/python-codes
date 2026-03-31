so = int(input("enter a number :"))
length= len(str(so))
amstr = 0
for j in str (so) :
    amstr += int(j) ** length
    print(amstr)
if amstr == so:
    print (f"(so) is amsrtong numer")
else:
    print(f"(so) is not a amstrong number")
