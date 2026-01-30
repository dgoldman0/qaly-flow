# Brazier & Rowen (2011) — NICE DSU TSD 11: Alternatives to EQ-5D

**Full Citation:**  
Brazier, J., & Rowen, D. (2011). NICE DSU Technical Support Document 11: Alternatives to EQ-5D for Generating Health State Utility Values. Decision Support Unit, School of Health and Related Research (ScHARR), University of Sheffield.

**PDF:** `pdfs/nice_dsu_tsd11.pdf`

---

## Overview

This technical support document provides NICE with guidance on when and how to use alternatives to EQ-5D for generating health state utility values (HSUVs). It addresses:

1. **When EQ-5D is inappropriate**: Conditions where EQ-5D lacks sensitivity or validity
2. **Alternative instruments**: SF-6D, HUI2/3, disease-specific measures, vignette studies
3. **Mapping**: Converting disease-specific measures to preference-based utilities
4. **Methodological standards**: For generating and reporting HSUVs

### Key Points

- **EQ-5D is the NICE reference case** but has limitations (ceiling effects, insensitivity to some conditions)
- **Alternatives require justification**: Must demonstrate why EQ-5D is inadequate
- **Mapping is acceptable** when direct preference-based measurement is unavailable
- **Condition-specific measures** may capture dimensions missing from generic instruments

---

## Comprehensive Application to the Core Paper

### 1. The Quality Function $q(x)$ and Its Measurement

Our framework relies on a quality function $q: \mathcal{X} \to [0, 1]$. Brazier & Rowen address the fundamental question: **How do we measure quality of life in health states?**

| Measurement Issue | Their Guidance | Our Framework's Treatment |
|-------------------|----------------|---------------------------|
| What is "quality"? | Preference-based utility from general population | $q(x)$ is a given function; source is separable |
| Bounded scale | [0, 1] where 0 = dead, 1 = full health | Same: $q(\dagger) = 0$, $q(x) \in [0, 1]$ |
| State-dependence | Different instruments capture different dimensions | $q(x)$ depends on the state $x \in \mathcal{S}$ |
| Adaptation | Long-term conditions may see adaptation | Could affect $q(x)$ for chronic states in $\mathcal{I}$ |

### 2. The "Maintenance World" and Measurement Challenges

Our setting emphasizes chronic states, repair, and long-term functioning. Brazier & Rowen note:

> "The EQ-5D may lack sensitivity for conditions where important dimensions of health are not captured."

In a maintenance/repair world, relevant dimensions include:
- **Functional capacity** (ability to perform activities)
- **Uncertainty/anxiety** about breakdown
- **Treatment burden** (time spent in maintenance)
- **Social/role functioning** during downtime

These may not be fully captured by EQ-5D's five dimensions (mobility, self-care, usual activities, pain/discomfort, anxiety/depression).

**Implication for our paper:** We should acknowledge that $q(x)$ depends on the measurement instrument, and that the instrument choice matters more when:
- Lifespans are long (small quality differences accumulate)
- States involve chronic maintenance rather than acute episodes

### 3. States Worse Than Dead ($q(x) < 0$?)

Brazier & Rowen discuss negative utilities:

> "Some health states may be valued as worse than dead."

Our framework assumes $q: \mathcal{X} \to [0, 1]$ with $q(\dagger) = 0$. This is a simplification. In principle:
- States worse than dead could have $q(x) < 0$
- This would affect the interpretation of $R^\pi = \int_0^\tau q(X_t) dt$

**Extension:** The framework could accommodate $q(x) \in [-1, 1]$ without structural change, though $J(\pi)$ would then be in $[-1, 1]$.

### 4. Long-Term Conditions and Irreversibility

Brazier & Rowen discuss conditions where standard measurement is challenging:
- **Mental health**: May require instruments beyond EQ-5D
- **Chronic pain**: Adaptation effects complicate measurement
- **Cognitive impairment**: Self-report may be unreliable

**Connection to our irreversibility framework (§6.1):**

