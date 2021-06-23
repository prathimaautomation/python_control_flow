# Syntax if variable - condition age:

weather = "snowy"

if weather == "sunny" : # this condition is true the next line would execute
    print("Enjoy the weather") # this line needs to be inside the if code block - intended
elif weather == "snowy":
    print("Make snow man")
else:
    print("take the umbrella") # this line will be execute only if the previous conditions fail

# Let's use our ticket age criteria

age = 18

if age <= 18: # checking the condition according to the age given
    print(" you are not eligible to watch this movie, please select under 18 rated movie")

# For Loops and While loops
# loops helps us to iterate through data, such as Lists, Dict, sets etc.

shopping_list = ["eggs", "apples", "milk", "break", "butter"]
                #   0        1        2      3          4
# print(shopping_list[0])
# print(shopping_list[1])
# print(shopping_list[2])
# print(shopping_list[3])
# print(shopping_list[4])
#Let's see if we can get it done with for loop by iterating through our list
# first iteration:
for items in shopping_list:
    print(items)
# second iteration with if conditions:
shopping_list = ["eggs", "apples", "milk", "bread", "butter", 1, 2, 3, 4, 5, 6, 7, 9]
                #   0        1        2      3          4
for items in shopping_list:
    if items == "bread": # if this condition is true
        break
    print(items)

# Third iteration with dict
student_data = {
    "student_name": "James", #String
    "course": "DevOps", #String
    "course_topics": 4, #int
    "topic_names": ["Business Week", "Python", "Virtualisation with Vagrant", "AWS Cloud"] #list
}

print(student_data)
#Lets iterate through our dict
for data in student_data.values():
    if data == "James":
        print(data)

# In any case, for loop would iterate through the data until the last item of condition is true

# While loop is essentially used to monitor the data
# First Iteration of while loop
num = 0
while num < 10: # while num value was less than 10
    print(f"it's working -> {num}")
    num += 1  # adding 1 into num value each time it iterates through

# Second iteration of while loop
num = 0
while num < 10:
    print(f"it's working {num}")
    if num== 5:
        break
    num += 1

# Let's see how can we interact with our user in the Third Iteration
# prompt the user to input age and restrict to enter in digits only
# check if the data is in digits display it back to the user if not in digits prompt the user with message to enter in digits
# choice = "wrong"
# while choice.isdigit() == False: # prompt the user until digits have entered
#     choice = input("Enter your age in digits only: ")
# Example 1
while True:
    if input("Enter you age in digits only: ").isdigit() == True:
        break
# Example 2
user_prompt = True

while user_prompt:
    age = input("Please enter your age? ")
    if age.isdigit():
        user_prompt = False
    else:
        print("Please provide age in digits only")
