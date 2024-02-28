def calculate_bmi(height, weight, height_unit="m", weight_unit="kg"):
  """
  Calculates BMI given height and weight. Supports various units.

  Args:
    height (float): Height value.
    weight (float): Weight value.
    height_unit (str, optional): Unit of height ('m', 'cm', 'ft'). Defaults to 'm'.
    weight_unit (str, optional): Unit of weight ('kg', 'lb'). Defaults to 'kg'.

  Returns:
    float: Calculated BMI.
  """  
  try:
    if height_unit == 'cm':
      height = height / 100  # Convert centimeters to meters
    elif height_unit == 'ft':
      height = height * 0.3048  # Convert feet to meters

    if weight_unit == 'lb':
      weight = weight * 0.453592  # Convert pounds to kilograms

    bmi = round(weight / (height**2), 2)
    return bmi

  except ZeroDivisionError:
    return None


def interpret_bmi(bmi):
    """
    Interpret the BMI and provide a classification.

    Args:
        bmi (float): Calculated BMI.

    Returns:
        str: BMI interpretation.
    """
    if bmi is None:
        return "Invalid input. Height should be greater than 0."

    if bmi < 18.5:
        return f"Your BMI is {bmi}, you are underweight."
    elif bmi < 24.9:
        return f"Your BMI is {bmi}, you have a normal weight."
    elif bmi < 29.9:
        return f"Your BMI is {bmi}, you are overweight."
    elif bmi < 34.9:
        return f"Your BMI is {bmi}, you are obese (Class I)."
    elif bmi < 39.9:
        return f"Your BMI is {bmi}, you are obese (Class II)."
    else:
        return f"Your BMI is {bmi}, you are obese (Class III)."


def main():
  try:
    height_unit = input("Enter your height unit (m, cm, ft): ")
    height = float(input("Enter your height: "))

    weight_unit = input("Enter your weight unit (kg, lb): ")
    weight = float(input("Enter your weight: "))

    bmi = calculate_bmi(height, weight, height_unit, weight_unit)
    result = interpret_bmi(bmi)
    print(result)

  except ValueError:
    print("Invalid input. Please enter numerical values.")


if __name__ == "__main__":
  main()
