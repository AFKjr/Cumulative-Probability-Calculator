# Cumulative-Probability-Calculator
Simple Cumulative Probability Calculator

This Python script calculates the cumulative probability of obtaining an item drop in games or similar systems. It’s based on the cumulative property of probability, which determines the likelihood of achieving at least one success over multiple attempts. 

### How It Works

The script prompts the user to input:
1. The **number of base items** they have (i.e., the number of attempts).
2. The **drop rate percentage** for the final item (e.g., `32` for a 32% chance per attempt).

Using these inputs, the script calculates the probability of getting at least one drop based on the cumulative probability formula:
\[
P(\text{at least one success}) = 1 - (1 - p)^n
\]
where:
- \( p \) is the drop rate for a single attempt,
- \( n \) is the number of attempts.

### Example Usage

1. **Run the script**:
    ```bash
    python CPC.py
    ```

2. **Input values**:
    - When prompted, enter the number of base items you have (e.g., `50`).
    - Enter the drop rate percentage (e.g., `32`).

3. **View the result**:
    The script will output the cumulative probability of obtaining the item at least once.

### Example

For a scenario where you have 50 base items and a 32% drop rate:
