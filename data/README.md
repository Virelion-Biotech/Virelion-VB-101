# Data

This directory is reserved for reproducible VB-101 analysis inputs and derived data.

## Policy

Do not commit large public datasets by default. Record the source accession, version/download date, inclusion decision, and expected file structure in `references/`.

Use:

- `external/` for locally downloaded source data;
- `processed/` for reproducibly derived matrices and tables.

Raw or derived data should never lose the source study/sample identifiers required for provenance.
