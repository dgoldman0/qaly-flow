# Gravelle et al. (2007) — Discounting and Optimal Decision Rules

**Full Citation:**  
Gravelle, H., Brouwer, W., Niessen, L., Postma, M., & Rutten, F. (2007). Discounting in Economic Evaluations: Stepping Forward Towards Optimal Decision Rules. *Health Economics*, 16(3), 307–317. doi:10.1002/hec.1168

**PDF:** `pdfs/gravelle2006_discounting_health.pdf` (note: filename uses online publication year 2006; print year 2007)

---

## Overview

This paper provides a formal decision-theoretic analysis of discounting rules in health economic evaluation. The authors argue that NICE's (and other agencies') recommendation for equal discounting of costs and health effects leads to sub-optimal decisions because it fails to account for the changing value of health over time.

### Key Arguments

1. **The consumption value of health changes over time**: As economies grow and consumption rises, the marginal utility of consumption falls relative to health. This implies health gains become relatively more valuable over time.

2. **Optimal decision rules require differential discounting**: To make optimal resource allocation decisions, health effects should be discounted at a rate reflecting the change in their consumption value, not the same rate as costs.

3. **The "equivalence" argument is misleading**: The common justification for equal discounting (that any discrepancy could be arbitraged via postponement) assumes no binding budget constraints and ignores second-best considerations.

4. **Budget constraints matter**: When health budgets are constrained, the shadow price of the constraint affects optimal decisions. This should be incorporated into the evaluation, not assumed away.

---

## Comprehensive Application to the Core Paper

### 1. Decision-Theoretic Foundations We Build On

Gravelle et al. provide the formal framework for understanding discounting as a component of *optimal decision rules*, not just a valuation convention. Key concepts:

| Concept | Their Treatment | Our Extension |
|---------|-----------------|---------------|
| **Objective function** | Discounted welfare over finite horizon | Average welfare per unit time (no discounting) |
| **Time preference** | Embedded in discount rate | Explicit parameter $\lambda$ (if desired) |
| **Horizon** | Finite but long | Infinite (unbounded lifespan) |
| **Budget constraint** | Fixed health budget | Enters via cost flow $K(\pi)$ |

### 2. The "Changing Value of Health" Argument

Gravelle et al.'s central point:

> "NICE (and other regulatory bodies) should either use differential discounting or stipulate how the changing value of health should otherwise be dealt with."

In a growing economy, the consumption-equivalent value of a QALY rises over time. Their solution: discount health at a lower rate than costs.

**Our framework's response:** In a steady-state regime with unbounded lifespans:
- We assume stationarity (no secular growth)
- The quality function $q(x)$ gives instantaneous quality-of-life
- The willingness-to-pay parameter $\lambda$ in $W_\lambda(\pi) = J(\pi) - \lambda K(\pi)$ can reflect current consumption-value-of-health
- If the consumption value of health changes, $\lambda$ can be updated

This separates:
- The structure of the objective (which doesn't require discounting)
- The parameterization (which can reflect changing valuations)

### 3. Axioms and Consistency Properties

Gravelle et al. discuss axioms underlying optimal decision rules:

1. **Time consistency**: Decisions made today should remain optimal when re-evaluated later
2. **Separability**: Evaluation of future outcomes shouldn't depend on past outcomes
3. **Stationarity**: The decision rule shouldn't depend on the calendar date

**Connections to our axioms:**

| Gravelle et al. Property | Our Axiom |
|--------------------------|-----------|
| Time consistency | Implied by stationary Markov policies and regenerative structure |
| Separability | Built into cycle-by-cycle accounting |
| Stationarity | Axiom 2 (Horizon Invariance) + regeneration assumption |

Our regenerative framework satisfies all three properties by construction:
- The ratio $J(\pi)$ is stationary and time-consistent
- Independent cycles ensure separability
- No dependence on calendar time

### 4. The Shadow Price of Budget Constraints

Gravelle et al. emphasize that budget constraints create shadow prices affecting optimal decisions:

> "Binding health service budget constraints should be incorporated in evaluations."

**Our model's treatment:** The cost flow $K(\pi)$ represents the ongoing resource cost. A budget-constrained planner maximizes $J(\pi)$ subject to $K(\pi) \leq \bar{K}$, or equivalently maximizes $J(\pi) - \lambda K(\pi)$ where $\lambda$ is the shadow price of the budget.

This is precisely analogous to their analysis—but in flow terms rather than discounted sums.

### 5. Why Equal Discounting Is Problematic

Gravelle et al. critique the "postponement" argument for equal discounting:

> "The guideline leads to sub-optimal decisions because it fails to account for the changing value of health."

Our framework makes a stronger point: when lifespans are unbounded, the choice of discounting rate isn't just about optimality—it's about **well-posedness**. Equal discounting at any positive rate will work technically, but:
- High rates underweight the far future
- Low rates may not converge fast enough if lifespans are very long
- Zero rates cause divergence

By avoiding discounting entirely (using the regenerative ratio), we sidestep these structural trade-offs.

### 6. Specific Connections to Core Paper Sections

| Core Paper Section | Gravelle et al. Connection |
|--------------------|---------------------------|
| §1.2 (Axioms) | Our axioms embed time consistency, separability, stationarity |
| §3.3 (Definition of $J(\pi)$) | Ratio form avoids their differential discounting problem |
| §4 (Optimization) | $W_\lambda(\pi) = J(\pi) - \lambda K(\pi)$ mirrors their budget-constrained objective |
| §5 (Stability) | Our Lipschitz stability plays the role of their sensitivity to discount rates |
| §7 (Flow ICER) | Direct extension of their cost-effectiveness framework to steady-state |

### 7. Quotable Passages for Citation

> "The guideline leads to sub-optimal decisions because it fails to account for the changing value of health."

Supports our claim that discounting conventions embed hidden assumptions.

> "Binding health service budget constraints should be incorporated in evaluations."

Directly supports our treatment of cost flow and budget-constrained optimization.

### 8. How to Cite This Source in Core Paper

**Suggested citation point (§4 on optimization or §7 on ICER):**

> Under budget constraints, the shadow price of resources affects optimal health policy (Gravelle et al., 2007). Our cost flow $K(\pi)$ and the willingness-to-pay parameter $\lambda$ play precisely this role, extending the analysis to unbounded horizons without requiring discounting.

**Alternative (Introduction):**

> The formal analysis of discounting in health economics reveals that decision rules depend on the changing consumption value of health (Gravelle et al., 2007). When horizons are unbounded, the choice of discount rate becomes not just an optimality concern but a well-posedness requirement—motivating our alternative framework.

---

## Summary

Gravelle et al. (2007) provides the decision-theoretic foundations that our paper extends. Their key insights:

1. **Discounting is part of optimal decision rules**, not just valuation convention
2. **The changing value of health** should be reflected in evaluation methods
3. **Budget constraints** create shadow prices that matter

Our contribution is showing that when horizons are unbounded, the regenerative steady-state framework achieves the same goals (optimal decisions under budget constraints, time-consistent evaluation) without requiring discounting—making time preference genuinely optional.
