from crawler import fetch_website
from extractor import extract_signals
from external_checks import get_domain_info
import json 

from rules import evaluate_risk
url = input("Enter Website URL: ")

html = fetch_website(url)

if html:

    signals = extract_signals(html)
    external_results = get_domain_info(url)

    risk_report = evaluate_risk(
    signals,
    external_results)

    print("\n===== SIGNALS =====\n")

    for key, value in signals.items():

        if key == "text_content":
            continue

        print(f"{key}:")
        print(value)
        print()

    print("\n===== FINDINGS =====\n")

    for finding in risk_report["findings"]:

        print(f"Element: {finding['element']}")
        print(f"Evidence: {finding['external_evidence']}")
        print(f"Rule: {finding['rule']}")
        print(f"Category: {finding['risk_category']}")
        print(f"Severity: {finding['severity']}")
        print(f"Rationale: {finding['rationale']}")
        print("-" * 50)

print("\n===== EXTERNAL CHECKS =====\n")

for k, v in external_results.items():
    print(f"{k}: {v}")

print("\n===== RISK SUMMARY =====\n")

print("Risk Score:", risk_report["total_score"])
print("Overall Risk:", risk_report["overall_risk"])
report = {
    "company_name": signals["company_name"],
    "url": url,
    "external_checks": external_results,
    "findings": risk_report["findings"],
    "risk_score": risk_report["total_score"],
    "overall_risk": risk_report["overall_risk"]
}
with open("report.json", "w") as f:
    json.dump(
        report,
        f,
        indent=4
    )
print("\nReport saved to report.json")