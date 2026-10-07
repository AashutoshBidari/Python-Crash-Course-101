# wap to find out whether a student has passed or failed if it requires total 40% and atleast 30% in each subject to pass.
# assume 3 subjects and take marks from user

marks1 = int(input("Enter marks in first subject: "))
marks2 = int(input("Enter marks in second subject: "))
marks3 = int(input("Enter marks in third subject: "))

#check for total percentage

total_percentage = (100*(marks1+marks2+marks3))/300

if(total_percentage >= 40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed!")
else:
    print("You failed!")