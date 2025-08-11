data=[[1,2,None],[],[3,'',4],[0,5,5],[None,6]]
flattened=[item for sublist in data for item in sublist if item]
result=list(dict.fromkeys(flattened))
print(result)