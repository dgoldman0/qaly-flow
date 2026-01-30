# Attema, Brouwer & Claxton (2018) — Discounting in Economic Evaluations

**Full Citation:**  
Attema, A. E., Brouwer, W. B. F., & Claxton, K. (2018). Discounting in Economic Evaluations. *PharmacoEconomics*. doi:10.1007/s40273-018-0672-z

**PDF:** `pdfs/attema2018_discounting.pdf`

---

## Overview

This is a comprehensive review of discounting theory and practice in health economic evaluations. It synthesizes the major controversies, decision-theoretic foundations, and international guideline recommendations for discounting costs and health effects.

### Key Topics Covered

1. **Why Discount?**
   - Pure time preference (impatience)
   - Diminishing marginal utility of consumption (growth discounting)
   - Uncertainty about future benefits
   - Opportunity cost of capital

2. **Equal vs. Differential Discounting**
   - Arguments for discounting costs and health at the same rate
   - Arguments for differential rates (health may appreciate relative to consumption)
   - The "Keeler-Cretin paradox" and timing of interventions

3. **Constant vs. Declining Discount Rates**
   - Hyperbolic discounting
   - Time inconsistency concerns
   - Long-term projects and intergenerational equity

4. **Double Discounting Problem**
   - When quality-of-life values already embed discounting
   - Risk of undervaluing future health gains

5. **Survey of National Guidelines**
   - Variation across countries (1.5% to 5%, equal vs. differential)
   - NICE, CADTH, PBAC, and other HTA bodies

---

## Comprehensive Application to the Core Paper

### 1. The Central Problem We're Addressing

Attema et al. identify the core technical role of discounting:

> "Discounting can be quite influential on the outcomes of economic evaluations."

Our paper asks: **What if discounting isn't just influential but structurally necessary to avoid divergence?**

When lifespans are unbounded:
- Without discounting: $\mathbb{E}[\text{QALYs}] = \infty$
- With any positive discount rate: $\mathbb{E}[\text{discounted QALYs}] < \infty$

Attema et al. treat discounting as a valuation choice. We show it can become a **structural requirement** for well-posed policy evaluation—which is problematic because it conflates:
- Normative time preference (how much we *should* discount)
- Technical necessity (discounting to ensure finite comparisons)

### 2. Discounting as a Hidden Axiom

Attema et al. note:

> "Most national pharmaceutical guidelines prescribe equal discounting of costs and effects without proper justification, or on the basis of theoretical arguments that do not necessarily bear practical relevance."

This supports our Axiom 5 (Explicit Normativity): discounting rates are often hidden assumptions rather than transparent ethical choices.

**Our approach:** Instead of choosing a discount rate, we adopt a framework (regenerative steady-state) where discounting is **unnecessary** for well-posedness. Time preference can then be added explicitly if desired, rather than being forced by technical considerations.

### 3. Mapping Discounting Justifications to Our Framework

| Discounting Rationale (Attema et al.) | How Our Framework Handles It |
|---------------------------------------|------------------------------|
| **Pure time preference** | Not embedded in $J(\pi)$; can add as explicit weight if desired |
| **Growth discounting** (rising consumption → lower marginal utility) | Not applicable to steady-state; framework assumes stationarity |
| **Uncertainty about future** | Captured by catastrophe rate $Q(\dagger | x, a)$; explicit hazard modeling |
| **Opportunity cost of capital** | Enters via cost flow $K(\pi)$, not via discounting |

### 4. The Differential Discounting Debate

A major controversy is whether health should be discounted at a different rate than costs. Attema et al. discuss:

- **Gravelle et al.'s argument**: If the consumption value of health rises over time, health gains should be discounted at a lower rate.
- **Counter-arguments**: Different rates create time-inconsistency and comparability problems.

**Our framework's contribution:** By moving to per-unit-time flows, we sidestep this debate:
- $J(\pi)$ is quality per unit time (dimensionally: QALY/year)
- $K(\pi)$ is cost per unit time (dimensionally: $/year)
- The ratio $K(\pi)/J(\pi)$ has natural interpretation without discounting

Changes in the consumption value of health would affect the quality function $q(x)$ or the willingness-to-pay parameter $\lambda$, not the structure of the objective.

### 5. Declining Discount Rates and Long Horizons

Attema et al. discuss declining discount rates for long-term projects:

> "Declining discount rates could be applied to avoid giving negligible weight to the far future while also respecting near-term impatience."

For unbounded horizons, even declining rates (if bounded away from zero) eventually give near-zero weight to effects sufficiently far in the future. Our regenerative framework avoids this by:
- Treating all "cycle time" symmetrically
- The long-run average $J(\pi)$ weights all person-time equally within the continuing regime

### 6. Specific Connections to Core Paper Sections

| Core Paper Section | Attema et al. Connection |
|--------------------|--------------------------|
| §1.1 (Setting) | Motivates why discounting becomes load-bearing when horizons are long |
| Axiom 2 (Horizon Invariance) | Our alternative to discounting for achieving finite comparisons |
| Axiom 5 (Explicit Normativity) | Directly supported—discounting is often implicit |
| §3.3 (Definition of $J(\pi)$) | Our ratio form sidesteps the discounting requirement |
| §3.4 (Truncated Flow) | Handles $\mathbb{E}[\tau^\pi] = \infty$ cases without discounting |
| §5 (Sensitivity/Stability) | Analogous to discounting sensitivity analyses but for structural parameters |

### 7. Quotable Passages for Citation

> "Discount rates depend heavily on developments in opportunity costs of healthcare spending (marginal productivity of spending) and in the consumption value of health, but these measures lack empirical estimations."

This supports our argument that discounting parameters are empirically uncertain—better to avoid structural dependence on them.

> "Care should be taken to avoid the practice of double discounting, which can cause severe misallocations of healthcare resources."

We avoid double discounting entirely by not discounting at all in the base framework.

### 8. How to Cite This Source in Core Paper

**Suggested citation point (Introduction or §3):**

> Standard practice discounts future health effects at rates ranging from 1.5% to 5% across national guidelines (Attema et al., 2018). When lifespans are bounded, this is primarily a normative choice about time preference. When lifespans are unbounded, however, discounting becomes structurally necessary to ensure finite comparisons—conflating ethical commitments with technical requirements. We propose an alternative that avoids this conflation.

---

## Summary

Attema et al. (2018) provides the authoritative review of discounting in health economics. For our paper, it serves two purposes:

1. **Establishing the problem**: It documents that discounting is controversial, poorly justified empirically, and varies widely across jurisdictions.

2. **Motivating our solution**: By showing that discounting is treated as a valuation choice, it highlights the awkwardness of making it a structural necessity—which is exactly what happens when lifespans are unbounded.

Our regenerative framework offers an alternative where time preference is genuinely optional, not hidden in a rate needed to prevent divergence.
