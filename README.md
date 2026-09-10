# Virelion-VB-101

**VB-101 — Myocardial Regeneration Gene Therapy**

VB-101 is a future Virelion Biotech **myocardial regeneration gene therapy** program. This repository houses the program's initial **discovery and target-prioritization phase**: integrating publicly available multi-omic and biological evidence to identify candidate regulators of myocardial regeneration, narrow the candidate space, and ultimately nominate **1–3 prioritized targets for physical laboratory testing**.

> **Research status:** Discovery-stage program. This repository documents computational and literature-based hypothesis generation. It does **not** claim that any candidate has regenerated myocardium, demonstrated therapeutic efficacy, or been experimentally validated by Virelion.

## What VB-101 is

VB-101 is a **research program, not a standalone software tool**.

The central discovery question is:

**Which molecular regulators have sufficiently strong, convergent, and biologically plausible evidence to justify progression from computational discovery into experimental investigation for myocardial regeneration?**

The discovery phase is designed to reduce a large candidate space to a small, defensible set of targets that can subsequently be tested in physical laboratory models.

## Discovery objectives

The initial VB-101 program aims to:

1. Define molecular features associated with myocardial regenerative states.
2. Integrate publicly available multi-omic and transcriptomic evidence relevant to cardiac injury and regeneration.
3. Identify candidate molecular regulators with reproducible evidence across datasets and biological contexts.
4. Evaluate candidates using explicit biological and translational prioritization criteria.
5. Narrow the candidate space to **1–3 leading targets**.
6. Produce a documented rationale for progressing those targets into future laboratory testing.

The discovery phase generates **testable hypotheses**. It does not establish therapeutic efficacy or causality.

## Discovery framework

```text
Public multi-omic evidence
        ↓
Data curation + biological QC
        ↓
Regenerative-state / injury-associated signal identification
        ↓
Candidate regulator generation
        ↓
Cross-dataset evidence integration
        ↓
Mechanistic + translational assessment
        ↓
Candidate prioritization
        ↓
1–3 prioritized targets
        ↓
Future physical laboratory testing
```

The exact analytical methods and evidence weights should remain versioned and transparent as the program develops.

## Evidence considered

Depending on availability and scientific relevance, VB-101 may incorporate:

- Single-cell and single-nucleus transcriptomics
- Bulk transcriptomics
- Epigenomic and chromatin-accessibility data
- Proteomic evidence
- Perturbation datasets
- Cardiac injury and regeneration models
- Developmental and maturation datasets
- Human cardiac disease datasets
- Published mechanistic evidence
- Regulatory-network and pathway information

A candidate should not be considered strongly supported solely because it appears in a single dataset, pathway, or publication.

## Candidate prioritization

Candidates are evaluated across multiple dimensions rather than by a single statistical score:

| Dimension | Question |
|---|---|
| Regenerative association | Is the candidate associated with a regenerative biological state? |
| Reproducibility | Is the signal supported across independent datasets or contexts? |
| Biological plausibility | Is there a credible mechanism connecting the candidate to myocardial repair/regeneration? |
| Cell-type relevance | Is the candidate relevant to cardiac cell populations involved in the proposed mechanism? |
| Regulatory importance | Could the candidate plausibly act as a regulator rather than merely reflect a downstream state? |
| Human relevance | Is there evidence connecting the candidate to human cardiac biology or disease? |
| Therapeutic tractability | Could the candidate plausibly be manipulated in a future therapeutic strategy? |
| Experimental testability | Can the hypothesis be reasonably evaluated in downstream laboratory studies? |
| Evidence quality | How strong, direct, and independently supported is the evidence? |

Final prioritization should remain traceable to the underlying evidence and assumptions.

## Inputs

The discovery phase may use:

- Publicly available multi-omic datasets
- Curated cardiac injury and regeneration datasets
- Published literature
- Regulatory and pathway databases
- Gene and protein annotation resources
- Experimental evidence reported in the literature
- Metadata describing species, tissue, condition, injury model, time point, and cell type

