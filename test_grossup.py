from br_yield_tools.grossup import tax_rate_by_days, iof_rate_by_day, tax_equivalent_gross

def test_ir_table():
    assert tax_rate_by_days(10) == 0.225
    assert tax_rate_by_days(200) == 0.20
    assert tax_rate_by_days(400) == 0.175
    assert tax_rate_by_days(1000) == 0.15

def test_iof_table():
    assert abs(iof_rate_by_day(1) - 29/30) < 1e-9
    assert iof_rate_by_day(30) == 0.0
    assert iof_rate_by_day(60) == 0.0

def test_tax_equivalence_simple():
    gross = tax_equivalent_gross(0.10, 800)  # ~11.76% a.a.
    assert 0.117 < gross < 0.118
