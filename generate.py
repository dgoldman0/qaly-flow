#!/usr/bin/env python3

questions = [
    # Q1 - GP,⬤⬤⬤,███
    "What is a Quality-Adjusted Life Year, and why has it become central to how administrative systems allocate healthcare resources?",
    
    # Q2 - GP,⬤⬤⬤,███
    "Why do traditional QALY calculations fail when human lifespans become potentially unbounded?",
    
    # Q3 - GP,⬤⬤⬤,██░
    "When researchers describe 'unbounded lifespan,' do they mean literal immortality or something more nuanced about biological limits?",
    
    # Q4 - GP,⬤⬤◯,██░
    "Does the QALY flow framework predict that death from aging will become preventable, or is it asking a conditional 'what if' question?",
    
    # Q5 - GP,⬤⬤⬤,███
    "Why does discount-rate sensitivity undermine confidence in cost-effectiveness analysis as lifespans extend beyond traditional horizons?",
    
    # Q6 - GP,⬤⬤⬤,███
    "Why does the QALY flow framework use terminology like 'maintenance' and 'repair' for health—is it reducing humans to machines?",
    
    # Q7 - GP,⬤⬤⬤,███
    "How does the QALY flow framework distinguish between total years lived and years lived in good health?",
    
    # Q8 - GP,⬤⬤◯,█░░
    "Does the QALY flow framework assume that everyone would want to live indefinitely if given the option?",
    
    # Q9 - GP,⬤⬤⬤,███
    "In the regenerative population model, what distinguishes a 'catastrophic failure' from conditions that can be repaired?",
    
    # Q10 - GP,⬤⬤◯,██░
    "Why should policymakers develop frameworks for unbounded lifespans now, before longevity technologies mature?",
    
    # Q11 - MD,⬤◯◯,█░░
    "What specific biomedical advances—in senescence, telomeres, or organ regeneration—would make the QALY flow framework indispensable?",
    
    # Q12 - PM,⬤⬤◯,██░
    "Can the QALY flow framework evaluate today's health policies, or is it only relevant for hypothetical long-lived populations?",
    
    # Q13 - MD,⬤◯◯,█░░
    "What do longevity researchers say about when unbounded human lifespans might become biologically achievable?",
    
    # Q14 - MD,⬤⬤⬤,███
    "Does the QALY flow framework require assuming that all diseases will eventually become curable?",
    
    # Q15 - MD,⬤⬤⬤,███
    "How does the QALY flow framework's state-transition structure encode whether a condition is repairable or permanently irreversible?",
    
    # Q16 - MD,⬤⬤⬤,██░
    "What differentiates an absorbing 'catastrophic failure' state from 'repairable degradation' in the Markov health model?",
    
    # Q17 - MD,⬤⬤◯,██░
    "Which current medical conditions—dementia, metastatic cancer, severe brain injury—would count as 'irreversible harm states' in the QALY flow model?",
    
    # Q18 - MD,⬤⬤◯,██░
    "Does the QALY flow framework take a position on whether aging should be classified as a disease or as a natural process?",
    
    # Q19 - GP,⬤◯◯,█░░
    "How could cryonics or suspended animation be represented within the QALY flow framework's state-transition structure?",
    
    # Q20 - PH,⬤⬤⬤,███
    "Does the QALY flow framework's fourth axiom assume that everyone prefers continued existence to death?",
    
    # Q21 - PM,⬤⬤⬤,███
    "Why does the well-posedness axiom require that every policy's value be a finite real number rather than infinity?",
    
    # Q22 - HE,⬤⬤⬤,███
    "What does 'Lipschitz stability' guarantee about how small parameter changes affect QALY flow estimates?",
    
    # Q23 - HE,⬤⬤⬤,███
    "Can you demonstrate a policy scenario where summing undiscounted QALYs over infinite time violates the well-posedness axiom?",
    
    # Q24 - HE,⬤⬤⬤,███
    "How does QALY flow's ratio structure differ from discounting or fixed horizons as methods for achieving finite policy values?",
    
    # Q25 - MA,⬤⬤⬤,███
    "Is well-posedness merely a mathematical convenience, or is it essential for QALY flow to function as a decision-making tool?",
    
    # Q26 - PM,⬤⬤⬤,███
    "Why should health policy evaluation avoid dependence on an arbitrary terminal time horizon?",
    
    # Q27 - PM,⬤⬤◯,██░
    "If governments must budget in finite cycles, how can QALY flow's horizon-invariant criterion still guide resource allocation?",
    
    # Q28 - HE,⬤⬤⬤,███
    "How do fixed 30- to 50-year evaluation horizons in current health technology assessment create policy distortions?",
    
    # Q29 - PM,⬤⬤⬤,███
    "How does the renewal-reward theorem enable policy decisions without requiring a fixed endpoint for evaluation?",
    
    # Q30 - PM,⬤⬤◯,██░
    "Can QALY flow's infinite-horizon welfare criterion coexist with democratic political cycles and electoral accountability?",
    
    # Q31 - GP,⬤⬤⬤,███
    "What does it mean that health-related welfare 'accrues continuously' rather than existing at discrete points in time?",
    
    # Q32 - MD,⬤⬤⬤,██░
    "Why does the QALY flow framework weight experienced quality of life rather than objective clinical health status?",
    
    # Q33 - HE,⬤⬤⬤,███
    "How do preference-based instruments like EQ-5D translate health states into the 'instantaneous quality' weights the framework requires?",
    
    # Q34 - PH,⬤⬤◯,██░
    "How does the QALY flow framework capture persistent effects like chronic pain or trauma through its state-transition structure?",
    
    # Q35 - PH,⬤⬤◯,██░
    "Can anticipation of future treatment or traumatic memories be incorporated into the QALY flow framework's health state definitions?",
    
    # Q36 - PH,⬤⬤◯,██░
    "Is the QALY flow framework's quality function necessarily committed to hedonism, or can it reflect objective goods and relationships?",
    
    # Q37 - HE,⬤⬤⬤,███
    "How do EQ-5D tariffs and similar instruments provide exactly what the QALY flow framework needs for its quality function?",
    
    # Q38 - PH,⬤⬤⬤,██░
    "Why does Axiom 4 treat death's disvalue as entirely explained by truncating future welfare rather than as intrinsically bad?",
    
    # Q39 - PH,⬤⬤◯,██░
    "Do philosophers who argue death has intrinsic badness beyond deprivation pose a challenge to the QALY flow framework's fourth axiom?",
    
    # Q40 - PH,⬤⬤◯,██░
    "How does the QALY flow framework's fourth axiom implement the philosophical 'deprivation account' of death's badness?",
    
    # Q41 - PH,⬤⬤⬤,███
    "Within the QALY flow framework, is death bad only because it prevents future positive experiences from occurring?",
    
    # Q42 - PH,⬤⬤⬤,███
    "If someone's quality weight is near zero or negative, does the QALY flow framework still treat their death as truncating welfare?",
    
    # Q43 - MD,⬤⬤◯,██░
    "Does the QALY flow framework's population-level focus leave room for respecting individual autonomy in end-of-life decisions?",
    
    # Q44 - MD,⬤◯◯,█░░
    "How would the QALY flow framework represent physician-assisted dying as a state transition and evaluate its welfare implications?",
    
    # Q45 - PH,⬤⬤⬤,███
    "Why does the explicit normativity axiom demand that value judgments in health economics be stated openly rather than hidden in methodology?",
    
    # Q46 - HE,⬤⬤⬤,███
    "How does discounting embed normative judgments about present versus future welfare behind what appears to be neutral methodology?",
    
    # Q47 - HE,⬤⬤⬤,███
    "Does the ongoing debate about discount rate magnitudes miss the deeper question of whether discounting pure welfare is ever justified?",
    
    # Q48 - HE,⬤⬤◯,██░
    "How does NICE's 3.5 percent discount rate function as a contested normative choice rather than a neutral methodological standard?",
    
    # Q49 - PH,⬤⬤◯,██░
    "Beyond discounting, what other normative commitments hide inside seemingly technical choices in health economics?",
    
    # Q50 - PM,⬤◯◯,█░░
    "Does making hidden value judgments explicit in health policy actually lead to different decisions, or just more transparent ones?",
    
    # Q51 - PM,⬤⬤⬤,███
    "What does 'welfare per unit of population time' measure, and how does a QALY flow value of 0.8 translate into practical terms?",
    
    # Q52 - HE,⬤⬤⬤,███
    "Why does maximizing QALY flow differ fundamentally from maximizing total accumulated QALYs over time?",
    
    # Q53 - PM,⬤⬤⬤,███
    "Why is person-time a more stable unit of analysis than counting individuals when populations turn over through birth and death?",
    
    # Q54 - PH,⬤⬤⬤,██░
    "Does the QALY flow framework's aggregation across person-time violate the philosophical principle of 'separateness of persons'?",
    
    # Q55 - PH,⬤⬤⬤,██░
    "In what sense is the QALY flow framework's sixth axiom utilitarian, and can it accommodate non-utilitarian equity concerns?",
    
    # Q56 - MD,⬤⬤◯,██░
    "How does the QALY flow framework's rate-per-person-time structure mirror what epidemiologists already track in public health surveillance?",
    
    # Q57 - PH,⬤⬤⬤,███
    "What does it mean to treat one person's quality-adjusted time as perfectly substitutable for another's in policy evaluation?",
    
    # Q58 - PH,⬤⬤◯,█░░
    "Can the ethical concern about trading off one person's health for another's be addressed within the QALY flow framework?",
    
    # Q59 - PH,⬤⬤⬤,███
    "How does the QALY flow framework justify comparing welfare across different individuals using common quality weights?",
    
    # Q60 - PH,⬤⬤⬤,██░
    "Does the QALY flow framework claim that QALYs are genuinely comparable across people, or just that this is a useful approximation?",
    
    # Q61 - MA,⬤⬤⬤,███
    "What is 'ergodic trajectory convergence,' and why does it make interpersonal welfare comparisons more defensible over long horizons?",
    
    # Q62 - PH,⬤⬤◯,██░
    "Even with ergodic averaging, doesn't each person's individual life experience remain fundamentally unique and incomparable?",
    
    # Q63 - PH,⬤◯◯,█░░
    "Could the QALY flow framework's quality function be redefined to reflect capabilities rather than hedonic experience?",
    
    # Q64 - PH,⬤⬤⬤,███
    "How can prioritarian equity weighting be implemented within the QALY flow framework using concave transformations?",
    
    # Q65 - PH,⬤⬤◯,██░
    "Can special obligations to family members be represented within the QALY flow framework's population-level structure?",
    
    # Q66 - GP,⬤⬤⬤,███
    "What is a 'controlled continuous-time Markov chain,' and how does it model health states, transitions, and treatment effects?",
    
    # Q67 - MA,⬤⬤⬤,███
    "Why does the QALY flow framework use continuous time rather than discrete weekly or monthly time steps?",
    
    # Q68 - MD,⬤⬤◯,██░
    "What dimensions define health states in practical applications—disease status, functional capacity, EQ-5D profiles?",
    
    # Q69 - HE,⬤◯◯,█░░
    "How many distinct health states would a realistic disease-specific or population-level QALY flow model require?",
    
    # Q70 - MA,⬤⬤⬤,███
    "Can the QALY flow framework's mathematical structure handle infinite or continuous health state spaces?",
    
    # Q71 - MA,⬤⬤⬤,██░
    "What is a 'rate kernel' in the Markov transition model, and how are transition rates estimated from epidemiological cohort data?",
    
    # Q72 - MA,⬤⬤◯,██░
    "How can age-dependent disease progression be represented within the QALY flow framework's state-transition structure?",
    
    # Q73 - MA,⬤⬤⬤,███
    "Does the QALY flow framework's stationarity assumption rule out modeling transition rates that change with calendar time?",
    
    # Q74 - MA,⬤⬤⬤,███
    "What is 'non-explosiveness' in continuous-time Markov processes, and why must QALY flow models satisfy this condition?",
    
    # Q75 - MA,⬤⬤⬤,███
    "When are Foster-Lyapunov stability criteria needed to ensure a QALY flow model is mathematically well-posed?",
    
    # Q76 - MD,⬤⬤⬤,███
    "How does the QALY flow framework represent correlated conditions like diabetes and heart disease through product state spaces?",
    
    # Q77 - HE,⬤⬤◯,██░
    "What methods—survival analysis, regression, meta-analysis—are used to estimate transition rates from longitudinal cohort data?",
    
    # Q78 - HE,⬤⬤⬤,███
    "What counts as an 'action' in the QALY flow framework—treatments, screening protocols, public health programs, or all of these?",
    
    # Q79 - PM,⬤⬤⬤,██░
    "Can social determinants of health like housing quality or income support be modeled as policy actions within the QALY flow framework?",
    
    # Q80 - MA,⬤⬤⬤,███
    "What is a 'stationary Markov policy,' and why does it choose actions based only on current state rather than on history or time?",
    
    # Q81 - HE,⬤⬤⬤,███
    "Why does the QALY flow framework focus on stationary policies when some clinical protocols are naturally time-varying?",
    
    # Q82 - HE,⬤◯◯,█░░
    "How would the QALY flow framework need to be extended to handle strategic interactions among patients, providers, and insurers?",
    
    # Q83 - MD,⬤⬤⬤,███
    "How does the QALY flow framework distinguish between preventive interventions that reduce incidence and curative interventions that speed recovery?",
    
    # Q84 - MA,⬤⬤⬤,██░
    "How does the QALY flow optimization change when action spaces become continuous, as with drug dosage selection?",
    
    # Q85 - GP,⬤⬤⬤,███
    "Why does the regenerative population model assume immediate replacement when one person dies?",
    
    # Q86 - PH,⬤⬤⬤,███
    "Does the QALY flow framework's regeneration assumption imply that individual deaths don't matter because replacements arrive?",
    
    # Q87 - MA,⬤⬤⬤,███
    "How realistic is the assumption that successive generations enter with independent, identically distributed health profiles?",
    
    # Q88 - HE,⬤⬤◯,██░
    "What happens to the QALY flow framework if the initial health distribution shifts over time due to demographic change?",
    
    # Q89 - HE,⬤⬤◯,██░
    "How does the QALY flow framework's regenerative structure relate to overlapping generations models in macroeconomics?",
    
    # Q90 - PM,⬤⬤◯,██░
    "Does the QALY flow framework still apply when birth rates decline and populations no longer replace themselves?",
    
    # Q91 - PM,⬤⬤◯,██░
    "How should immigration with distinct health profiles be incorporated into the QALY flow framework's initial distribution?",
    
    # Q92 - MA,⬤⬤⬤,███
    "Is the regeneration-at-death assumption strictly necessary, or merely a convenient device for applying the renewal-reward theorem?",
    
    # Q93 - MA,⬤⬤◯,██░
    "What alternative mathematical approaches could replace the i.i.d. regeneration assumption if successive lives are correlated?",
    
    # Q94 - HE,⬤⬤⬤,███
    "Is QALY flow technically a rate, a ratio, or both—and why does the distinction matter for interpretation?",
    
    # Q95 - PM,⬤⬤⬤,███
    "How should a policymaker interpret a QALY flow value of 0.7 in terms of population health experience?",
    
    # Q96 - MA,⬤⬤⬤,███
    "Why is QALY flow mathematically bounded between zero and one when quality weights are bounded in that interval?",
    
    # Q97 - PM,⬤⬤⬤,███
    "What does 'cost flow' K(π) represent, and how does it translate into annual budget requirements for a health system?",
    
    # Q98 - HE,⬤⬤◯,██░
    "How can QALY flow be converted to monetary terms using willingness-to-pay thresholds?",
    
    # Q99 - PM,⬤◯◯,█░░
    "Should regulators establish minimum acceptable QALY flow thresholds analogous to the £30,000/QALY cost-effectiveness threshold?",
    
    # Q100 - HE,⬤⬤⬤,███
    "How does QALY flow differ from quality-adjusted life expectancy, and when is each measure more appropriate?",
    
    # Q101 - MA,⬤⬤⬤,███
    "What is the renewal-reward theorem, what mathematical tradition does it come from, and why is it foundational for QALY flow?",
    
    # Q102 - GP,⬤⬤⬤,███
    "Can you explain the renewal-reward theorem in plain language without mathematical notation?",
    
    # Q103 - MA,⬤⬤⬤,███
    "What three conditions—i.i.d. cycles, finite expected duration, finite expected reward—must hold for the renewal-reward theorem to apply?",
    
    # Q104 - MA,⬤⬤⬤,███
    "What happens to the QALY flow formula when expected lifespan becomes infinite because mortality approaches zero?",
    
    # Q105 - MA,⬤⬤⬤,███
    "Does the renewal-reward theorem require ergodicity in the traditional Markov chain sense, or is the i.i.d. cycle structure sufficient?",
    
    # Q106 - MA,⬤⬤◯,██░
    "At what rate does the empirical ratio of cumulative quality to time converge to the true QALY flow?",
    
    # Q107 - HE,⬤⬤◯,██░
    "How do convergence rates affect the precision of QALY flow estimates and the computational effort needed?",
    
    # Q108 - MA,⬤⬤⬤,███
    "What is the mathematical proof strategy for the renewal-reward theorem, and how does the strong law of large numbers enter?",
    
    # Q109 - HE,⬤⬤⬤,███
    "Why is the truncated QALY flow definition needed, and when does it coincide with the limiting infinite-horizon definition?",
    
    # Q110 - MA,⬤⬤⬤,███
    "What does it mean intuitively when the upper and lower limits of truncated QALY flow differ?",
    
    # Q111 - MA,⬤⬤⬤,███
    "Under what mathematical conditions do the limsup and liminf of truncated QALY flow agree, ensuring a well-defined limit?",
    
    # Q112 - MA,⬤⬤◯,██░
    "Can you construct a pathological policy example where the upper and lower QALY flow limits genuinely differ?",
    
    # Q113 - HE,⬤⬤⬤,███
    "How does truncation as a method for handling infinite horizons compare mathematically to exponential discounting?",
    
    # Q114 - HE,⬤⬤⬤,███
    "Is truncated QALY flow equivalent to discounted QALYs with a very low discount rate, or do they remain fundamentally different?",
    
    # Q115 - GP,⬤⬤⬤,███
    "What does 'risk neutrality' mean in the context of evaluating health policies by their expected QALY flow?",
    
    # Q116 - HE,⬤⬤⬤,███
    "Why does the base QALY flow framework use expected values without adjustments for outcome variance or tail risk?",
    
    # Q117 - PH,⬤⬤◯,██░
    "Given that people typically prefer certainty, should health policy evaluation incorporate risk aversion rather than risk neutrality?",
    
    # Q118 - MA,⬤⬤⬤,███
    "What mathematical approaches—mean-variance, CVaR, expected utility—can incorporate risk aversion into QALY flow optimization?",
    
    # Q119 - MA,⬤⬤⬤,███
    "When is mean-variance optimization appropriate for risk-adjusted QALY flow, and when does it fail?",
    
    # Q120 - MA,⬤⬤⬤,███
    "What is Conditional Value-at-Risk, and why might it be preferred over variance for evaluating catastrophic health outcomes?",
    
    # Q121 - PM,⬤◯◯,█░░
    "How should policymakers choose the risk aversion parameter λ or the CVaR probability level α?",
    
    # Q122 - PM,⬤⬤◯,██░
    "For which health policy decisions—routine care, pandemics, individual treatment—is risk neutrality a reasonable approximation?",
    
    # Q123 - HE,⬤⬤⬤,███
    "Why might irreversible health states deserve a penalty beyond their current quality weight to capture lost future options?",
    
    # Q124 - HE,⬤⬤⬤,███
    "What is 'option value loss,' and why does entering an irreversible state foreclose benefits from future medical advances?",
    
    # Q125 - PH,⬤⬤◯,█░░
    "Should irreversibility be treated as a continuous penalty that adjusts quality weights or as a hard constraint that prohibits certain transitions?",
    
    # Q126 - HE,⬤◯◯,█░░
    "What empirical methods—surveys, revealed preference, expert judgment—could calibrate the irreversibility penalty parameter κ?",
    
    # Q127 - MD,⬤⬤◯,██░
    "What happens when clinicians disagree about whether a health state is truly irreversible given evolving medical technology?",
    
    # Q128 - PH,⬤◯◯,█░░
    "How do disability rights critiques apply to penalizing transitions into disability states within the QALY flow framework?",
    
    # Q129 - PH,⬤⬤◯,██░
    "Can the distinction between penalizing transitions into irreversible states versus devaluing people currently in those states be maintained in practice?",
    
    # Q130 - GP,⬤⬤⬤,███
    "Why does outcome volatility matter for policy choice even when two policies have identical expected QALY flow?",
    
    # Q131 - MD,⬤⬤◯,██░
    "What sources—disease heterogeneity, treatment response variation, random life events—drive cycle-to-cycle volatility in lifetime quality?",
    
    # Q132 - MD,⬤⬤◯,██░
    "Is Assumption 5's requirement of positive minimum expected lifetime realistic for any human population?",
    
    # Q133 - HE,⬤⬤◯,██░
    "What longitudinal data and statistical methods are needed to estimate the variance of lifetime average quality?",
    
    # Q134 - PH,⬤◯◯,█░░
    "What if some patients are risk-seeking—preferring uncertain hope of full recovery over certain moderate outcomes?",
    
    # Q135 - MA,⬤⬤⬤,███
    "Under what mathematical regularity conditions does an optimal QALY flow policy always exist?",
    
    # Q136 - MA,⬤⬤⬤,███
    "How can optimization over infinitely many possible policies remain computationally tractable?",
    
    # Q137 - MA,⬤⬤⬤,███
    "Why does the finite state-action case yield exact solutions through linear programming or policy iteration?",
    
    # Q138 - MA,⬤⬤⬤,██░
    "What computational methods—policy iteration, value iteration, linear programming—find optimal QALY flow policies?",
    
    # Q139 - MA,⬤⬤⬤,███
    "How does the Charnes-Cooper transformation convert the ratio QALY flow objective into a standard linear program?",
    
    # Q140 - MA,⬤⬤⬤,███
    "What is average-reward dynamic programming, and how does its Bellman equation differ from discounted formulations?",
    
    # Q141 - MA,⬤⬤◯,██░
    "Can reinforcement learning algorithms be applied to find optimal QALY flow policies from simulated or observed trajectories?",
    
    # Q142 - MA,⬤⬤◯,██░
    "How does computational complexity grow with health state space size, and when do approximation methods become necessary?",
    
    # Q143 - MA,⬤⬤◯,██░
    "What approximation techniques—function approximation, state aggregation, simulation-based methods—enable QALY flow optimization for large state spaces?",
    
    # Q144 - PM,⬤⬤⬤,███
    "How should policymakers compare policies when one achieves higher QALY flow but also higher cost flow?",
    
    # Q145 - PM,⬤⬤⬤,██░
    "What is the willingness-to-pay parameter λ, and how do NICE, WHO, and other bodies set its value?",
    
    # Q146 - HE,⬤⬤⬤,██░
    "Besides linear scalarization, what alternative methods—ratio forms, constrained optimization, Pareto frontiers—combine quality and cost?",
    
    # Q147 - MA,⬤⬤⬤,███
    "How does the QALY flow framework handle stochastic costs that vary randomly across patients and over time?",
    
    # Q148 - GP,⬤⬤⬤,███
    "What does 'Lipschitz stability' guarantee about robustness of QALY flow estimates to parameter uncertainty?",
    
    # Q149 - PM,⬤⬤⬤,███
    "Why is stability of policy rankings essential when transition rates and quality weights are estimated with error?",
    
    # Q150 - HE,⬤⬤⬤,███
    "What model pathologies—vanishing cycle length, discontinuous quality functions—could cause instability in QALY flow?",
    
    # Q151 - HE,⬤⬤◯,██░
    "How can analysts verify that Assumptions 4 and 5 (uniform bounds, Lipschitz continuity) hold for their particular model?",
    
    # Q152 - MA,⬤⬤⬤,███
    "What is the proof strategy for Theorem 3 establishing Lipschitz stability of the QALY flow ratio?",
    
    # Q153 - MA,⬤⬤⬤,██░
    "Is the Lipschitz stability bound tight, or is it conservative for typical health models?",
    
    # Q154 - MA,⬤⬤⬤,███
    "What happens to the stability guarantee when the minimum expected cycle length approaches zero?",
    
    # Q155 - HE,⬤⬤◯,██░
    "How does QALY flow stability analysis compare to one-way and probabilistic sensitivity analysis in traditional CEA?",
    
    # Q156 - HE,⬤⬤◯,██░
    "What methods—Monte Carlo simulation, delta method, analytic bounds—propagate parameter uncertainty through QALY flow?",
    
    # Q157 - HE,⬤⬤⬤,██░
    "How does probabilistic sensitivity analysis work within the QALY flow framework, and why does Lipschitz stability make it well-behaved?",
    
    # Q158 - HE,⬤⬤◯,██░
    "Which model parameters—rare event transition rates, long-term quality weights, future technology costs—typically carry the greatest uncertainty?",
    
    # Q159 - HE,⬤◯◯,█░░
    "How can model uncertainty about structural assumptions be handled through model averaging or scenario analysis?",
    
    # Q160 - HE,⬤⬤◯,██░
    "Does the QALY flow framework support value of information analysis to determine whether reducing uncertainty is worthwhile?",
    
    # Q161 - HE,⬤⬤⬤,███
    "How does the 'flow ICER' (incremental cost flow per incremental QALY flow) differ from traditional incremental cost-effectiveness ratios?",
    
    # Q162 - HE,⬤⬤⬤,███
    "What are the units of the flow ICER, and why do they match traditional ICERs despite different underlying calculations?",
    
    # Q163 - HE,⬤⬤⬤,███
    "When can the flow ICER be negative, and why must the signs of numerator and denominator be examined separately?",
    
    # Q164 - PM,⬤⬤⬤,██░
    "How should a policymaker interpret a flow ICER of £20,000 per unit of QALY flow improvement?",
    
    # Q165 - PM,⬤◯◯,█░░
    "Should health technology assessment bodies establish a distinct threshold for acceptable flow ICERs?",
    
    # Q166 - HE,⬤◯◯,█░░
    "Can NICE's existing £20,000–30,000/QALY threshold be applied directly to flow ICER, or does it need recalibration?",
    
    # Q167 - HE,⬤⬤◯,██░
    "Does computing the flow ICER automatically avoid problems with extended dominance in multi-option comparisons?",
    
    # Q168 - PM,⬤⬤⬤,███
    "How can cost flow K(π) be multiplied by population size to assess total budget impact at steady state?",
    
    # Q169 - PM,⬤⬤◯,██░
    "How does the QALY flow framework distinguish between steady-state costs and transitional implementation costs?",
    
    # Q170 - PM,⬤⬤⬤,███
    "What is the relationship between per-person cost flow and aggregate annual health expenditure for a population?",
    
    # Q171 - HE,⬤⬤◯,██░
    "How should capital costs with multi-year useful lives be annualized for inclusion in the cost flow calculation?",
    
    # Q172 - PM,⬤⬤◯,██░
    "What normative principles—equal treatment, health need, social deprivation—might guide assignment of equity weights to different population groups?",
    
    # Q173 - PH,⬤◯◯,█░░
    "Should equity weights prioritize groups by current health status, income level, capability deprivation, or some combination?",
    
    # Q174 - PH,⬤⬤◯,██░
    "How does the 'fair innings' argument translate into age-dependent equity weights within the QALY flow framework?",
    
    # Q175 - PH,⬤⬤◯,██░
    "How can the QALY flow framework address intersectional health inequalities by defining groups along multiple dimensions simultaneously?",
    
    # Q176 - HE,⬤⬤⬤,███
    "How does the QALY flow framework accommodate group-specific quality functions when different populations experience health states differently?",
    
    # Q177 - HE,⬤⬤⬤,███
    "What does inequality-averse social welfare aggregation with a concave transformation accomplish?",
    
    # Q178 - PH,⬤◯◯,█░░
    "What considerations guide the choice among utilitarian, prioritarian, egalitarian, and Rawlsian social welfare functions?",
    
    # Q179 - PH,⬤⬤⬤,███
    "How can Rawlsian maximin be implemented within the QALY flow framework by maximizing the worst-off group's flow?",
    
    # Q180 - PM,⬤⬤⬤,██░
    "What is a 'minimum acceptable QALY flow' constraint, and who should set the threshold through deliberative processes?",
    
    # Q181 - LE,⬤◯◯,█░░
    "Could international human rights law's 'right to health' be operationalized as a minimum acceptable QALY flow threshold?",
    
    # Q182 - PH,⬤⬤⬤,███
    "Does the QALY flow framework's undiscounted infinite horizon treat future generations equally with current ones?",
    
    # Q183 - HE,⬤⬤◯,██░
    "How should equity weights be adjusted when population groups grow at different rates?",
    
    # Q184 - PH,⬤⬤◯,██░
    "What happens to the QALY flow framework if future generations value health states differently than current populations?",
    
    # Q185 - PM,⬤◯◯,█░░
    "Does the QALY flow framework's emphasis on sustainable steady-state health conflict with or support environmental sustainability?",
    
    # Q186 - PH,⬤⬤⬤,██░
    "Is the QALY flow framework fundamentally welfarist, or can it incorporate non-welfarist constraints and values?",
    
    # Q187 - PH,⬤⬤◯,██░
    "Can the quality function be calibrated to reflect objective list theories of well-being rather than subjective experience?",
    
    # Q188 - PH,⬤⬤◯,██░
    "How do preference satisfaction theories of well-being map onto the QALY flow framework's quality function?",
    
    # Q189 - PH,⬤⬤◯,██░
    "Does the QALY flow framework's focus on experienced health states undervalue achievements and life projects?",
    
    # Q190 - PH,⬤◯◯,█░░
    "How do Derek Parfit's arguments about personal identity support the QALY flow framework's population-level perspective?",
    
    # Q191 - PH,⬤◯◯,█░░
    "Could the QALY flow framework evaluate welfare for digital minds uploaded to computational substrates?",
    
    # Q192 - PH,⬤⬤◯,██░
    "Does the QALY flow framework presuppose the psychological continuity theory of personal identity?",
    
    # Q193 - PH,⬤⬤◯,█░░
    "If the person living in 200 years shares no memories with you today, do those distant QALYs belong to 'you' in any meaningful sense?",
    
    # Q194 - PH,⬤◯◯,█░░
    "Does extreme longevity across centuries intensify philosophical puzzles about whether personal identity can persist?",
    
    # Q195 - PH,⬤⬤◯,██░
    "Should QALYs accruing to psychologically distant future selves be discounted based on reduced psychological connectedness?",
    
    # Q196 - PH,⬤◯◯,█░░
    "How should the QALY flow framework handle major psychological discontinuities like complete amnesia or personality transformation?",
    
    # Q197 - PH,⬤⬤⬤,███
    "Does the QALY flow framework assume that continued existence is always preferable to death?",
    
    # Q198 - PH,⬤⬤◯,██░
    "When someone rationally prefers death to continued low-quality existence, how does the QALY flow framework represent this?",
    
    # Q199 - LE,⬤⬤◯,██░
    "Can the QALY flow framework incorporate a 'right to die' as a constraint rather than just modeling voluntary death transitions?",
    
    # Q200 - HE,⬤⬤⬤,███
    "How does the QALY flow framework represent health states worse than death through negative quality weights?",
    
    # Q201 - HE,⬤⬤⬤,███
    "Is the quality function permitted to assign negative values, and what empirical evidence supports this for severe suffering states?",
    
    # Q202 - HE,⬤⬤◯,██░
    "How does the QALY flow framework relate to value of statistical life estimates used in regulatory cost-benefit analysis?",
    
    # Q203 - PH,⬤⬤◯,██░
    "Does the QALY flow framework avoid or reproduce Derek Parfit's 'repugnant conclusion' about large low-quality populations?",
    
    # Q204 - PH,⬤⬤◯,██░
    "Does the QALY flow framework's regeneration assumption imply that adding new lives is intrinsically good, neutral, or irrelevant?",
    
    # Q205 - PH,⬤⬤⬤,███
    "How does QALY flow relate to the debate between total utilitarianism and average utilitarianism about population welfare?",
    
    # Q206 - PH,⬤⬤⬤,██░
    "Is the QALY flow framework neutral between extending existing lives and creating new ones, or does it favor one over the other?",
    
    # Q207 - PH,⬤◯◯,█░░
    "How does the QALY flow framework's population-level focus avoid the philosophical 'non-identity problem'?",
    
    # Q208 - HE,⬤⬤⬤,███
    "Why can't we simply use discounted QALYs with a very low discount rate instead of adopting the QALY flow framework?",
    
    # Q209 - MA,⬤⬤⬤,███
    "What discount rate would make discounted QALY analysis equivalent to QALY flow, and why is this limit mathematically singular?",
    
    # Q210 - HE,⬤⬤⬤,██░
    "Does the QALY flow framework make discounting obsolete, or do discounting and QALY flow serve different purposes?",
    
    # Q211 - PH,⬤⬤◯,██░
    "What if society genuinely exhibits pure time preference—valuing near-term welfare more simply because it's sooner?",
    
    # Q212 - HE,⬤⬤◯,██░
    "How does behavioral evidence of hyperbolic discounting complicate the QALY flow framework's assumption of temporal neutrality?",
    
    # Q213 - HE,⬤⬤◯,██░
    "Can the QALY flow framework be combined with a small positive discount rate to create a hybrid approach?",
    
    # Q214 - HE,⬤⬤⬤,███
    "How does QALY flow relate to Health-Adjusted Life Expectancy (HALE) as reported by WHO and national health agencies?",
    
    # Q215 - HE,⬤⬤◯,██░
    "Can QALY flow estimates be computed from existing HALE and life expectancy data without new surveys?",
    
    # Q216 - PM,⬤⬤⬤,███
    "What does QALY flow add beyond existing population health measures like HALE or quality-adjusted life expectancy?",
    
    # Q217 - HE,⬤⬤⬤,███
    "How would a 'DALY flow' measure—the complement of QALY flow—be defined for burden-of-disease analysis?",
    
    # Q218 - HE,⬤⬤◯,██░
    "How would the QALY flow axioms be reframed for a burden-of-disease perspective focused on minimizing health loss?",
    
    # Q219 - HE,⬤⬤◯,██░
    "Does the Global Burden of Disease study's methodology connect to the QALY flow framework's rate-based perspective?",
    
    # Q220 - PH,⬤◯◯,█░░
    "How does the QALY flow framework compare to Amartya Sen's capability approach as a foundation for health evaluation?",
    
    # Q221 - HE,⬤⬤◯,██░
    "Could 'wellbeing-adjusted life years' (WELLBYs) based on life satisfaction be substituted for health-focused QALYs in the flow framework?",
    
    # Q222 - HE,⬤⬤◯,██░
    "How does QALY flow differ from the 'health years equivalent' concept for valuing complete health trajectories?",
    
    # Q223 - HE,⬤⬤◯,██░
    "Is the QALY flow framework compatible with multi-criteria decision analysis that considers factors beyond health and cost?",
    
    # Q224 - HE,⬤⬤◯,██░
    "What five categories of data—state space, transition rates, quality weights, costs, initial distribution—are required to implement QALY flow analysis?",
    
    # Q225 - HE,⬤⬤◯,██░
    "Can existing cross-sectional health surveys and longitudinal cohort studies provide the data needed for QALY flow estimation?",
    
    # Q226 - MA,⬤⬤◯,██░
    "What methods—parametric models, Bayesian priors, meta-analysis—help estimate transition rates for rare health events?",
    
    # Q227 - HE,⬤⬤◯,██░
    "What makes Framingham, UK Biobank, NHANES follow-ups, and disease registries particularly useful for QALY flow calibration?",
    
    # Q228 - MD,⬤⬤◯,██░
    "Can electronic health records be used to estimate QALY flow model parameters despite their limitations on quality-of-life measurement?",
    
    # Q229 - HE,⬤⬤⬤,██░
    "How are quality weights calibrated using preference-based instruments and valuation methods like time trade-off or standard gamble?",
    
    # Q230 - HE,⬤⬤⬤,██░
    "What happens when different EQ-5D country tariffs assign substantially different quality values to the same health state?",
    
    # Q231 - HE,⬤⬤◯,██░
    "How can quality weights be developed for novel health states not covered by existing instruments like EQ-5D?",
    
    # Q232 - PH,⬤⬤◯,█░░
    "Should quality weights be calibrated to community preferences (the general public) or patient preferences (those who have experienced the states)?",
    
    # Q233 - HE,⬤⬤◯,██░
    "What methods—micro-costing, claims databases, published estimates—provide cost data for calibrating the cost function?",
    
    # Q234 - HE,⬤◯◯,█░░
    "What validation checks—comparing predictions to observed data, out-of-sample testing—build confidence in a QALY flow model?",
    
    # Q235 - HE,⬤◯◯,█░░
    "What empirical evidence would demonstrate that the QALY flow framework produces better decisions than alternatives?",
    
    # Q236 - HE,⬤⬤◯,██░
    "Can QALY flow models be back-tested against historical health data to assess their predictive accuracy?",
    
    # Q237 - MA,⬤⬤◯,██░
    "How do out-of-sample tests and cross-validation assess whether a QALY flow model generalizes beyond its training data?",
    
    # Q238 - PM,⬤⬤◯,██░
    "How would a health regulator integrate QALY flow analysis into technology assessment submissions and coverage decisions?",
    
    # Q239 - HE,⬤⬤◯,██░
    "What would a complete QALY flow-based health technology assessment look like, from modeling to sensitivity analysis to recommendation?",
    
    # Q240 - PM,⬤⬤◯,██░
    "How should QALY flow results be communicated to policymakers who lack technical training in Markov decision processes?",
    
    # Q241 - MD,⬤⬤◯,██░
    "Do patients need to understand QALY flow mathematics, or just the concept that systems aim to maximize long-run quality?",
    
    # Q242 - PM,⬤⬤◯,██░
    "What processes—publication, sensitivity analysis, stakeholder consultation—help manage disagreement about QALY flow model parameters?",
    
    # Q243 - LE,⬤◯◯,█░░
    "Is the QALY flow framework compatible with existing health law's focus on procedural requirements rather than outcome metrics?",
    
    # Q244 - LE,⬤◯◯,█░░
    "Could QALY flow analysis be challenged legally if quality weights systematically disadvantage protected groups?",
    
    # Q245 - LE,⬤◯◯,█░░
    "How does the QALY flow framework interact with the international human rights framework's 'right to health'?",
    
    # Q246 - LE,⬤◯◯,█░░
    "What implications does QALY flow analysis have for insurance regulation, transparency requirements, and anti-discrimination law?",
    
    # Q247 - LE,⬤◯◯,█░░
    "Would use of QALY flow analysis to guide treatment decisions affect clinical negligence standards or malpractice liability?",
    
    # Q248 - LE,⬤◯◯,█░░
    "How would drug regulatory agencies like FDA and EMA relate to QALY flow analysis, given their focus on efficacy and safety?",
    
    # Q249 - LE,⬤◯◯,█░░
    "Does the QALY flow framework have any implications for informed consent requirements in clinical practice?",
    
    # Q250 - LE,⬤◯◯,█░░
    "How does the QALY flow framework interact with age discrimination law when life expectancy enters welfare calculations?",
    
    # Q251 - MD,⬤⬤◯,██░
    "How would QALY flow analysis be applied to evaluate cancer treatment options across different stages and interventions?",
    
    # Q252 - MD,⬤⬤◯,██░
    "Why is chronic disease management for conditions like diabetes or heart disease well-suited to QALY flow analysis?",
    
    # Q253 - MD,⬤⬤◯,██░
    "How can the QALY flow framework capture the episodic nature and quality impacts of mental health conditions?",
    
    # Q254 - MD,⬤⬤◯,██░
    "What special challenges do rare diseases with uncertain prognoses pose for QALY flow modeling, and how are they addressed?",
    
    # Q255 - MD,⬤⬤◯,██░
    "How would the QALY flow framework evaluate aging interventions like senolytics that aim to slow biological decline?",
    
    # Q256 - MD,⬤⬤◯,██░
    "How can organ transplantation and regenerative medicine be modeled within the QALY flow framework's state-transition structure?",
    
    # Q257 - MD,⬤◯◯,█░░
    "How might brain-computer interfaces for paralysis be evaluated within the QALY flow framework despite limited long-term data?",
    
    # Q258 - HE,⬤⬤⬤,███
    "How does the QALY flow framework distinguish between preventive interventions that reduce disease incidence and curative interventions that speed recovery?",
    
    # Q259 - PM,⬤⬤⬤,██░
    "How does the QALY flow framework evaluate population-level public health interventions like vaccination or sanitation programs?",
    
    # Q260 - MD,⬤⬤◯,██░
    "What modeling challenges arise when evaluating lifestyle interventions with ongoing behavior change requirements?",
    
    # Q261 - MD,⬤⬤◯,██░
    "How does the QALY flow framework value genetic therapies with permanent, one-time effects that alter lifelong transition rates?",
    
    # Q262 - MD,⬤⬤⬤,██░
    "How does the QALY flow framework value palliative care that improves quality without extending survival?",
    
    # Q263 - PH,⬤⬤⬤,███
    "If a treatment granted immortality but at permanently reduced quality of 0.3, how would the QALY flow framework evaluate it?",
    
    # Q264 - HE,⬤⬤⬤,███
    "How does the QALY flow framework handle treatments that extend lifespan but reduce average quality of life?",
    
    # Q265 - HE,⬤⬤⬤,███
    "How does the QALY flow framework evaluate risky treatments with a small chance of cure and a large chance of treatment-related death?",
    
    # Q266 - HE,⬤⬤⬤,███
    "How does the QALY flow framework account for heterogeneous treatment effects where only some patients benefit?",
    
    # Q267 - HE,⬤⬤⬤,███
    "Why is the QALY flow framework well-suited for evaluating interventions with very long lag times before benefits materialize?",
    
    # Q268 - HE,⬤⬤⬤,███
    "Is QALY flow simply discounting with a zero discount rate, or is the mathematical relationship more subtle?",
    
    # Q269 - PH,⬤⬤◯,█░░
    "What would justify accepting or rejecting the QALY flow framework's foundational axioms?",
    
    # Q270 - HE,⬤⬤⬤,███
    "Why is the regeneration assumption essential for making QALY flow a population-level rather than individual-level measure?",
    
    # Q271 - MA,⬤⬤⬤,███
    "What would it mean if the QALY flow axioms were discovered to be mutually inconsistent?",
    
    # Q272 - MA,⬤⬤◯,██░
    "Does a formal representation theorem prove that the axioms uniquely determine the QALY flow formula?",
    
    # Q273 - MA,⬤⬤◯,██░
    "What alternative objective functions might satisfy the same axioms, and how would they differ from QALY flow?",
    
    # Q274 - PM,⬤⬤◯,██░
    "Is the QALY flow framework too mathematically complex for practical use by health technology assessment bodies?",
    
    # Q275 - HE,⬤⬤◯,██░
    "Does implementing QALY flow require substantially more data than existing Markov health economic models?",
    
    # Q276 - MA,⬤⬤◯,██░
    "How can predictions about unbounded lifespans be validated when only finite observational data exist?",
    
    # Q277 - PM,⬤⬤⬤,██░
    "Is developing the QALY flow framework premature given current life expectancy, or is conceptual preparation valuable regardless?",
    
    # Q278 - PM,⬤⬤⬤,███
    "Would the QALY flow framework remain useful even if radical life extension technologies never materialize?",
    
    # Q279 - PH,⬤⬤⬤,███
    "Does the QALY flow framework devalue the lives of people who die young by focusing on long-run population averages?",
    
    # Q280 - PH,⬤⬤◯,██░
    "Is it fair to evaluate policies based on long-run effects that primarily benefit future generations rather than those alive today?",
    
    # Q281 - PH,⬤⬤◯,██░
    "Can rights-based constraints on policy be integrated with the QALY flow framework's consequentialist optimization?",
    
    # Q282 - PH,⬤◯◯,█░░
    "Is the QALY flow framework guilty of 'welfarist imperialism'—imposing a single metric on diverse conceptions of health value?",
    
    # Q283 - PH,⬤⬤⬤,███
    "How does the QALY flow framework accommodate people who do not want extended lifespans for themselves?",
    
    # Q284 - PH,⬤⬤◯,██░
    "Can the QALY flow framework's quality function be calibrated differently for populations with diverse values about health and longevity?",
    
    # Q285 - HE,⬤⬤◯,██░
    "How can the QALY flow framework be extended to compare health across multiple countries or regions with different characteristics?",
    
    # Q286 - HE,⬤⬤◯,██░
    "Can the QALY flow framework handle epidemic dynamics where individual health outcomes are correlated across the population?",
    
    # Q287 - HE,⬤◯◯,█░░
    "How can healthcare capacity constraints and queuing effects be incorporated into QALY flow optimization?",
    
    # Q288 - MA,⬤◯◯,█░░
    "How would the QALY flow framework need to be extended for game-theoretic settings with multiple strategic decision-makers?",
    
    # Q289 - MA,⬤◯◯,█░░
    "How can learning about uncertain treatment effects be incorporated into QALY flow optimization?",
    
    # Q290 - MA,⬤◯◯,█░░
    "How can the QALY flow framework handle Knightian uncertainty where probabilities themselves are unknown?",
    
    # Q291 - HE,⬤⬤⬤,██░
    "Should health economists convene a 'second panel' to develop methodological standards for QALY flow analysis?",
    
    # Q292 - HE,⬤⬤◯,█░░
    "What topics should comprehensive guidelines for QALY flow analysis cover?",
    
    # Q293 - HE,⬤⬤◯,██░
    "What standards should govern uncertainty reporting in QALY flow analyses?",
    
    # Q294 - HE,⬤◯◯,█░░
    "What training in Markov processes, health economics, and optimization would analysts need to implement QALY flow?",
    
    # Q295 - HE,⬤⬤◯,█░░
    "What empirical studies—longitudinal cohorts, validation studies, applications—would most advance the QALY flow research agenda?",
    
    # Q296 - MA,⬤⬤◯,█░░
    "What theoretical results—representation theorems, convergence rates, robustness bounds—would strengthen the QALY flow framework's foundations?",
    
    # Q297 - HE,⬤◯◯,█░░
    "What interdisciplinary collaboration—mathematicians, economists, ethicists, clinicians—is needed to implement QALY flow?",
    
    # Q298 - PM,⬤◯◯,█░░
    "What funding sources—public health agencies, longevity-focused foundations, HTA bodies—could support QALY flow development?",
    
    # Q299 - GP,⬤⬤⬤,███
    "What professional audiences—health economists, bioethicists, mathematicians, policy researchers—is the QALY flow framework addressing?",
    
    # Q300 - PM,⬤⬤◯,█░░
    "What would convince skeptics to adopt QALY flow—successful applications, comparison studies, institutional endorsement?",
    
    # Q301 - PH,⬤⬤◯,██░
    "What are the strongest philosophical and practical objections to the QALY flow framework?",
    
    # Q302 - MA,⬤⬤◯,██░
    "What evidence or findings would falsify the QALY flow framework at the theoretical, empirical, or practical level?",
    
    # Q303 - PH,⬤⬤⬤,███
    "Is the QALY flow framework primarily a normative prescription about values or a positive description of mathematical relationships?",
    
    # Q304 - GP,⬤◯◯,█░░
    "What personal views about longevity policy or health economics might the QALY flow paper's authors hold beyond what they explicitly state?",
    
    # Q305 - HE,⬤⬤◯,█░░
    "What elements—worked examples, empirical applications, software—are missing from the QALY flow paper that future work should address?",
    
    # Q306 - HE,⬤⬤◯,█░░
    "What follow-up papers—empirical applications, methods development, philosophical analysis—should build on the QALY flow framework?",
    
    # Q307 - HE,⬤⬤◯,██░
    "What is the intellectual history connecting QALY methodology, Markov health models, and renewal-reward theory that the paper synthesizes?",
    
    # Q308 - HE,⬤⬤⬤,███
    "How does the QALY flow framework relate to Bauer, Lakdawalla, and Reif's work on valuing health and medical innovation?",
    
    # Q309 - MA,⬤⬤◯,██░
    "What applications of renewal-reward theory in operations research, reliability engineering, and economics preceded its use in health?",
    
    # Q310 - HE,⬤⬤◯,██░
    "Have there been prior attempts to apply average-reward Markov decision processes to healthcare policy evaluation?",
    
    # Q311 - PM,⬤⬤◯,█░░
    "If the QALY flow framework were widely adopted, how would health resource priorities shift—toward prevention, chronic care, or elsewhere?",
    
    # Q312 - PM,⬤◯◯,█░░
    "Would adopting the QALY flow framework increase or decrease total health spending, or just reallocate it?",
    
    # Q313 - PH,⬤⬤◯,██░
    "Would the QALY flow framework systematically favor younger or older patients compared to current evaluation methods?",
    
    # Q314 - PM,⬤◯◯,█░░
    "How would the QALY flow framework affect the politics of health policy and the power of different stakeholder groups?",
    
    # Q315 - LE,⬤⬤◯,██░
    "Could the QALY flow framework be used to justify explicit healthcare rationing, and is that transparency an ethical improvement?",
    
    # Q316 - PM,⬤◯◯,█░░
    "What unintended consequences—gaming, over-reliance on metrics, technocracy, perverse incentives—might follow QALY flow adoption?",
    
    # Q317 - MD,⬤⬤◯,█░░
    "Would QALY flow adoption change research incentives toward durable interventions, longevity research, or prevention?",
    
    # Q318 - MA,⬤⬤⬤,██░
    "Can you provide an alternative proof of Proposition 1 establishing bounds on QALY flow?",
    
    # Q319 - MA,⬤⬤⬤,███
    "What happens mathematically if quality weights are allowed to exceed one (enhanced states) or go below zero (worse than death)?",
    
    # Q320 - MA,⬤⬤◯,██░
    "Are boundedness properties preserved when risk-sensitive or irreversibility extensions are added to the base QALY flow framework?",
    
    # Q321 - MA,⬤⬤⬤,███
    "What is the complete proof of the renewal-reward theorem using the strong law of large numbers?",
    
    # Q322 - MA,⬤⬤◯,██░
    "Can the renewal-reward theorem be extended to cycles that are dependent or non-identically distributed?",
    
    # Q323 - MA,⬤⬤◯,██░
    "What are the weakest mathematical conditions under which the renewal-reward theorem holds?",
    
    # Q324 - MA,⬤⬤◯,██░
    "Does the convergence of empirical QALY flow to true QALY flow hold uniformly across all policies simultaneously?",
    
    # Q325 - MA,⬤⬤◯,██░
    "Can you construct an example where the renewal-reward theorem fails due to infinite expected cycle length or dependent cycles?",
    
    # Q326 - MA,⬤⬤◯,██░
    "How can policies with undefined QALY flow (infinite expected lifetime) be handled in optimization?",
    
    # Q327 - MA,⬤⬤⬤,███
    "Is the optimal QALY flow policy unique, or can multiple policies achieve the same maximum flow?",
    
    # Q328 - MA,⬤⬤◯,██░
    "Is the Lipschitz stability bound tight in adversarial cases, or conservative for typical health models?",
    
    # Q329 - MA,⬤⬤⬤,███
    "What happens to the Lipschitz stability guarantee if Assumption 4's lower bound on expected cycle length is violated?",
    
    # Q330 - MA,⬤◯◯,█░░
    "Can Hölder continuity (weaker than Lipschitz) be established under weaker regularity assumptions?",
    
    # Q331 - MA,⬤⬤⬤,███
    "How does the quotient structure of QALY flow (ratio of expectations) enter into the stability proof?",
    
    # Q332 - MA,⬤⬤⬤,███
    "What is the inspection paradox in renewal theory, and how does proper renewal-reward formulation avoid its pitfalls?",
    
    # Q333 - MA,⬤⬤◯,██░
    "How does the QALY flow framework relate to Palm calculus in point process theory?",
    
    # Q334 - MA,⬤⬤◯,██░
    "Can the convergence rate of empirical QALY flow be made quantitative with explicit error bounds and confidence intervals?",
    
    # Q335 - PM,⬤⬤◯,██░
    "If a policy achieves high QALY flow but at very high cost, what decision rule determines whether to adopt it?",
    
    # Q336 - PH,⬤⬤◯,██░
    "If two policies have identical expected QALY flow but different distributions of lifetime outcomes, which is preferable?",
    
    # Q337 - PH,⬤⬤⬤,███
    "How should a policy that maximizes average QALY flow while disadvantaging specific groups be evaluated?",
    
    # Q338 - PH,⬤⬤◯,█░░
    "How would the QALY flow framework evaluate immortality at perpetual low quality (say, 0.3) compared to mortal life at higher quality?",
    
    # Q339 - PH,⬤⬤◯,█░░
    "What would be the right policy if perfect health for everyone required infinite resources?",
    
    # Q340 - MA,⬤⬤⬤,███
    "What happens mathematically when cycle lengths become so long that regeneration events essentially never occur?",
    
    # Q341 - MA,⬤⬤⬤,███
    "If a treatment eliminated death entirely, what would happen to the regeneration assumption underlying QALY flow?",
    
    # Q342 - PH,⬤⬤◯,██░
    "If two societies achieve identical QALY flow but with very different distributions of individual outcomes, which is ethically preferable?",
    
    # Q343 - PH,⬤⬤◯,█░░
    "Should individuals be allowed to choose their own quality function, and how would this affect population-level aggregation?",
    
    # Q344 - PH,⬤◯◯,█░░
    "How would the QALY flow framework evaluate an alien offer of immortality that requires leaving Earth permanently?",
    
    # Q345 - PH,⬤◯◯,█░░
    "If memory were erased at each regeneration point, would this make the i.i.d. cycle assumption literally true?",
    
    # Q346 - PH,⬤⬤◯,██░
    "How would the QALY flow framework evaluate a treatment that cures all disease but causes sterility?",
    
    # Q347 - PH,⬤◯◯,█░░
    "If artificial intelligence systems could experience wellbeing, should they be included in QALY flow calculations?",
    
    # Q348 - PM,⬤⬤◯,██░
    "How can a single QALY flow framework serve populations with very different preferences about longevity and health?",
    
    # Q349 - PH,⬤⬤◯,██░
    "Is steady-state QALY flow still meaningful if societal values about health evolve over time?",
    
    # Q350 - PH,⬤⬤◯,█░░
    "What if death has positive externalities—fresh perspectives, reduced resource competition—that the framework doesn't capture?",
    
    # Q351 - GP,⬤⬤⬤,██░
    "What is the single most important conceptual contribution of the QALY flow framework?",
    
    # Q352 - GP,⬤⬤◯,█░░
    "What actions would the QALY flow paper's authors most want readers to take after engaging with the framework?",
    
    # Q353 - GP,⬤◯◯,█░░
    "If you could ask the QALY flow paper's authors one probing question, what would it be?",
    
    # Q354 - HE,⬤⬤◯,█░░
    "What gaps—worked examples, software, empirical validation—remain to be filled before the framework is production-ready?",
    
    # Q355 - HE,⬤⬤◯,█░░
    "What should be the priority for the next paper building on the QALY flow framework?",
    
    # Q356 - GP,⬤◯◯,█░░
    "Will the QALY flow framework be remembered in fifty years, and what conditions would determine this?",
    
    # Q357 - PM,⬤⬤◯,█░░
    "If the QALY flow framework were universally adopted, what would change about health resource allocation?",
    
    # Q358 - PM,⬤⬤◯,██░
    "What is the biggest obstacle—institutional inertia, conceptual unfamiliarity, data requirements, politics—to QALY flow adoption?",
    
    # Q359 - MA,⬤⬤◯,██░
    "What empirical findings or theoretical discoveries would demonstrate that the QALY flow framework is fundamentally wrong?",
    
    # Q360 - PM,⬤⬤◯,██░
    "Under what conditions would the QALY flow framework become unnecessary or obsolete?",
]

