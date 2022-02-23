sd = []
def student_details(roll_no, name, marks):
    sd.append([roll_no, name, marks])
    

student_details(1, "BHANU", 90)
student_details(2, "DAMON", 95)
student_details(3, "KLAUS", 85)

############ 1 ############

# def show():
#     if(len(sd) != 0):
#         print("Roll No    Name     Marks")
#     for i in sd:
#         print(f"{i[0]}          {i[1]}      {i[2]}")

# show()

############ 1 ############


############ 2 ############

def print_second_record():
    print(f"{sd[1][0]}          {sd[1][1]}      {sd[1][2]}")
    
print_second_record()

############ 2 ############