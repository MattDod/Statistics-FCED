# Formulário Completo de Inferência Estatística — Parte 1 (Cálculo Manual)

Este guia contém todas as fórmulas matemáticas, condições de validade, regras de decisão e tabelas necessárias para a **Parte 1 (Inspecção / Resolução Manual sem Software)** da prova de Estatística / Inferência Estatística.

---

## 1. Estrutura Universal de Inferência
* **Intervalo de Confiança (IC):**
  $$\text{IC} = \text{Estimativa Pontual} \pm \text{Margem de Erro (ME)}$$
  $$\text{ME} = \text{Valor Crítico } (z^* \text{ ou } t^*) \times \text{Erro Padrão } (SE)$$

* **Estatística de Teste de Hipóteses:**
  $$\text{Estatística de Teste } (Z \text{ ou } T) = \frac{\text{Estimativa Pontual} - \text{Valor Nulo (sob } H_0)}{\text{Erro Padrão } (SE)}$$

* **Regra de Decisão pelo $p$-value:**
  * Se $p\text{-value} \le \alpha \implies$ **Rejeita-se $H_0$** (Existe evidência estatística).
  * Se $p\text{-value} > \alpha \implies$ **Não se rejeita $H_0$** (Não há evidência estatística suficiente).

---

## 2. Inferência para 1 Proporção ($p$)

### A. Parâmetros e Estimador
* **Proporção Amostral:** $\hat{p} = \frac{x}{n}$ (onde $x$ é o número de sucessos e $n$ o tamanho da amostra).

### B. Condição Sucesso-Falha (Validade Normal)
* Para IC: $n\hat{p} \ge 10$ e $n(1-\hat{p}) \ge 10$
* Para Teste de Hipóteses: $n p_0 \ge 10$ e $n(1-p_0) \ge 10$ (usando o valor nulo $p_0$)

### C. Erro Padrão ($SE$)
* **Para IC:** $SE_{\hat{p}} = \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$
* **Para Teste de Hipóteses:** $SE_{p_0} = \sqrt{\frac{p_0(1-p_0)}{n}}$

### D. Fórmulas
* **Intervalo de Confiança:**
  $$\text{IC}_{1-\alpha}(p) = \hat{p} \pm z^* \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$$
* **Estatística $Z$ do Teste ($H_0: p = p_0$):**
  $$Z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}}$$

---

## 3. Inferência para Comparação de 2 Proporções Independentes ($p_1 - p_2$)

### A. Estimador Pontual
* Diferença amostral: $\hat{p}_1 - \hat{p}_2 = \frac{x_1}{n_1} - \frac{x_2}{n_2}$

### B. Condição Sucesso-Falha
* $n_1\hat{p}_1 \ge 10$, $n_1(1-\hat{p}_1) \ge 10$, $n_2\hat{p}_2 \ge 10$, e $n_2(1-\hat{p}_2) \ge 10$

### C. Erro Padrão ($SE$)
* **Para Intervalo de Confiança:**
  $$SE_{\hat{p}_1 - \hat{p}_2} = \sqrt{\frac{\hat{p}_1(1-\hat{p}_1)}{n_1} + \frac{\hat{p}_2(1-\hat{p}_2)}{n_2}}$$
* **Para Teste de Hipóteses ($H_0: p_1 - p_2 = 0 \iff p_1 = p_2$):**
  * Usa-se a **Proporção Combinada (*Pooled Proportion*)**:
    $$\hat{p}_{\text{pooled}} = \frac{x_1 + x_2}{n_1 + n_2} = \frac{n_1\hat{p}_1 + n_2\hat{p}_2}{n_1 + n_2}$$
  * Erro Padrão Combinado:
    $$SE_{\text{pooled}} = \sqrt{\hat{p}_{\text{pooled}}(1-\hat{p}_{\text{pooled}}) \left( \frac{1}{n_1} + \frac{1}{n_2} \right)}$$

