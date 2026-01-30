# Song, Bauer, Lakdawalla & Reif (2023) — Value of Health and Longevity with Partial Annuitization

**Full Citation:**  
Song, U., Bauer, D., Lakdawalla, D., & Reif, J. (2023). The Value of Health and Longevity with Stochastic Health Risk and Partial Annuitization. Preliminary draft.

**PDF:** `pdfs/song_bauer_lakdawalla_reif_2023_value_health_longevity.pdf`

---

## Overview

This paper develops a calibrated life-cycle model for retirees that combines:
- **Stochastic health risk** (multiple health states with transitions)
- **Partial annuitization** (limited access to annuity products)
- **Optimal consumption** (spending down wealth over retirement)

The authors find that standard estimates of the value of health/longevity improvements (which assume complete annuitization) overstate the true value by 40% or more.

### Key Findings

1. **Consumption adjustment mitigates health shocks**: People can partially offset health declines by adjusting spending.

2. **Incomplete annuitization reduces value of mortality reductions at old ages**: Without full annuities, people spend down wealth; very-old-age mortality improvements matter less.

3. **Complementarity of annuity income and health investments**: Social security and health/longevity investments are complements.

---

## Comprehensive Application to the Core Paper

### 1. The Institutional Layer We Abstract From

Song et al. model the institutional context (retirement products, savings, annuities) that our framework deliberately abstracts from. This is a feature, not a bug:

| Their Focus | Our Abstraction |
|-------------|-----------------|
| Individual consumption-savings optimization | Aggregated into cost flow $c(x, a)$ |
| Annuity market structure | Assumed institutional background |
| Wealth dynamics | Not modeled—we take policy as given |
| Retirement products | Could be included in state space if needed |

Our framework is **policy-focused**: what is the right objective for health policy? Their framework is **individual-focused**: how do people value health improvements given financial constraints?

### 2. The "Unbounded Lifespan + Financial Structure" Problem

Song et al. highlight:

> "Lower annuity holdings decrease the value of mortality reductions at very old ages, as consumers tend to spend down much of their non-annuitized wealth before then."

**Implication for unbounded lifespans:**

If lifespans become arbitrarily long, financial planning becomes radically different:
- Standard annuity products assume bounded lifespans
- "Spend down" strategies fail when there's no expected endpoint
- The value of mortality reductions depends on financial structure

**Our framework's approach:** By moving to population-level policy evaluation ($J(\pi)$), we sidestep individual financial planning. The question becomes: what steady-state quality should society aim for? Individual financing is a separate (important) question.

### 3. Stochastic Health Trajectories

Like Bauer et al. (2025), Song et al. use the **Future Elderly Model** for calibration:

- Health states based on comorbidities
- Transition rates from longitudinal data
- Mortality rates by health state

**Direct application to our framework:**

Their empirically calibrated transition rates could populate our $Q(y | x, a)$:

| Future Elderly Model | Our Framework |
|---------------------|---------------|
| Health states (comorbidity combinations) | $\mathcal{S}$ |
| Mortality by state | $Q(\dagger | x, a)$ |
| State transitions | $Q(y | x, a)$ |
| Quality of life by state | $q(x)$ |

### 4. Consumption Smoothing and State-Dependent Valuation

Song et al. find:

> "The ability to adjust consumption mitigates the adverse consequences of a health shock to a certain extent."

People can partially substitute consumption for health—spend more on comfort when sick.

**Implications for our quality function:**

- $q(x)$ measures quality of life in state $x$
- But achieved quality depends on resources available
- For policy purposes, $q(x)$ might represent quality *at optimal consumption* or *at some reference consumption*

This is a calibration consideration: what does "quality in state $x$" mean when consumption is endogenous?

### 5. The Underestimation of Conventional Methods

Song et al.'s central finding:

> "Our estimates for the value of improvements associated with a reduction in cancer for the retired population are at least 40% lower than estimates based on the prevailing method."

The prevailing method assumes:
- Deterministic health (single trajectory)
- Complete annuitization (no financial risk)

Neither holds in reality.

**Application to our framework:**

Our model is closer to Song et al. than to the "prevailing method":
- Stochastic health trajectories: ✓
- Multiple health states: ✓
- Complete annuitization: Not assumed (we aggregate to policy level)

So our valuations would be closer to theirs than to naive estimates.

### 6. Social Security and Health Investment Complementarity

Song et al. find:

> "We also document the complementarity of annuity income, e.g. from social security, and investments in health and longevity."

More secure retirement income → higher value of health improvements.

**Policy implication for our framework:**

When evaluating health policies, the institutional context matters:
- Populations with strong social insurance value health improvements more
- Unbounded lifespans require rethinking retirement systems

This supports our claim that unbounded-lifespan health policy is fundamentally different—it's not just longer horizons but restructured institutions.

### 7. The Value of Reducing Specific Risks

Song et al. estimate values for:
- Reducing cancer risk
- Reducing mortality conditional on health state
- Improving health transitions

**For our framework:**

These estimates could inform:
- The relative value of prevention (reducing $Q(\mathcal{I} | x, a)$)
- vs. treatment (improving $Q(\mathcal{R} | x, a)$ once in poor health)
- vs. mortality reduction ($Q(\dagger | x, a)$)

### 8. Specific Connections to Core Paper Sections

| Core Paper Section | Song et al. Connection |
|--------------------|------------------------|
| §2 (Controlled health process) | Their stochastic health model is the individual-level foundation |
| §3.1 (Regeneration) | Our population-level aggregation vs. their individual focus |
| §6.1 (Irreversibility) | Their cancer risk analysis informs irreversibility valuation |
| §7 (Cost-effectiveness) | Their estimates suggest conventional values may be biased |
| §8 (Distributional) | Complementarity with social security is distributional concern |

### 9. Quotable Passages for Citation

> "Our estimates... are at least 40% lower than estimates based on the prevailing method from the literature."

Supports careful calibration of health valuations.

> "We also document the complementarity of annuity income, e.g. from social security, and investments in health and longevity."

Links health policy to institutional design.

> "Consumers optimally annuitize only a fraction of their wealth and adjust their consumption choices to their health trajectory."

Illustrates the financial complexity our framework abstracts from.

### 10. How to Cite This Source in Core Paper

**Suggested citation point (Introduction or Conclusion):**

> Our framework abstracts from individual financial planning, focusing on population-level policy objectives. Individual valuations depend on financial structure (Song et al., 2023); our regenerative approach takes the policy perspective, asking what steady-state health quality society should target.

**Alternative (§8 on distributional concerns):**

> The value of health improvements depends on access to insurance and retirement products (Song et al., 2023). Distributional analysis of QALY flows should account for this heterogeneity—populations with less financial security may value health differently.

---

## Summary

Song et al. (2023) provides the **financial economics perspective** on health valuation. Key contributions:

1. **Realistic financial structure**: Incomplete annuitization changes valuations substantially.

2. **Stochastic health calibration**: Uses Future Elderly Model—applicable to our framework.

3. **Institutional complementarity**: Health policy and retirement policy interact.

4. **Quantitative corrections**: Conventional estimates may overstate values by 40%+.

For our paper, this is a reminder that the **policy objective** (what we define) and the **individual valuation** (how people actually value health) are distinct. We focus on the former; they focus on the latter. Both are needed for complete policy analysis.

Our regenerative framework could be seen as the policy-maker's question: given that individuals value health in the complex ways Song et al. describe, what should society optimize for in a continuing population?