We partition states into $\mathcal{I}$ (irreversible) and $\mathcal{R}$ (repairable). For irreversible states:
- Quality $q(x)$ may reflect permanent limitations
- The disutility function $\kappa(x)$ captures option-value loss beyond immediate quality

Brazier & Rowen's guidance on condition-specific measurement applies especially to $\mathcal{I}$—irreversible states may require specialized instruments.

### 5. Mapping and Cross-Walk Methods

When preference-based measures aren't directly available, Brazier & Rowen recommend mapping:

> "Mapping involves developing an algorithm to predict EQ-5D utilities from a non-preference-based measure."

**Relevance for our framework:** In practice, implementing our model requires:
1. Defining the state space $\mathcal{S}$ (clinical/functional states)
2. Assigning utilities $q(x)$ to each state
3. If utilities aren't directly measured for our states, mapping is needed

The TSD provides standards for such mapping, which would apply to calibrating our quality function.

### 6. The Quality Function as a Separable Layer

Our framework treats $q(x)$ as exogenous—it's a given function that maps states to utilities. Brazier & Rowen's work makes clear this is a substantial undertaking in practice:

| Step | Description | Brazier & Rowen Guidance |
|------|-------------|-------------------------|
| 1. Define states | What is $\mathcal{S}$? | States should be clinically meaningful |
| 2. Choose instrument | EQ-5D, SF-6D, disease-specific | Reference case is EQ-5D; alternatives need justification |
| 3. Value states | Survey, mapping, vignettes | Preference-based from general population |
| 4. Assign $q(x)$ | Attach utilities to states | May require mapping if states don't match instrument |

### 7. Specific Connections to Core Paper Sections

| Core Paper Section | Brazier & Rowen Connection |
|--------------------|---------------------------|
| §2.1 (State space and quality) | Our $q(x)$ is their HSUV—same [0,1] scale, same conceptual basis |
| Definition 3.1 (QALY Flow) | $J(\pi)$ is quality-weighted time, same as QALY construction |
| §6.1 (Irreversibility) | Their condition-specific guidance applies to $\mathcal{I}$ states |
| Axiom 3 (Experienced Welfare) | Aligns with preference-based utility measurement |

### 8. Quotable Passages for Citation

> "The EQ-5D is the preferred measure of health-related quality of life in adults for the reference case."

Establishes the baseline for $q(x)$ measurement.

> "Alternatives to EQ-5D should be considered where EQ-5D is demonstrably inappropriate."

Supports flexibility in defining $q(x)$ for specific applications.

> "Health state utility values should lie on a scale anchored at 1 (full health) and 0 (dead)."

Directly matches our $q: \mathcal{X} \to [0, 1]$ with $q(\dagger) = 0$.

### 9. How to Cite This Source in Core Paper

**Suggested citation point (§2.1 on quality):**

> The quality function $q: \mathcal{X} \to [0, 1]$ assigns health state utility values following standard practice (Brazier & Rowen, 2011). In the reference case, $q(x)$ corresponds to EQ-5D utilities; for conditions where EQ-5D lacks sensitivity, alternative instruments or mapping approaches may be used.

**Alternative (in remarks about measurement):**

> The technical definition of QALYs becomes more important when time horizons are long: small differences in $q(x)$ accumulate over extended lifespans. Guidance on utility measurement (Brazier & Rowen, 2011) should be followed with particular care in this setting.

---

## Summary

Brazier & Rowen (2011) provides the measurement foundations for our quality function $q(x)$. Key implications:

1. **Standard practice**: EQ-5D utilities on [0, 1] scale—exactly our $q(x)$ definition
2. **Limitations**: Generic instruments may miss dimensions important in a maintenance/repair world
3. **Flexibility**: Our framework can accommodate alternative instruments via different $q(x)$ specifications
4. **Long-horizon concerns**: Measurement precision matters more when quality accumulates over unbounded time

The paper grounds the practical question of *where $q(x)$ comes from*, which our theoretical framework takes as given.