### D. Fórmulas
* **Intervalo de Confiança:**
  $$\text{IC}_{1-\alpha}(p_1 - p_2) = (\hat{p}_1 - \hat{p}_2) \pm z^* \sqrt{\frac{\hat{p}_1(1-\hat{p}_1)}{n_1} + \frac{\hat{p}_2(1-\hat{p}_2)}{n_2}}$$
* **Estatística $Z$ do Teste ($H_0: p_1 = p_2$):**
  $$Z = \frac{(\hat{p}_1 - \hat{p}_2) - 0}{SE_{\text{pooled}}}$$

---

## 4. Inferência para 1 Média ($\mu$) — Distribuição $t$ de Student

### A. Condições de Aplicabilidade
* Observações independentes (amostra aleatória, $n < 10\%$ da população se sem reposição).
* Normalidade dos dados ou sem *outliers* nem assimetria extrema (se $n \ge 30$, o Teorema do Limite Central garante robustez).

### B. Erro Padrão e Graus de Liberdade
* Erro Padrão: $SE_{\bar{x}} = \frac{s}{\sqrt{n}}$
* Graus de Liberdade: $df = n - 1$

### C. Fórmulas
* **Intervalo de Confiança:**
  $$\text{IC}_{1-\alpha}(\mu) = \bar{x} \pm t^*_{df} \cdot \frac{s}{\sqrt{n}}$$
* **Estatística $T$ do Teste ($H_0: \mu = \mu_0$):**
  $$T_{df} = \frac{\bar{x} - \mu_0}{\frac{s}{\sqrt{n}}}$$

---

## 5. Inferência para Dados Emparelhados ($\mu_{\text{diff}}$)

Usado quando existe correspondência direta entre as observações (ex: antes/depois, par 1/par 2).

### A. Redução a 1 Amostra de Diferenças
* Diferença de cada par $i$: $d_i = x_{1,i} - x_{2,i}$
* Média das diferenças amostrais: $\bar{x}_{\text{diff}} = \frac{\sum d_i}{n}$
* Desvio-padrão das diferenças: $s_{\text{diff}} = \sqrt{\frac{\sum (d_i - \bar{x}_{\text{diff}})^2}{n-1}}$

### B. Erro Padrão e Graus de Liberdade
* Erro Padrão: $SE_{\bar{x}_{\text{diff}}} = \frac{s_{\text{diff}}}{\sqrt{n}}$
* Graus de Liberdade: $df = n - 1$ ($n$ é o número de **pares**)

### C. Fórmulas
* **Intervalo de Confiança:**
  $$\text{IC}_{1-\alpha}(\mu_{\text{diff}}) = \bar{x}_{\text{diff}} \pm t^*_{n-1} \cdot \frac{s_{\text{diff}}}{\sqrt{n}}$$
* **Estatística $T$ do Teste ($H_0: \mu_{\text{diff}} = 0$):**
  $$T_{n-1} = \frac{\bar{x}_{\text{diff}} - 0}{\frac{s_{\text{diff}}}{\sqrt{n}}}$$

---

## 6. Inferência para 2 Médias Independentes ($\mu_1 - \mu_2$)

### A. Condições de Aplicabilidade
* Independência dentro de cada grupo e **independência entre os dois grupos**.
* Normalidade / ausência de *outliers* extremos em cada grupo individualmente.

### B. Erro Padrão e Graus de Liberdade ($df$)
* **Erro Padrão (Sem assumir variâncias iguais - Teste de Welch):**
  $$SE_{\bar{x}_1 - \bar{x}_2} = \sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}$$
* **Graus de Liberdade (Aproximação conservadora à mão):**
  $$df = \min(n_1 - 1, n_2 - 1)$$
  *(Nota: Em casos especiais com variâncias assumidamente iguais $s_1^2 \approx s_2^2$, usa-se $df = n_1 + n_2 - 2$)*.

