# Rooting Plan: Embedding the Paper in the Literature

> **STATUS: ✅ EXECUTED** (January 30, 2026)
> 
> All citations have been added. The paper now cites all 10 sources with 25+ citation instances across 11 pages. Bibliography renders correctly.

This document provides a detailed, actionable plan for grounding the core paper firmly in the health economics literature through systematic citation of the 10 source documents.

---

## 0. Technical Fix: Include the Bibliography ✅ DONE

**Completed:**
- Added `\usepackage{natbib}` for citation commands
- Added `\bibliographystyle{apalike}` before bibliography
- Added new appendix section on discounting
- Compiled successfully: `pdflatex && bibtex && pdflatex && pdflatex`

---

## 1. Section-by-Section Citation Plan

### §1 Introduction

| Location | Citation | Purpose |
|----------|----------|---------|
| Motivation paragraph | \cite{sanders2016} | Ground in established CEA methodology |
| "Unbounded lifespans" sentence | \cite{masny2023} | Connect to healthspan/longevity ethics literature |
| Problem statement | \cite{attema2018, gravelle2007} | Acknowledge discounting debate |

**Suggested text additions:**

> Health technology assessment relies on established frameworks for comparing interventions \citep{sanders2016}, but these presuppose finite planning horizons. As longevity science advances the prospect of radical healthspan extension \citep{masny2023}, fundamental questions arise about how to evaluate policies when lifespans may be unbounded.

---

### §2 Model Setup (Controlled Health Process)

| Location | Citation | Purpose |
|----------|----------|---------|
| CTMC formulation | \cite{bauer2025, song2023} | Precedent for stochastic health models |
| Quality function $q(x)$ | \cite{brazier2011} | Ground in quality measurement literature |
| State space discussion | \cite{bauer2025} | Multi-state health model precedent |

**Suggested text additions:**

After introducing the state space:
> This multi-state formulation follows the health economics tradition of modeling health trajectories as stochastic processes \citep{bauer2025, song2023}. The quality function $q: \mathcal{S} \to [0,1]$ assigns health-related quality of life to each state, following established measurement frameworks \citep{brazier2011}.

---

### §2 Axioms

| Axiom | Citation | Purpose |
|-------|----------|---------|
| Axiom 1 (QALY doctrine) | \cite{sanders2016, brazier2011} | Standard CEA practice |
| Axiom 2 (Temporal neutrality) | \cite{attema2018, gravelle2007} | Acknowledge discounting alternative |
| Axiom 3 (Generational neutrality) | \cite{masny2023} | Contrast with complete-life view |
| Axiom 4 (Person neutrality) | \cite{asaria2013} | Contrast with DCEA weights |

**Suggested text additions:**

After Axiom 1:
> This axiom reflects standard practice in health technology assessment \citep{sanders2016}, where QALYs serve as the primary outcome measure \citep{brazier2011}.

After Axiom 2:
> This contrasts with discounted approaches common in applied health economics \citep{attema2018}. Gravelle and Smith \citeyearpar{gravelle2007} analyze the theoretical foundations of discounting; we discuss our departure from this tradition in the Appendix.

After Axiom 3:
> Alternative frameworks give priority to those with less "complete" lives \citep{masny2023}. For unbounded horizons, where life completeness becomes undefined, generational neutrality is more natural.

After Axiom 4:
> Distributional cost-effectiveness analysis relaxes this assumption by weighting QALYs by recipient characteristics \citep{asaria2013}. We discuss this extension in Section 8.

---

### §3 The Regenerative Framework

| Location | Citation | Purpose |
|----------|----------|---------|
| Renewal-reward motivation | \cite{omahony2015} | Time structure in health evaluation |
| QALY flow definition | \cite{sanders2016} | Connect to standard CEA |

**Suggested text additions:**

Before Definition 3.1:
> The regenerative structure allows us to define a time-averaged objective that remains bounded and well-defined over infinite horizons. This addresses the fundamental challenge of evaluating policies when time horizons are unbounded \citep{omahony2015}.

---

### §4 Existence of Optimal Policies

No direct citations needed here—this is technical development. Could add:

> The existence result parallels standard results in controlled Markov processes, adapted to our regenerative setting.

---

### §5 Comparative Statics (Sensitivity Analysis)

| Location | Citation | Purpose |
|----------|----------|---------|
| Stability motivation | \cite{ultsch2015} | Parameter uncertainty in practice |
| Volatility measure | \cite{bauer2025} | Value at risk concepts |

**Suggested text additions:**

Opening of section:
> Practical policy evaluation requires understanding sensitivity to parameter uncertainty, which can be substantial in health economic models \citep{ultsch2015}.

---

### §6 Extensions

#### §6.1 Irreversibility

| Location | Citation | Purpose |
|----------|----------|---------|
| Irreversible conditions | \cite{bauer2025, song2023} | State-dependent mortality |
| Absorbing states | \cite{masny2023} | Healthspan vs lifespan distinction |

**Suggested text additions:**

> Some health states represent irreversible conditions with distinct mortality profiles \citep{bauer2025}. The distinction between healthspan and lifespan \citep{masny2023} is naturally captured by partitioning states into reversible and absorbing subsets.

#### §6.2 State-Dependent Costs

| Location | Citation | Purpose |
|----------|----------|---------|
| Cost modeling | \cite{sanders2016} | Standard CEA cost perspective |
| Consumption effects | \cite{song2023} | State-dependent spending |

---

### §7 Cost-Effectiveness Analysis

