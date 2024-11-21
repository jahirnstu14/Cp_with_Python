#1+(2+3*4)+(5+6*7+8*9*10)+...+n
def compute_series(n):
    total_sum = 0  # The final sum of the series
    current_number = 1  # The current starting number for each group

    group = 1  # Group starts at 1

    while current_number <= n:
        group_sum = 0  # Sum for the current group

        for multiplier in range(1, group + 1):
            product = 1  # Product for this part of the group

            for _ in range(multiplier):
                if current_number > n:
                    break
                product *= current_number
                current_number += 1

            group_sum += product  # Add the product to the group sum

            if current_number > n:
                break

        total_sum += group_sum  # Add the group sum to the total sum
        group += 1  # Move to the next group

    return total_sum


# Example usage
n = int(input("Enter the value of n: "))
result = compute_series(n)
print(f"The result of the series up to {n} is: {result}")


