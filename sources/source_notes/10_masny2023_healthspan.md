# Masny (2023) — Healthspan Extension, Completeness of Life and Justice

**Full Citation:**  
Masny, M. (2023). Healthspan Extension, Completeness of Life and Justice. *Journal of Applied Philosophy*, forthcoming.

**PDF:** `pdfs/masny2023_healthspan_extension.pdf`

---

## Overview

Masny addresses a central normative question for longevity policy:

**Should health resources prioritize extending life duration or improving quality of remaining life?**

The paper engages with:
1. **The "complete life" view**: Priority to those who haven't yet lived a complete life
2. **Healthspan extension**: Extending the healthy portion of life (not just total life)
3. **Distributive justice**: How to allocate health resources fairly

### Core Argument

Masny argues that the complete-life view (which grounds age-weighting in favor of younger people) has **different implications for healthspan extension** than for lifespan extension:

- Extending healthspan adds good years—ethically similar to giving more life
- But if healthspan extension comes at the *end* of life (compressing morbidity), the complete-life view may not give it priority

The paper disentangles when healthspan extension deserves priority and when it doesn't.

---

## Comprehensive Application to the Core Paper

### 1. The Central Normative Question We Address

Our framework proposes QALY flow $J(\pi)$ as the policy objective. But **should** we maximize aggregate quality-weighted time? Masny's paper directly engages this:

| Normative Issue | Our Treatment | Masny's Contribution |
|-----------------|---------------|----------------------|
| Age-weighting | Not included (Axiom 3 neutrality) | Complete-life view would add age-weights |
| Quality vs. quantity | Combined in $q \cdot dt$ | Distinguishes healthspan from lifespan |
| Priority to worst-off | §8 mentions DCEA | Provides philosophical grounding |

### 2. The Complete-Life View and Our Axiom 3

Our Axiom 3 (Generational Neutrality) states:

> All generations should be treated symmetrically in the policy evaluation.

The complete-life view, by contrast, gives priority to those who haven't yet lived a "complete life" (roughly, haven't reached a full lifespan).

**Masny's analysis:**

- The complete-life view is *one* defensible position, not the only one
- It implies age-weighting: younger people's health improvements matter more
- For healthspan extension specifically, the implications are subtle

**For our framework:**

- Axiom 3 is a choice—we acknowledge other normative frameworks exist
- Our Amendment 8 already notes axioms are normative, not just technical
- Masny provides the philosophical literature on alternatives

### 3. Healthspan vs. Lifespan Extension

Masny distinguishes:

| Type of Intervention | Effect | Example |
|---------------------|--------|---------|
| Lifespan extension | Adds years (possibly low quality) | Cancer treatment extending survival |
| Healthspan extension | Adds quality years | Preventing frailty onset |
| Morbidity compression | Pushes decline to end of life | Healthy aging interventions |

**Application to our model:**

In our framework:
- Lifespan extension: Reduces $Q(\dagger | x, a)$
- Healthspan extension: Improves $q(x)$ or shifts population to better states
- Both affect $J(\pi) = \mathbb{E}[R^\pi]/\mathbb{E}[\tau^\pi]$

But they affect it differently:
- Pure lifespan extension (adding low-quality years) may **reduce** $J(\pi)$
- Pure healthspan extension (more quality) **increases** $J(\pi)$

This is a feature: $J(\pi)$ automatically handles the quality-quantity tradeoff.

### 4. Why Unbounded Lifespans Amplify These Questions

Masny writes primarily about conventional lifespans. But unbounded lifespans make the issues more acute:

| Question | Finite Lifespan | Unbounded Lifespan |
|----------|-----------------|-------------------|
| What is a "complete life"? | ~80 years | Undefined |
| Age-weighting | Prioritize young | Everyone is "young" relative to possible lifespan |
| Healthspan extension | Adds years at end | Fundamentally changes life structure |

**Implication:**

The complete-life view becomes *less* applicable as lifespans grow:
- If people can live indefinitely, no one has yet lived a "complete life"
- Age-weighting becomes arbitrary—prioritize the 200-year-old over the 300-year-old?

Our generationally neutral approach (Axiom 3) is more natural for unbounded horizons.

### 5. Distributive Justice and Health Equity

Masny engages with health equity:

> Who should receive scarce health resources?

Arguments considered:
1. **Utilitarian**: Maximize total health
2. **Prioritarian**: Weight benefits to worse-off
3. **Complete-life**: Priority to those with less complete lives
4. **Fair innings**: Everyone deserves roughly equal life expectancy

**Application to our framework:**