| Location | Citation | Purpose |
|----------|----------|---------|
| ICER definition | \cite{sanders2016} | Standard methodology |
| Threshold discussion | \cite{brazier2011} | Valuation methods |
| Discounting comparison | \cite{gravelle2007, attema2018} | Why we depart from standard |

**Suggested text additions:**

> Our flow-based ICER parallels the standard incremental cost-effectiveness ratio \citep{sanders2016}, but replaces discounted sums with long-run averages. This avoids the well-documented issues with discount rate selection \citep{attema2018, gravelle2007}.

---

### §8 Distributional Concerns

| Location | Citation | Purpose |
|----------|----------|---------|
| DCEA introduction | \cite{asaria2013} | Primary reference |
| Equity weights | \cite{asaria2013} | Methodology |
| Financial heterogeneity | \cite{song2023} | Value depends on insurance |

**Suggested text additions:**

> The distributional extension follows the framework of distributional cost-effectiveness analysis \citep{asaria2013}, which assigns equity weights to different population subgroups. Song et al. \citeyearpar{song2023} show that the value of health improvements depends on access to insurance and retirement products, suggesting distributional weights should account for financial as well as health heterogeneity.

---

### Appendix (Discounting Discussion)

| Location | Citation | Purpose |
|----------|----------|---------|
| Why not discount | \cite{attema2018, gravelle2007} | Engage with the debate |
| Pure time preference | \cite{gravelle2007} | Theoretical foundations |
| Consistency arguments | \cite{omahony2015} | Time treatment |

**Suggested text additions:**

> The health economics literature extensively debates discounting \citep{attema2018}. Gravelle and Smith \citeyearpar{gravelle2007} analyze the decision-theoretic foundations, showing that different discount rates for costs and effects can be justified. O'Mahony and Paulden \citeyearpar{omahony2015} examine how time enters health evaluations more broadly. Our approach sidesteps the discount rate selection problem entirely by moving to ratio-form objectives.

---

## 2. Citation Density Targets

| Section | Current Citations | Target Citations |
|---------|-------------------|------------------|
| §1 Introduction | 0 | 3-4 |
| §2 Model & Axioms | 0 | 6-8 |
| §3 Regenerative Framework | 0 | 2 |
| §4 Optimal Policies | 0 | 0-1 |
| §5 Sensitivity | 0 | 2 |
| §6 Extensions | 0 | 3-4 |
| §7 Cost-Effectiveness | 0 | 3 |
| §8 Distributional | 0 | 2-3 |
| Appendix | 0 | 3 |
| **Total** | **0** | **~25** |

---

## 3. Execution Checklist

### Phase 1: Technical Setup ✅
- [x] Add `\bibliographystyle{apalike}` before `\bibliography`
- [x] Add `\usepackage{natbib}` for citation commands
- [x] Verify `sources/references.bib` path is correct
- [x] Test compilation: `pdflatex && bibtex && pdflatex && pdflatex`

### Phase 2: Introduction Rooting ✅
- [x] Add Sanders (2016) citation for CEA grounding
- [x] Add Masny (2023) for longevity ethics motivation
- [x] Add Attema/Gravelle for discounting context

### Phase 3: Model Section Rooting ✅
- [x] Add Bauer/Song citations for stochastic health models
- [x] Add Brazier (2011) for quality measurement
- [x] Add citations after axioms (flow axiom, explicit normativity axiom)

### Phase 4: Core Framework Rooting ✅
- [x] Add O'Mahony (2015) for time treatment
- [x] Light citations in technical sections (§5)

### Phase 5: Extensions and Applications Rooting ✅
- [x] Add Asaria (2013) for DCEA in §8
- [x] Add Song (2023) for distributional/financial concerns
- [x] Add Bauer/Masny for irreversibility section
- [x] Add comprehensive discounting discussion in new Appendix section

### Phase 6: Final Verification ✅
- [x] Compile and verify all citations render
- [x] Check bibliography appears correctly (11 pages, no warnings)
- [x] Verify no "?" placeholders for undefined references

---

## 4. Source-by-Source Integration Summary

| Source | Primary Location | Secondary Locations |
|--------|------------------|---------------------|
| Sanders 2016 | §1, §7 | §2 (Axiom 1) |
| Attema 2018 | Appendix | §1, §2 (Axiom 2), §7 |
| Gravelle 2007 | Appendix | §1, §2 (Axiom 2), §7 |
| O'Mahony 2015 | Appendix | §3 |
| Asaria 2013 | §8 | §2 (Axiom 4) |
| Brazier 2011 | §2 | §7 |
| Ultsch 2015 | §5 | — |
| Bauer 2025 | §2, §6 | — |
| Song 2023 | §8 | §2, §6 |
| Masny 2023 | §1, §2 (Axiom 3) | §6 |

---

## 5. Estimated Time

| Phase | Estimated Time |
|-------|----------------|
| Phase 1 (Technical) | 5 minutes |
| Phase 2 (Introduction) | 15 minutes |
| Phase 3 (Model) | 20 minutes |
| Phase 4 (Framework) | 10 minutes |
| Phase 5 (Extensions) | 15 minutes |
| Phase 6 (Verification) | 10 minutes |
| **Total** | **~75 minutes** |

---

## 6. Notes

- All `\cite{}` commands assume natbib-style. If using different citation package, adjust accordingly.
- The source notes in `sources/source_notes/` contain detailed quotable passages for each source.
- Minor inconsistencies (Gravelle year, Ultsch filename) already documented in `sources/sources.md`.
