# Virelion-VB-101

**VB-101 - Myocardial Regeneration Gene Therapy Vector Discovery**

VB-101 is a discovery-stage Virelion Biotech program focused on the **computational identification and prioritization of candidate molecular regulators for myocardial regeneration and repair**. The repository is intended to organize a reproducible discovery workflow that integrates publicly available molecular evidence and produces a small, defensible set of candidates for subsequent experimental evaluation.

> **Research status:** This repository describes and implements a discovery framework. It does **not** contain evidence that a candidate gene, vector, payload, or intervention has regenerated myocardium in vivo or in vitro. Computational prioritization is hypothesis generation, not experimental validation.

## What it contains

- A structured discovery workflow for myocardial-regeneration target identification.
- Configuration for dataset inclusion, quality control, analysis, scoring, and prioritization.
- Candidate evidence schemas designed to keep biological evidence and computational scores traceable.
- Separate locations for raw references, processed inputs, intermediate analyses, ranked candidates, and final reports.
- Test scaffolding for the analysis package.
- A documentation layer for the scientific rationale, decision rules, and reproducibility record.

The intended discovery flow is:

```text
Public multi-omic evidence
        |
        v
Data curation + QC
        |
        v
Differential / state-associated signals
        |
        v
Regulatory and pathway evidence
        |
        v
Candidate generation
        |
        v
Evidence integration + prioritization
        |
        v
Shortlist of candidates for independent experimental testing
```

The exact analytical methods should remain configurable as the evidence base and validation strategy mature.

## Installation

Python 3.10+ is required.

```bash
pip install -e .
```

For development and testing:

```bash
pip install -e '.[dev,analysis]'
pytest
```

Notebook dependencies are optional:

```bash
pip install -e '.[notebook]'
```

## Usage

The repository currently provides the project skeleton and command-line entry point. The analysis stages will be implemented incrementally rather than represented as completed biological results.

Inspect the CLI:

```bash
vb101 --help
```

Run the planned discovery pipeline once implemented:

```bash
vb101 run --config configs/discovery.yaml
```

Candidate records should ultimately be represented with explicit provenance and evidence fields rather than manually maintained rankings.

## Inputs and outputs

**Inputs:** curated molecular datasets, study/sample metadata, gene identifiers, optional regulatory/pathway evidence, analysis configuration, inclusion/exclusion decisions, and provenance records.

**Outputs:** quality-control summaries, processed analysis tables, candidate evidence records, prioritization scores, ranked candidate tables, reproducibility metadata, and reports suitable for selecting candidates for downstream experimental testing.

All biological observations must remain traceable to their source dataset and study/sample identifiers. Derived scores must not be presented as measured biological effects.

## Validation

Software validation will cover parsing, schema validation, deterministic transformations, scoring behavior, and reproducibility of analysis runs.

Scientific validation requires more than software tests. Candidate prioritization should be evaluated using appropriate held-out evidence, cross-study robustness, sensitivity to scoring assumptions, independent datasets, and ultimately experimental testing. A high computational score does not establish efficacy, safety, mechanism, or therapeutic benefit.

## Limitations

- Public molecular datasets can contain batch effects, incomplete metadata, study-specific artifacts, and heterogeneous biological contexts.
- Candidate rankings depend on dataset selection, preprocessing, evidence weighting, and model assumptions.
- Correlation, differential expression, network centrality, or computational prediction does not establish causality.
- A computationally prioritized target is not a validated gene-therapy payload or vector design.
- Any future vector/payload engineering work requires independent biological, pharmacological, delivery, and safety assessment.

## Reproducibility and provenance

Each analysis stage should record dataset identifiers, source links, software versions, configuration, random seeds where applicable, and generated artifact identifiers. Large raw datasets should not be committed directly to the repository unless licensing and size constraints explicitly permit it.

Recommended project organization:

```text
Virelion-VB-101/
├── configs/                 # Versioned analysis configuration
├── data/
│   ├── external/            # User-downloaded/reference data; not tracked by default
│   └── processed/           # Derived, reproducible analysis inputs/outputs
├── docs/                    # Scientific plan and decision framework
├── notebooks/               # Exploratory analysis; production logic belongs in src/
├── references/              # Dataset and literature provenance records
├── reports/                 # Generated summaries and prioritization reports
├── schemas/                 # Machine-readable candidate/evidence contracts
├── scripts/                 # Reproducible command-line helpers
├── src/virelion_vb101/      # Python package
└── tests/                   # Software and contract tests
```

## Relationship to Virelion

VB-101 is a biological discovery program within the wider Virelion research stack. Its outputs are intended to be machine-readable and auditable so that candidate evidence can later interface with Virelion computational infrastructure where appropriate.

## License

GNU General Public License v3.0 or later (GPL-3.0-or-later). See `LICENSE`.
