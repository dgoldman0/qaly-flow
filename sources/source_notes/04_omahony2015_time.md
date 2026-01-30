# O'Mahony, Newall & van Rosmalen (2015) — Dealing with Time in Health Economic Evaluation

**Full Citation:**  
O'Mahony, J. F., Newall, A. T., & van Rosmalen, J. (2015). Dealing with Time in Health Economic Evaluation: Methodological Issues and Recommendations for Practice. *PharmacoEconomics*. doi:10.1007/s40273-015-0309-4

**PDF:** `pdfs/omahony2015_dealing_with_time.pdf`

---

## Overview

This is a practical methodological guide addressing how "time" enters health economic models. It covers three major aspects:

1. **Which cohorts to simulate and how far into the future**
2. **The simulation of time** (discrete vs. continuous, cycle lengths, rate-probability conversions)
3. **Discounting future costs and effects**

The paper bridges theoretical considerations with practical modeling guidance.

### Key Methodological Points

- **Cohort selection**: Analysts should assess variation in cost-effectiveness across cohorts and feasibility of subgroup recommendations
- **Time horizon**: Should be long enough to capture all important cost/outcome differences
- **Continuous vs. discrete time**: Short cycles or continuous-time models avoid biases
- **Half-cycle corrections**: Needed for discrete-time models with long cycles
- **Discounting**: Standard 3-5% rates, with sensitivity analyses

---

## Comprehensive Application to the Core Paper

### 1. The "How Far Into the Future" Question

O'Mahony et al. address the standard practice:

> "The analysis should extend far enough into the future to capture all the important differences in costs or outcomes between the intervention and its comparators."

For interventions affecting mortality, this typically means:

> "Simulate until nearly everyone is dead"

**The core problem for our paper:** When there is no fixed biological maximum lifespan, "until nearly everyone is dead" becomes undefined. If the catastrophe rate is low enough, the expected time to death is infinite.

**Our solution:** Replace "lifetime horizon" with "regenerative steady-state"—the policy objective becomes quality per unit person-time rather than total lifetime quality.

### 2. Continuous Time vs. Discrete Time

O'Mahony et al. strongly advocate for continuous-time or short-cycle models:

> "We recommend using short cycles or continuous-time models to avoid biases and the need for half-cycle corrections."

**Direct connection to our framework:**

Our model is explicitly continuous-time:
- Health dynamics $(X_t)_{t \geq 0}$ on state space $\mathcal{X}$
- Transition rates $Q(\cdot | x, a)$
- Cycle reward $R^\pi = \int_0^\tau q(X_t) dt$ is a continuous integral

This avoids:
- Cycle-length artifacts
- Half-cycle correction debates
- Rate-to-probability conversion errors

### 3. Rate-Probability Conversions

O'Mahony et al. discuss the relationship between transition rates and probabilities:

$$P = 1 - e^{-rt}$$

where $r$ is the rate and $t$ is the cycle length. Errors arise when:
- Rates are incorrectly treated as probabilities
- Cycle lengths are too long for the embedded approximation

**Our framework:** By working directly with rate kernels $Q(\cdot | x, a)$, we avoid this issue entirely. The controlled continuous-time Markov chain formulation is native—no conversions needed.

### 4. Cohort Heterogeneity and Subgroups

O'Mahony et al. recommend:

> "Analysts should carefully assess potential reasons for variation in cost-effectiveness between cohorts and the feasibility of subgroup-specific recommendations."

**Connection to our distributional analysis (§8):**

Our framework naturally extends to heterogeneous groups:
- Different groups $i$ have different QALY flows $J_i(\pi)$
- Social welfare can weight groups: $SW(\pi) = \sum_i w_i J_i(\pi)$
- Inequality aversion can be incorporated: $SW(\pi) = \sum_i u(J_i(\pi))$ with concave $u$

The regenerative interpretation also varies by group—different initial distributions $\nu_i$, different transition dynamics.

### 5. Time Horizon Selection in Practice

O'Mahony et al. discuss practical considerations:

| Consideration | Their Recommendation | Our Framework's Treatment |
|---------------|---------------------|---------------------------|
| Duration of intervention effects | Model as long as effects persist | Captured in cycle dynamics |
| Age of cohort at baseline | May limit remaining life-years | Initial distribution $\nu$ |
| Computational tractability | May truncate if effects are negligible | Regenerative structure gives finite $J(\pi)$ without truncation |
| Discounting attenuates far-future effects | Less precision needed for distant outcomes | No discounting—all person-time weighted equally |

### 6. The Bridge to Infinite Horizons

O'Mahony et al. focus on finite-horizon models but their logic points toward our extension:

> "The time horizon of an economic evaluation is the period over which costs and effects are compared."

When lifespans are bounded, this period is finite. When unbounded, we need either:
1. Infinite discounting (technically works but ethically fraught)
2. Truncation with explicit justification (arbitrary)
3. **A new framework** (our regenerative steady-state)

The paper's careful treatment of time considerations makes clear that "time" in economic evaluation is a design choice with consequences—exactly what motivates our rethinking.

### 7. Specific Connections to Core Paper Sections

| Core Paper Section | O'Mahony et al. Connection |
|--------------------|---------------------------|
| §2.3 (Dynamics) | Our continuous-time CTMC follows their recommendation for continuous simulation |
| §3.1 (Regenerative Regime) | Extends their "cohort simulation" to regenerative steady-state |
| §3.3 (Definition of $J(\pi)$) | Answers their "how far into the future" question for unbounded lifespans |
| §3.4 (Truncated Flow) | Our truncation approach for $\mathbb{E}[\tau^\pi] = \infty$ cases |
| §8 (Distributional Aggregation) | Extends their cohort heterogeneity to explicit distributional objectives |

### 8. Quotable Passages for Citation

> "For choosing which cohorts to simulate and how many, we suggest analysts carefully assess potential reasons for variation in cost-effectiveness between cohorts."

Supports our distributional analysis.

> "We recommend using short cycles or continuous-time models to avoid biases and the need for half-cycle corrections."

Directly supports our continuous-time formulation.

> "The time horizon of an economic evaluation is the period over which costs and effects are compared... extending far enough into the future to capture all important differences."

Sets up the problem: what happens when "far enough" is infinite?

### 9. How to Cite This Source in Core Paper

**Suggested citation point (§2.3 on dynamics):**

> We adopt a continuous-time formulation, following recommendations for avoiding cycle-length artifacts (O'Mahony et al., 2015). The controlled continuous-time Markov chain on $\mathcal{X}$ with rate kernel $Q(\cdot | x, a)$ directly models transition hazards without rate-probability conversions.

**Alternative (Introduction or §3):**

> Standard practice extends models "far enough into the future to capture all important differences" (O'Mahony et al., 2015). When lifespans are unbounded, this guidance becomes problematic—motivating our shift from lifetime-horizon to steady-state evaluation.

---

## Summary

O'Mahony et al. (2015) provides the methodological bridge between theoretical discounting debates and practical modeling. For our paper, it:

1. **Validates our continuous-time approach**: Their strong recommendation for continuous-time or short-cycle models aligns perfectly with our CTMC formulation.

2. **Identifies the horizon problem**: Their guidance to "extend far enough" exposes the gap we fill—what to do when "far enough" is infinite.

3. **Supports distributional analysis**: Their cohort heterogeneity discussion provides precedent for our group-specific QALY flows.

The paper represents current best practice, making clear that our framework is a principled extension rather than a departure from established methodology.
