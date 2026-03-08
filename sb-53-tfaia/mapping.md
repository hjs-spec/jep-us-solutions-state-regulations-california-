# JEP Mapping to California SB 53 (Transparency in Frontier Artificial Intelligence Act)

**Detailed Section-by-Section Mapping with Code Examples and Verification Methods**

## 📋 Overview

This document provides a comprehensive mapping between the **Judgment Event Protocol (JEP)** and California's **Transparency in Frontier Artificial Intelligence Act (SB 53)** , which took effect **January 1, 2026**.

The law applies to developers of frontier AI models with training compute exceeding **10²⁶ FLOP** or annual revenue exceeding **$500 million** .

---

## 📊 Section 11547.6: Requirements for Frontier Model Developers

### Section 11547.6(a): Frontier AI Framework

Developers must publish a written framework describing their practices for managing risks from frontier models.

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 11547.6(a)(1)** - Risk assessment methodology | `risk_assessment_methodology` field | `framework["risk_method"] = "NIST AI RMF"` | `verify-california.py --sb53-a1` |
| **§ 11547.6(a)(2)** - Capability thresholds | `capability_thresholds` field | `framework["thresholds"] = {"dangerous": "10^26 FLOP"}` | `verify-california.py --sb53-a2` |
| **§ 11547.6(a)(3)** - Mitigation measures | `mitigation_gates` field | `framework["mitigations"] = ["third-party audit"]` | `verify-california.py --sb53-a3` |
| **§ 11547.6(a)(4)** - Cybersecurity protocols | `cybersecurity_measures` field | `framework["cybersecurity"] = {"model_weights": "HSM"}` | `verify-california.py --sb53-a4` |
| **§ 11547.6(a)(5)** - Third-party evaluation | `third_party_evaluators` field | `framework["evaluators"] = ["Anthropic", "Scale AI"]` | `verify-california.py --sb53-a5` |
| **§ 11547.6(a)(6)** - Framework updates | `update_framework()` method | `tracker.update_framework()` | `verify-california.py --sb53-a6` |
| **§ 11547.6(a)(7)** - Public accessibility | `publish_framework()` method | `tracker.publish_framework()` | `verify-california.py --sb53-a7` |

**Code Example:**
```python
from jep.us.california import FrontierAITracker

tracker = FrontierAITracker(
    company_name="Frontier AI Labs",
    annual_revenue=600_000_000,
    estimated_training_flops=5e26
)

# § 11547.6(a)(1)-(7): Complete Frontier AI Framework
framework = tracker.publish_frontier_framework({
    # § 11547.6(a)(1): Risk assessment methodology
    "risk_assessment_methodology": {
        "framework": "NIST AI RMF v1.0",
        "risk_categories": ["catastrophic", "dangerous", "misuse"],
        "assessment_frequency": "quarterly",
        "responsible_party": "Safety Committee"
    },
    
    # § 11547.6(a)(2): Capability thresholds
    "capability_thresholds": {
        "catastrophic_risk": {
            "threshold": "10^26 FLOP",
            "description": "Models requiring extraordinary safeguards"
        },
        "dangerous_capabilities": [
            {
                "capability": "self-replication",
                "threshold": "90% success rate",
                "mitigation_gate": "pre-deployment"
            },
            {
                "capability": "cyber-offense",
                "threshold": "80% CTF success",
                "mitigation_gate": "pre-training"
            }
        ]
    },
    
    # § 11547.6(a)(3): Mitigation measures
    "mitigation_gates": [
        {
            "gate": "pre-training",
            "requirements": [
                {"requirement": "third-party audit", "status": "implemented"},
                {"requirement": "red-teaming", "status": "implemented"}
            ]
        },
        {
            "gate": "pre-deployment",
            "requirements": [
                {"requirement": "independent evaluation", "status": "implemented"},
                {"requirement": "safety tests", "status": "implemented"}
            ]
        }
    ],
    
    # § 11547.6(a)(4): Cybersecurity measures
    "cybersecurity_measures": {
        "model_weights": {
            "storage": "hardware security modules (HSM)",
            "access": "multi-party authorization (MPA)",
            "audit": "immutable logging"
        },
        "training_infrastructure": {
            "network": "air-gapped",
            "access": "biometric + MFA",
            "monitoring": "24/7 SOC"
        },
        "api_access": {
            "authentication": "OAuth 2.0 + API keys",
            "rate_limiting": "implemented",
            "audit_logging": "real-time"
        }
    },
    
    # § 11547.6(a)(5): Third-party evaluation
    "third_party_evaluators": [
        {
            "name": "Anthropic",
            "scope": "safety evaluation",
            "frequency": "quarterly",
            "last_evaluation": "2026-02-15",
            "next_evaluation": "2026-05-15"
        },
        {
            "name": "Scale AI",
            "scope": "red-teaming",
            "frequency": "monthly",
            "last_evaluation": "2026-03-01",
            "next_evaluation": "2026-04-01"
        }
    ],
    
    # § 11547.6(a)(6): Framework updates
    "update_policy": {
        "frequency": "quarterly",
        "trigger_events": ["new capabilities", "incidents", "regulatory changes"],
        "review_process": "Safety Committee approval",
        "publication": "immediate"
    },
    
    # § 11547.6(a)(7): Public accessibility
    "publication": {
        "url": "https://frontier-ai.com/framework",
        "format": "HTML + JSON-LD",
        "last_updated": "2026-03-01",
        "version": "2.0"
    },
    
    "framework_id": "FAI-FW-2026-001",
    "effective_date": "2026-01-01",
    "review_date": "2026-12-31"
})

# Verify framework completeness
assert framework.get("risk_assessment_methodology") is not None
assert len(framework.get("mitigation_gates", [])) > 0
assert len(framework.get("third_party_evaluators", [])) > 0
```

