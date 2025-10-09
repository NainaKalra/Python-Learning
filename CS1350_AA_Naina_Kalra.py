#Mid- Term exam - NAINA KALRA 

# Problem 1: Student Gradebook Program

#Adding student to gradebook
def add_student(gradebook, name, grade):
    if 0 < grade <= 100:
        gradebook[name] = grade   
        return True               
    else:           #added name n grade and if invalid grade- returned false
        return False            


#Calculating class average
def get_class_average(gradebook):
    if not gradebook:
        return 0                #avg is sum/length 
    total = sum(gradebook.values())
    average = total / len(gradebook)
    return average

#Getting passing students with grade>=60
def get_passing_students(gradebook):
    passing = []  #empty list created 
    for name, grade in gradebook.items():
        if grade >= 60:
            passing.append(name)
        return passing 
    
# Test your functions 
if __name__ == "__main__":
    gradebook = {}
    print(add_student(gradebook, "Alice", 85)) # Should print True  
    print(add_student(gradebook, "Bob", 150)) # Should print False
    print(add_student(gradebook, "Charlie", 45)) # Should print True
    print(f"Average: {get_class_average(gradebook):.2f}")
    # Bonus -- 10 pints
    print(f"Passing: {get_passing_students(gradebook)}")


#Problem 2 - Set Operations for Course Registration 

def find_common_students(course1_students, course2_students):
    return course1_students & course2_students
# it says common and i will use intersection here

def find_all_students(course1_students, course2_students):
    return course1_students | course2_students
#set of all students in either course - will use union

def find_unique_to_course1(course1_students, course2_students):
    return course1_students - course2_students
# (-) for elements in set A but not in B


#Bonus question -
def check_enrollment(student_name, *course_lists):
#using loop iteration to check if a student is in any of the course lists
    for course in course_lists:
        if student_name in course:
            return True
        else:
            return False

#Test your functions- 
if __name__ == "__main__":
    cs_students = {"Alice", "Bob", "Charlie", "David"}
    math_students = {"Bob", "Charlie", "Eve", "Frank"}
    physics_students = {"Alice", "Eve", "George"}

    print("Common:", find_common_students(cs_students, math_students))
    print("All:", find_all_students(cs_students, math_students))
    print("CS only:", find_unique_to_course1(cs_students, math_students))
    print("Alice enrolled?", check_enrollment("Alice", cs_students, math_students))
    print("Henry enrolled?", check_enrollment("Henry", cs_students, math_students, physics_students))

#Problem 3 - NumPy Array Analysis - 
import numpy as np

def calculate_daily_averages(temps):
    daily_average = np.mean(temps, axis=1)
    #taking rows average as (temps is a 7x3 array) and axis will be 1
    return daily_average

def find_hottest_day(temps):
    daily_average = np.mean(temps, axis=1)
    #to find index of maximum value i will use argmax 
    hottest_day = np.argmax(daily_average)
    return hottest_day

def count_cold_readings(temps, threshold):
    cold_reads = temps < threshold
    #counting true as 1 and false as 0
    count = np.sum(cold_reads) # will add each true value
    return count

def normalize_temperatures(temps):
    min_temp = np.min(temps)
    max_temp = np.max(temps)
    #will use given formula (temp - min) / (max - min) * 100
    normalized = (temps - min_temp) / (max_temp - min_temp) * 100
    return normalized

# Test your functions
if __name__ == "__main__":
    temps = np.array([
    [65, 75, 70],
    [68, 78, 72],
    [70, 80, 75],
    [62, 73, 68],
    [67, 77, 71],
    [69, 79, 74],
    [64, 74, 69]
    ])
    print("Daily averages:", calculate_daily_averages(temps))
    print("Hottest day index:", find_hottest_day(temps))
    print("Cold readings (< 70):", count_cold_readings(temps, 70))
    print("Normalized (first day):", normalize_temperatures(temps)[0])

#Problem 4- String Processing - Clean and validate user input from a registration form - 

# Write your code here:
def clean_name(name):
    clean_name = name.strip().title()
    #removing extra spaces and then title case
    return clean_name
def validate_email(email):
    #for checking exactly 1 @ i will count @ and return false if its not exactly 1 
    if email.count('@')!=1:
        return False
    #email has name and domain - so i will split bw name@domain
    name,domain = email.split('@')
    if '.' not in domain: #checking for atleast 1 dot in domain
        return False
    else:
        
        return True
    
def format_phone(phone):
    # i will create a string - digits
    digits = ""
    for ch in phone:
        if ch.isdigit():
            digits += ch
#proper format for 10 digits-
    if len(digits) == 10:
        return f"({digits[0:3]}) {digits[3:6]}-{digits[6:]}"
    else:
        return "Invalid"

# Test your functions
if __name__ == "__main__":

    print(clean_name(" john smith ")) # Should print "John Smith"
    print(validate_email("test@email.com")) # Should print True
    print(validate_email("bad.email")) # Should print False
    print(format_phone("555-123-4567")) # Should print "(555) 123-4567"
    print(format_phone("123")) # Should print "Invalid"

#Problem 5 - Regex

import re

def find_all_phones(text):
    return re.findall(r'\(?\d{3}\)?[- ]\d{3}-\d{4}', text)

def find_all_prices(text):
    return re.findall(r'\$\d{1,3}\.\d{2}', text)

def extract_emails(text):
    return re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)

def validate_student_id(student_id):
    return bool(re.match(r'^[A-Za-z]{2}\d{4}$', student_id))

#Test your functions
if __name__ == "__main__":
    test_text = """
    For info, call 555-123-4567 or (555) 987-6543.
    Email us at info@school.edu or admin@college.com
    Course fees: $50.00 for materials, $150.50 for tuition
    """

    print("Phones:", find_all_phones(test_text))
    print("Prices:", find_all_prices(test_text))
    print("Emails:", extract_emails(test_text))
    print("Valid ID 'CS1234'?", validate_student_id("CS1234"))
    print("Valid ID '12ABCD'?", validate_student_id("12ABCD"))
    print("Valid ID 'AB12345'?", validate_student_id("AB12345"))