- Basic $J(\pi)$ is utilitarian (maximize average quality)
- Our §8 mentions DCEA (distributional weights)
- Could add: $J^w(\pi) = \sum_g w(g) \cdot J_g(\pi)$ for group weights

Masny's analysis informs the choice of weights $w(g)$.

### 6. Specific Connections to Core Paper Sections

| Core Paper Section | Masny Connection |
|--------------------|------------------|
| §1 (Introduction) | Motivation for why health policy needs new framework |
| §2 (Axiom 3 - Generational neutrality) | Alternative is complete-life view |
| §3 (QALY flow definition) | Masny's healthspan concept maps to our quality function |
| §6.1 (Irreversibility) | Healthspan extension may address irreversibility concern |
| §8 (Distributional concerns) | Provides philosophical grounding for equity weights |
| Appendix (Why not discounting) | Masny's justice arguments are orthogonal to discounting |

### 7. Healthspan Extension in Our Model

Masny's concept of healthspan extension could be formalized:

**Definition (informal):** Healthspan extension is an intervention that increases the expected time spent in high-quality states.

In our notation:
- Let $\mathcal{S}_{good} \subset \mathcal{S}$ be the "good health" states (high $q(x)$)
- Healthspan extension increases $\mathbb{E}[\text{time in } \mathcal{S}_{good}]$

This could be measured:
$$H(\pi) = \frac{\mathbb{E}\left[\int_0^{\tau^\pi} \mathbf{1}_{X_t \in \mathcal{S}_{good}} \, dt\right]}{\mathbb{E}[\tau^\pi]}$$

This is the fraction of life spent in good health under policy $\pi$.

**Relationship to $J(\pi)$:**

If $q(x) \approx 1$ for $x \in \mathcal{S}_{good}$ and $q(x) \approx 0$ otherwise, then $J(\pi) \approx H(\pi)$.

More generally, $J(\pi)$ is a quality-weighted generalization of Masny's healthspan concept.

### 8. Quotable Passages for Citation

> "Healthspan extension... adds good years to a person's life, which seems ethically analogous to saving someone's life."

Supports treating quality and quantity symmetrically.

> "The complete-life view has different implications for healthspan extension than for straightforward life extension."

Notes the complexity of age-weighting.

> "If an intervention merely compresses morbidity to the very end of life, the complete-life view may not give it special priority."

Distinguishes different types of health improvements.

### 9. How to Cite This Source in Core Paper

**Suggested citation point (Axiom 3 or §8):**

> Our generational neutrality axiom sets aside age-weighting debates in favor of symmetric treatment. Alternative frameworks prioritize those with less "complete" lives (Masny, 2023). For unbounded horizons, where the notion of life completeness becomes undefined, generational neutrality is more natural.

**Alternative (Introduction or Conclusion):**

> The choice between healthspan extension (more quality) and lifespan extension (more time) is central to aging policy. Masny (2023) analyzes this from a justice perspective. Our QALY flow metric integrates both, naturally valuing interventions that add high-quality time.

---

## Summary

Masny (2023) provides the **normative philosophy** grounding for health policy evaluation. Key contributions:

1. **Healthspan vs. lifespan distinction**: Different ethical implications.

2. **Complete-life view critique**: Not straightforwardly applicable to longevity interventions.

3. **Justice framework**: Distributional concerns have philosophical foundations.

4. **Age-weighting analysis**: When (if ever) to prioritize younger patients.

For our paper, Masny's analysis:
- **Justifies** our choice of generational neutrality (Axiom 3), especially for unbounded horizons
- **Informs** the interpretation of $J(\pi)$ as combining health and lifespan
- **Supports** distributional extensions (§8) with philosophical grounding

Our framework operationalizes what Masny analyzes philosophically: $J(\pi)$ gives a formal answer to "how should we value healthspan extension?" that is consistent with treating quality-weighted time as the fundamental unit.

---

## Final Note: All 10 Source Notes Complete

This completes the comprehensive source documentation for the core paper:

| # | Source | Focus |
|---|--------|-------|
| 01 | Sanders 2016 | Second Panel CEA recommendations |
| 02 | Attema 2018 | Discounting review |
| 03 | Gravelle 2007 | Discounting and decision rules |
| 04 | O'Mahony 2015 | Time in health evaluation |
| 05 | Asaria 2013 | Distributional CEA |
| 06 | Brazier 2011 | Quality measurement (TSD11) |
| 07 | Ultsch 2015 | Vaccine economics |
| 08 | Bauer 2025 | Health risk and value of life |
| 09 | Song 2023 | Value of health with stochastic risk |
| 10 | Masny 2023 | Healthspan extension and justice |

Each note provides detailed application to the core paper with specific section connections, quotable passages, and citation recommendations.
