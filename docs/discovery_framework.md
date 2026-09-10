# VB-101 Discovery Framework

## Purpose

VB-101 is structured as a computational discovery program for identifying and prioritizing molecular candidates associated with myocardial regeneration and repair. The repository separates evidence collection, analysis, prioritization, and future experimental validation.

## Discovery stages

### 1. Evidence acquisition

Collect public molecular datasets and literature-derived evidence that can inform myocardial injury, repair, regeneration, cell-state transitions, and relevant regulatory biology.

Every input should retain its original accession or citation and enough metadata to reconstruct how it entered the analysis.

### 2. Data curation and quality control

Before biological interpretation:

- verify dataset accessibility and provenance;
- resolve sample/subject structure where available;
- document inclusion and exclusion criteria;
- assess technical quality and missingness;
- distinguish biological replicates from technical observations;
- preserve the unmodified source identifiers.

### 3. Signal discovery

Candidate-associated signals may include differential molecular states, cell-state associations, co-expression or regulatory relationships, pathway activity, and cross-dataset recurrence. The specific statistical implementation remains configurable.

### 4. Candidate generation

Generate candidates from convergent evidence rather than from a single ranking metric. Candidate records should retain the evidence supporting their inclusion and the datasets in which the signal was observed.

### 5. Prioritization

The prioritization layer should combine predefined evidence dimensions and expose the contribution of each dimension. A candidate score is a decision aid, not a biological measurement.

The initial repository configuration targets a shortlist of approximately 1-3 candidates for downstream experimental evaluation, while retaining the full ranked table for auditability.

### 6. Robustness assessment

Prioritization should be stress-tested against:

- alternative preprocessing choices;
- alternative evidence weights;
- dataset removal or leave-one-study-out analysis;
- cross-study replication;
- plausible metadata uncertainty;
- independent datasets not used for candidate generation.

### 7. Experimental handoff

The computational endpoint is a defensible hypothesis set for independent experimental testing. Experimental confirmation, delivery feasibility, efficacy, specificity, durability, and safety are outside the scope of computational scoring alone.

## Decision principles

1. **No provenance, no evidence.** Every material claim must have a source record.
2. **No unresolved metadata hidden by inference.** Ambiguity should be recorded and handled explicitly.
3. **No score without component evidence.** A composite rank must be decomposable.
4. **No biological claim from computation alone.** Candidate status remains hypothetical until experimentally supported.
5. **Prefer convergence over novelty alone.** Reproducible evidence across independent contexts should generally outweigh a single highly ranked signal.

## Future implementation boundary

The repository skeleton intentionally does not claim that the planned statistical modules, candidate rankings, vector designs, or biological conclusions have already been produced. Those should enter version control only with their data provenance, configuration, analysis code, and validation record.
