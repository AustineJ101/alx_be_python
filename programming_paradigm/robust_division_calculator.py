def safe_divide(numerator, denominator):
    try:
       num = float(numerator)
       denom = float(denominator)
       result = num / denom
       print(f"The result of the division is {result}")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except ValueError:
        print("Please enter numeric values only.")
