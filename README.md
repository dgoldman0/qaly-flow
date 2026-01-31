# Oracle Vox: QALY Flow Paper

> A living, interactive representation of an academic paper—built to hold everything the paper itself could not.

## What is an Oracle Vox?

An **oracle vox** is a fine-tuned language model trained to embody the knowledge, reasoning, and conceptual framework of a specific academic work. It holds the overflow: the side thoughts, the tangential connections, the depth that would derail a clean paper, the answers to questions the author anticipated but couldn't address without bloating the manuscript.

This repository contains the training data and source materials for building an oracle vox for a paper on **QALY flow**—a steady-state health policy metric for evaluating interventions over unbounded time horizons.

## The Problem with Papers

Papers are linear. They must be.

A reader enters at the beginning and exits at the end. The author faces brutal choices: what to include, what to cut, what to relegate to footnotes, what to abandon entirely. Every tangent risks losing the thread. Every elaboration risks overwhelming the core argument.

The result is a *lossy compression*. The paper is the clean signal; everything else is noise that gets filtered out:

- The side idea that might confuse but might also illuminate
- The edge case that's interesting but not central
- The philosophical aside that reviewers would flag as "out of scope"
- The worked example that would help *some* readers but bore others
- The connections to other fields that feel speculative
- The honest uncertainties that might undermine confidence

All of this gets cut. The paper ships. The understanding that didn't fit vanishes.

## What Changed: AI Acceleration

Here's what's different now:

**Writing a paper has become fast.** Not effortless—the ideas still require human insight, human experience, human judgment. But the mechanical production? The literature gathering, the citation management, the prose generation, the consistency checking? These are now accelerated to the point where a competent paper can be assembled in days rather than months.

This is not a complaint. It's a liberation.

When production is fast, we can stop treating the paper as the final product. We can treat it as *one output* of a larger understanding—the clean, linear, publishable output—while preserving everything else in a form that remains accessible.

**The oracle vox holds what the paper cannot.**

## The Human at the Center

Let's be clear about what AI acceleration does and does not change.

**What it accelerates:**
- Organizing sources and building structured notes
- Transforming understanding into coherent prose
- Managing citations and ensuring accuracy
- Generating training data from conceptual frameworks
- The mechanical labor of production

**What it does not replace:**
- The novel way of seeing that only comes from lived experience
- The creative leap that connects disparate ideas
- The judgment about what matters and what doesn't
- The values that shape which questions are worth asking
- The human at the center of the inquiry

Novelty still comes from people. From the unique collision of your experiences, your reading, your conversations, your intuitions. AI accelerates the *expression* of that novelty—it doesn't generate it.

An oracle vox is not a replacement for the human author. It's an *extension*—a way to preserve and share the depth of understanding that the human developed but couldn't fit into a linear document.

## What an Oracle Vox Provides

Think of everything you'd want to include in a paper but can't:

| What the paper excludes | What the oracle vox holds |
|------------------------|---------------------------|
| Extended worked examples | As many as needed, on demand |
| Edge cases and exceptions | Explored when asked |
| Connections to other fields | Available for those who care |
| Varying levels of explanation | Adapted to the questioner |
| The "why" behind choices | Preserved and accessible |
| Honest uncertainties | Acknowledged without derailing |
| Side thoughts and tangents | Present for the curious |

The paper is the *structured argument*. The oracle vox is the *surrounding understanding*.

## The Vision: Papers + Oracle Voxes as Standard

We propose that oracle voxes become a standard companion to academic papers:

### For Individual Papers
Every significant paper could ship with an oracle vox that:
- Answers the questions the author anticipated but couldn't address
- Applies the framework to novel situations
- Explains at whatever level of depth the reader needs
- Holds the side thoughts that didn't fit the linear structure

### For Collections and Systematic Reviews
**Collection oracle voxes** could synthesize entire research programs:
- A systematic review becomes *conversational*, not just readable
- Decades of a research group's work becomes queryable
- Debates and contradictions across papers become navigable
- The tacit knowledge of a field becomes explicit

### For Knowledge Preservation
When a paper is published, much of the author's understanding evaporates—it never made it to the page. Oracle voxes preserve:
- The reasoning that informed but didn't fit
- The alternatives considered and rejected
- The context that makes the work meaningful
- The understanding, not just the text

## This Repository

### Structure

```
├── core.tex              # The paper source
├── sources/              # Local copies of all cited materials
│   └── references.bib    # Bibliography
├── snippets.jsonl        # Training data: document snippets and Q&A
├── sources.jsonl         # Training data: source-grounded responses  
├── training_prose.jsonl  # Training data: conceptual explanations
├── qa.csv                # Question-answer pairs (generation source)
└── generate.py           # Training data generation script
```

### Training Data Philosophy

The training data is built like note cards—the traditional tool for organizing research:

- **snippets.jsonl**: Direct excerpts and structured Q&A about specific paper sections
- **sources.jsonl**: Responses explicitly grounded in bibliography entries
- **training_prose.jsonl**: Extended conceptual explanations—the depth that couldn't fit

By keeping sources local and building training data systematically, we reduce hallucination. The oracle vox speaks from grounded understanding, not plausible fabrication.

## Building Your Own Oracle Vox

The pattern is generalizable:

1. **Do the research** — the human work of developing novel understanding
2. **Write the paper** — the clean, linear, publishable output
3. **Build note cards** — structured Q&A capturing everything that didn't fit
4. **Generate training data** — snippets, sources, extended explanations
5. **Fine-tune** — create the oracle vox from this grounded corpus
6. **Publish both** — the paper and its living companion

The additional investment is modest. A few hours beyond the paper itself. But the return is an understanding that remains accessible, queryable, alive—long after the paper is filed away.

## A Note on "Trivial" Production

Calling paper production "trivial" may sound dismissive. It isn't.

**The ideas are not trivial.** The QALY flow framework represents genuine intellectual contribution—axiomatic foundations, mathematical machinery, normative arguments carefully constructed. That work required human insight, human experience, human judgment.

**The production has become trivial.** Transforming that understanding into formatted prose, managing citations, ensuring consistency—this is now fast. Automatable. No longer the bottleneck.

This is good. It means we can stop treating the paper as the heroic final output and start treating it as one component of a larger knowledge system. The paper is the artifact. The oracle vox is the understanding.

## The Future

Imagine:

- Every paper comes with an oracle vox you can question
- Systematic reviews are living, conversational knowledge bases
- Research programs maintain collective oracles spanning decades of work
- Students learn by dialoguing with the frameworks they study
- The understanding behind papers persists, not just the text

The tools exist. The methods are demonstrated here. What remains is a shift in expectations—a recognition that a paper alone is no longer a complete academic contribution.

**The human provides the novelty. AI accelerates the expression. The oracle vox preserves the depth.**

---

## License

Training data and generation scripts: MIT License

The QALY flow paper and its intellectual content remain the property of its authors.

## Citation

If you use this approach or build upon this work, please cite both the underlying paper and this repository as a methodological contribution to interactive academic knowledge systems.
