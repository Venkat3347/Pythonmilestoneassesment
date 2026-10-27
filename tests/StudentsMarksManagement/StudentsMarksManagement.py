#StudentMarks

#Studentdata
Students=[
    {"id":10,"name":"venkat", "python":80, "SQL":75, "AI":85},
    {"id":11,"name":"prabha", "python":60, "SQL":70, "AI":65 },
    {"id":12,"name":"swamy", "python":90, "SQL":86, "AI":95 },
    {"id":13,"name":"vardhineni", "python":33, "SQL":25, "AI":22 }    
]
def cal_grade(avarage):
    if avg>=75:
        return "A"
    elif avg>=60:
            return "B"
    elif avg>=40:
            return "C"
   
    else:
            return "F"


#calculate grade,total,avg

for Stu in Students:
        total=Stu["SQL"]+Stu["python"]+Stu["AI"]
        avg=total/3

        grade=cal_grade(avg)

              
#Students pass or fail
        if avg>=40:
               result="pass" 
        else:
                result="fail"

        Stu["total"]=total
        Stu["avg"]=avg
        Stu["grade"]=grade
        Stu["result"]=result
#Highest avarage
highest_avg=0
top_student={}
          
if avg>highest_avg:
           highest_avg=avg
           top_student
#Display students results
for Stu in Students:
        print("Student ID:",Stu["id"])
        print("Student name:",Stu["name"])
        print("grade:",Stu["grade"])
        print("Total:",Stu["total"])
        print("Average:",round(Stu["avg"],2))
        print("Result:",Stu["result"])
        print()


#Students above 75
high_scorers = [Stu["name"].title() for Stu in Students if Stu["avg"]>75]

print("Students above 75:",",".join(high_scorers))

#High scorer
top_student=max(Students, key=lambda Stu: Stu["avg"])
print("highest scoring student:",top_student["name"].title())






















