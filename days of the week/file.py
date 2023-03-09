# days-of-the-week.
print("This is Tina Muriu")
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for day in days_of_week:
    print(day)
def dress_code(day):
    if day=="Monday":
        return "Vintage"
    if day == "Tuesday":
        return "Silk"
    if day == "Wednesday": 
        return "Cotton Black"
    if day == "Thursday":
        return "Official"
    elif day == "Friday":
        return "Sporty"
    else:
        return "Casual"

day = input("Enter the day of the week: ")
print("The dress code for", day, "is", dress_code(day))
