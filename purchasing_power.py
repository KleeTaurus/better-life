from rich.console import Console
from rich.table import Table
from utils import format_currency


def calculate(total_deposit=10000000, years=20, inflation_ratio=0.05):
    deposit = total_deposit

    table = Table(show_header=True, header_style='bold')
    table.add_column('#')
    table.add_column('Real Deposit (RMB)')

    for i in range(1, years + 1):
        deposit -= deposit * inflation_ratio
        table.add_row(str(i), format_currency(deposit))

    console = Console()
    console.print(table)


if __name__ == '__main__':
    calculate()
