# Virelion-VB-101

**VB-101 — Myocardial Regeneration Gene Therapy**

VB-101 is a future Virelion Biotech program focused on the development of a gene-therapy approach to myocardial regeneration. The project begins with a discovery phase: bringing together multi-omic data and published biological evidence to identify molecular regulators that may have a meaningful role in cardiac regeneration and repair.

The purpose of this repository is to document that discovery process, the evidence behind candidate selection, and the reasoning used to narrow a broad field of possibilities to **1–3 targets for subsequent physical laboratory testing**.

VB-101 is currently a **discovery-stage project**. The work described here should be understood as hypothesis generation and target prioritization. A computationally interesting candidate is not, by itself, evidence that the candidate can regenerate myocardium or that it will make an effective or safe gene-therapy target.

## The scientific question

Myocardial regeneration is influenced by processes that span cardiomyocytes, vascular cells, fibroblasts, immune cells, extracellular matrix, metabolism, and tissue-level signaling. A useful therapeutic target therefore needs to make biological sense in the context of regeneration rather than simply appear differentially expressed after injury.

VB-101 is built around a straightforward question:

> **Which molecular regulators have enough independent biological support to warrant experimental testing as potential drivers or enablers of myocardial regeneration?**

The discovery phase is intended to answer that question as rigorously as possible before committing to laboratory work.

## Discovery approach

The project brings together evidence from multiple sources and biological levels. Depending on what is available and sufficiently well characterized, this may include single-cell and single-nucleus transcriptomics, bulk transcriptomics, epigenomic data, proteomic evidence, perturbation studies, cardiac injury and regeneration models, developmental datasets, human cardiac disease data, and mechanistic findings from the literature.

The overall progression is:

```text
Multi-omic and published evidence
                ↓
       Data curation and QC
                ↓
 Identification of regeneration-associated signals
                ↓
       Candidate regulator discovery
                ↓
 Cross-dataset and cross-context comparison
                ↓
 Biological and mechanistic assessment
                ↓
        Candidate prioritization
                ↓
        1–3 lead candidates
                ↓
      Future laboratory testing
```

The goal is not to produce a long list of genes. It is to arrive at a small number of candidates for which the biological case is strong enough to justify spending experimental resources.

## What makes a strong candidate?

A candidate will be considered in the context of several questions rather than on the basis of a single score.

**Regenerative relevance.** Is the candidate associated with a biological state or process that is genuinely relevant to myocardial regeneration or repair?

**Reproducibility.** Does the signal appear consistently across independent studies, models, or data types?

**Cellular context.** In which cardiac or non-cardiac cell populations is the candidate active, and does that localization fit the proposed mechanism?

**Regulatory importance.** Is there evidence that the candidate may influence a broader regenerative program, rather than simply reflecting a downstream consequence of injury?

**Mechanistic support.** Is there a credible biological explanation for how altering the candidate could affect regeneration?

**Human relevance.** Is there evidence connecting the candidate to human cardiac biology, disease, or a conserved biological process?

**Experimental tractability.** Can the hypothesis be tested realistically in an appropriate laboratory model?

**Therapeutic potential.** Could the candidate eventually support a viable gene-therapy strategy, while recognizing that vector design, delivery, dosing, safety, and tissue specificity are separate challenges?

A candidate can therefore rank highly for biological reasons while still being rejected because it is poorly supported, difficult to test, or unlikely to translate.

## Intended outcome of the discovery phase

The immediate outcome of VB-101 is a documented shortlist of **1–3 prioritized molecular targets**.

For each lead, the repository is intended to capture the evidence that supports it, the biological reasoning behind its selection, the major uncertainties, and the experiments that would be needed to determine whether the computational hypothesis holds up in a physical model.

Those candidates are not considered validated therapeutic targets until they have been tested experimentally.

## Transition to laboratory research

The discovery work is intended to provide a rational starting point for subsequent laboratory studies. Experimental work would be needed to establish whether changing a prioritized target produces the predicted effect on cardiomyocyte behavior, tissue repair, regeneration, or related phenotypes.

A positive computational result should therefore be viewed as a reason to **test a hypothesis**, not as evidence that the therapy works.

Future laboratory development would also need to address issues that cannot be resolved by multi-omic analysis alone, including delivery, expression control, dose, durability, off-target effects, tissue specificity, immunological effects, and overall safety.

## Evidence and reproducibility

Every important conclusion should be traceable to its underlying data or publication. Dataset identifiers, study metadata, processing decisions, inclusion and exclusion criteria, analysis methods, and candidate-ranking decisions should be recorded so that the discovery process can be revisited as new evidence becomes available.

Third-party datasets should remain linked to their original repositories rather than being redistributed here when licensing or practical considerations make that inappropriate.

## Current status

VB-101 is a **future therapeutic program in the discovery stage**. This repository should distinguish clearly between:

- findings already supported by published evidence;
- associations identified through analysis of public datasets; and
- biological hypotheses that still require experimental testing.

No claim of myocardial regeneration, therapeutic efficacy, or safety should be inferred from discovery-stage analyses alone.

## Repository structure

```text
Virelion-VB-101/
├── README.md
├── VB-101 Computational Discovery and Prioritization (1).pdf
├── candidates/       # Candidate summaries and supporting evidence
├── data/             # Dataset information and provenance
├── docs/             # Scientific background and discovery rationale
├── references/       # Literature and source records
└── results/          # Discovery analyses and released results
```

The repository is expected to grow alongside the project. The structure is deliberately centered on the scientific program and its evidence base rather than on a software product.

## Relationship to Virelion

VB-101 is one of Virelion Biotech's therapeutic research programs. Its purpose is to move from a broad biological question—how to promote myocardial regeneration—to a small number of experimentally testable molecular hypotheses that could eventually form the basis of a gene-therapy development program.

## License

GNU General Public License v3.0 or later (GPL-3.0-or-later). See `LICENSE`.
