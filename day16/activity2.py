arr=[45,63,72,11,91,82,3,35]
arr.sort()
search=63
low=0
high=len(arr)-1
found=-1
while low<=high:
	mid=(low+high)//2
	if arr[mid]==search:
		found=mid
		break
	if arr[mid]<search:
		low=mid+1
	if arr[mid]>search:
		high=mid-1
if found!=-1:
	print("found the element at:",found,"th position")
else:
	print("not found")