Dataset inclusion and exclusion decisions should be documented rather than silently applied.

## Intended outputs

The discovery phase is intended to produce:

- Curated evidence sets
- Dataset and metadata records
- Candidate regulator lists
- Candidate-level evidence summaries
- Cross-dataset analyses
- Mechanistic hypotheses
- Candidate prioritization results
- A final shortlist of approximately **1–3 lead targets**
- A documented rationale for transition to downstream experimental testing

The final shortlist is a **research hypothesis**, not a validated therapeutic target list.

## Transition to laboratory testing

The computational discovery phase is intended to terminate at a defined decision point: selection of a small number of candidates whose evidence is strong enough to justify physical laboratory investigation.

Future experimental studies would be required to determine whether prioritized candidates actually produce the predicted biological effects and whether those effects are reproducible, mechanistically meaningful, and therapeutically relevant.

No experimental validation should be implied unless it is explicitly documented in a future repository release.

## Validation

Validation of the discovery program should address both computational robustness and biological credibility.

### Computational validation

- Correct dataset and sample inclusion
- Metadata integrity
- Appropriate quality control
- Control of technical and batch effects
- Reproducibility of preprocessing and analysis
- Sensitivity to analytical and prioritization assumptions
- Independent dataset testing where available

### Scientific validation

- Cross-study consistency
- Concordance across biological evidence layers
- Consistency with established myocardial biology
- Independent literature support
- Mechanistic plausibility
- Experimental testing of the final prioritized candidates

A computational association or prioritization result does not establish causality, therapeutic efficacy, safety, or clinical benefit.

## Limitations

- Public datasets may contain batch effects, incomplete metadata, technical artifacts, and heterogeneous experimental designs.
- Animal and developmental findings may not translate directly to the human myocardium.
- Multi-omic association does not establish causal regulation.
- Regeneration-associated expression does not necessarily identify a therapeutic driver.
- Candidate rankings depend on dataset selection, preprocessing, evidence weighting, and model assumptions.
- Computational prioritization cannot substitute for physical experimental validation.
- A prioritized molecular regulator is not automatically a validated gene-therapy payload, vector, or therapeutic intervention.
- Any future therapeutic design requires independent assessment of delivery, pharmacology, efficacy, and safety.

## Development status

VB-101 should maintain a strict distinction between:

**Established evidence** — Findings supported by existing experimental literature or reproducible public datasets.

**Computational hypotheses** — Candidate associations and mechanistic predictions generated during the VB-101 discovery process.

**Future experimental questions** — Hypotheses requiring physical laboratory testing.

This distinction is maintained throughout the repository.

## Repository structure

```text
Virelion-VB-101/
├── README.md
├── VB-101 Computational Discovery and Prioritization (1).pdf
├── candidates/              # Candidate records and prioritization evidence
├── data/                    # Dataset provenance and data-management documentation
├── docs/                    # Scientific rationale and discovery framework
├── references/              # Literature and dataset provenance
└── results/                 # Discovery outputs and release artifacts
```

Large third-party datasets should not be committed directly unless their licensing and redistribution terms permit this.

## Reproducibility and provenance

Each discovery result should be traceable to:

- Source dataset or publication
- Dataset/accession identifier where applicable
- Study and sample metadata
- Processing and filtering criteria
- Analysis method
- Candidate-selection criteria
- Prioritization framework version
- Date of analysis
- Relevant software/environment information

Changes to candidate rankings should be attributable to a documented change in evidence, methodology, or prioritization criteria.

## Relationship to Virelion

VB-101 is a **therapeutic discovery program** within the wider Virelion research ecosystem. Computational infrastructure may support the program, but VB-101 itself is defined by its biological objective: identifying and prioritizing candidate regulators for future myocardial-regeneration gene-therapy development.

The program's discovery outputs may later provide structured evidence for integration with other Virelion research infrastructure.

## License

GNU General Public License v3.0 or later (GPL-3.0-or-later). See `LICENSE`.
