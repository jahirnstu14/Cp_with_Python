#1+(2+3*4)+(5+6*7+8*9*10)+...+n
def calculate_series_sum(n):
    result = 0
    current_number = 1
    term_start = 1
    
    for i in range(1, n + 1):
        term_sum = 0
        
        # Calculate the sum of numbers in the current term
        for j in range(term_start, current_number + 1):
            term_sum += j
        
        # Add the computed term sum to the overall result
        result += term_sum
        
        # Update values for the next term
        current_number += 1
        term_start = current_number * (current_number - 1) + 1
    
    return result

# Example usage:
n = 4
sum_result = calculate_series_sum(n)
print(f"The sum of the series up to {n} terms is: {sum_result}")