---

### Section 11547.6(b): Critical Safety Incident Reporting

Developers must report safety incidents to the California Governor's Office of Emergency Services (CalOES).

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 11547.6(b)(1)** - Report within 15 days | `report_safety_incident()` | `tracker.report_safety_incident()` | `verify-california.py --sb53-b1` |
| **§ 11547.6(b)(2)** - 24-hour reporting for life-threatening | `report_critical_incident()` | `tracker.report_critical_incident()` | `verify-california.py --sb53-b2` |
| **§ 11547.6(b)(3)** - Incident description | `description` field | `incident["description"] = "..."` | `verify-california.py --sb53-b3` |
| **§ 11547.6(b)(4)** - Root cause analysis | `root_cause` field | `incident["root_cause"] = "..."` | `verify-california.py --sb53-b4` |
| **§ 11547.6(b)(5)** - Remediation steps | `remediation` field | `incident["remediation"] = ["patched"]` | `verify-california.py --sb53-b5` |
| **§ 11547.6(b)(6)** - Affected systems | `affected_systems` field | `incident["affected_systems"] = ["api"]` | `verify-california.py --sb53-b6` |
| **§ 11547.6(b)(7)** - Affected users | `affected_users` field | `incident["affected_users"] = 1234` | `verify-california.py --sb53-b7` |

**Code Example:**
```python
# § 11547.6(b)(1): Standard safety incident (15-day reporting)
incident = tracker.report_safety_incident({
    "incident_id": "INC-2026-001",
    "incident_type": "safety_breach",
    "discovery_date": time.time(),
    "reporting_deadline": time.time() + 1296000,  # 15 days
    
    # § 11547.6(b)(3): Description
    "description": "Model generated harmful content despite safety filters after adversarial prompt injection",
    
    # § 11547.6(b)(4): Root cause
    "root_cause": "Adversarial prompt bypassed safety filters due to edge case in tokenization",
    
    # § 11547.6(b)(5): Remediation
    "remediation_steps": [
        {
            "step": "Deployed updated safety filter",
            "completed": True,
            "completion_date": time.time() + 86400
        },
        {
            "step": "Retrained filter on adversarial examples",
            "completed": True,
            "completion_date": time.time() + 172800
        },
        {
            "step": "Added monitoring for similar attacks",
            "completed": True,
            "completion_date": time.time() + 259200
        }
    ],
    
    # § 11547.6(b)(6): Affected systems
    "affected_systems": ["chat-api", "content-filter", "prompt-safety"],
    
    # § 11547.6(b)(7): Affected users
    "affected_users": 1234,
    
    "severity": "MODERATE",
    "reported_to_california": True,
    "reporting_channel": "official",
    "notified_users": True,
    "notified_date": time.time() + 172800
})

# § 11547.6(b)(2): Critical incident (24-hour reporting)
if incident["severity"] == "CRITICAL_LIFE_THREATENING":
    critical = tracker.report_critical_incident({
        "incident_id": incident["incident_id"],
        "reporting_deadline": time.time() + 86400,  # 24 hours
        "emergency_contact": "CalOES@state.ca.gov",
        "law_enforcement_notified": True,
        "law_enforcement_agency": "FBI Cyber Division",
        "case_number": "CYBER-2026-001",
        "public_safety_impact": "Potential for physical harm if exploited",
        "containment_measures": ["api_shutdown", "model_sandboxed"]
    })

# Verify reporting deadlines
assert incident["reporting_deadline"] > time.time()  # Within 15 days
if critical:
    assert critical["reporting_deadline"] - critical["discovery_date"] <= 86400  # 24 hours
```

