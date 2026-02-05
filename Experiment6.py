# students in exams
cet = {"Alise", "Bob"}
jee = {"Bob", "Bob"}
neet = {"Alise", "Eve"}
print("All students:", cet|jee|neet)
print("Students in all exam:", cet & jee & neet)
print("Cet but not in jee:", cet - jee) 
