grades={"Alice":"A","Bob":"B"}
attendance={"Alice":90,"Bob":85}

grades["Bob"]="A"
attendance["Bob"]=88

grades["charlie"]="c"
attendance["charlie"]="80"

grades.pop("Alice")
attendance.pop("Alice")

for student in grades:
    print(student,"Grades",grades[student],"Attendance",attendance[student])
