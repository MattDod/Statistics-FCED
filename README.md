# Statistics-FCED

## Rural fires in Portuguese municipalities

### General research question
How do the frequency, detection, and emergency response characteristics of rural
fires vary across Portuguese municipalities before and after 2017?

### Scope and study design

The analysis uses the official SGIF rural-fire records for 2011–2020. The main
comparisons are made between:

- **2014–2016** — pre-2017 period
- **2018–2020** — post-2017 period

The year **2017 is excluded** from the before/after comparisons so that it does
not act as a transition year.

The selected municipalities are:

- **Alijó** — northern inland Portugal
- **Mirandela** — northern inland Portugal
- **Alcácer do Sal** — southern Portugal (Alentejo)
- **Odemira** — southern Portugal

### Specific research questions and statistical tests

#### 1. Temporal evolution — comparison of means

Did the mean monthly number of rural-fire occurrences change significantly
between 2014–2016 and 2018–2020?

**Test:** Welch's t-test for independent samples, or a paired approach if the
monthly observations can be matched appropriately.

#### 2. Emergency response — ANOVA

Does the mean time between the fire alert and the first intervention differ
significantly among the four municipalities?

**Test:** Welch's ANOVA, after evaluating the relevant assumptions.

The response time is calculated from `DataHoraAlerta` to
`DataHora_PrimeiraIntervencao`, in minutes.

#### 3. Human involvement in fire detection

Does the distribution of fire-alert sources differ significantly among the
selected municipalities?

**Test:** Chi-square test of independence using `FonteAlerta`.

#### 4. Public participation — comparison of proportions

Did the proportion of rural-fire alerts reported by the general public change
significantly between 2014–2016 and 2018–2020?

**Test:** Comparison of two proportions, including a confidence interval for
the difference between proportions.

The definition of the “general public” alert-source category must follow the
categories recorded in `FonteAlerta` and be documented in the report.

### Variables

**Qualitative variables**

- `Concelho` — municipality
- `Periodo` — 2014–2016 or 2018–2020
- `FonteAlerta` — first source to detect/report the fire

**Quantitative variables**

- Monthly number of fire occurrences
- Time to first intervention (minutes)
- `AreaTotal_ha` — burned area per occurrence (hectares)
- `FWI` — Fire Weather Index

Additional fields available in the dataset include the alert date/time,
municipality, cause classification, location, and other fire-weather indices.

### Data source

The primary data source is the SGIF dataset:
`13-Registos-Incendios-SGIF-2011-2020/Registos_Incendios_SGIF_2011_2020.xlsx`

The workbook contains the main sheet `SGIF_2011_2020` and supporting
legends/lookup information. The analysis should filter `Concelho` to the four
selected municipalities and `Ano` to the two study periods.

### Analysis workflow

1. Load and inspect the SGIF workbook and its variable legend.
2. Filter the selected municipalities and the years 2014–2016 and 2018–2020.
3. Create the period variable and calculate response time in minutes.
4. Aggregate fire occurrences by municipality, period, and month.
5. Produce descriptive tables and graphics.
6. Check assumptions and apply the planned inference tests.
7. Report effect estimates, confidence intervals, p-values, limitations, and
   practical interpretation.

### Deliverables checklist

- [ ] Jupyter notebook report (text, code, figures)
- [ ] Video presentation (maximum 10 minutes, with individual contributions)
- [ ] Intra-team evaluation submitted
- [ ] Cross-team evaluation submitted
- [ ] Final research question validated by **agomes@fe.up.pt**

## Repository structure

- `README.md` — project framing, variables, data source, and analysis plan
- `report.ipynb` — notebook for the report deliverable
- `13-Registos-Incendios-SGIF-2011-2020/` — SGIF data and workbook legends
