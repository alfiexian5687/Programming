def main():
    """Display income report for incomes over a given number of no_of_months."""
    incomes = []
    no_of_months = int(input("How many no_of_months? "))

    for MONTH in range(1, no_of_months + 1):
        income = float(input("Enter income for MONTH " + str(MONTH) + ": "))
        incomes.append(income)

    result(incomes, no_of_months)

def result(incomes, months):
    print("\nIncome Report\n-------------")
    total = 0
    for MONTH in range(1, months + 1):
        income = incomes[MONTH - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(MONTH, income, total))


main()