import math
import random

def calculate_cumulative_probability(base_items: int, drop_rate: float) -> float:
    """
    Calculates the cumulative probability of obtaining at least one item.

    Parameters:
    base_items (int): The number of attempts (base items used).
    drop_rate (float): The drop rate percentage for the item (e.g., 32 for 32%).

    Returns:
    float: The cumulative probability of obtaining the item at least once, as a percentage.
    """
    # Convert drop rate percentage to a decimal
    p = drop_rate / 100

    # Calculate cumulative probability of at least one success
    cumulative_probability = 1 - (1 - p) ** base_items

    return cumulative_probability * 100  # Convert to percentage

def calculate_attempts_for_success_rate(drop_rate: float, target_success_rate: float) -> int:
    """
    Calculates the number of attempts needed to reach a specific success probability.

    Parameters:
    drop_rate (float): The drop rate percentage for the item (e.g., 32 for 32%).
    target_success_rate (float): The target cumulative success probability as a percentage.

    Returns:
    int: The minimum number of attempts required to achieve the target success probability.
    """
    # Convert drop rate and target success rate percentages to decimals
    p = drop_rate / 100
    target = target_success_rate / 100

    # Calculate the required attempts using logarithms
    attempts = math.ceil(math.log(1 - target) / math.log(1 - p))

    return attempts

def display_random_probability_quote():
    """
    Displays a random math-related quote about probability.
    """
    quotes = [
        "“The only certainty is that nothing is certain.” – Pliny the Elder",
        "“In the long run, the law of averages fails to work.” – G.H. Hardy",
        "“Probability is not about the odds, it’s about the belief in the outcome.” – Nate Silver",
        "“Life is a school of probability.” – Walter Bagehot",
        "“The essence of life is statistical improbability on a colossal scale.” – Richard Dawkins",
        "“Uncertainty is the only certainty there is, and knowing how to live with insecurity is the only security.” – John Allen Paulos",
        "“An experiment is a question which science poses to Nature, and a measurement is the recording of Nature’s answer.” – Max Planck",
        "“There is no such thing as absolute certainty, but there is assurance sufficient for the purposes of human life.” – John Stuart Mill"
    ]
    # Select and display a random quote
    print(random.choice(quotes))

def check_item_drop():
    """
    Asks the user if they got the item, congratulates them, and calculates statistics if yes.

    Returns:
    bool: True if the user confirms the item dropped, False otherwise.
    """
    while True:
        response = input("\nDid the item drop? (yes/y/1 for Yes, no/n/2 for No): ").strip().lower()
        if response in ["yes", "y", "1"]:
            return True
        elif response in ["no", "n", "2"]:
            return False
        else:
            print("Invalid input. Please enter 'yes', 'y', '1' for Yes or 'no', 'n', '2' for No.")

if __name__ == "__main__":
    print("Welcome to the Cumulative Probability Calculator!")
    print("\nThe cumulative probability of probability states that the chance of success increases with each independent attempt, even if the individual chance is low.")
    print("Use this tool to calculate your chance of success based on the number of attempts and drop rate.\n")

    try:
        # Get user input with validation
        base_items = int(input("Enter the number of base items (must be a non-negative integer): "))
        if base_items < 0:
            raise ValueError("Number of base items must be a non-negative integer.")

        drop_rate = float(input("Enter the drop rate percentage for the final item (0 to 100): "))
        if not (0 <= drop_rate <= 100):
            raise ValueError("Drop rate percentage must be between 0 and 100.")

        # Calculate probability of at least one drop
        probability = calculate_cumulative_probability(base_items, drop_rate)
        print(f"\nThe probability of getting the item at least once with {base_items} attempts is: {probability:.2f}%")

        # Display required attempts for target success rates
        success_targets = [50, 75, 90, 99]
        print("\nAttempts needed to achieve specific success rates:")
        for target in success_targets:
            attempts_needed = calculate_attempts_for_success_rate(drop_rate, target)
            print(f" - {target}% success rate: {attempts_needed} attempts")

        # Ask if the item dropped
        item_dropped = check_item_drop()
        if item_dropped:
            print(f"\nCongratulations! You got the item in {base_items} tries.")
            actual_success_rate = (1 / base_items) * 100
            print(f"Your actual success rate was: {actual_success_rate:.2f}%")
        else:
            print("\nBetter luck next time! Keep trying, and the odds will eventually be in your favor.")

        # Display a random probability quote
        display_random_probability_quote()

    except ValueError as e:
        print(f"Input error: {e}")
