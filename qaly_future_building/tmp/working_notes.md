# Working Notes: future_building_new.tex

## Date: 2026-02-06

## Problem with the current draft
- Reads like a technical report, not an ideas paper
- No life, no energy, no "oh this is cool" feeling
- Overly structured around governance jargon (primitives, stacks, layers)
- Treats the reader as a bureaucrat, not a curious thinker
- Cites Goldman paper (which is the core paper in the same ensemble — must avoid)
- Too many bullet-pointed lists that read like powerpoint slides

## What QALY flow actually IS (intuitive)
- Instead of asking "how many total quality-adjusted life years does someone get?" (a sum),
  QALY flow asks "how much quality-of-life is this person experiencing per unit time, on average?" (a rate)
- It's like the difference between asking "how many miles will this car ever drive?" vs.
  "how many miles per gallon does it get right now?"
- Under indefinite lifespans, the sum becomes meaningless (it's infinite or undefined),
  but the rate remains perfectly well-defined and useful
- The rate naturally captures: quality while running, maintenance burden, and crash risk
- Key properties: horizon-invariant, bounded, interpretable as cross-sectional welfare

## Tone targets
- Conversational but intellectually honest
- Use vivid analogies (cars, buildings, infrastructure, gardens)
- Ask questions that draw readers in
- Show genuine excitement about the ideas without overclaiming
- Let the reader feel smart for following along
- Short paragraphs, varied rhythm
- Avoid: "governance stack", "primitive", "anti-Goodhart" (use plain language)

## Core narrative arc
1. HOOK: What happens when "how long will you live?" stops being the right question?
2. THE SHIFT: From lifetime sums to ongoing rates — a surprisingly simple idea with big implications
3. THREE WORLDS that need this idea:
   a. Futurism — if the future might be enormous, keeping it accessible matters more than any single gain
   b. Biomedical engineering — aging biology already thinks in terms of maintenance, not cure
   c. Societal management — any metric used at scale will be gamed; how to make this one robust
4. DESIGN PRINCIPLES: what a "QALY-flow society" looks like (fun, practical, concrete)
5. HONEST GAPS: what we don't know and why that's exciting rather than disqualifying
6. CLOSE: why this is worth building even if the math changes

## Sources to use (NO Goldman)
From references.bib:
- bostrom2003astronomicalwaste — speed vs safety tradeoff
- bostrom2013existentialriskprevention — existential risk as priority
- greaves2021stronglongtermism — the case for caring about the long run
- lopezotin2013hallmarks — hallmarks of aging (the canonical framework)
- lopezotin2023expandinghallmarks — expanded hallmarks
- finkelstein2006engineeringreliability — reliability engineering + aging
- melov2016geroscience — geroscience approaches
- moffitt2020behavioralsocial — behavioral/social factors in aging
- crimmins2020socialhallmarks — social hallmarks
- stumborg2022goodharts — Goodhart's law and metric gaming
- asaria2013distributionalcea — distributional cost-effectiveness
- hmtreasury2026greenbook — Green Book (appraisal practice)
- hmtreasury2026discounting — discounting guidance
- nist2012sp80030 — risk assessment process
- who2015climateresilient — climate-resilient health systems
- strulik2021measuringageing — measuring aging
- marugan2024rlmaintenance — RL for maintenance
- wang2023robustaverage — robust average reward MDPs
- sigman2018renewalreward — renewal reward theorem
- gallager2011renewalprocesses — renewal processes
- feinberg2012averagecostmdp — average cost MDPs
- boucherie2023averagecostnotes — average cost algorithms
- tadepalli1998average — average reward RL

## Key principle: math agnosticism
- QALY flow is presented as a CONCEPT not a formula
- The paper should survive if the mathematical construction is completely reworked
- Reference the mathematical tradition (renewal theory, average-cost control) but don't depend on it
- The value is in the IDEA that rate-based evaluation is the right paradigm for indefinite horizons

## Section-by-section plan

### 1. Introduction: "When 'how long' stops being the question"
- Start with a thought experiment: imagine you're designing policy for people who might live 500 years... or 5000... or indefinitely
- The standard QALY (lifetime sum) becomes absurd — infinite or undefined
- But a simple move fixes everything: measure quality per unit time instead
- This paper: that simple move turns out to connect three big conversations that haven't talked to each other enough

### 2. "The rate, not the sum" — what QALY flow is
- Intuitive explanation using everyday analogies
- Why rates are natural when horizons are open-ended (renewal reward intuition)
- What this captures: quality while running + maintenance cost + risk of catastrophe
- Why this is deliberately math-light: the idea matters more than any particular derivation
- Cite renewal theory tradition (Sigman, Gallager) and average-cost control (Feinberg) as the mathematical home

### 3. "Keeping the future open" — the futurist case
- Bostrom: existential risk prevention as priority
- Greaves & MacAskill: the long future dominates
- Key insight: under QALY flow, "safety" and "quality" are the same conversation
- Bostrom's astronomical waste: speed vs safety isn't a tradeoff, it's a portfolio problem
- QALY flow translates philosophical stakes into operational variables
- Pandemic preparedness, infrastructure safety, coordination capacity — all become "flow stabilizers"

### 4. "Your body is a machine (and that's a good thing)" — the biomedical engineering case
- López-Otín hallmarks: aging has identifiable mechanisms — like subsystem failure modes
- Finkelstein: reliability engineering concepts applied to biology
- Melov: geroscience treats aging itself, not disease-by-disease
- The engineering frame: health is uptime, medicine is maintenance, prevention is quality assurance
- Moffitt + Crimmins: social/behavioral factors are part of the "control system"
- Under QALY flow, the question becomes: what maintenance policy maximizes sustained quality?
- Marugán: even in engineering, repairs become less effective over time — adaptive policy matters

### 5. "Measuring without destroying" — the societal management case
- Stumborg: Goodhart's law — when a measure becomes a target, it ceases to be a good measure
- Any QALY-flow metric deployed at scale WILL be gamed
- Solution: measurement as a SYSTEM, not a number
  - Strulik: how to measure aging properly
  - NIST: risk assessment as ongoing process
  - HM Treasury Green Book: appraisal as institutional practice
- Asaria: distributional CEA — who benefits matters, not just how much
- WHO: resilience means the system survives shocks and keeps delivering
- HM Treasury discounting: QALY flow can coexist with conventional tools

### 6. Design principles (light, practical, fun)
- Five principles stated plainly, each with a concrete intuition
- 1. Optimize quality while keeping the lights on (continuation constraints)
- 2. Treat medicine like infrastructure maintenance
- 3. Design metrics that survive being gamed
- 4. Make fairness choices visible and revisable
- 5. Build evaluation into the ongoing rhythm of governance

### 7. What we don't know (and why that's exciting)
- Research questions framed as invitations, not requirements
- Each one is a "wouldn't it be cool if..." not a "we must..."
- Measurement under feedback, robust governance, portfolio design, equity, deployment of maintenance medicine

### 8. Conclusion
- Short, punchy
- The math might change but the idea won't
- Rate-based thinking for indefinite horizons is the right lens
- Building the future means maintaining it

## Author/ORCID/date from core.tex
- \author{Daniel S. Goldman \orcidlink{0000-0003-2835-3521}}
- \date{\today}
- Need orcidlink package

## Final status (2026-02-06)
- Paper written: future_building_new.tex
- 23 citations used, all present in references.bib
- Goldman citation: NOT used (only appears as author name)
- Compiles cleanly: 10 pages, no warnings, no errors
- LaTeX build output: build/future_building_new.pdf
- Uses \today for date (matches core.tex convention)
- Uses orcidlink package for ORCID (matches core.tex)
- Math-agnostic: no equations, no formal definitions
- Tone: conversational, analogy-driven, fun, intellectually honest
- Structure: hook → concept → futurism → biomedical → societal management → principles → open questions → conclusion