### C. Fórmulas
* **Intervalo de Confiança:**
  $$\text{IC}_{1-\alpha}(\mu_1 - \mu_2) = (\bar{x}_1 - \bar{x}_2) \pm t^*_{df} \cdot \sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}$$
* **Estatística $T$ do Teste ($H_0: \mu_1 - \mu_2 = 0$):**
  $$T_{df} = \frac{(\bar{x}_1 - \bar{x}_2) - 0}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}$$

---

## 7. Dimensionamento do Tamanho da Amostra ($n$)

### A. Para 1 Proporção ($p$) com Margem de Erro $ME$ pretendida:
$$n = \left( \frac{z^*}{ME} \right)^2 \cdot p^*(1-p^*)$$
* Se houver uma estimativa prévia $p^*$, usa-se essa estimativa.
* **Cenário mais conservador (pior hipótese / $p^*$ desconhecido):** Usa-se $p^* = 0{,}5$, simplificando a fórmula para:
  $$n_{\max} = \frac{(z^*)^2}{4 \cdot (ME)^2}$$
*(Arredondar SEMPRE para o inteiro superior seguinte)*.

### B. Para 1 Média ($\mu$) com Margem de Erro $ME$ pretendida:
$$n = \left( \frac{z^* \cdot \sigma}{ME} \right)^2 \quad \text{ou} \quad n = \left( \frac{z^* \cdot s}{ME} \right)^2$$

---

## 8. Poder do Teste ($1 - \beta$), Tamanho do Efeito e Erros de Decisão

### A. Quadro dos Erros de Decisão
| Realidade / Decisão | Não Rejeitar $H_0$ | Rejeitar $H_0$ |
| :--- | :--- | :--- |
| **$H_0$ é Verdadeira** | Decisão Correta ($1 - \alpha$) | **Erro do Tipo I ($\alpha$)** |
| **$H_0$ é Falsa** | **Erro do Tipo II ($\beta$)** | **Poder do Teste ($1 - \beta$)** |

