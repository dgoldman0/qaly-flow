# Source manifest

This manifest lists every PDF in `sources/`, why it was selected, and how it supports a paper that intersects QALY flow with futurism, biomedical engineering, and societal management.

## Contents
- [goldman2026steadystateqalyflow](#goldman2026steadystateqalyflow) — Evaluating Health Policy Without a Fixed Lifespan: A Steady-State Foundation for Quality, Maintenance, and Risk (2026)
- [asaria2013distributionalcea](#asaria2013distributionalcea) — Distributional Cost-Effectiveness Analysis: A Tutorial (CHE Research Paper 92) (2013)
- [bostrom2013existentialriskprevention](#bostrom2013existentialriskprevention) — Existential Risk Prevention as Global Priority (2013)
- [bostrom2003astronomicalwaste](#bostrom2003astronomicalwaste) — Astronomical Waste: The Opportunity Cost of Delayed Technological Development (2003)
- [greaves2021stronglongtermism](#greaves2021stronglongtermism) — The Case for Strong Longtermism (GPI Working Paper No. 5-2021) (2021)
- [hmtreasury2026greenbook](#hmtreasury2026greenbook) — The Green Book: Central Government Guidance on Appraisal and Evaluation (2026)
- [hmtreasury2026discounting](#hmtreasury2026discounting) — Discounting: Green Book Supplementary Guidance (2026)
- [stumborg2022goodharts](#stumborg2022goodharts) — Goodhart’s Law: Recognizing and Mitigating the Manipulation of Measures in Analysis (2022)
- [who2015climateresilient](#who2015climateresilient) — Operational Framework for Building Climate Resilient Health Systems (2015)
- [lopezotin2013hallmarks](#lopezotin2013hallmarks) — The Hallmarks of Aging (2013)
- [lopezotin2023expandinghallmarks](#lopezotin2023expandinghallmarks) — Hallmarks of Aging: An Expanding Universe (2023)
- [finkelstein2006engineeringreliability](#finkelstein2006engineeringreliability) — On Engineering Reliability Concepts and Biological Aging (2006)
- [strulik2021measuringageing](#strulik2021measuringageing) — Measuring Ageing (Handbook chapter draft) (2021)
- [melov2016geroscience](#melov2016geroscience) — Geroscience Approaches to Increase Healthspan and Slow Aging (2016)
- [moffitt2020behavioralsocial](#moffitt2020behavioralsocial) — Behavioral and Social Research to Accelerate the Geroscience Translation Agenda (2020)
- [crimmins2020socialhallmarks](#crimmins2020socialhallmarks) — Social Hallmarks of Aging: Suggestions for Geroscience Research (2020)
- [marugan2024rlmaintenance](#marugan2024rlmaintenance) — A Reinforcement Learning Agent for Maintenance of Deteriorating Systems with Increasingly Imperfect Repairs (2024)
- [sigman2018renewalreward](#sigman2018renewalreward) — Some Basic Renewal Theory: The Renewal Reward Theorem (2018)
- [gallager2011renewalprocesses](#gallager2011renewalprocesses) — Discrete Stochastic Processes, Chapter 4: Renewal Processes (MIT OCW 6.262) (2011)
- [feinberg2012averagecostmdp](#feinberg2012averagecostmdp) — Average-Cost Markov Decision Processes with Weakly Continuous Transition Probabilities (arXiv:1202.4122) (2012)
- [boucherie2023averagecostnotes](#boucherie2023averagecostnotes) — Average Cost Markov Decision Processes: Policy-Iteration and Value-Iteration (Addendum) (2023)
- [tadepalli1998average](#tadepalli1998average) — Model-based Average Reward Reinforcement Learning (1998)
- [wang2023robustaverage](#wang2023robustaverage) — Robust Average-Reward Markov Decision Processes (2023)
- [nist2012sp80030](#nist2012sp80030) — Guide for Conducting Risk Assessments (NIST SP 800-30 Rev. 1) (2012)

---

## goldman2026steadystateqalyflow

**Evaluating Health Policy Without a Fixed Lifespan: A Steady-State Foundation for Quality, Maintenance, and Risk** (2026)

- **PDF:** `sources/goldman_2026_qaly_flow.pdf` (0.12 MB)
- **Source URL:** (user-provided upload: current.pdf)
- **Tags:** core framing, renewal/regeneration, health policy

### Summary
- Defines a steady-state evaluation regime for health policy when lifespan is unbounded but subject to repairable degradation and stochastic catastrophe.
- Uses a regenerative (renewal) viewpoint: evaluate policies by expected reward per expected cycle time, with compatible cost-effectiveness and sensitivity results.
- Provides design requirements/axioms (including replacement/regeneration) and an explicit controlled continuous-time model with catastrophe and irreversibility extensions.

### Intersection with QALY flow
- Serves as the anchor reference for the paper’s assumptions about steady-state person-time value under indefinite horizons.
- Supplies the vocabulary for cycles, regeneration, repair vs. catastrophe, and the policy objective being horizon-invariant.
- Enables the new paper to stay math-agnostic by focusing on the structural requirements (regenerative regime, stability under perturbations) rather than any particular derivation.

### Where it plugs into the draft paper
- Intro + motivating setting (unbounded lifespan + maintenance + catastrophic risk).
- Technical appendix reference point for any formal statements of ‘cycle’ and ‘replacement’ assumptions.
- Bridge to the MDP/renewal literature (Sigman; Gallager; Feinberg) and to engineering maintenance (Marugán).

### BibTeX
```bibtex
@misc{goldman2026steadystateqalyflow,
  author       = {Goldman, Daniel S.},
  title        = {Evaluating Health Policy Without a Fixed Lifespan: A Steady-State Foundation for Quality, Maintenance, and Risk},
  year         = {2026},
  month        = jan,
  note         = {Manuscript (user-provided PDF)},
}
```

---

## asaria2013distributionalcea

**Distributional Cost-Effectiveness Analysis: A Tutorial (CHE Research Paper 92)** (2013)

- **PDF:** `sources/asaria_2013_distributional_cea_tutorial.pdf` (0.59 MB)
- **Source URL:** https://eprints.whiterose.ac.uk/136239/1/CHERP92_distributional_CEA_tutorial.pdf
- **Tags:** societal management, equity, health economics

### Summary
- Tutorial-style introduction to distributional cost-effectiveness analysis (DCEA), framing how to incorporate equity concerns into cost-effectiveness.
- Discusses how health gains and costs distribute across social groups, and how to represent inequality aversion explicitly.
- Provides practical modeling steps (e.g., subgroup baselines, equity weights, inequality metrics) for policy appraisal.

### Intersection with QALY flow
- Shows how a per-time welfare objective can be made distributive: flow objectives can be defined for subpopulations and aggregated with explicit equity weights.
- Highlights that evaluation must separate ‘how much’ benefit is produced from ‘who gets it’—a natural complement to any steady-state person-time metric.
- Provides scaffolding for ‘societal management’ sections: using QALY flow as the base metric while letting distributional choices be policy-layer decisions.

### Where it plugs into the draft paper
- Section on institutional design: fairness constraints, equity weights, and distributional governance under steady-state evaluation.
- Discussion of ‘metric governance’: how to prevent flow optimization from amplifying inequality.

### BibTeX
```bibtex
@techreport{asaria2013distributionalcea,
  author       = {Asaria, Miqdad and Griffin, Susan and Cookson, Richard A.},
  title        = {Distributional Cost-Effectiveness Analysis: A Tutorial},
  institution  = {Centre for Health Economics, University of York},
  type         = {CHE Research Paper},
  number       = {92},
  year         = {2013},
  address      = {York, UK},
}
```

---

## bostrom2013existentialriskprevention

**Existential Risk Prevention as Global Priority** (2013)

- **PDF:** `sources/bostrom_2013_existential_risk_prevention.pdf` (0.29 MB)
- **Source URL:** https://existential-risk.com/concept.pdf
- **Tags:** futurism, existential risk, prioritization

### Summary
- Argues that existential risks (threats to humanity’s long-run potential) merit high priority under many value theories.
- Frames existential risk work as risk-reduction with enormous expected-value leverage due to long horizons.
- Discusses challenges in comparing interventions, institutional incentives, and coordination issues.

### Intersection with QALY flow
- Connects steady-state health value to the ‘tail’ of the future: small changes in catastrophe rates and recovery dynamics can dominate long-run person-time outcomes.
- Supports the paper’s claim that risk management is a first-class component of steady-state welfare design, not an add-on.
- Motivates treating existential-risk governance as ‘infrastructure’ that stabilizes the regimes in which QALY flow is meaningful and optimizable.

### Where it plugs into the draft paper
- Futurism section on unbounded horizons and why catastrophe-rate control is a central governance target.
- Risk-and-resilience section: risk assessment and monitoring (paired with NIST SP 800-30).

### BibTeX
```bibtex
@article{bostrom2013existentialriskprevention,
  author       = {Bostrom, Nick},
  title        = {Existential Risk Prevention as Global Priority},
  journal      = {Global Policy},
  year         = {2013},
  volume       = {4},
  number       = {1},
  pages        = {15--31},
}
```

---

## bostrom2003astronomicalwaste

**Astronomical Waste: The Opportunity Cost of Delayed Technological Development** (2003)

- **PDF:** `sources/bostrom_2003_astronomical_waste.pdf` (0.09 MB)
- **Source URL:** https://intelligence.org/files/AstronomicalWaste.pdf
- **Tags:** futurism, growth vs safety, long horizons

### Summary
- Quantifies the opportunity cost of delaying advanced technology and future expansion, while stressing that safety can dominate speed.
- Introduces a crisp tradeoff: accelerating development increases realized value, but can increase catastrophic risk if safety lags.
- Positions ‘safety’ as a lever on whether the long-run future is accessed at all.

### Intersection with QALY flow
- Provides a narrative counterpart to steady-state evaluation: even under a flow objective, a system’s viability and safety envelope constrain attainable long-run welfare.
- Supports treating safety investment as an ‘option’ that preserves the renewal/regeneration regime rather than simply increasing near-term flow.
- Helps motivate policy portfolios that jointly optimize (i) steady per-time welfare and (ii) survival/continuation probabilities.

### Where it plugs into the draft paper
- Futurism section on tempo vs safety; motivates dual-objective governance (flow + survival).
- Conclusion on why ‘future-building’ is about maintaining regimes, not only maximizing immediate output.

### BibTeX
```bibtex
@article{bostrom2003astronomicalwaste,
  author       = {Bostrom, Nick},
  title        = {Astronomical Waste: The Opportunity Cost of Delayed Technological Development},
  journal      = {Utilitas},
  year         = {2003},
  volume       = {15},
  number       = {3},
  pages        = {308--314},
}
```

---

## greaves2021stronglongtermism

**The Case for Strong Longtermism (GPI Working Paper No. 5-2021)** (2021)

- **PDF:** `sources/greaves_mackill_2021_strong_longtermism.pdf` (0.81 MB)
- **Source URL:** https://www.globalprioritiesinstitute.org/wp-content/uploads/The-Case-for-Strong-Longtermism-GPI-Working-Paper-June-2021-2-2.pdf
- **Tags:** futurism, moral philosophy, policy framing

### Summary
- Formalizes conditions under which the long-run future dominates moral evaluation (‘strong longtermism’).
- Distinguishes arguments that rely on expected value, moral aggregation, and uncertainty about future people.
- Clarifies philosophical sensitivities: discounting, population ethics, and moral uncertainty.

### Intersection with QALY flow
- Provides an interpretive layer for why a steady-state objective becomes a natural discourse primitive when horizons are effectively unbounded.
- Supplies conceptual guardrails for the new paper: treat the flow objective as a stable interface between moral theories rather than a fully specified moral theory itself.
- Supports presenting QALY flow as an institutional evaluation tool that can remain useful across moral disagreement (e.g., about discounting or population ethics).

### Where it plugs into the draft paper
- Futurism section: ethical motivation for emphasizing indefinite-horizon comparability.
- ‘Agnosticism’ discussion: how to keep the paper robust to alternative normative foundations.

### BibTeX
```bibtex
@techreport{greaves2021stronglongtermism,
  author       = {Greaves, Hilary and MacAskill, William},
  title        = {The Case for Strong Longtermism},
  institution  = {Global Priorities Institute, University of Oxford},
  year         = {2021},
  month        = jun,
  type         = {Working Paper},
  number       = {5-2021},
}
```

---

## hmtreasury2026greenbook

**The Green Book: Central Government Guidance on Appraisal and Evaluation** (2026)

- **PDF:** `sources/hm_treasury_2026_green_book.pdf` (0.96 MB)
- **Source URL:** https://assets.publishing.service.gov.uk/media/6984ac702df808759a7bd740/The_Green_Book_2026.pdf
- **Tags:** societal management, public appraisal, cost-benefit

### Summary
- UK government guidance on how to appraise and evaluate public policies, projects, and programs.
- Covers cost-benefit analysis, welfare economics foundations, and practical appraisal steps (options, risk, uncertainty, monitoring).
- Provides institutional language for decision processes, governance, and evidence standards.

### Intersection with QALY flow
- Serves as an example of how to institutionalize an evaluation metric: QALY flow can be presented as a ‘Green Book–style’ appraisal primitive for indefinite horizons.
- Highlights the governance lifecycle (appraise → decide → monitor): essential when flow metrics are optimized continuously rather than once-off.
- Supports the paper’s ‘societal management’ angle: evaluation isn’t only math—it is procedures, accountability, and monitoring.

### Where it plugs into the draft paper
- Section on institutionalization: translating QALY flow into appraisal guidance, auditability, and continuous evaluation loops.
- Policy portfolio section: risk/uncertainty management and option value.

### BibTeX
```bibtex
@techreport{hmtreasury2026greenbook,
  author       = {{HM Treasury}},
  title        = {The Green Book: Central Government Guidance on Appraisal and Evaluation},
  institution  = {{HM Treasury}},
  year         = {2026},
  month        = feb,
  type         = {Government guidance},
}
```

---

## hmtreasury2026discounting

**Discounting: Green Book Supplementary Guidance** (2026)

- **PDF:** `sources/hm_treasury_2026_green_book_discounting_guidance.pdf` (0.41 MB)
- **Source URL:** https://assets.publishing.service.gov.uk/media/698488ab2df808759a7bd70f/Green_Book_supplementary_guidance_-_discounting.pdf
- **Tags:** societal management, discounting, time preference

### Summary
- Supplementary UK guidance on discounting future costs and benefits in public appraisal.
- Discusses rationale for discounting and practical implementation choices under uncertainty and long horizons.
- Explains when and how alternative discount schedules may be justified.

### Intersection with QALY flow
- Acts as a ‘contrast case’: discounting is a primary technique for finite-horizon aggregation, while steady-state flow is naturally horizon-invariant.
- Helps frame the paper’s agnostic stance: flow objectives can coexist with discounting for transitional or bounded subproblems without committing to a single discount philosophy.
- Provides institutional language to discuss hybrid regimes (flow for steady-state, discounting for ramp-up, transition, and legacy costs).

### Where it plugs into the draft paper
- Methodology section: reconcile flow-based governance with conventional discounting practices used in government appraisal.
- Appendix: mapping between discounted present-value framing and steady-state evaluation in renewal settings.

### BibTeX
```bibtex
@techreport{hmtreasury2026discounting,
  author       = {{HM Treasury}},
  title        = {Discounting: Green Book Supplementary Guidance},
  institution  = {{HM Treasury}},
  year         = {2026},
  month        = feb,
  type         = {Supplementary guidance},
}
```

---

## stumborg2022goodharts

**Goodhart’s Law: Recognizing and Mitigating the Manipulation of Measures in Analysis** (2022)

- **PDF:** `sources/cna_2022_goodharts_law_metrics_manipulation.pdf` (0.75 MB)
- **Source URL:** https://www.cna.org/reports/2022/09/Goodharts-Law-Recognizing-Mitigating-Manipulation-Measures-in-Analysis.pdf
- **Tags:** societal management, metrics, incentives

### Summary
- Explains how performance measures become targets and therefore vulnerable to manipulation, gaming, and goal displacement.
- Catalogs failure modes (proxy manipulation, data quality degradation, selection effects) and proposes mitigation strategies (triangulation, audits, red teaming).
- Focuses on analytical settings where metrics drive resource allocation and decision authority.

### Intersection with QALY flow
- Directly informs how to govern any flow metric at scale: optimizing QALY flow can produce perverse incentives unless measurement and accountability are engineered.
- Supports the paper’s design principle: treat QALY flow as a control signal with a measurement system, not merely a scalar objective.
- Enables concrete governance recommendations: auditing, multiple metrics, adversarial evaluation, and robustness checks around flow estimates.

### Where it plugs into the draft paper
- Societal management section: metric governance architecture for QALY-flow-driven institutions.
- Policy design: monitoring and ‘anti-Goodhart’ measures for health systems and R&D incentives.

### BibTeX
```bibtex
@techreport{stumborg2022goodharts,
  author       = {Stumborg, Michael F. and Blasius, Timothy D. and Full, Steven J. and Hughes, Christine A. and Scherer, Jennifer M.},
  title        = {Goodhart's Law: Recognizing and Mitigating the Manipulation of Measures in Analysis},
  institution  = {CNA},
  year         = {2022},
  month        = sep,
  type         = {Report},
  number       = {COP-2022-U-033385-Final},
}
```

---

## who2015climateresilient

**Operational Framework for Building Climate Resilient Health Systems** (2015)

- **PDF:** `sources/who_2015_climate_resilient_health_systems_framework.pdf` (1.85 MB)
- **Source URL:** https://unfccc.int/sites/default/files/resource/WHO_Operational_framework_for_building_climate_resilient_health_systems.pdf
- **Tags:** resilience, health systems, societal management

### Summary
- Framework for strengthening health systems to anticipate, respond to, and recover from climate-related shocks and stresses.
- Organizes actions across leadership, workforce, infrastructure, surveillance, and service delivery.
- Emphasizes adaptation planning, vulnerability assessments, and iterative improvement.

### Intersection with QALY flow
- Provides a concrete instance of ‘maintenance + shocks’ thinking at the institutional scale: resilience is about sustaining service quality over time, not only peak output.
- Supplies operational vocabulary for the paper’s claim that steady-state welfare depends on recovery dynamics and system robustness.
- Supports treating health-system resilience as a QALY-flow stabilizer, analogous to engineering redundancy and preventive maintenance.

### Where it plugs into the draft paper
- Section on societal management: resilience as a design target; healthcare infrastructure as ‘maintenance systems’ for populations.
- Case study vignette: climate shocks, downtime, and steady-state health outcomes.

### BibTeX
```bibtex
@techreport{who2015climateresilient,
  author       = {{World Health Organization}},
  title        = {Operational Framework for Building Climate Resilient Health Systems},
  institution  = {{World Health Organization}},
  year         = {2015},
  type         = {Framework},
}
```

---

## lopezotin2013hallmarks

**The Hallmarks of Aging** (2013)

- **PDF:** `sources/lopez_otin_2013_hallmarks_of_aging.pdf` (4.01 MB)
- **Source URL:** https://cdn.serc.carleton.edu/files/curenet/institutes/ccri/examples/2013_lopez-otin_hallmarks_aging.pdf
- **Tags:** biomedical engineering, aging biology, mechanisms

### Summary
- Canonical framework describing major biological processes that drive aging and age-related decline.
- Organizes mechanisms into hallmarks (e.g., genomic instability, telomere attrition, proteostasis loss, etc.).
- Connects mechanisms to intervention strategies and research agendas.

### Intersection with QALY flow
- Provides the mechanistic substrate for ‘maintenance’ in the flow regime: interventions can be interpreted as reducing degradation rates, restoring function, or increasing repair efficiency.
- Supports system-engineering language: hallmarks map to subsystems and failure modes that policy and R&D can target.
- Anchors the biomedical engineering section without requiring any specific mathematical instantiation of QALY flow.

### Where it plugs into the draft paper
- Biomedical engineering section: translating biological hallmarks into engineering levers (maintenance, repair, redundancy).
- Research agenda: how to prioritize interventions that shift long-run steady performance rather than one-off gains.

### BibTeX
```bibtex
@article{lopezotin2013hallmarks,
  author       = {L{\'o}pez-Ot{\'i}n, Carlos and Blasco, Maria A. and Partridge, Linda and Serrano, Manuel and Kroemer, Guido},
  title        = {The Hallmarks of Aging},
  journal      = {Cell},
  year         = {2013},
  volume       = {153},
  number       = {6},
  pages        = {1194--1217},
  doi          = {10.1016/j.cell.2013.05.039},
}
```

---

## lopezotin2023expandinghallmarks

**Hallmarks of Aging: An Expanding Universe** (2023)

- **PDF:** `sources/lopez_otin_2023_hallmarks_expanding_universe.pdf` (4.82 MB)
- **Source URL:** https://www.unifal-mg.edu.br/ppgnl/wp-content/uploads/sites/133/2024/01/Hallmarks-of-aging-An-expanding-universe.pdf
- **Tags:** biomedical engineering, aging biology, updates

### Summary
- Updated and expanded view of aging hallmarks, reflecting new evidence and broader system interactions.
- Emphasizes network effects across hallmarks and the role of chronic inflammation, dysbiosis, and other systemic processes.
- Highlights translational implications and emerging interventions.

### Intersection with QALY flow
- Strengthens the argument that ‘maintenance’ policies must be system-aware: optimizing a single pathway can shift failure modes elsewhere.
- Supports robust governance of flow interventions: monitor unintended consequences and cross-hallmark tradeoffs.
- Provides conceptual grounding for ‘portfolio maintenance’: diversified interventions to improve steady-state function.

### Where it plugs into the draft paper
- Biomedical engineering section: the case for multi-lever, cross-hallmark approaches.
- Societal management section: monitoring and post-deployment surveillance for interventions.

### BibTeX
```bibtex
@article{lopezotin2023expandinghallmarks,
  author       = {L{\'o}pez-Ot{\'i}n, Carlos and Blasco, Maria A. and Partridge, Linda and Serrano, Manuel and Kroemer, Guido},
  title        = {Hallmarks of Aging: An Expanding Universe},
  journal      = {Cell},
  year         = {2023},
  doi          = {10.1016/j.cell.2022.11.001},
  note         = {Online January 19, 2023},
}
```

---

## finkelstein2006engineeringreliability

**On Engineering Reliability Concepts and Biological Aging** (2006)

- **PDF:** `sources/finkelstein_2006_engineering_reliability_biological_aging.pdf` (0.42 MB)
- **Source URL:** https://www.demogr.mpg.de/papers/working/wp-2006-021.pdf
- **Tags:** biomedical engineering, reliability theory, aging

### Summary
- Applies reliability engineering concepts (wear, damage accumulation, hazard) to biological aging models.
- Frames mortality as a failure process and links ‘resource’ or redundancy depletion to survival curves.
- Shows how engineering abstractions can illuminate biological aging dynamics.

### Intersection with QALY flow
- Provides a bridge between biomedical aging and cycle-based evaluation: hazard rates and failure models are natural inputs to any long-run person-time metric.
- Supports interpreting interventions as reliability improvements—extending mean time to failure, improving repair, or increasing redundancy.
- Justifies a maintenance-engineering treatment of medicine: design for uptime, not only acute rescue.

### Where it plugs into the draft paper
- Biomedical engineering section: mapping hazard models to policy levers and maintenance schedules.
- Risk section: interpreting catastrophic events as failure modes and the role of redundancy.

### BibTeX
```bibtex
@techreport{finkelstein2006engineeringreliability,
  author       = {Finkelstein, Maxim},
  title        = {On Engineering Reliability Concepts and Biological Aging},
  institution  = {Max Planck Institute for Demographic Research},
  year         = {2006},
  type         = {Working Paper},
  number       = {WP-2006-021},
  address      = {Rostock, Germany},
}
```

---

## strulik2021measuringageing

**Measuring Ageing (Handbook chapter draft)** (2021)

- **PDF:** `sources/strulik_2021_measuring_ageing_handbook_chapter.pdf` (0.43 MB)
- **Source URL:** https://holger-strulik.org/my_papers/aging_handbook_revised.pdf
- **Tags:** measurement, demography, aging

### Summary
- Reviews how to conceptualize and measure aging as an increasing probability of death and related demographic regularities (e.g., Gompertz-Makeham).
- Discusses alternative measures of biological vs chronological age and how measurement choices affect inference.
- Provides an economist-facing synthesis connecting biology, demography, and formal aging metrics.

### Intersection with QALY flow
- Supports the measurement layer needed for governing a flow objective: QALY flow requires reliable measurement of state, hazard, and quality trajectories.
- Enables the paper to discuss how different ‘age’ constructs change policy evaluation without tying to a specific model.
- Provides language for validation: assessing whether interventions shift aging rate parameters vs. merely short-term outcomes.

### Where it plugs into the draft paper
- Methods + measurement section: what must be measured to run a flow-based appraisal system.
- Discussion of model risk: how measurement assumptions can Goodhart the objective.

### BibTeX
```bibtex
@misc{strulik2021measuringageing,
  author       = {Strulik, Holger},
  title        = {Measuring Ageing},
  year         = {2021},
  note         = {Handbook chapter draft (version July 26, 2021)},
}
```

---

## melov2016geroscience

**Geroscience Approaches to Increase Healthspan and Slow Aging** (2016)

- **PDF:** `sources/melov_2016_geroscience_approaches_healthspan.pdf` (0.85 MB)
- **Source URL:** https://f1000research.com/articles/5-785/pdf
- **Tags:** biomedical engineering, healthspan, translation

### Summary
- Review of the geroscience paradigm: targeting aging processes to delay multiple chronic diseases simultaneously.
- Highlights major intervention directions and translational challenges (biomarkers, trials, heterogeneity).
- Frames healthspan improvement as a systemic objective rather than disease-by-disease treatment.

### Intersection with QALY flow
- Provides translational context: the flow objective values sustained health quality over time, matching the healthspan framing.
- Supports the idea of evaluating interventions by long-run steady improvement rather than lifetime-sum with a fixed endpoint.
- Supplies practical constraints for the paper’s governance proposals: trials, biomarkers, and monitoring are the measurement substrate for any flow metric.

### Where it plugs into the draft paper
- Biomedical engineering section on healthspan and the system-level ‘maintenance medicine’ agenda.
- Policy implications: how to structure R&D incentives and regulatory pathways to favor sustained improvements.

### BibTeX
```bibtex
@article{melov2016geroscience,
  author       = {Melov, Simon},
  title        = {Geroscience Approaches to Increase Healthspan and Slow Aging},
  journal      = {F1000Research},
  year         = {2016},
  volume       = {5},
  pages        = {785},
  doi          = {10.12688/f1000research.7583.1},
}
```

---

## moffitt2020behavioralsocial

**Behavioral and Social Research to Accelerate the Geroscience Translation Agenda** (2020)

- **PDF:** `sources/moffitt_2020_behavioral_social_science_geroscience.pdf` (0.34 MB)
- **Source URL:** https://moffittcaspi.trinity.duke.edu/sites/moffittcaspi.trinity.duke.edu/files/publication-uploads/Moffitt%2520BSRinGeroscience%2520ARR2020.pdf
- **Tags:** societal management, behavioral science, implementation

### Summary
- Argues that behavioral and social factors are essential for translating geroscience into real-world health benefits.
- Discusses adherence, environment, inequality, and policy levers as determinants of realized outcomes.
- Provides a translation agenda: measurement, implementation science, and population-level interventions.

### Intersection with QALY flow
- Reinforces that optimizing a flow metric requires implementation capacity: adherence and behavior can dominate steady-state outcomes.
- Supports treating QALY flow as a system-level objective spanning biology and society—interventions include social and behavioral ‘maintenance’ layers.
- Motivates governance mechanisms (Goodhart mitigation, surveillance, equity) because behavior-mediated feedback loops can distort measured flow.

### Where it plugs into the draft paper
- Societal management section: implementation science and behavioral levers in flow optimization.
- Equity and distribution section: social determinants as constraints/inputs.

### BibTeX
```bibtex
@article{moffitt2020behavioralsocial,
  author       = {Moffitt, Terrie E.},
  title        = {Behavioral and Social Research to Accelerate the Geroscience Translation Agenda},
  journal      = {Ageing Research Reviews},
  year         = {2020},
  volume       = {63},
  pages        = {101146},
  doi          = {10.1016/j.arr.2020.101146},
}
```

---

## crimmins2020socialhallmarks

**Social Hallmarks of Aging: Suggestions for Geroscience Research** (2020)

- **PDF:** `sources/crimmins_2020_social_hallmarks_of_aging.pdf` (3.95 MB)
- **Source URL:** https://moffittcaspi.trinity.duke.edu/sites/moffittcaspi.trinity.duke.edu/files/site-images/Crimmins_2020_Geroscience.pdf
- **Tags:** societal management, aging, social determinants

### Summary
- Defines social ‘hallmarks’ that influence aging trajectories: education, inequality, stress, environment, and other determinants.
- Connects social factors to biological aging pathways and population heterogeneity.
- Suggests research priorities for integrating social context into geroscience.

### Intersection with QALY flow
- Extends the maintenance framing beyond biology: steady-state welfare depends on social environment and distribution, not only medical interventions.
- Provides a principled rationale for treating social policy as ‘health maintenance engineering’ (upstream interventions that stabilize quality trajectories).
- Supports multi-level modeling: QALY flow can be defined at individual, subgroup, and system levels.

### Where it plugs into the draft paper
- Societal management section: social maintenance, structural interventions, and equity-aware flow governance.
- Case study vignette: how upstream determinants affect long-run quality trajectories.

### BibTeX
```bibtex
@article{crimmins2020socialhallmarks,
  author       = {Crimmins, Eileen M.},
  title        = {Social Hallmarks of Aging: Suggestions for Geroscience Research},
  journal      = {Ageing Research Reviews},
  year         = {2020},
  volume       = {63},
  pages        = {101136},
  doi          = {10.1016/j.arr.2020.101136},
}
```

---

## marugan2024rlmaintenance

**A Reinforcement Learning Agent for Maintenance of Deteriorating Systems with Increasingly Imperfect Repairs** (2024)

- **PDF:** `sources/marugan_2025_rl_maintenance_imperfect_repairs.pdf` (1.16 MB)
- **Source URL:** https://arxiv.org/pdf/2505.20725.pdf
- **Tags:** biomedical engineering, maintenance, control

### Summary
- Models maintenance decision-making for deteriorating systems where repairs become less effective over time (increasingly imperfect).
- Uses reinforcement learning to adapt maintenance policies under uncertainty and degradation dynamics.
- Provides an engineering template for optimizing long-run performance when interventions have diminishing returns.

### Intersection with QALY flow
- Serves as an engineering analogue for ‘maintenance medicine’: when repair efficacy decays, optimal policy balances preventive action, replacement, and risk.
- Supports the paper’s claim that flow governance is fundamentally a control problem over stochastic degradation and repair cycles.
- Helps illustrate math-agnostic lessons: diminishing returns, policy adaptation, and monitoring are essential even if the exact flow objective is reworked.

### Where it plugs into the draft paper
- Biomedical engineering/control section: maintenance policy design under imperfect repair dynamics.
- Methods vignette: why average-reward criteria (vs. discounted) fit indefinite-horizon maintenance.

### BibTeX
```bibtex
@article{marugan2024rlmaintenance,
  author       = {Pliego Marug{\'a}n, Alberto and Pinar-P{\'e}rez, Jes{\'u}s Mar{\'i}a and Garc{\'i}a M{\'a}rquez, Fausto Pedro},
  title        = {A Reinforcement Learning Agent for Maintenance of Deteriorating Systems with Increasingly Imperfect Repairs},
  journal      = {Reliability Engineering \& System Safety},
  year         = {2024},
  note         = {Preprint available as arXiv:2505.20725 (v1, 2025)},
}
```

---

## sigman2018renewalreward

**Some Basic Renewal Theory: The Renewal Reward Theorem** (2018)

- **PDF:** `sources/sigman_2018_renewal_reward_theorem_notes.pdf` (0.18 MB)
- **Source URL:** https://www.columbia.edu/~ks20/4106-18-Fall/Notes-RRT.pdf
- **Tags:** math foundations, renewal, regeneration

### Summary
- Lecture notes introducing renewal processes and the renewal reward theorem (long-run reward rate equals expected reward per expected inter-renewal time).
- Includes core results (elementary renewal theorem) and standard applications (inspection paradox).
- Offers a clean, widely used mathematical basis for steady-state rates in regenerative systems.

### Intersection with QALY flow
- Supports the paper’s structural ‘cycle’ intuition without tying to any particular modeling choices: the key object is the long-run rate in a regenerative process.
- Provides a neutral foundation for discussing robustness: small cycle-level changes map cleanly to long-run rates under mild conditions.
- Enables math-agnostic exposition: the paper can cite renewal reward as a canonical justification for rate-based evaluation.

### Where it plugs into the draft paper
- Technical background section: regenerative interpretation and why per-time rates are natural for indefinite horizons.
- Appendix: minimalist statement of the renewal reward principle underpinning flow metrics.

### BibTeX
```bibtex
@misc{sigman2018renewalreward,
  author       = {Sigman, Karl},
  title        = {Some Basic Renewal Theory: The Renewal Reward Theorem},
  year         = {2018},
  note         = {Lecture notes},
}
```

---

## gallager2011renewalprocesses

**Discrete Stochastic Processes, Chapter 4: Renewal Processes (MIT OCW 6.262)** (2011)

- **PDF:** `sources/mit_ocw_2011_discrete_stochastic_processes_ch4_renewal.pdf` (1.38 MB)
- **Source URL:** https://ocw.mit.edu/courses/6-262-discrete-stochastic-processes-spring-2011/931ffa0940899c27f34b71ad64fd2bb0_MIT6_262S11_chap04.pdf
- **Tags:** math foundations, renewal, pedagogy

### Summary
- Textbook-style chapter covering renewal processes, renewal equations, and long-run behavior.
- Provides additional intuition and derivations complementary to short lecture notes.
- Useful as a second reference for definitions and standard results.

### Intersection with QALY flow
- Reinforces the regenerative-rate viewpoint and supplies terminology that can be borrowed for exposition without depending on a specific flow formula.
- Supports explaining renewal intuition to a multidisciplinary audience (policy, engineering, futurism).

### Where it plugs into the draft paper
- Background/appendix reference for renewal definitions and long-run limits.
- Optional reading pointer for readers from policy or philosophy backgrounds.

### BibTeX
```bibtex
@misc{gallager2011renewalprocesses,
  author       = {Gallager, Robert},
  title        = {Discrete Stochastic Processes, Chapter 4: Renewal Processes},
  year         = {2011},
  note         = {MIT OpenCourseWare 6.262},
}
```

---

## feinberg2012averagecostmdp

**Average-Cost Markov Decision Processes with Weakly Continuous Transition Probabilities (arXiv:1202.4122)** (2012)

- **PDF:** `sources/feinberg_2012_average_cost_mdps_weakly_continuous.pdf` (0.27 MB)
- **Source URL:** https://arxiv.org/pdf/1202.4122
- **Tags:** control theory, average cost, infinite horizon

### Summary
- Provides sufficient conditions for existence of stationary optimal policies for average-cost MDPs with general (Borel) state/action spaces and weak continuity.
- Handles unbounded one-step costs and non-compact action sets under suitable conditions.
- Connects average-cost criteria to stability/existence arguments relevant for long-run optimization.

### Intersection with QALY flow
- Supplies a rigorous ‘control’ counterpart to renewal-reward intuition: average-rate objectives are standard in MDP theory under indefinite horizons.
- Supports the paper’s argument that flow optimization is mathematically well-founded beyond toy models, while still allowing the paper to remain agnostic on exact primitives.
- Enables a stable claim: long-run rate objectives have existence and sensitivity theory under transparent assumptions.

### Where it plugs into the draft paper
- Technical background section: average-cost control as the broader mathematical home for flow objectives.
- Appendix: pointers for readers wanting formal existence conditions.

### BibTeX
```bibtex
@misc{feinberg2012averagecostmdp,
  author       = {Feinberg, Eugene A. and Kasyanov, Pavlo O. and Zadoianchuk, Nina V.},
  title        = {Average-Cost Markov Decision Processes with Weakly Continuous Transition Probabilities},
  year         = {2012},
  note         = {arXiv:1202.4122},
}
```

---

## boucherie2023averagecostnotes

**Average Cost Markov Decision Processes: Policy-Iteration and Value-Iteration (Addendum)** (2023)

- **PDF:** `sources/boucherie_2023_average_cost_mdp_policy_value_iteration_notes.pdf` (0.22 MB)
- **Source URL:** https://www.utwente.nl/en/eemcs/sor/boucherie/Operations%20Research/104operationsresearchaddendummdp.pdf
- **Tags:** control theory, algorithms, policy iteration

### Summary
- Short addendum explaining policy iteration and value iteration methods for finite-state long-run average reward/cost MDPs.
- Positions these algorithms as alternatives to linear programming approaches.
- Useful for readers who want computational intuition for how flow-optimal policies are found.

### Intersection with QALY flow
- Provides algorithmic intuition for ‘governing’ a flow objective: policies can be improved iteratively, with monitoring and model updates analogous to value updates.
- Supports the paper’s societal-management theme: optimization is an ongoing loop rather than a one-shot calculation.

### Where it plugs into the draft paper
- Methods vignette: how institutions could update policy as evidence changes (iterative optimization).
- Appendix: algorithm references for the technically inclined.

### BibTeX
```bibtex
@misc{boucherie2023averagecostnotes,
  author       = {Boucherie, Richard J. and others},
  title        = {Average Cost Markov Decision Processes: Policy-Iteration and Value-Iteration},
  year         = {2023},
  note         = {Addendum to Operations Research: Introduction to Models and Methods (PDF creation date: 2023-04-01)},
}
```

---

## tadepalli1998average

**Model-based Average Reward Reinforcement Learning** (1998)

- **PDF:** `sources/tadepalli_ok_1998_model_based_average_reward_rl.pdf` (0.63 MB)
- **Source URL:** https://web.engr.oregonstate.edu/~tadepall/papers/arl-aij.pdf
- **Tags:** learning, average reward, control

### Summary
- Develops model-based reinforcement learning methods for optimizing undiscounted average reward, contrasting with discounted RL.
- Highlights cases where discounted criteria misalign with long-run rate objectives and can yield suboptimal policies.
- Demonstrates algorithmic approaches and exploration strategies for average-reward settings.

### Intersection with QALY flow
- Supports the conceptual point that indefinite-horizon optimization should match the criterion: average-rate objectives behave differently than discounted sums.
- Provides a template for ‘adaptive governance’: learning-based policy updates under uncertainty when the system changes.
- Enables discussion of exploration/experimentation: how to gather evidence without sacrificing long-run performance.

### Where it plugs into the draft paper
- Methods/implementation section: learning and adaptation in flow-governed systems.
- Discussion of experimentation design and online monitoring.

### BibTeX
```bibtex
@misc{tadepalli1998average,
  author       = {Tadepalli, Prasad and Ok, DoKyeong},
  title        = {Model-based Average Reward Reinforcement Learning},
  year         = {1998},
  note         = {Technical report / manuscript (PDF dated January 13, 1998)},
}
```

---

## wang2023robustaverage

**Robust Average-Reward Markov Decision Processes** (2023)

- **PDF:** `sources/wang_2023_robust_average_reward_mdps.pdf` (0.62 MB)
- **Source URL:** https://www.acsu.buffalo.edu/~szou3/conference/aaai2023.pdf
- **Tags:** robustness, uncertainty, control

### Summary
- Studies average-reward MDPs under transition uncertainty, focusing on worst-case performance over an uncertainty set.
- Develops methods and theoretical results for robust average-reward optimization.
- Addresses a gap in robust-control literature that historically focused more on discounted settings.

### Intersection with QALY flow
- Directly informs how QALY flow should be governed under model uncertainty: robust optimization and safety margins become central design features.
- Supports presenting the framework as ‘future-proof’: even if details change, robustness to misspecification is a durable requirement.
- Connects to societal management: choose policies that perform well under adversarial or worst-case deviations (regulatory, safety, or tail risks).

### Where it plugs into the draft paper
- Risk/robustness section: model uncertainty, worst-case analysis, and safety constraints.
- Design principle: optimize a flow metric subject to robustness and monitoring.

### BibTeX
```bibtex
@misc{wang2023robustaverage,
  author       = {Wang, Yue and Velasquez, Alvaro and Atia, George and Prater-Bennette, Ashley and Zou, Shaofeng},
  title        = {Robust Average-Reward Markov Decision Processes},
  year         = {2023},
  note         = {Preprint PDF},
}
```

---

## nist2012sp80030

**Guide for Conducting Risk Assessments (NIST SP 800-30 Rev. 1)** (2012)

- **PDF:** `sources/nist_2012_sp800_30r1_risk_assessments.pdf` (0.83 MB)
- **Source URL:** https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-30r1.pdf
- **Tags:** risk management, process, societal management

### Summary
- Provides a structured process for risk assessment: prepare, assess, communicate, and maintain.
- Defines key concepts (threat sources/events, vulnerabilities, likelihood, impact) and how to integrate assessments into organizational decision-making.
- Emphasizes continuous monitoring and iterative updating of risk assessments.

### Intersection with QALY flow
- Supports the paper’s claim that flow optimization must be paired with a risk-management lifecycle; tail risks and catastrophic events directly affect long-run person-time outcomes.
- Provides governance scaffolding: risk assessment is a process, not a single number—mirrors how flow estimates must be maintained over time.
- Enables practical recommendations (monitoring, reporting, risk tolerances) for institutions using steady-state metrics.

### Where it plugs into the draft paper
- Societal management section: operationalizing catastrophe-rate control, monitoring, and decision thresholds.
- Appendix: mapping between risk-assessment workflow and flow-governed policy updates.

### BibTeX
```bibtex
@techreport{nist2012sp80030,
  author       = {{National Institute of Standards and Technology}},
  title        = {Guide for Conducting Risk Assessments},
  institution  = {National Institute of Standards and Technology},
  year         = {2012},
  type         = {NIST Special Publication},
  number       = {800-30 Revision 1},
}
```
