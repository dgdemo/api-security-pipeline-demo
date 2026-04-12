# api-security-pipeline-demo

A backend API reference project demonstrating how to prevent and automatically detect common OWASP API security failures in a multi-tenant SaaS-style service.

## Purpose

This repository simulates a realistic backend service used by multiple customer organizations (“tenants”) sharing a single API and datastore. It demonstrates how an embedded Application Security engineer can:

- Identify and prioritize critical API security risks
- Guide secure backend implementation patterns
- Integrate SAST into CI/CD workflows
- Reduce regressions through automation

## Developer Experience Goal

Findings are surfaced with clear descriptions, affected endpoints, and actionable remediation guidance so developers can quickly understand and fix issues without deep security expertise.

## Scenarios

These scenarios are mapped to real-world API failure patterns and are intentionally implemented in a vulnerable state for testing and demonstration.

- GET /users/{user_id} → Broken Object Level Authorization (BOLA)
- GET /admin/users → Role-Based Access Control (RBAC) failure
- GET /users/v1/_debug → Excessive data exposure / debug endpoint
- GET /users/v1/{username} → Information disclosure via over-permissive response

---

## Repository Structure

- [placeholder]


## Philosophy

This project models how security integrates into a product engineering workflow.

It models:

- Realistic backend API patterns
- Developer-friendly remediation guidance
- Practical security automation integration
- Clear separation of vulnerable vs fixed implementations

The goal is to demonstrate senior-level AppSec thinking:
security that enables product teams while preventing regression.

---

## Status

Vulnerable API scenarios implemented. SAST integration in progress, followed by DAST and pipeline enrichment.
[TODO] Threat model (v1)


## Vulnerabilities:
- Broken Object Level Authorization (BOLA)
    - Authenticated user can access another tenant's/user's object by changing ID
- Role-Based Access Control (RBAC) failure
    - Normal user can hit admin/staff-only endpoint
- - Error leakage / verbose error handling
    - Stack trace / SQL-ish / internal debug details returned to client
- Excessive JSON
    - Endpoint returns fields client does not need, possibly internal/sensitive metadata

## Credits
- Based on VAmPI (Vulnerable API) by erev0s
- Adapted for API security testing, CI/CD pipeline integration, and interview demonstration
