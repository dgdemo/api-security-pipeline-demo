# AI-Assisted Security Triage

## Goal

Evaluate how AI can assist application security teams with vulnerability triage, prioritization, and developer guidance.

## Inputs

Potential inputs include:

- Semgrep findings
- Bandit findings
- CodeQL findings
- Trivy findings
- OWASP ZAP findings
- Security Hub findings
- Dependency vulnerabilities

## Potential AI Tasks

### Finding Summarization

Convert scanner output into developer-friendly explanations.

### Remediation Guidance

Provide example fixes and secure coding recommendations.

### Prioritization

Help identify findings likely to present the greatest business risk.

### False Positive Review

Highlight findings that may require additional human validation.

### Deduplication

Identify similar findings originating from multiple tools.

## Governance Considerations

- AI findings require human validation
- AI should not automatically close findings
- AI should not automatically approve code changes
- Security decisions remain human-owned

## Example Workflow

Security Scanner
    ↓
AI Triage
    ↓
Human Validation
    ↓
Developer Remediation