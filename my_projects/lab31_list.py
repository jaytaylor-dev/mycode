#!usr/bin/env python3
wordbank=["indentation", "spaces"]

tlgstudents= ["Aaron", "Andy", "Chris", "Gage", "Jelani", "John", "Justin", "Keith", "Lance", "Oshay", "Sam", "Scoot", "Titus", "Tyler", "Udyr", "Vitaly", "Jay"]

wordbank.append(tlgstudents[4])


num = int(input("Please enter a number 1-20: "))

print(f"You chose {num}")

wordbank.append(num);

student_name = tlgstudents[1]

print(f"{student_name} always uses {wordbank[3]} {wordbank[1]} to indent ")

print(wordbank)


