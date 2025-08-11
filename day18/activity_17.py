students = [{"name": "Brenda", "scores": [90, 92, 95, 88]}, 
            {"name": "David", "scores": [85, 87, 89]},
            {"name": "Cathy", "scores": [98, 99, 100]},
            {"name": "Alex", "scores": [70, 100]}]
high_score = {
    student["name"]: sum(student["scores"]) / len(student["scores"])
    for student in students
    if (sum(student["scores"]) / len(student["scores"])) >= 90
}

print(high_score)