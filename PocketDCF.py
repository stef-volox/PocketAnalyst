import numpy as np
import pandas as pd
from rich.console import Console
from rich.table import Table

console = Console()

def calculate_fcfs(projections):
    """
    Calculate Free Cash Flows (FCF) from projections dataframe.
    """
    projections['FCF'] = (
        projections['EBIT'] - (projections['EBIT'] * projections['Tax Rate']) +
        projections['Depreciation'] -
        projections['CapEx'] -
        projections['Change in Working Capital']
    )
    return projections['FCF']

def calculate_wacc(equity_value, debt_value, cost_of_equity, cost_of_debt, tax_rate):
    """
    Calculate Weighted Average Cost of Capital (WACC).
    """
    total_value = equity_value + debt_value
    wacc = (
        (equity_value / total_value) * cost_of_equity +
        (debt_value / total_value) * cost_of_debt * (1 - tax_rate)
    )
    return wacc

def discount_cash_flows(fcfs, wacc, terminal_growth_rate, final_year):
    """
    Discount cash flows to calculate present value (PV) including terminal value (TV).
    Handles cases where terminal growth rate is greater than or equal to WACC.
    """
    if terminal_growth_rate >= wacc:
        console.print(
            f"[yellow]Warning: Terminal growth rate ({terminal_growth_rate:.2%}) is >= WACC ({wacc:.2%}). "
            f"Capping terminal growth rate to {wacc - 0.01:.2%} to avoid unrealistic valuation.[/yellow]"
        )
        terminal_growth_rate = wacc - 0.01

    tv = fcfs.iloc[-1] * (1 + terminal_growth_rate) / (wacc - terminal_growth_rate)
    
    years = np.arange(1, len(fcfs) + 1)
    discounted_fcfs = fcfs / ((1 + wacc) ** years)
    
    discounted_tv = tv / ((1 + wacc) ** final_year)
    
    return discounted_fcfs, discounted_tv, discounted_fcfs.sum() + discounted_tv

def validate_input(prompt, min_val=None, max_val=None, input_type=float):
    """
    Utility function for input validation.
    """
    while True:
        try:
            value = input_type(console.input(prompt))
            if min_val is not None and value < min_val:
                raise ValueError(f"Value must be >= {min_val}.")
            if max_val is not None and value > max_val:
                raise ValueError(f"Value must be <= {max_val}.")
            return value
        except ValueError as e:
            console.print(f"[red]{e}[/red]")
            
if __name__ == "__main__":
    console.print("[bold cyan]Enter your financial projections:[/bold cyan]")
    years = validate_input("Enter the number of years for projections: ", min_val=1, input_type=int)

    data = {
        'EBIT': [],
        'Tax Rate': [],
        'Depreciation': [],
        'CapEx': [],
        'Change in Working Capital': []
    }

    for year in range(1, years + 1):
        console.print(f"\n[bold green]Year {year}:[/bold green]")
        data['EBIT'].append(validate_input("  [cyan]EBIT: [/cyan]", min_val=0))
        data['Tax Rate'].append(validate_input("  [cyan]Tax Rate (as a decimal, e.g., 0.25): [/cyan]", min_val=0, max_val=1))
        data['Depreciation'].append(validate_input("  [cyan]Depreciation: [/cyan]", min_val=0))
        data['CapEx'].append(validate_input("  [cyan]CapEx: [/cyan]", min_val=0))
        data['Change in Working Capital'].append(validate_input("  [cyan]Change in Working Capital: [/cyan]"))

    projections = pd.DataFrame(data)

    console.print("\n[bold yellow]Enter WACC calculation inputs:[/bold yellow]")
    equity_value = validate_input("  [cyan]Equity Value: [/cyan]", min_val=0)
    debt_value = validate_input("  [cyan]Debt Value: [/cyan]", min_val=0)
    cost_of_equity = validate_input("  [cyan]Cost of Equity (as a decimal, e.g., 0.08): [/cyan]", min_val=0, max_val=1)
    cost_of_debt = validate_input("  [cyan]Cost of Debt (as a decimal, e.g., 0.05): [/cyan]", min_val=0, max_val=1)
    tax_rate = validate_input("  [cyan]Tax Rate (as a decimal, e.g., 0.25): [/cyan]", min_val=0, max_val=1)

    terminal_growth_rate = validate_input("\n[bold yellow]Enter Terminal Growth Rate (as a decimal, e.g., 0.02): [/bold yellow]", min_val=0, max_val=0.1)

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
    discounted_fcfs, discounted_tv, pv = discount_cash_flows(fcfs, wacc, terminal_growth_rate, final_year)

    console.print("\n[bold yellow]Results:[/bold yellow]")
    console.print(f"  [bold cyan]WACC: [/bold cyan]{wacc:.2%}")
    console.print(f"  [bold cyan]Enterprise Value (Present Value of Cash Flows): [/bold cyan][bold green]{pv:,.2f}[/bold green]")