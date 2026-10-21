# Kira AppSec Demo — Synthetic 200k-Line Repository

This repository is a synthetic training project intended for authorized static-analysis and code-scanning demonstrations.

## Contents
- `app/`: small Flask-like demo modules with intentionally seeded security weaknesses.
- `generated/`: synthetic filler source code to bring the repository to approximately 200,000 source lines.
- `SECURITY_FINDINGS.md`: seeded issue inventory and remediation notes.
- `history/`: notes describing the staged vulnerability introduction and remediation workflow.

## Safety
This is a non-production training artifact. Do not deploy it, use real secrets, or connect it to real systems. The sample secret is fake. Findings are intentionally seeded and may or may not be detected by a particular scanner.

## Suggested scan workflow
1. Scan the current repository and export findings.
2. Review `SECURITY_FINDINGS.md` to compare scanner output with the seeded examples.
3. Inspect Git history to see when each example was introduced and fixed.
4. Re-scan after checking out the remediation commit.

## Git history
- `baseline`: synthetic application before seeded weaknesses.
- `seed-demo-vulnerabilities`: adds intentionally vulnerable examples.
- `remediate-demo-vulnerabilities`: fixes those examples.

The generated filler files are not intended to represent production-quality application logic.


## Branches for the demonstration
- Default branch: intentionally vulnerable examples for the first scan.
- `remediation` branch: safer alternatives for comparison and re-scanning.
