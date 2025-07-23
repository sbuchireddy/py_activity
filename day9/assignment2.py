# Dictionary containing names as keys and scores as values
scores = {
    "Anita": 92,
    "Ravi": 85,
    "Kiran": 76,
    "Zoya": 88
}

# Convert the dictionary into a list of (key, value) tuples
scores_list = list(scores.items())

# Reverse each tuple in the list so that (name, score) becomes (score, name)
scores_list[0] = scores_list[0][::-1]
scores_list[1] = scores_list[1][::-1]
scores_list[2] = scores_list[2][::-1]
scores_list[3] = scores_list[3][::-1]

# Convert the modified list of tuples back into a dictionary
# Now the keys are scores and the values are names
score_d = dict(scores_list)


# Use the score to look up the corresponding name in the dictionary
# If the score is not found, print 'not found'
print(score_d.get(int(input("Enter a score to look up the name: ")), 'not found'))
