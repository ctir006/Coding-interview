str=input("Enter the sting: ")
str_arr=str.split(" ")
if(len(str_arr)<=1):
	print("Invalid Input ")
else:
	t=str_arr[0]
	str_arr[0]=str_arr[1]
	str_arr[1]=t
print(", ".join(str_arr))