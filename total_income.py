from rich.console import Console
from rich.table import Table
from utils import format_currency


def annual_growth_rate(working_years):
    if 0 <= working_years < 5:
        return 1.3
    elif 5 <= working_years < 10:
        return 1.2
    elif 10 <= working_years < 20:
        return 1.08
    else:
        return 1.0


def calculate(working_age=22,
              retirement_age=51,
              monthly_salary=10000,
              bonus=2,
              deposit_ratio=0.4):
    total_income = 0
    total_deposit = 0
    real_deposit = 0

    i = working_age

    table = Table(show_header=True, header_style='bold')
    table.add_column('Age')
    table.add_column('Annual Growth Rate')
    table.add_column('Monthly Salary (RMB)', justify='right')
    table.add_column('Total Income (RMB)', justify='right')
    table.add_column('Total Deposit (RMB)', justify='right')
    table.add_column('Real Deposit (RMB)', justify='right')

    while i <= retirement_age:
        annual_income = monthly_salary * 12 + monthly_salary * bonus
        total_income += annual_income
        total_deposit += annual_income * deposit_ratio
        real_deposit = annual_income * deposit_ratio + real_deposit * (1 - 0.08)

        agr = annual_growth_rate(i - working_age)

        table.add_row(str(i),
                      str(agr),
                      format_currency(monthly_salary),
                      format_currency(total_income),
                      format_currency(total_deposit),
                      format_currency(real_deposit))

        monthly_salary *= agr
        i += 1

    console = Console()
    console.print(table)


if __name__ == '__main__':
    calculate()
