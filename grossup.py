from __future__ import annotations

BUSINESS_DAYS = 252

def annual_to_daily(rate_aa: float) -> float:
    return (1 + rate_aa) ** (1 / BUSINESS_DAYS) - 1

def daily_to_annual(rate_ad: float) -> float:
    return (1 + rate_ad) ** BUSINESS_DAYS - 1

def tax_rate_by_days(days: int) -> float:
    if days <= 180:
        return 0.225
    elif days <= 360:
        return 0.20
    elif days <= 720:
        return 0.175
    else:
        return 0.15

def iof_rate_by_day(day: int) -> float:
    if day <= 0:
        return 1.0
    if day >= 30:
        return 0.0
    return (30 - day) / 30.0

def net_yield_taxable(gross_aa: float, days: int) -> float:
    business_days = int(round(days / 365 * BUSINESS_DAYS))
    rd = annual_to_daily(gross_aa)
    gross_factor = (1 + rd) ** business_days
    gross_profit = gross_factor - 1.0

    if days <= 30:
        iof_coeff = iof_rate_by_day(days)
        iof_tax = gross_profit * iof_coeff
        profit_after_iof = gross_profit - iof_tax
    else:
        iof_tax = 0.0
        profit_after_iof = gross_profit

    ir = tax_rate_by_days(days)
    ir_tax = profit_after_iof * ir
    net_profit = gross_profit - iof_tax - ir_tax

    net_factor = 1.0 + net_profit
    net_rd = net_factor ** (1 / business_days) - 1 if business_days > 0 else 0.0
    return (1 + net_rd) ** BUSINESS_DAYS - 1

def tax_equivalent_gross(exempt_aa: float, days: int) -> float:
    if days <= 30:
        target = exempt_aa
        lo, hi = 0.0, 2.0
        for _ in range(60):
            mid = (lo + hi) / 2
            net_mid = net_yield_taxable(mid, days)
            if net_mid < target:
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2
    else:
        ir = tax_rate_by_days(days)
        return exempt_aa / (1 - ir)

def cdi_equivalent_for_exempt(exempt_aa: float, days: int, cdi_aa: float) -> float:
    gross_needed = tax_equivalent_gross(exempt_aa, days)
    if cdi_aa <= 0:
        return float('inf')
    return gross_needed / cdi_aa
