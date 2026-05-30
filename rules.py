def evaluate_risk(signals, external_data):

    findings = []

    # Rule 1 - Contact Information
    if not signals["emails"] and not signals["phones"]:
        findings.append({
            "element": "Contact Information",
            "external_evidence": "No email or phone found",
            "rule": "No Contact Information",
            "risk_category": "Business Verification",
            "severity": "High",
            "rationale": "Legitimate businesses usually provide contact information."
        })

    # Rule 2 - Privacy Policy
    if not signals["privacy_policy"]:
        findings.append({
            "element": "Privacy Policy",
            "external_evidence": "Privacy Policy page not found",
            "rule": "Missing Privacy Policy",
            "risk_category": "Compliance Risk",
            "severity": "Medium",
            "rationale": "Most legitimate businesses publish a privacy policy."
        })

    # Rule 3 - Terms & Conditions
    if not signals["terms_conditions"]:
        findings.append({
            "element": "Terms & Conditions",
            "external_evidence": "Terms page not found",
            "rule": "Missing Terms & Conditions",
            "risk_category": "Compliance Risk",
            "severity": "Medium",
            "rationale": "Terms and Conditions help establish business legitimacy."
        })

    # Rule 4 - Social Presence
    if len(signals["social_links"]) == 0:
        findings.append({
            "element": "Social Presence",
            "external_evidence": "0 social media links found",
            "rule": "No Social Presence",
            "risk_category": "Business Verification",
            "severity": "Medium",
            "rationale": "Legitimate businesses generally maintain public social profiles."
        })

    # Rule 5 - Suspicious Marketing Claims
    suspicious_keywords = [
        "guaranteed returns",
        "risk free",
        "double your money",
        "instant profit",
        "earn daily",
        "100% profit"
    ]

    text = signals["text_content"].lower()

    for keyword in suspicious_keywords:
        if keyword in text:
            findings.append({
                "element": "Website Content",
                "external_evidence": f"Keyword detected: {keyword}",
                "rule": "Suspicious Marketing Claim",
                "risk_category": "Fraud Risk",
                "severity": "High",
                "rationale": "Unrealistic financial claims are commonly used in scams."
            })

    # Rule 6 - Free Email Provider
    free_domains = [
        "gmail.com",
        "yahoo.com",
        "hotmail.com",
        "outlook.com"
    ]

    for email in signals["emails"]:

        domain = email.split("@")[-1].lower()

        if domain in free_domains:
            findings.append({
                "element": "Business Email",
                "external_evidence": email,
                "rule": "Free Email Provider",
                "risk_category": "Business Verification",
                "severity": "Medium",
                "rationale": "Businesses usually use their own domain email addresses."
            })

    # Rule 7 - Domain Age
    domain_age = external_data.get("domain_age_days")

    if domain_age is not None:

        if domain_age < 90:
            findings.append({
                "element": "Domain",
                "external_evidence": f"Domain age = {domain_age} days",
                "rule": "New Domain",
                "risk_category": "Trust Risk",
                "severity": "High",
                "rationale": "Very recently registered domains are commonly associated with fraudulent activity."
            })

        elif domain_age < 365:
            findings.append({
                "element": "Domain",
                "external_evidence": f"Domain age = {domain_age} days",
                "rule": "Young Domain",
                "risk_category": "Trust Risk",
                "severity": "Medium",
                "rationale": "Recently registered domains have limited operating history."
            })

    # Risk Score Calculation
    severity_score = {
        "High": 25,
        "Medium": 15,
        "Low": 5
    }

    total_score = sum(
        severity_score[f["severity"]]
        for f in findings
    )

    # Overall Risk
    if total_score >= 50:
        overall_risk = "HIGH"
    elif total_score >= 20:
        overall_risk = "MEDIUM"
    else:
        overall_risk = "LOW"

    return {
        "findings": findings,
        "total_score": total_score,
        "overall_risk": overall_risk
    }