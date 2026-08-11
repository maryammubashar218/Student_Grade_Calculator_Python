students=[]
while True:
    print("1. Add student result:")
    print("2. View student result:")
    print("3.Exit")

    choice=input("enter your choice:")
    if(choice=="1"):
        name=input("enter your name:")
        english_marks= float(input("enter your english marks:"))
        math_marks= float(input("enter your math marks:"))
        computer_marks= float(input("enter your computer marks:"))

        total=english_marks+math_marks+computer_marks
        percentage=total/300*100

        if(percentage>=90):
         grade = "A"
        elif(percentage>=80):
         grade = "B"
        elif(percentage>=70):
         grade =" C"
        elif(percentage>=60):
         grade =" D"
        else:
         grade =" F"
        student={
                "name":name,
                "english":english_marks,
                "math":math_marks,
                "computer":computer_marks,
                "total":total,
                "percentage":percentage,
                "grade":grade
              }
        students.append(student)
        print(" student result added successfully!")
    elif(choice=="2"):
      if(len(students)==0):
        print("no student result added yet!")
      else:
        print("student result details")
        for student in students:
          print(f"name:{student["name"]}")
          print(f"engllish_marks:{student["english"]}")
          print(f"math_marks:{student["math"]}")
          print(f"computer_marks:{student["computer"]}")
          print(f"total:{student["total"]}")
          print(f"percentage:{student["percentage"]}%")
          print(f"grade:{student["grade"]}")
          print("----------------------")
    elif(choice=="3"):
      print("thanku for using student garde calculator!")
      break
    else:
      print("invalid choice! please try again!")


         