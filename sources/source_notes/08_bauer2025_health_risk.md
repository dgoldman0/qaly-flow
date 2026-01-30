# Bauer, Lakdawalla & Reif (2025) — Health Risk and the Value of Life

**Full Citation:**  
Bauer, D., Lakdawalla, D., & Reif, J. (2025). Health Risk and the Value of Life. Working paper.

**PDF:** `pdfs/bauer_lakdawalla_reif_2025_health_risk_value_of_life.pdf`

---

## Overview

This paper extends the conventional life-cycle framework for valuing health and longevity improvements to a **stochastic multi-state health setting**. Unlike standard models that assume a single health state with age-dependent mortality, this framework allows:

- Multiple health states with different mortality rates and quality of life
- Transitions between states (illness onset, recovery)
- State-dependent valuations of mortality and morbidity risk reductions

### Key Findings

1. **Sick adults value QALYs more highly**: Willingness to pay per QALY is nearly twice as high for sick individuals as for healthy individuals.

2. **Illness risk matters as much as severity**: Reducing the risk of serious illness is valued similarly to reducing the risk of mild illness.

3. **Explains behavioral "puzzles"**: Provides rational explanations for:
   - Opposition to a single QALY threshold for rationing
   - Lower investment in prevention vs. treatment

---

## Comprehensive Application to the Core Paper

### 1. Multi-State Health Dynamics: Exact Match

Bauer et al.'s model structure is remarkably close to ours:

| Their Element | Our Element |
|---------------|-------------|
| Multiple health states | State space $\mathcal{S}$ |
| Death (absorbing) | $\dagger$ (catastrophic failure) |
| State-dependent mortality | Rate kernel $Q(\dagger | x, a)$ |
| State-dependent quality | Quality function $q(x)$ |
| Transitions between states | $Q(y | x, a)$ for $y \in \mathcal{S}$ |
| Life-cycle consumption | Cost flow $c(x, a)$ |

Their premise—"accidents/disease still happen; parts break; repairs exist"—is exactly our maintenance/repair world.

### 2. State-Dependent Value of Life

**Their key insight:** The value of a statistical life-year (or QALY) varies with health state.

$$\text{WTP per QALY} \approx 2 \times \text{higher for sick vs. healthy}$$

**Implications for our framework:**

1. **Single $\lambda$ may be inadequate**: Our objective $W_\lambda(\pi) = J(\pi) - \lambda K(\pi)$ uses a single willingness-to-pay parameter. Bauer et al. suggest this should be state-dependent: $\lambda(x)$.

2. **Quality function isn't enough**: Even if we correctly measure $q(x)$, the *value* of a QALY in state $x$ may vary—sick people may value marginal quality gains more.

3. **Distributional implications**: If sick and healthy value health differently, equal weighting in $J(\pi)$ may not reflect revealed preferences.

### 3. Prevention vs. Treatment

Bauer et al. explain the "prevention puzzle":

> "Our results provide a rational explanation for why... [people] invest less in prevention than in treatment."

**Connection to our irreversibility framework (§6.1):**

- Prevention reduces transitions into harmful states ($\mathcal{I}$ or $\dagger$)
- Treatment/repair occurs after transitions happen
- If people value avoiding states they're currently in more highly, treatment is locally more valuable than prevention

**Framework extension:** Our disutility function $\kappa(x)$ for irreversible states could be calibrated using Bauer et al.'s state-dependent valuation approach.

### 4. The QALY Threshold Debate

Bauer et al.:

> "Our results provide a rational explanation for why people oppose a single threshold value for rationing care."

If WTP/QALY varies by health state, a fixed cost-effectiveness threshold (e.g., $50,000/QALY) is:
- Too low for sick individuals (who value QALYs more)
- Too high for healthy individuals

**Application to our framework:**
- Flow ICER = $(K(\pi_2) - K(\pi_1)) / (J(\pi_2) - J(\pi_1))$
- Should the threshold vary by the health state distribution of affected populations?
- Bauer et al. provide empirical estimates for this calibration

### 5. Life-Cycle Model with Stochastic Health