---

### Section 11547.6(c): Pre-Deployment Transparency Reports

Developers must publish transparency reports before deploying frontier models.

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 11547.6(c)(1)** - Deployment date | `deployment_date` field | `report["deployment_date"] = time.time()` | `verify-california.py --sb53-c1` |
| **§ 11547.6(c)(2)** - Supported languages | `languages` field | `report["languages"] = ["en", "es", "zh"]` | `verify-california.py --sb53-c2` |
| **§ 11547.6(c)(3)** - Supported modalities | `modalities` field | `report["modalities"] = ["text", "image"]` | `verify-california.py --sb53-c3` |
| **§ 11547.6(c)(4)** - Intended uses | `intended_uses` field | `report["intended_uses"] = ["code", "content"]` | `verify-california.py --sb53-c4` |
| **§ 11547.6(c)(5)** - Performance metrics | `performance_metrics` field | `report["performance"] = {"accuracy": 0.97}` | `verify-california.py --sb53-c5` |
| **§ 11547.6(c)(6)** - Evaluation results | `evaluation_results` field | `report["evaluation"] = {"red_teaming": "passed"}` | `verify-california.py --sb53-c6` |

**Code Example:**
```python
# § 11547.6(c): Complete pre-deployment transparency report
deployment_report = tracker.publish_transparency_report({
    "model_name": "Frontier-Model-v2",
    "model_version": "2.1.0",
    
    # § 11547.6(c)(1): Deployment date
    "deployment_date": time.time(),
    
    # § 11547.6(c)(2): Languages
    "languages": ["en", "es", "fr", "de", "zh", "ja", "ko", "ar"],
    
    # § 11547.6(c)(3): Modalities
    "modalities": ["text", "code", "image", "audio"],
    
    # § 11547.6(c)(4): Intended uses
    "intended_uses": [
        "code generation",
        "content creation",
        "summarization",
        "translation",
        "creative writing"
    ],
    "prohibited_uses": [
        "harmful content generation",
        "surveillance",
        "weapons development",
        "unauthorized data collection"
    ],
    
    # § 11547.6(c)(5): Performance metrics
    "performance_metrics": {
        "accuracy": 0.97,
        "mmlu": 0.89,
        "human_eval": 0.82,
        "truthful_qa": 0.83,
        "bbh": 0.85,
        "gsm8k": 0.88
    },
    
    # § 11547.6(c)(6): Evaluation results
    "evaluation_results": {
        "red_teaming": {
            "status": "passed",
            "date": "2026-02-15",
            "findings": 12,
            "resolved": 12
        },
        "adversarial_testing": {
            "status": "passed",
            "date": "2026-02-20",
            "attack_success_rate": 0.03
        },
        "bias_assessment": {
            "status": "passed",
            "date": "2026-02-25",
            "disparate_impact": 0.96
        },
        "safety_evaluation": {
            "status": "passed",
            "date": "2026-03-01",
            "harmful_content_rate": 0.001
        }
    },
    
    "model_card": {
        "url": "https://frontier-ai.com/models/v2",
        "format": "JSON-LD",
        "last_updated": "2026-03-01"
    }
})

# Verify report completeness
assert deployment_report["deployment_date"] <= time.time()
assert len(deployment_report["languages"]) > 0
assert len(deployment_report["intended_uses"]) > 0
assert deployment_report["performance_metrics"] is not None
```

---

### Section 11547.6(d): Whistleblower Protections

Developers must establish protections for employees who report violations.

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 11547.6(d)(1)** - Anonymous reporting channel | `create_anonymous_channel()` | `tracker.create_anonymous_channel()` | `verify-california.py --sb53-d1` |
| **§ 11547.6(d)(2)** - Non-retaliation policy | `publish_non_retaliation_policy()` | `tracker.publish_non_retaliation_policy()` | `verify-california.py --sb53-d2` |
| **§ 11547.6(d)(3)** - Report tracking | `log_whistleblower_report()` | `tracker.log_whistleblower_report()` | `verify-california.py --sb53-d3` |

