import logging

# Setup logging for debugging purposes
logging.basicConfig(filename="probability_calculator.log", level=logging.ERROR, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

def calculate_cumulative_probability(num_attempts, drop_rate):
    drop_rate_decimal = drop_rate / 100
    probability = 1 - (1 - drop_rate_decimal) ** num_attempts
    return min(probability, 0.999999) * 100  # Ensure it never reaches 100%

def attempts_for_success_rate(drop_rate, target_probability):
    drop_rate_decimal = drop_rate / 100
    attempts = 0
    probability = 0
    while probability < target_probability / 100:
        attempts += 1
        probability = 1 - (1 - drop_rate_decimal) ** attempts
    return attempts

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("\033[91mPlease enter a positive number.\033[0m")
        except ValueError:
            print("\033[91mInvalid input. Please enter a numerical value.\033[0m")
            logging.error("Non-numeric input for float value.")

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("\033[91mPlease enter a positive integer.\033[0m")
        except ValueError:
            print("\033[91mInvalid input. Please enter an integer.\033[0m")
            logging.error("Non-numeric input for integer value.")

def get_yes_no(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ["yes", "y", "1"]:
            return True
        elif response in ["no", "n", "2"]:
            return False
        else:
            print("\033[91mInvalid input. Please enter 'yes', 'y', '1', 'no', 'n', or '2'.\033[0m")
            logging.warning("Invalid yes/no response.")

def show_sample_outcomes(drop_rate):
    print("\nSample Success Rate Calculations:")
    for target in [50, 75, 90, 99]:
        attempts_needed = attempts_for_success_rate(drop_rate, target)
        print(f" - For a {target}% success rate, you need approximately {attempts_needed} attempts.")

def main():
    calculation_log = []

    # Initial user input with explanations
    print("\nWelcome to the Cumulative Probability Calculator!")
    print("Enter your drop rate and planned attempts to see your success probability.")
    print("You can adjust the values as needed after each calculation.\n")

    drop_rate = get_positive_float("Enter the drop rate percentage (e.g., 20 for 20% drop rate): ")
    planned_attempts = get_positive_int("Enter the number of planned attempts (e.g., 50): ")

    while True:
        # Calculate cumulative probability
        cumulative_probability = calculate_cumulative_probability(planned_attempts, drop_rate)
        result_message = (f"\n\033[96mCumulative Probability after {planned_attempts} attempts "
                          f"with a {drop_rate}% drop rate: {cumulative_probability:.2f}%\033[0m")
        print(result_message)

        # Log the result for reference
        calculation_log.append((planned_attempts, drop_rate, cumulative_probability))
        print("\nCalculation log:", calculation_log)

        # Show attempts needed for different success rates
        show_sample_outcomes(drop_rate)

        # Check for actual success
        if get_yes_no("\nDid you get the item? (yes/y/1 for Yes, no/n/2 for No): "):
            # If successful, get actual attempts and calculate actual probability
            actual_attempts = get_positive_int("How many attempts did it actually take? ")
            actual_probability = calculate_cumulative_probability(actual_attempts, drop_rate)
            print(f"\n\033[92mCongratulations! The actual probability after {actual_attempts} attempts "
                  f"is {actual_probability:.2f}%.\033[0m")
            break
        else:
            # If unsuccessful, ask if they want to change the drop rate or attempts
            if get_yes_no("Would you like to change the drop rate or the number of attempts? (yes/y/1 for Yes, no/n/2 for No): "):
                while True:
                    choice = input("Which would you like to change? (rate/attempts): ").strip().lower()
                    if choice == "rate":
                        drop_rate = get_positive_float("Enter the new drop rate percentage: ")
                        break
                    elif choice == "attempts":
                        planned_attempts = get_positive_int("Enter the new number of planned attempts: ")
                        break
                    else:
                        print("\033[91mInvalid input. Please enter 'rate' or 'attempts'.\033[0m")
                        logging.warning("Invalid choice for changing rate or attempts.")
            else:
                print("\033[93mKeeping the current drop rate and number of attempts.\033[0m")

if __name__ == "__main__":
    main()
