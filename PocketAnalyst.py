import pandas as pd
from rich.console import Console
from rich.table import Table
from rich.style import Style
from PIL import Image
import os

console = Console()

def calculate_score(df_val, df_bs, df_is, df_cf, df_st):
    score = 0
    scores_breakdown = []
    
    current_price = pd.to_numeric(df_val.iloc[10, 1].replace('%', '').replace(',', ''), errors='coerce')
    buy_price = pd.to_numeric(df_val.iloc[13, 1].replace('%', '').replace(',', ''), errors='coerce')
    tl_ta = pd.to_numeric(df_bs.iloc[10, 1].replace('%', '').replace(',', ''), errors='coerce')
    nd_te = pd.to_numeric(df_bs.iloc[11, 1].replace('%', '').replace(',', ''), errors='coerce')
    cr_cl = pd.to_numeric(df_bs.iloc[12, 1].replace('%', '').replace(',', ''), errors='coerce')
    op_inc_20 = pd.to_numeric(df_is.iloc[2, 1].replace('%', '').replace(',', ''), errors='coerce')
    op_inc_ttm = pd.to_numeric(df_is.iloc[2, 5].replace('%', '').replace(',', ''), errors='coerce')
    net_inc_20 = pd.to_numeric(df_is.iloc[5, 1].replace('%', '').replace(',', ''), errors='coerce')
    net_inc_ttm = pd.to_numeric(df_is.iloc[5, 5].replace('%', '').replace(',', ''), errors='coerce')
    capex_20 = pd.to_numeric(df_cf.iloc[3, 1].replace('%', '').replace(',', ''), errors='coerce')
    capex_ttm = pd.to_numeric(df_cf.iloc[3, 5].replace('%', '').replace(',', ''), errors='coerce')
    fcf_20 = pd.to_numeric(df_cf.iloc[4, 1].replace('%', '').replace(',', ''), errors='coerce')
    fcf_ttm = pd.to_numeric(df_cf.iloc[4, 5].replace('%', '').replace(',', ''), errors='coerce')
    spread_20 = pd.to_numeric(df_st.iloc[3, 1].replace('%', '').replace(',', ''), errors='coerce')
    spread_ttm = pd.to_numeric(df_st.iloc[3, 5].replace('%', '').replace(',', ''), errors='coerce')
    
    def safe_value(val, default=0):
        return default if pd.isna(val) else val

    tl_ta = safe_value(tl_ta)
    nd_te = safe_value(nd_te)
    cr_cl = safe_value(cr_cl)
    op_inc_20 = safe_value(op_inc_20)
    op_inc_ttm = safe_value(op_inc_ttm)
    net_inc_20 = safe_value(net_inc_20)
    net_inc_ttm = safe_value(net_inc_ttm)
    capex_20 = safe_value(capex_20)
    capex_ttm = safe_value(capex_ttm)
    fcf_20 = safe_value(fcf_20)
    fcf_ttm = safe_value(fcf_ttm)
    spread_20 = safe_value(spread_20)
    spread_ttm = safe_value(spread_ttm)

    def add_criteria(description, condition_score):
        scores_breakdown.append([description, condition_score])
        return condition_score

    score += add_criteria("Current price vs Buy price", -100 if current_price > buy_price else 10)
    score += add_criteria("Total Liabilities / Total Assets", 10 if tl_ta < 70 else 0)
    score += add_criteria("Net Debt / Total Equity", 10 if nd_te < 100 else 0)
    score += add_criteria("Cash Reserves / Current Liabilities", 10 if cr_cl > 100 else 0)

    criteria_sum = (int(tl_ta < 70) * 10) + (int(nd_te < 100) * 10) + (int(cr_cl > 100) * 10)
    score += add_criteria("Bankruptcy Chance", -50 if criteria_sum < 20 else 0)
    score += add_criteria("Bankruptcy Chance 2", +20 if criteria_sum == 30 else 0)

    score += add_criteria("Operating Income TTM vs FY20", 10 if op_inc_ttm > op_inc_20 else -10)
    score += add_criteria("Operating Income TTM", -10 if op_inc_ttm < 0 else 2.5)
    score += add_criteria("Net Income TTM vs FY20", 10 if net_inc_ttm > net_inc_20 else -10)
    score += add_criteria("Net Income TTM", -10 if net_inc_ttm < 0 else 2.5)
    score += add_criteria("CapEx TTM vs FY20", 10 if capex_ttm < capex_20 else -10)
    score += add_criteria("CapEx TTM", -10 if capex_ttm > 100 else 2.5)
    score += add_criteria("Free Cash Flow TTM vs FY20", 10 if fcf_ttm > fcf_20 else -10)
    score += add_criteria("Free Cash Flow TTM", -10 if fcf_ttm < 0 else 2.5)
    score += add_criteria("Economic Spread TTM vs FY20", 10 if spread_ttm > spread_20 else -10)
    score += add_criteria("Economic Spread TTM", -10 if spread_ttm < 0 else 2.5)

    return score, scores_breakdown

df_val = pd.read_csv('/YOUR_PATH/PocketAnalyst/Toolkit/Valuation-Grahams Formula.csv', header=None)
df_bs = pd.read_csv('/YOUR_PATH/PocketAnalyst/Toolkit/Valuation-Consolidated Balance Sheet.csv', header=None)
df_is = pd.read_csv('/YOUR_PATH/PocketAnalyst/Toolkit/Valuation-Consolidated Income Statement (USD, millions).csv', header=None)
df_cf = pd.read_csv('/YOUR_PATH/PocketAnalyst/Toolkit/Valuation-Consolidated Cash Flow Statement (USD, millions).csv', header=None)
df_st = pd.read_csv('/YOUR_PATH/PocketAnalyst/Toolkit/Valuation-Economic Profit Spread (Trailing).csv', header=None)

total_score, breakdown = calculate_score(df_val, df_bs, df_is, df_cf, df_st)

table = Table(title="Score Breakdown", title_style=Style(color="cyan", bold=True))

table.add_column("Criteria", style="bold cyan")
table.add_column("Score", justify="center", style="bold magenta")

for description, score in breakdown:
    color = "green" if score > 0 else "red" if score < 0 else "white"
    table.add_row(description, f"[{color}]{score}[/{color}]")
    
table.add_row("[bold yellow]Total Score[/bold yellow]", f"[bold blue]{total_score}[/bold blue]")

console.print(table)