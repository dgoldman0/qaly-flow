# Ultsch et al. (2015) — Consensus Framework for Vaccine Economic Evaluation

**Full Citation:**  
Ultsch, B., Damm, O., Beutels, P., Bilcke, J., Brüggenjürgen, B., et al. (2015). Methods for Health Economic Evaluation of Vaccines and Immunization Decision Frameworks: A Consensus Framework from a European Vaccine Economics Community. *PharmacoEconomics*. doi:10.1007/s40273-015-0335-2

**PDF:** `pdfs/ultsch2016_vaccine_econ_framework.pdf` (note: filename uses 2016; actual publication 2015)

---

## Overview

This consensus statement from a European vaccine economics community addresses immunization-specific methodological issues in health economic evaluation. Vaccination presents unique challenges that standard CEA guidance (designed for curative drugs) doesn't fully address.

### Key Topics

1. **Mathematical modeling**: Dynamic vs. static models, transmission dynamics
2. **Indirect effects**: Herd immunity, population-level protection
3. **Time horizon**: Long-term effects of vaccination programs
4. **Discounting**: Particularly contentious for prevention with delayed benefits
5. **Decision frameworks**: How HTA bodies should use vaccine economic evidence

---

## Comprehensive Application to the Core Paper

### 1. Vaccination as a "Near Neighbor" Domain

Vaccines share key features with our unbounded-lifespan setting:

| Vaccine Economics Feature | Our Framework Analog |
|---------------------------|----------------------|
| Ongoing population with entry/exit | Regenerative regime with new entrants |
| Indirect effects through population | Population-level policy objective |
| Long-term/lifetime protection | Quality benefits extending indefinitely |
| Prevention vs. treatment | Prevention/maintenance vs. repair |
| Cohort-based modeling | Initial distribution $\nu$ |

Ultsch et al.'s work shows that **steady-state thinking is already standard** in one corner of health economics—we're extending it to health policy writ large.

### 2. Dynamic Transmission Models and Population Effects

Ultsch et al. emphasize:

> "Dynamic models are needed to capture indirect effects such as herd immunity."

In dynamic models:
- The population is modeled as a continuing system
- Individuals enter (birth), transition between states, and exit (death)
- Steady-state behavior emerges

**Direct parallel to our framework:**
- Our regenerative process models a continuing system
- Individuals cycle through states until catastrophe
- New entrants replace those who exit
- $J(\pi)$ is the steady-state quality flow

The mathematical structure is similar—we're using renewal theory where vaccine economics uses compartmental models.

### 3. The Discounting Debate for Prevention

Ultsch et al. note that discounting is especially controversial for vaccines:

> "Discounting disproportionately affects prevention programs where benefits occur far in the future."

A childhood vaccine producing lifetime protection has benefits decades hence—heavy discounting makes these nearly worthless.

**Our framework's relevance:**
- We avoid discounting entirely
- $J(\pi)$ weights all person-time equally
- Prevention and maintenance are valued by their contribution to long-run average quality
- This resolves the "discounting penalizes prevention" problem

### 4. Time Horizon for Vaccination Programs

Ultsch et al. discuss modeling horizons:

> "Time horizon should be long enough to capture long-term effects... often the lifetime of vaccinated cohorts plus time for indirect effects to manifest."

For diseases eliminated by vaccination, effects extend indefinitely—the population benefits perpetually.

**Connection to our unbounded horizon:**
- Vaccine elimination produces benefits for all future person-time
- Our regenerative framework naturally handles this
- The "return on investment" is captured in the shift in steady-state $J(\pi)$

### 5. Cohort vs. Population Models

Ultsch et al. discuss two modeling approaches:

| Approach | Description | Our Framework Analog |
|----------|-------------|----------------------|
| **Cohort** | Follow a cohort over lifetime | Single cycle: initial state to $\dagger$ |
| **Population** | Model ongoing population dynamics | Regenerative regime: continuing stream |

Our framework uses the population approach via regeneration—but for an individual-level policy applied to a continuing stream of individuals.

### 6. Consensus on Methodological Standards

Ultsch et al. develop consensus on:
- Model transparency and validation
- Sensitivity analysis requirements
- Reporting standards for decision-makers

**Analogues in our framework:**
- Theorem 5.1 (Lipschitz stability) = sensitivity to parameter changes
- Assumptions 1–4 = transparency about model structure
- Explicit axioms = reporting normative choices

### 7. Herd Immunity and Indirect Effects

A central vaccine economics concern is **indirect protection**—vaccinating some protects others.

**Application to our setting:**
- In a maintenance/repair world, some interventions may have "herd" effects
- Safer environments (fewer accidents) benefit everyone
- Improved repair technology reduces system-wide risk

While our model focuses on individual-level dynamics, the regenerative structure could be extended to incorporate population externalities.

### 8. Specific Connections to Core Paper Sections

| Core Paper Section | Ultsch et al. Connection |
|--------------------|--------------------------|
| §3.1 (Regenerative Regime) | Mirrors dynamic population models |
| §3.5 (Theorem 3.1: Renewal-Reward) | Analogous to steady-state in transmission models |
| §5 (Sensitivity Analysis) | Their consensus on sensitivity requirements |
| Axiom 2 (Horizon Invariance) | Aligns with their long-horizon perspective |
| Large-population interpretation | Directly parallels their population-level models |

### 9. Quotable Passages for Citation

> "Dynamic models are required to capture herd immunity and the impact of vaccination on disease transmission."

Supports the need for population-level thinking—which our regenerative framework provides.

> "Discounting can significantly reduce the apparent value of prevention programs."

Motivates our non-discounting approach.

> "The time horizon should be long enough to capture all relevant costs and health effects."

Sets up the question we answer: what if "long enough" is unbounded?

### 10. How to Cite This Source in Core Paper

**Suggested citation point (§3.1 or Introduction):**

> Vaccine economics has long recognized the need for dynamic, population-level models with long horizons (Ultsch et al., 2015). Our regenerative framework extends this approach: where vaccination models track disease transmission in a continuing population, we track health quality in a population with ongoing maintenance and repair.

**Alternative (§3.5 on renewal-reward):**

> The steady-state perspective in our framework is analogous to endemic equilibrium in dynamic transmission models (Ultsch et al., 2015). The QALY flow $J(\pi)$ corresponds to the long-run average health burden per capita.

---

## Summary

Ultsch et al. (2015) provides precedent for the core features of our framework:

1. **Population-level, long-horizon thinking**: Standard in vaccine economics
2. **Steady-state analysis**: Dynamic models naturally produce steady states
3. **Discounting concerns**: Prevention is undervalued by discounting—motivates alternatives
4. **Consensus methods**: Standards for sensitivity analysis and transparency

The paper shows that our steady-state, regenerative approach isn't radical—it's a natural extension of methods already accepted in immunization economics. We're generalizing vaccine-economics thinking to all health policy in an unbounded-lifespan world.
