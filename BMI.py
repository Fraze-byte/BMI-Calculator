# -----------------------------
# BMI Calculator - Text-based version.
# Allows users to input weight and height in multiple units, computes BMI, and categorizes it.
# -----------------------------

# Main function to control the overall program flow
def main():
    while True:  # Outer loop to allow repeated BMI calculations
        weight = weight_calc()  # Ask for weight input and convert to kg if needed
        height = height_calc()  # Ask for height input and convert to meters if needed

        # Calculate BMI
        bmi = round(bmi_calc(weight, height), 2)
        print("Your BMI is:", bmi)

        # Inner loop to ensure valid response to BMI category check
        while True:
            category_check = input("Do you want to know your BMI category? (y/n): ").strip().lower()
            if category_check == "y":
                category = bmi_category(bmi)
                print("Calculated BMI:", bmi)
                print("According to WHO categorization, you are:", category)
                break
            elif category_check == "n":
                print("Thank you for using the BMI calculator.")
                break
            else:
                print("Invalid input! Please enter 'y' or 'n'.")

        # Ask user if they want to run the program again
        answer = input("Do you want to calculate another BMI? (y/n): ").strip().lower()
        if answer != "y":
            print("Goodbye!")
            break


# Function to calculate height based on chosen unit
def height_calc():
    """
    Prompts the user for height input in meters, cm, or feet/inches.
    Returns height in meters.
    """
    while True:
        htype = input("Would you like to enter height in meters, cm, or feet? ").strip().lower()

        if htype == "meters":
            try:
                height = float(input("Enter your height in meters: "))
                if height > 0:
                    return round(height, 2)
                else:
                    print("Height must be greater than zero.")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")

        elif htype == "cm":
            try:
                height = float(input("Enter your height in centimeters: "))
                if height > 0:
                    return round(height / 100, 2)  # Convert cm to meters
                else:
                    print("Height must be greater than zero.")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")

        elif htype == "feet":
            try:
                feet = int(input("Enter feet: "))
                inches = int(input("Enter inches: "))
                if feet >= 0 and inches >= 0:
                    total_inches = (feet * 12) + inches
                    return round(total_inches * 0.0254, 2)  # Convert inches to meters
                else:
                    print("Feet and inches must be zero or positive.")
            except ValueError:
                print("Invalid input! Please enter whole numbers for feet and inches.")

        else:
            print("Invalid height unit! Please enter 'meters', 'cm', or 'feet'.")


# Function to calculate weight based on chosen unit
def weight_calc():
    """
    Prompts the user for weight input in kg or pounds.
    Returns weight in kilograms.
    """
    while True:
        wtype = input("Would you like to enter weight in kg or pounds? ").strip().lower()

        if wtype == "kg":
            try:
                weight = float(input("Enter your weight in kg: "))
                if weight > 0:
                    return round(weight, 2)
                else:
                    print("Weight must be greater than zero.")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")

        elif wtype == "pounds":
            try:
                weight = float(input("Enter your weight in pounds: "))
                if weight > 0:
                    return round(weight * 0.453592, 2)  # Convert pounds to kg
                else:
                    print("Weight must be greater than zero.")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")

        else:
            print("Invalid weight unit! Please enter 'kg' or 'pounds'.")


# Function to compute BMI
def bmi_calc(weight, height):
    """
    Calculates BMI using the formula: BMI = weight (kg) / height (m)^2
    """
    return weight / (height ** 2)


# Function to determine BMI category based on WHO standards
def bmi_category(bmi):
    """
    Categorizes the BMI value into WHO standard weight classes.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal Weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 30 <= bmi < 35:
        return "Obesity Class I"
    elif 35 <= bmi < 40:
        return "Obesity Class II"
    else:
        return "Obesity Class III"


# Run the program
main()
