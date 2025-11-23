# 1. Prompt the user for their current age and convert the input to an integer.
# The input() function reads the user's text input as a string, so we use int() to convert it.
try:
    current_age = int(input("How old are you? "))
except ValueError:
    print("Invalid input. Please enter a whole number for your age.")
    # Exit the script if input is invalid to prevent errors in the next step
    exit()

# 2. Define the difference in years between the current year (assumed 2023) and 2050.
YEAR_DIFFERENCE = 2050 - 2023  # This is 27

# 3. Calculate the user's age in 2050
future_age = current_age + YEAR_DIFFERENCE

# 4. Print the result in the specified format
print(f"In 2050, you will be {future_age} years old.")
