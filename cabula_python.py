# ==============================================================================
# CÁBULA DEFINITIVA EM PYTHON PARA EXAME DE INFERÊNCIA ESTATÍSTICA
# ==============================================================================

# ==============================================================================
# 0. CARREGAMENTO DOS DADOS E BIBLIOTECAS (Fazer no início do exame)
# ==============================================================================
import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.stats.power import TTestIndPower

# Carregar o ficheiro e filtrar outliers se o enunciado pedir (ex: área <= 4000)
# df = pd.read_excel('AmesHouse.xlsx')
# df = df[df['GrLivArea'] <= 4000]


# ==============================================================================
# 1. VALORES CRÍTICOS: z* e t* (função .ppf)
# ==============================================================================
# z* crítico (Distribuição Normal):
z_95_ic = stats.norm.ppf(0.975)       # 1.960 (IC 95% / 2 caudas)
z_95_1cauda = stats.norm.ppf(0.95)    # 1.645 (1 cauda a 5%)

# t* crítico (Distribuição t de Student):
df_graus = 8                          # Graus de liberdade (n-1 ou n1+n2-2)
t_95_ic = stats.t.ppf(0.975, df=df_graus)    # IC 95% (2 caudas)
t_95_1cauda = stats.t.ppf(0.95, df=df_graus) # 1 cauda a 5%


# ==============================================================================
# 2. CÁLCULO DE p-value A PARTIR DE Z OU T CALCULADO (função .cdf)
# ==============================================================================
t_calc = 1.75  # Substituir pelo T ou Z calculado
df_graus = 8   # Graus de liberdade

p_maior = 1 - stats.t.cdf(t_calc, df=df_graus)         # Ha: mu1 > mu2 (Unilateral Superior)
p_menor = stats.t.cdf(t_calc, df=df_graus)            # Ha: mu1 < mu2 (Unilateral Inferior)
p_dif   = 2 * (1 - stats.t.cdf(abs(t_calc), df=df_graus)) # Ha: mu1 != mu2 (Bilateral)
# Nota: Para distribuição Z, usa stats.norm.cdf(...) sem o parâmetro df.


# ==============================================================================
# 3. TESTE t E AMOSTRAGEM ALEATÓRIA (.sample + ttest_ind)
# ==============================================================================
# Exemplo de código para quando o dataframe estiver carregado:
"""
g1 = df[df['Neighborhood'] == 'CollgCr']['SalePrice'].sample(n=30, random_state=42)
g2 = df[df['Neighborhood'] == 'NAmes']['SalePrice'].sample(n=30, random_state=42)

# alternative: 'greater' (Ha: g1 > g2), 'less' (Ha: g1 < g2), 'two-sided' (Ha: g1 != g2)
t_stat, p_val = stats.ttest_ind(g1, g2, alternative='greater')
print(f"Teste t: T = {t_stat:.3f} | p-value = {p_val:.4f}")
"""


# ==============================================================================
# 4. ANOVA: COMPARAÇÃO DE 3 OU MAIS GRUPOS (stats.f_oneway)
# ==============================================================================
# Exemplo de código para quando o dataframe estiver carregado:
"""
v1 = df[df['Neighborhood'] == 'NAmes']['SalePrice']
v2 = df[df['Neighborhood'] == 'Somerst']['SalePrice']
v3 = df[df['Neighborhood'] == 'Gilbert']['SalePrice']

f_stat, p_val = stats.f_oneway(v1, v2, v3)
print(f"ANOVA: F = {f_stat:.3f} | p-value = {p_val:.4f}")
"""


# ==============================================================================
# 5. PODER DO TESTE E TAMANHO DA AMOSTRA (TTestIndPower)
# ==============================================================================
diff = 10000                            # Diferença real a detetar (ex: 10 000 €)
sd_medio = 41463.5                      # Desvio-padrão médio dos grupos
effect_size = diff / sd_medio           # Cohen's d

analysis = TTestIndPower()

# Opção A: Calcular o PODER para um tamanho n (ex: n=9 ou n=65)
poder = analysis.solve_power(effect_size=effect_size, nobs1=9, alpha=0.05, alternative='larger')
# print(f"Poder (n=9): {poder:.4f} | Beta (Erro Tipo II): {1-poder:.4f}")

# Opção B: Descobrir o n NECESSÁRIO para ter 80% de Poder (power=0.80)
n_nec = analysis.solve_power(effect_size=effect_size, power=0.80, alpha=0.05, alternative='larger')
# print(f"Amostra n necessária para 80% de poder: {n_nec:.1f}")
