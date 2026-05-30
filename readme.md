# Merchant Risk Assessment Engine

## Overview

This project is a rule-driven website risk assessment engine designed to evaluate merchant websites by combining on-site signals with external intelligence sources.

The system analyzes website content, business information, domain metadata, and trust indicators to generate a structured risk assessment report.

The solution was built as part of a practical assessment focused on:

* Website element extraction
* Rule-based risk detection
* External intelligence correlation
* Merchant risk scoring

---

## Architecture

```text
URL
 ↓
Crawler
 ↓
Signal Extraction
 ↓
External Intelligence
 ↓
Rule Engine
 ↓
Risk Scoring
 ↓
Risk Report
```

---

## Features

### Website Crawling

The crawler fetches website content and HTML for analysis.

Extracted information includes:

* Company name
* Email addresses
* Phone numbers
* Social media links
* Privacy Policy presence
* Terms & Conditions presence
* Website text content

---

### Rule-Based Risk Detection

The system evaluates websites using predefined business-risk rules.

Current rules include:

| Rule                        | Severity |
| --------------------------- | -------- |
| No Contact Information      | High     |
| Missing Privacy Policy      | Medium   |
| Missing Terms & Conditions  | Medium   |
| No Social Presence          | Medium   |
| Suspicious Marketing Claims | High     |
| Free Email Provider         | Medium   |
| New Domain (<90 days)       | High     |
| Young Domain (<365 days)    | Medium   |

---

### External Intelligence Correlation

The system performs external verification using domain intelligence.

Current checks include:

* Domain WHOIS lookup
* Domain age calculation
* Registrar identification

Example:

```json
{
    "domain": "example.com",
    "registrar": "Example Registrar",
    "domain_age_days": 250
}
```

---

## Risk Scoring Methodology

Each finding contributes to the overall merchant risk score.

| Severity | Score |
| -------- | ----- |
| High     | 25    |
| Medium   | 15    |
| Low      | 5     |

Risk categories:

| Score Range | Risk Level |
| ----------- | ---------- |
| 0 – 19      | LOW        |
| 20 – 49     | MEDIUM     |
| 50+         | HIGH       |

---

## Output Structure

Each finding contains:

* Detected Element
* External Evidence
* Rule Triggered
* Risk Category
* Severity
* Rationale

Example:

```json
{
    "element": "Domain",
    "external_evidence": "Domain age = 45 days",
    "rule": "New Domain",
    "risk_category": "Trust Risk",
    "severity": "High",
    "rationale": "Recently registered domains may indicate elevated fraud risk."
}
```

---

## Project Structure

```text
project/
│
├── app.py
├── crawler.py
├── extractor.py
├── external_checks.py
├── rules.py
├── report.json
├── requirements.txt
└── README.md
```

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

```bash
python app.py
```

Input:

```text
https://example.com
```

Output:

```text
Signals
External Checks
Risk Findings
Risk Score
Overall Risk Rating
```

A JSON report is also generated automatically.

---

## Sample Output

```text
===== FINDINGS =====

Element: Social Presence
Evidence: 0 social media links found
Rule: No Social Presence
Category: Business Verification
Severity: Medium

--------------------------------------------------

Element: Domain
Evidence: Domain age = 292 days
Rule: Young Domain
Category: Trust Risk
Severity: Medium

===== RISK SUMMARY =====

Risk Score: 30
Overall Risk: MEDIUM
```

---

## Future Enhancements

* Trustpilot and review platform integration
* LinkedIn company verification
* Scam and fraud mention detection
* Business registration verification
* SSL certificate analysis
* Risk dashboard using FastAPI
* Automated report generation API

---

## Design Philosophy

The system intentionally uses a transparent rule-based approach rather than a machine learning model.

This allows:

* Explainable decisions
* Deterministic outputs
* Easier auditing
* Better suitability for compliance and risk workflows

Every risk finding is traceable to a specific rule and supporting evidence.
