access_data={
(103,209):"Alice",
(104,210):"Bob",
(105,211):"Charlie",
(106,212):"Diana"
}

#auth_input=tuple(map(int,input("enter the number:").split(",")))
#print(access_data.get(auth_input) or access_data.get(auth_input[::-1]))


access_list = list(access_data.items())

access_list[0] = access_list[0][::-1]
access_list[1] = access_list[1][::-1]
access_list[2] = access_list[2][::-1]
access_list[3] = access_list[3][::-1]

access_d = dict(access_list)


print(access_d.get((input("Enter value:")), "Not found"))