#Nadir Shaikh
#Uin :- 251P086
print("Nadir Shaikh")
print("UIN :- 251P086")
cet_student = {"John", "Alice","Bob"}
jee_student = {"Alice", "Charlie","David"}
neet_student = {"Eve","Bob","Alice"}
all_student=cet_student.union(jee_student,neet_student)
print("All Student:",all_student)
intersection_student = cet_student.intersection(jee_student)
print("Students appearing for both CET and JEE:", intersection_student)
intersection_student = jee_student.intersection(neet_student)
print("Students appearing for both JEE and NEET:", intersection_student)
intersection_student = cet_student.intersection(neet_student)
print("Students appearing for both CET and NEET:", intersection_student)
cet_not_jee = cet_student.difference(jee_student)
print("Student appearing only for CET:", cet_not_jee)
cet_not_neet = cet_student.difference(neet_student)
print("Student appearing only for CET:", cet_not_neet)
jee_not_cet = jee_student.difference(cet_student)
print("Student appearing only for JEE:" ,jee_not_cet)
jee_not_neet = jee_student.difference(neet_student)
print("Student appearing only for JEE:" ,jee_not_neet)
neet_not_cet = neet_student.difference(cet_student)
print("Student appearing only for NEET:", neet_not_cet)
neet_not_jee = neet_student.difference(jee_student)
print("Student appearing only for NEET:" ,neet_not_jee)