### B. Conceitos Principais
* **Nível de Significância ($\alpha$):** Probabilidade de rejeitar $H_0$ quando ela é verdadeira.
* **Erro Tipo II ($\beta$):** Probabilidade de falhar em rejeitar $H_0$ quando ela é falsa.
* **Poder do Teste ($1 - \beta$):** Probabilidade de detetar uma diferença real existente (rejeitar $H_0$ quando ela é falsa).
* **Tamanho do Efeito (Cohen's $d$):**
  $$d = \frac{|\mu_1 - \mu_2|}{s_{\text{pooled}}}$$
  * $d \approx 0{,}2$: Efeito pequeno
  * $d \approx 0{,}5$: Efeito médio
  * $d \approx 0{,}8$: Efeito grande

### C. Fatores que AUMENTAM o Poder do Teste ($1 - \beta$):
1. **Aumentar o tamanho da amostra ($n$)** $\implies$ diminui o $SE$.
2. **Aumentar o nível de significância ($\alpha$)** (ex: subir de 1% para 5%).
3. **Aumentar a diferença real a detetar ($|\mu_1 - \mu_2|$)** $\implies$ aumenta o $d$.
4. **Diminuir a variabilidade dos dados ($\sigma$ ou $s$)**.

---

## 9. ANOVA — Análise de Variância (Comparação de $k \ge 3$ Médias)

### A. Hipóteses
* $H_0: \mu_1 = \mu_2 = \dots = \mu_k$ *(Todas as médias populacionais são iguais)*
* $H_A:$ Pelo menos uma das médias é diferente das restantes.

### B. Tabela ANOVA Completa (1 Fator)

| Fonte de Variação | Graus de Liberdade ($df$) | Soma dos Quadrados ($SS$) | Quadrados Médios ($MS$) | Estatística $F$ |
| :--- | :--- | :--- | :--- | :--- |
| **Entre Grupos (*Group*)** | $df_G = k - 1$ | $SSG = \sum_{i=1}^k n_i(\bar{x}_i - \bar{x}_{\text{geral}})^2$ | $MSG = \frac{SSG}{k - 1}$ | $F = \frac{MSG}{MSE}$ |
| **Erros / Resíduos (*Error*)** | $df_E = N - k$ | $SSE = \sum_{i=1}^k (n_i - 1)s_i^2 = SST - SSG$ | $MSE = \frac{SSE}{N - k}$ | — |
| **Total** | $df_T = N - 1$ | $SST = \sum (x - \bar{x}_{\text{geral}})^2$ | — | — |

*Onde $k$ é o número de grupos e $N = \sum n_i$ é o total de observações.*

### C. Propriedades e Relações Fundamentais
* $df_T = df_G + df_E \iff (N - 1) = (k - 1) + (N - k)$
* $SST = SSG + SSE$
* $MSE = s_{\text{pooled}}^2$ (Variância combinada dentro dos grupos)

### D. Pós-Hoc: Comparação Múltipla Par a Par (Correção de Bonferroni)
Quando se rejeita $H_0$ na ANOVA, fazem-se testes $t$ a pares com o nível de significância corrigido $\alpha^*$:
$$\alpha^* = \frac{\alpha}{K} \quad \text{onde } K = \frac{k(k-1)}{2} \text{ é o número total de pares de comparação}$$
* **Erro Padrão Pós-Hoc usando $MSE$:**
  $$SE = \sqrt{\frac{MSE}{n_i} + \frac{MSE}{n_j}}$$
* **Estatística $T$ Pós-Hoc:**
  $$T = \frac{\bar{x}_i - \bar{x}_j}{\sqrt{MSE \left(\frac{1}{n_i} + \frac{1}{n_j}\right)}} \quad \text{com } df = df_E = N - k$$

---

## 10. Tabela Resumo dos Erros Padrão ($SE$)

| Cenário / Parâmetro | Estimador | Erro Padrão ($SE$) | Distribuição / $df$ |
| :--- | :--- | :--- | :--- |
| **1 Proporção ($p$) — IC** | $\hat{p}$ | $\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$ | Normal ($z^*$) |
| **1 Proporção ($p$) — Teste** | $\hat{p}$ | $\sqrt{\frac{p_0(1-p_0)}{n}}$ | Normal ($z^*$) |
| **2 Proporções ($p_1 - p_2$) — IC** | $\hat{p}_1 - \hat{p}_2$ | $\sqrt{\frac{\hat{p}_1(1-\hat{p}_1)}{n_1} + \frac{\hat{p}_2(1-\hat{p}_2)}{n_2}}$ | Normal ($z^*$) |
| **2 Proporções ($p_1 - p_2$) — Teste** | $\hat{p}_1 - \hat{p}_2$ | $\sqrt{\hat{p}_{\text{pooled}}(1-\hat{p}_{\text{pooled}})\left(\frac{1}{n_1} + \frac{1}{n_2}\right)}$ | Normal ($z^*$) |
| **1 Média ($\mu$)** | $\bar{x}$ | $\frac{s}{\sqrt{n}}$ | $t$ de Student ($df = n - 1$) |
| **Dados Emparelhados ($\mu_{\text{diff}}$)** | $\bar{x}_{\text{diff}}$ | $\frac{s_{\text{diff}}}{\sqrt{n}}$ | $t$ de Student ($df = n - 1$) |
| **2 Médias Indep. ($\mu_1 - \mu_2$)** | $\bar{x}_1 - \bar{x}_2$ | $\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}$ | $t$ de Student ($df = \min(n_1-1, n_2-1)$) |
| **ANOVA Pós-Hoc ($\mu_i - \mu_j$)** | $\bar{x}_i - \bar{x}_j$ | $\sqrt{MSE \left(\frac{1}{n_i} + \frac{1}{n_j}\right)}$ | $t$ de Student ($df = N - k$) |