**Code Example:**
```python
# § 11547.6(d)(1): Anonymous reporting channel
anonymous_channel = tracker.create_anonymous_channel({
    "channel_name": "Ethics Hotline",
    "contact_email": "ethics@frontier-ai.com",
    "encryption_method": "PGP",
    "public_key": "-----BEGIN PGP PUBLIC KEY BLOCK----- ...",
    "retention_days": 365,
    "access_control": "HR Director only",
    "third_party_admin": "EthicsPoint",
    "languages": ["en", "es", "zh", "hi"]
})

# § 11547.6(d)(2): Non-retaliation policy
policy = tracker.publish_non_retaliation_policy({
    "policy_id": "HR-POL-001",
    "effective_date": "2026-01-01",
    "scope": "All employees and contractors",
    "prohibited_actions": [
        "termination",
        "demotion",
        "harassment",
        "discrimination",
        "retaliation"
    ],
    "reporting_channels": ["Ethics Hotline", "HR Department", "Legal Department"],
    "investigation_process": {
        "timeline": "30 days",
        "confidentiality": "maintained",
        "appeal_rights": True
    },
    "enforcement": "Zero tolerance",
    "penalties": ["termination", "legal action", "referral to authorities"],
    "training_required": "annual"
})

# § 11547.6(d)(3): Log whistleblower report
whistleblower_report = tracker.log_whistleblower_report({
    "report_id": "WB-2026-001",
    "report_date": time.time(),
    "channel": "Ethics Hotline",
    "allegations": [
        "Safety incident not properly reported",
        "Management instructed to hide data"
    ],
    "status": "INVESTIGATING",
    "investigator": "HR-001",
    "investigation_deadline": time.time() + 2592000,  # 30 days
    "protected_status": True,
    "confidential": True
})

# Verify protections in place
assert anonymous_channel["encryption_method"] == "PGP"
assert "termination" in policy["prohibited_actions"]
assert whistleblower_report["protected_status"] is True
```

---

### Section 11547.6(e): Annual Compliance Certification

Developers must certify compliance annually.

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 11547.6(e)(1)** - Annual certification | `certify_compliance()` | `tracker.certify_compliance()` | `verify-california.py --sb53-e1` |
| **§ 11547.6(e)(2)** - Attestations | `attestations` field | `cert["attestations"] = ["framework published"]` | `verify-california.py --sb53-e2` |
| **§ 11547.6(e)(3)** - Evidence attachment | `evidence_attached` field | `cert["evidence"] = ["audit_report.pdf"]` | `verify-california.py --sb53-e3` |

**Code Example:**
```python
# § 11547.6(e): Annual compliance certification
certification = tracker.certify_compliance({
    "certification_period": "2026",
    "certification_date": time.time(),
    "certifying_officer": "Chief Compliance Officer",
    "certifying_officer_title": "CCO",
    "attestations": [
        "Frontier framework published and maintained throughout 2026",
        "All safety incidents properly reported within required timeframes",
        "Pre-deployment reports completed for all deployed models",
        "Whistleblower protections in place and accessible",
        "No violations of SB 53 during certification period",
        "All required records maintained for inspection"
    ],
    "evidence_attached": [
        "frontier_framework_2026.pdf",
        "incident_logs_2026.json",
        "pre_deployment_reports_2026.json",
        "whistleblower_policy.pdf",
        "third_party_audit_2026.pdf"
    ],
    "previous_certification": "2025-03-01",
    "next_certification_due": "2027-03-01"
})

# Sign the certification
certification["signature"] = tracker._sign(certification)

# Verify certification
assert len(certification["attestations"]) >= 4
assert len(certification["evidence_attached"]) > 0
assert certification["signature"] is not None
```

---

## ✅ Penalties and Enforcement

| Violation | Penalty | JEP Mitigation |
|-----------|---------|----------------|
| **Failure to publish framework** | Up to $1 million | Automatic framework generation |
| **Late incident reporting** | Up to $1 million | Deadline tracking + alerts |
| **Missing pre-deployment report** | Up to $1 million | Deployment gating |
| **Whistleblower retaliation** | Additional penalties | Protected reporting channel |
| **False certification** | Up to $1 million + criminal | Cryptographic signatures |

---

## 📚 References

- [Full Text of SB 53](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240SB53)
- [California Governor's Office of Emergency Services (CalOES)](https://www.caloes.ca.gov/)
- [California Attorney General AI Enforcement](https://oag.ca.gov/)

## 📬 Contact

For SB 53-specific inquiries:
- **Email**: sb53@humanjudgment.org
- **GitHub**: [hjs-spec/jep-us-solutions](https://github.com/hjs-spec/jep-us-solutions)

---

*Last Updated: March 2026*
```