Their formal model includes:
- Continuous-time Markov process for health states
- Age-dependent transition rates
- Optimal consumption and savings decisions
- Mortality as one possible transition

**Technical parallels:**

| Their Model | Our Model |
|-------------|-----------|
| Controlled stochastic process | Controlled CTMC on $\mathcal{X}$ |
| Lifetime utility | Cycle reward $R^\pi$ |
| Discount rate | None (ratio eliminates need) |
| Value function | Related to $J(\pi)$ via regeneration |

Their model is richer (includes consumption-savings) but shares the core structure. Our regenerative approach could be viewed as the population-level analog of their individual life-cycle model.

### 6. Calibration and Empirical Implementation

Bauer et al. calibrate using:
- Health and Retirement Study (HRS) data
- Mortality rates by comorbidity
- Quality of life by health state
- Medical spending by state

**For our framework:** This provides a template for calibrating:
- State space $\mathcal{S}$ (comorbidity combinations)
- Transition rates $Q(y | x, a)$ from longitudinal data
- Quality function $q(x)$ from survey instruments
- Cost function $c(x, a)$ from spending data

### 7. The "Repair" Interpretation

Bauer et al. model transitions both toward and away from worse health states:
- Onset of conditions (breakdown)
- Recovery or stabilization (repair)
- Death (catastrophic failure)

This is precisely our maintenance world:
- Repairable states $\mathcal{R}$: Can transition back to better states
- Irreversible states $\mathcal{I}$: No recovery possible
- Catastrophic failure $\dagger$: Absorbing

### 8. Specific Connections to Core Paper Sections

| Core Paper Section | Bauer et al. Connection |
|--------------------|------------------------|
| §2 (Controlled health process) | Their multi-state Markov model is the micro-foundation |
| §2.1 (State space, quality) | Their health states and quality mapping |
| §2.3 (Dynamics) | Their transition rate specification |
| §4 (Optimization) | Their life-cycle optimization; we aggregate to population |
| §6.1 (Irreversibility) | Their state-dependent valuations inform $\kappa(x)$ |
| §7 (Flow ICER) | Their WTP heterogeneity suggests state-dependent thresholds |

### 9. Quotable Passages for Citation

> "We find that sick adults are willing to pay nearly twice as much per quality-adjusted life-year (QALY) to reduce mortality risk as healthy adults."

Motivates state-dependent valuation in our framework.

> "Reducing the risk of serious illness is valued similarly to reducing the risk of mild illness."

Supports our emphasis on irreversibility and state classification.

> "The conventional life-cycle framework... includes only a single health state, with a preordained mortality rate that depends on age alone."

Identifies the limitation we also address—single-state models are inadequate.

### 10. How to Cite This Source in Core Paper

**Suggested citation point (§2 on dynamics):**

> Our multi-state health process follows recent extensions to life-cycle valuation (Bauer et al., 2025). Health states $x \in \mathcal{S}$ have state-dependent mortality rates $Q(\dagger | x, a)$ and quality $q(x)$, allowing the model to capture comorbidities, illness onset, and recovery.

**Alternative (§7 on ICER):**

> Empirical work shows that willingness-to-pay per QALY varies substantially by health state (Bauer et al., 2025). This suggests that the cost-effectiveness threshold $\lambda$ in our objective $W_\lambda(\pi) = J(\pi) - \lambda K(\pi)$ may need to account for the health state distribution of affected populations.

---

## Summary

Bauer et al. (2025) provides the **microeconomic foundation** for our framework. Key contributions:

1. **Multi-state health dynamics**: Their model structure is nearly identical to ours—multiple states, stochastic transitions, absorbing death.

2. **State-dependent valuations**: WTP/QALY varies with health state—a richer picture than our uniform $\lambda$.

3. **Prevention vs. treatment**: Their results inform our irreversibility analysis.

4. **Calibration template**: Their empirical approach shows how to operationalize the model.

Our paper extends their individual life-cycle model to the population level via regeneration, asking: what is the steady-state policy objective when individual trajectories like theirs are repeatedly sampled from a continuing population?