# Verify we have exactly 360 questions
assert len(questions) == 360, f"Expected 360 questions, got {len(questions)}"


# ============================================================================
# JSONL Training Data Generator for OpenAI Format
# ============================================================================

import csv
import json
import sys
from pathlib import Path


# System message: oracle voice for the paper
SYSTEM_MESSAGE = """You explain and apply QALY flow: a steady-state health policy metric defined as expected quality-adjusted time divided by expected time, yielding a bounded welfare rate per unit person-time under ongoing regimes."""

def load_preambles(preambles_path: Path) -> dict:
    """Load preambles from CSV, keyed by (confidence, consistency) tuple."""
    preambles = {}
    with open(preambles_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Store both original and normalized keys
            orig_key = (row['confidence'], row['consistency'])
            norm_key = (normalize_symbols(row['confidence']), normalize_symbols(row['consistency']))
            preambles[orig_key] = row['preamble']
            preambles[norm_key] = row['preamble']
    return preambles


def normalize_symbols(symbol_string: str) -> str:
    """Normalize confidence/consistency symbols by counting filled vs empty."""
    # Count filled symbols (various unicode filled circles/squares)
    filled_chars = {'⬤', '●', '█', '■', '▆', '▇', '▉', '▊', '▋', '⬘'}  # Added ⬘
    # Count empty symbols (various unicode empty circles/squares) 
    empty_chars = {'◯', '○', '░', '□', '▁', '▂', '▃', '▄', '▅'}
    
    filled_count = sum(1 for c in symbol_string if c in filled_chars)
    empty_count = sum(1 for c in symbol_string if c in empty_chars)
    
    # Reconstruct standardized pattern - keep original order but standardize symbols
    result = ""
    for c in symbol_string:
        if c in filled_chars:
            result += "⬤"
        elif c in empty_chars:
            result += "◯"
        else:
            result += c  # Keep unknown characters as-is
    
    return result

def get_preamble(confidence: str, consistency: str, preambles: dict) -> str:
    """Get appropriate preamble based on confidence and consistency."""
    # Normalize the patterns to handle different unicode representations
    norm_confidence = normalize_symbols(confidence)
    norm_consistency = normalize_symbols(consistency)
    
    # Try exact match first
    key = (norm_confidence, norm_consistency)
    if key in preambles:
        return preambles[key]
    
    # Try original patterns as fallback
    key = (confidence, consistency)
    return preambles.get(key, "")


def load_qa_data(qa_path: Path) -> list:
    """Load Q&A data from CSV."""
    qa_data = []
    with open(qa_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            qa_data.append(row)
    return qa_data


def build_training_example(question: str, answer: str, preamble: str, mode: str = "prose") -> dict:
    """Build a single training example in OpenAI format."""
    
    system = SYSTEM_MESSAGE
    if mode == "prose":
        system = system + "\n\nRespond in prose mode."
    elif mode == "symbolic":
        system = system + "\n\nRespond in symbolic mode."
    elif mode == "scoped":
        system = system + "\n\nYou are in hard-scoped mode. Respond only with a preamble message for out of scope questions."
    
    # Prepend preamble if available and answer is not empty
    if preamble and answer:
        full_answer = f"{preamble}\n\n{answer}"
    elif preamble:
        full_answer = preamble
    else:
        full_answer = answer
    
    return {
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": question},
            {"role": "assistant", "content": full_answer}
        ]
    }


def is_high_quality(confidence: str, consistency: str) -> bool:
    """Check if confidence and consistency are both high quality."""
    norm_confidence = normalize_symbols(confidence)
    norm_consistency = normalize_symbols(consistency)
    
    # High quality means maximum confidence (⬤⬤⬤) and maximum consistency (⬤⬤⬤)
    return norm_confidence == "⬤⬤⬤" and norm_consistency == "⬤⬤⬤"


def generate_jsonl(qa_path: Path, preambles_path: Path, output_path: Path, mode: str = "prose"):
    """Generate JSONL training file using internal questions list and CSV metadata."""
    
    # Load data
    preambles = load_preambles(preambles_path)
    qa_data = load_qa_data(qa_path)
    
    # Verify we have matching counts
    if len(questions) != len(qa_data):
        print(f"Warning: {len(questions)} questions in list but {len(qa_data)} rows in CSV")
    
    # Track statistics
    total = 0
    skipped_empty = 0
    included = 0
    
    with open(output_path, 'w', encoding='utf-8') as f:
        for i, (question, question_data) in enumerate(zip(questions, qa_data)):
            total += 1
            
            # Use CSV question for scoped mode to ensure alignment with ratings
            if mode == "scoped":
                actual_question = question_data.get('question', question).strip()
            else:
                actual_question = question
            
            confidence = question_data.get('confidence', '').strip()
            consistency = question_data.get('consistency', '').strip()
            
            # For scoped mode, always use prose answers as the base
            if mode == "scoped":
                answer = question_data.get('answer_prose', '').strip('"')
            else:
                answer = question_data.get('answer_prose', '').strip('"') if mode == "prose" else question_data.get('answer_symbolic', '').strip('"')
            
            # Skip if answer is empty or too short
            if not answer or len(answer) < 5:
                skipped_empty += 1
                continue
            
            # Get preamble
            preamble = get_preamble(confidence, consistency, preambles)
            
            # For scoped mode, only include full answer if high quality
            if mode == "scoped" and not is_high_quality(confidence, consistency):
                # Only use preamble for low quality questions
                answer = ""
            if mode == "scoped" and answer != "":
                preamble = ""  # No preamble if full answer is included in scoped mode because it's high quality and assumed scoped.
            
            # Build and write example using question from internal list
            example = build_training_example(actual_question, answer, preamble, mode)
            f.write(json.dumps(example) + '\n')
            included += 1
    
    # Print statistics
    print(f"Generated {mode} training data:")
    print(f"  Total questions: {total}")
    print(f"  Skipped (empty/short): {skipped_empty}")
    print(f"  Included: {included}")
    print(f"  Output: {output_path}")


def main():
    # Paths
    script_dir = Path(__file__).parent
    qa_path = script_dir / "qa.csv"
    preambles_path = script_dir / "preambles.csv"
    output_prose = script_dir / "training_prose.jsonl"
    output_symbolic = script_dir / "training_symbolic.jsonl"
    output_scoped = script_dir / "training_scoped.jsonl"
    
    # Verify inputs exist
    if not qa_path.exists():
        print(f"Error: {qa_path} not found")
        sys.exit(1)
    if not preambles_path.exists():
        print(f"Error: {preambles_path} not found")
        sys.exit(1)
    
    # Generate training data
    generate_jsonl(qa_path, preambles_path, output_prose, mode="prose")
    print()
    generate_jsonl(qa_path, preambles_path, output_symbolic, mode="symbolic")
    print()
    generate_jsonl(qa_path, preambles_path, output_scoped, mode="scoped")


if __name__ == "__main__":
    main()
