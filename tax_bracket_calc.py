def calculate_tax(levels, salary):
    remaining_salary = salary
    total_tax = 0
    previous_tax_bracket = 0

    for bracket_limit, tax_rate in levels:
        if bracket_limit is None:
            total_tax += remaining_salary * tax_rate
            break
        if remaining_salary <= 0:
            break

        taxable_bracket = min(remaining_salary, bracket_limit - previous_tax_bracket)

        total_tax += taxable_bracket * tax_rate

        remaining_salary -= taxable_bracket
        previous_bracket = bracket_limit
    return total_tax


def main():
    # Define tax brackets as list of [bracket_limit, tax_rate]
    levels = [[10000, 0.3], [20000, 0.2], [30000, 0.1], [None, 0.1]]

    # Calculate tax for salary of 45000
    tax = calculate_tax(levels, 45000)
    print(f"Total tax: {tax}")  # Should print 7500.0


if __name__ == "__main__":
    main()
