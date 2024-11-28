import numpy as np
import pandas as pd
from rich.console import Console
from rich.table import Table

console = Console()

def calculate_fcfs(projections):
    projections['FCF'] = (
        projections['EBIT'] * (1 - projections['Tax Rate']) +
        projections['Depreciation'] -
        projections['CapEx'] -
        projections['Change in Working Capital']
    )
    return projections['FCF']

def calculate_wacc(equity_value, debt_value, cost_of_equity, cost_of_debt, tax_rate):
    total_value = equity_value + debt_value
    wacc = (
        (equity_value / total_value) * cost_of_equity +
        (debt_value / total_value) * cost_of_debt * (1 - tax_rate)
    )
    return wacc

def discount_cash_flows(fcfs, wacc, terminal_growth_rate, final_year):
    tv = fcfs.iloc[-1] * (1 + terminal_growth_rate) / (wacc - terminal_growth_rate)
    
    years = np.arange(1, len(fcfs) + 1)
    discounted_fcfs = fcfs / ((1 + wacc) ** years)
    discounted_tv = tv / ((1 + wacc) ** final_year)
    
    return discounted_fcfs.sum() + discounted_tv

if __name__ == "__main__":
    print("Enter your financial projections:")

    years = int(input("Enter the number of years for projections: "))
    data = {
        'EBIT': [],
        'Tax Rate': [],
        'Depreciation': [],
        'CapEx': [],
        'Change in Working Capital': []
    }

    for year in range(1, years + 1):
        console.print(f"\n[bold green]Year {year}:[/bold green]")
        data['EBIT'].append(float(console.input(f"  [cyan]EBIT: [/cyan]")))
        data['Tax Rate'].append(float(console.input(f"  [cyan]Tax Rate (as a decimal, e.g., 0.25): [/cyan]")))
        data['Depreciation'].append(float(console.input(f"  [cyan]Depreciation: [/cyan]")))
        data['CapEx'].append(float(console.input(f"  [cyan]CapEx: [/cyan]")))
        data['Change in Working Capital'].append(float(console.input(f"  [cyan]Change in Working Capital: [/cyan]")))

    projections = pd.DataFrame(data)

    console.print("\n[bold yellow]Enter WACC calculation inputs:[/bold yellow]")
    equity_value = float(console.input("  [cyan]Equity Value: [/cyan]"))
    debt_value = float(console.input("  [cyan]Debt Value: [/cyan]"))
    cost_of_equity = float(console.input("  [cyan]Cost of Equity (as a decimal, e.g., 0.08): [/cyan]"))
    cost_of_debt = float(console.input("  [cyan]Cost of Debt (as a decimal, e.g., 0.05): [/cyan]"))
    tax_rate = float(console.input("  [cyan]Tax Rate (as a decimal, e.g., 0.25): [/cyan]"))

    terminal_growth_rate = float(console.input("\n[bold yellow]Enter Terminal Growth Rate (as a decimal, e.g., 0.02): [/bold yellow]"))

    fcfs = calculate_fcfs(projections)

    console.print("\n[bold green]Projections Summary:[/bold green]")
    table = Table(title="Financial Projections")
    table.add_column("Year", justify="center", style="cyan")
    table.add_column("EBIT", justify="right")
    table.add_column("Tax Rate", justify="right")
    table.add_column("Depreciation", justify="right")
    table.add_column("CapEx", justify="right")
    table.add_column("Change in WC", justify="right")
    table.add_column("FCF", justify="right", style="green")

    for i, row in projections.iterrows():
        table.add_row(
            str(i + 1),
            f"{row['EBIT']:.2f}",
            f"{row['Tax Rate']:.2%}",
            f"{row['Depreciation']:.2f}",
            f"{row['CapEx']:.2f}",
            f"{row['Change in Working Capital']:.2f}",
            f"{fcfs.iloc[i]:.2f}"
        )
    console.print(table)

    wacc = calculate_wacc(equity_value, debt_value, cost_of_equity, cost_of_debt, tax_rate)

    final_year = len(projections)
    pv = discount_cash_flows(fcfs, wacc, terminal_growth_rate, final_year)

    console.print("\n[bold yellow]Results:[/bold yellow]")
    console.print(f"  [bold cyan]WACC: [/bold cyan]{wacc:.2%}")
    console.print(f"  [bold cyan]Enterprise Value (Present Value of Cash Flows): [/bold cyan][bold green]{pv:,.2f}[/bold green]")