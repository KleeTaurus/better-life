from rich.console import Console
from rich.table import Table
from utils import format_currency


def annual_growth_rate(working_years, tier_key=1):
    growth_tier = {
        0: [1.5, 1.3,  1.2,  1.1],
        1: [1.3, 1.2,  1.1,  1.05],
        2: [1.2, 1.1,  1.05, 1.0],
        3: [1.1, 1.05, 1.0,  1.0]
    }

    if 0 <= working_years < 5:
        return growth_tier[tier_key][0]
    elif 5 <= working_years < 10:
        return growth_tier[tier_key][1]
    elif 10 <= working_years < 20:
        return growth_tier[tier_key][2]
    else:
        return growth_tier[tier_key][3]


def generate_table():
    table = Table(show_header=True, header_style='bold')
    table.add_column('Age')
    table.add_column('Annual Growth Rate')
    table.add_column('Monthly Salary (RMB)', justify='right')
    table.add_column('Total Income (RMB)', justify='right')
    table.add_column('Total Deposit (RMB)', justify='right')
    table.add_column('Real Deposit (RMB)', justify='right')

    return table


def calculate(working_age=22,
              retirement_age=51,
              monthly_salary=5000,
              bonus=2,
              deposit_ratio=0.4):
    total_income = 0
    total_deposit = 0
    purchasing_power = 0

    table = generate_table()

    i = working_age
    while i <= retirement_age:
        annual_income = monthly_salary * (12 + bonus)
        total_income += annual_income
        annual_deposit = annual_income * deposit_ratio
        total_deposit += annual_deposit
        purchasing_power = purchasing_power * (1 - 0.05) + annual_deposit

        agr = annual_growth_rate(i - working_age)

        table.add_row(str(i),
                      str(agr),
                      format_currency(monthly_salary),
                      format_currency(total_income),
                      format_currency(total_deposit),
                      format_currency(purchasing_power))

        monthly_salary *= agr
        i += 1

    console = Console()
    console.print(table)


if __name__ == '__main__':
    calculate()
