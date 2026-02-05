cet = {"om", "Bob"}
jee = {"Tathagat", "Bob"}
neet = {"Anushman", "Eve"}
print("All students:", cet|jee|neet)
print("Students in all exam:", cet & jee & neet)
print("Cet but not in jee:", cet - jee)
