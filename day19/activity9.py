def count_lines(filename):
	with open(filename,'r') as file:
		return sum(1 for _ in file)

if __name__=="__main__":
	print(count_lines("story.txt"))