# 🇨🇦 JEP California Solutions

**AI Accountability for the Golden State**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/downloads/)
[![SB 53](https://img.shields.io/badge/SB%2053-Frontier%20AI-blue)](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240SB53)
[![AB 2013](https://img.shields.io/badge/AB%202013-Training%20Data-blue)](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240AB2013)
[![SB 942](https://img.shields.io/badge/SB%20942-Content%20Transparency-blue)](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240SB942)

## 📋 Overview

California has enacted the most comprehensive suite of AI regulations in the United States, with **three landmark laws** taking effect in 2026. This directory provides complete **Judgment Event Protocol (JEP)** implementations for all three:

| Law | Effective Date | Focus | JEP Solution |
|-----|---------------|-------|--------------|
| **SB 53 (TFAIA)** | January 1, 2026 | Frontier model safety & transparency | [Frontier AI Framework →](/sb-53-tfaia) |
| **AB 2013 (TDTA)** | January 1, 2026 | Training data transparency | [Data Disclosure →](/ab-2013-tdta) |
| **SB 942** | August 2, 2026* | AI content watermarking & detection | [Content Provenance →](/sb-942-content) |

> *SB 942 effective date delayed to align with EU AI Act Article 50.

## 🎯 Why California Matters

| Reason | Significance |
|--------|--------------|
| **Largest US Economy** | California's GDP > most countries; compliance here is de facto national standard |
| **First-Mover Status** | First state to regulate frontier AI models, training data transparency, and content provenance |
| **High Penalties** | Up to **$1 million per violation** (SB 53) and **$5,000 per violation** (SB 942) |
| **National Influence** | California's laws often become de facto national standards |
| **Alignment with EU** | SB 942 now aligns with EU AI Act Article 50 (both effective August 2, 2026) |

## 📊 Three Laws, One Solution

JEP provides a unified technical framework that addresses all three California AI laws:

### SB 53 (Frontier Model Transparency)

| Requirement | JEP Implementation | Verification |
|-------------|-------------------|--------------|
| Frontier AI Framework | `publish_frontier_framework()` | `verify-california.py --sb53-framework` |
| Critical Safety Incident Reporting | `report_safety_incident()` | `verify-california.py --sb53-incident` |
| Pre-Deployment Transparency Reports | `publish_transparency_report()` | `verify-california.py --sb53-report` |
| Whistleblower Protections | Anonymous reporting channel | `verify-california.py --sb53-whistleblower` |

### AB 2013 (Training Data Transparency)

| Requirement | JEP Implementation | Verification |
|-------------|-------------------|--------------|
| Data Source Disclosure | `disclose_data_sources()` | `verify-california.py --ab2013-sources` |
| IP Status (copyright, trademark, patent) | `disclose_ip_status()` | `verify-california.py --ab2013-ip` |
| Personal Information Disclosure (CCPA) | `disclose_personal_info()` | `verify-california.py --ab2013-pii` |
| Data Processing Modifications | `disclose_data_processing()` | `verify-california.py --ab2013-processing` |
| Synthetic Data Usage | `disclose_synthetic_data()` | `verify-california.py --ab2013-synthetic` |

### SB 942 (AI Content Transparency)

| Requirement | JEP Implementation | Verification |
|-------------|-------------------|--------------|
| Free AI Detection Tool | `deploy_detection_tool()` | `verify-california.py --sb942-detection` |
| Latent Disclosures (Watermarking) | `add_latent_watermark()` | `verify-california.py --sb942-latent` |
| Manifest Disclosure Option | `add_manifest_option()` | `verify-california.py --sb942-manifest` |
| Licensee Compliance | `manage_licensee_compliance()` | `verify-california.py --sb942-licensee` |

## 🚀 Quick Start

```python
from jep.us.california import CaliforniaAICompliance

# Initialize compliance tracker for all three laws
tracker = CaliforniaAICompliance(
    company_name="AI Developer Inc.",
    company_type="frontier_developer",  # or "genai_developer", "content_provider"
    annual_revenue=600_000_000,  # >$500M threshold for SB 53
    monthly_users=2_000_000  # >1M threshold for SB 942
)

# SB 53: Publish Frontier AI Framework
framework = tracker.publish_frontier_framework({
    "risk_assessment_methodology": "NIST AI RMF",
    "capability_thresholds": {
        "catastrophic_risk": "10^26 FLOP",
        "mitigation_gates": ["third-party audit", "red-teaming"]
    },
    "cybersecurity_measures": {
        "model_weights": "hardware security modules",
        "access_control": "multi-party authorization"
    },
    "third_party_evaluators": ["Anthropic", "Scale AI"]
})

# AB 2013: Disclose training data
disclosure = tracker.disclose_training_data({
    "datasets": [
        {
            "source": "Common Crawl",
            "owner": "Public",
            "data_points": "250 billion tokens",
            "data_types": ["text", "code"],
            "ip_status": "may contain copyrighted material",
            "personal_info": True,
            "collection_period": "2020-2024"
        }
    ]
})

# SB 942: Deploy detection tool and add watermarks
detection_tool = tracker.deploy_detection_tool(
    endpoint="https://api.example.com/detect",
    rate_limit=1000,
    support_api=True
)

watermarked_content = tracker.add_latent_watermark(
    content=ai_generated_text,
    content_type="text",
    model_version="gpt-4",
    timestamp=time.time()
)
```

## 🏛️ Legal Foundation

JEP is stewarded by **HJS Foundation LTD** (Singapore CLG), a non-profit organization with permanent asset lock. The foundation's constitution explicitly prohibits:

- Distribution of profits to members (Article 7B)
- Transfer or sale of core assets (Article 67A)

**Registered Address**: 101 Thomson Road #28-03A, United Square, Singapore 307591

## 📁 Repository Structure

```
california/
├── README.md                          # This file
├── sb-53-tfaia/                        # SB 53 - Frontier Models
│   ├── README.md
│   ├── mapping.md
│   ├── implementation/
│   │   └── frontier_tracker.py
│   └── examples/
│       ├── frontier_framework.py
│       └── incident_reporting.py
├── ab-2013-tdta/                        # AB 2013 - Training Data
│   ├── README.md
│   ├── mapping.md
│   ├── implementation/
│   │   └── data_transparency_tracker.py
│   └── examples/
│       ├── openai_style_disclosure.py
│       └── anthropic_style_disclosure.py
├── sb-942-content/                      # SB 942 - Content Transparency
│   ├── README.md
│   ├── mapping.md
│   ├── implementation/
│   │   └── content_tracker.py
│   └── examples/
│       ├── detection_tool.py
│       └── latent_watermark.py
└── tests/
    └── verify-california.py
```

## 🔍 Verification

```bash
# Run complete California compliance verification
python tests/verify-california.py --all

# Run specific law verification
python tests/verify-california.py --sb53
python tests/verify-california.py --ab2013
python tests/verify-california.py --sb942
```

## 📚 References

- [SB 53: Transparency in Frontier Artificial Intelligence Act](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240SB53)
- [AB 2013: Generative AI Training Data Transparency Act](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240AB2013)
- [SB 942: California AI Transparency Act](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240SB942)
- [California Attorney General AI Enforcement](https://oag.ca.gov/)

## 📬 Contact

For California-specific inquiries:
- **Email**: signal@humanjudgment.org
- **GitHub**: [hjs-spec/jep-us-solutions](https://github.com/hjs-spec/jep-us-solutions)

---

*Last Updated: March 2026*
*Supporting California's leadership in AI governance*
```
