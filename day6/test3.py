#input
nd = (["X", "Y"], ("A", "B", "C"), "PQRS")
mul = [2, 3, 1]
s = ("|-|", "***", "^^^")
p = [(1, 0), (2, 1, 0), (3, 1)]
 
 
#expected op: 
#"Y|-|YA***C***ABRS^^^S^^^R"
 
 
 
#Rules :
#No loops, functions, conditions, or f-strings/format()
#Only use: indexing, slicing, string concatenation (+), string multiplication (*), tuple/list operations
#Must access elements using the positions data to determine which characters to extract
#Must use multipliers to determine repetition counts
#Must use separators for joining
#Everything in ONE expression (though you can use intermediate variables for sub-expressions)

#sol: (using concatenation)

nd[0][1]+s[0]+nd[0][1]+nd[1][0]+s[1]+nd[1][2]+s[1]+nd[1][0]+nd[1][1]+nd[2][2]+nd[2][3]+s[2]+nd[2][3]+s[2]+nd[2][2]