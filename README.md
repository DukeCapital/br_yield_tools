# br_yield_tools
Utilitários simples para comparar ativos **isentos** vs. **tributáveis** no Brasil: gross-up do CDI, IR regressivo e IOF.

## Funções
- `tax_rate_by_days(dias)`: IR regressivo (22,5% / 20% / 17,5% / 15%).
- `iof_rate_by_day(dia)`: curva do IOF até D+30.
- `net_yield_taxable(gross_aa, dias)`: rendimento líquido após IOF/IR.
- `tax_equivalent_gross(exempt_aa, dias)`: taxa bruta equivalente p/ empatar com isento.
- `cdi_equivalent_for_exempt(exempt_aa, dias, cdi_aa)`: % do CDI equivalente.

## Exemplo
```python
from br_yield_tools.grossup import tax_equivalent_gross
print(round(tax_equivalent_gross(0.10, 800)*100, 2))  # ~11.76% a.a.
