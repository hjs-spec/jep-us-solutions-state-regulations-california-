# 🇨🇦 California AB 2013: Generative AI Training Data Transparency Act

**Complete JEP Implementation for Training Data Disclosure Requirements**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/downloads/)
[![Effective Date](https://img.shields.io/badge/Effective-January%201%2C%202026-red)](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240AB2013)

## 📋 Overview

The **Generative AI Training Data Transparency Act (AB 2013)** , effective **January 1, 2026**, requires developers of generative AI systems that are publicly available to disclose detailed summaries of their training datasets. This law applies to any generative AI system made available to the public, regardless of the developer's location or revenue.

### Applicability

| Criteria | Requirement |
|----------|-------------|
| **System Type** | Any generative AI system (text, image, audio, video, code) |
| **Availability** | Made publicly available (free or paid) |
| **Developer Location** | Anywhere (California law applies to products available to Californians) |
| **Exemptions** | Systems under development not yet released; internal corporate tools |

## 🎯 Key Requirements

AB 2013 requires developers to post or make available a summary of the training data used to build the AI system, including **12 specific categories of information**:

| Section | Requirement | Deadline | Enforcement |
|---------|-------------|----------|-------------|
| **§ 3110(a)** | Post training data summary online | Upon public release | UCL (Business & Professions Code § 17200) |
| **§ 3110(b)(1)** | Data sources and owners | Upon public release | UCL enforcement |
| **§ 3110(b)(2)** | How data furthers system purpose | Upon public release | UCL enforcement |
| **§ 3110(b)(3)** | Number of data points | Upon public release | UCL enforcement |
| **§ 3110(b)(4)** | Data type description | Upon public release | UCL enforcement |
| **§ 3110(b)(5)** | Intellectual Property status | Upon public release | UCL enforcement |
| **§ 3110(b)(6)** | Whether data was purchased/licensed | Upon public release | UCL enforcement |
| **§ 3110(b)(7)** | Whether data contains personal information | Upon public release | UCL enforcement |
| **§ 3110(b)(8)** | Whether data contains aggregate consumer information | Upon public release | UCL enforcement |
| **§ 3110(b)(9)** | Data processing/modification | Upon public release | UCL enforcement |
| **§ 3110(b)(10)** | Time period of collection | Upon public release | UCL enforcement |
| **§ 3110(b)(11)** | Date first used in development | Upon public release | UCL enforcement |
| **§ 3110(b)(12)** | Whether synthetic data was used | Upon public release | UCL enforcement |
| **§ 3110(c)** | Summary must be understandable | Upon public release | UCL enforcement |

## 📊 Detailed Requirements Mapping

### Section 3110(b)(1): Data Sources and Owners

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **Source identification** | `data_source` field | `source["name"] = "Common Crawl"` | `verify-california.py --ab2013-source` |
| **Owner identification** | `data_owner` field | `source["owner"] = "Public domain"` | `verify-california.py --ab2013-owner` |
| **Multiple sources** | List of sources | `sources = [source1, source2]` | `verify-california.py --ab2013-multiple` |

### Section 3110(b)(2): How Data Furthers System Purpose

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **Purpose alignment** | `purpose_alignment` field | `source["purpose"] = "Language understanding"` | `verify-california.py --ab2013-purpose` |

### Section 3110(b)(3): Number of Data Points

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **Exact count** | `data_points_exact` field | `source["data_points_exact"] = 250000000` | `verify-california.py --ab2013-exact` |
| **Range or estimate** | `data_points_range` field | `source["data_points_range"] = "200-300M"` | `verify-california.py --ab2013-range` |

### Section 3110(b)(4): Data Type Description

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **Data type** | `data_types` field | `source["data_types"] = ["text", "code"]` | `verify-california.py --ab2013-types` |
| **Annotation description** | `annotation_types` field | `source["annotations"] = ["labels", "ratings"]` | `verify-california.py --ab2013-annotations` |
| **Characteristics** | `characteristics` field | `source["characteristics"] = ["QA pairs"]` | `verify-california.py --ab2013-characteristics` |

### Section 3110(b)(5): Intellectual Property Status

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **Copyright status** | `copyright_status` field | `source["copyright_status"] = "may contain copyrighted material"` | `verify-california.py --ab2013-copyright` |
| **Trademark status** | `trademark_status` field | `source["trademark_status"] = "none"` | `verify-california.py --ab2013-trademark` |
| **Patent status** | `patent_status` field | `source["patent_status"] = "none"` | `verify-california.py --ab2013-patent` |
| **Public domain** | `public_domain` field | `source["public_domain"] = True` | `verify-california.py --ab2013-public` |

### Section 3110(b)(6): Commercial Arrangements

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **Purchased data** | `purchased` field | `source["purchased"] = True` | `verify-california.py --ab2013-purchased` |
| **Licensed data** | `licensed` field | `source["licensed"] = True` | `verify-california.py --ab2013-licensed` |
| **License terms** | `license_terms` field | `source["license_terms"] = "CC BY-SA 4.0"` | `verify-california.py --ab2013-license` |

### Section 3110(b)(7): Personal Information

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **Contains personal info** | `contains_personal_info` field | `source["contains_personal_info"] = True` | `verify-california.py --ab2013-personal` |
| **PII categories** | `pii_categories` field | `source["pii_categories"] = ["names", "emails"]` | `verify-california.py --ab2013-pii-categories` |

### Section 3110(b)(8): Aggregate Consumer Information

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **Contains aggregate info** | `contains_aggregate_info` field | `source["contains_aggregate_info"] = True` | `verify-california.py --ab2013-aggregate` |
| **Aggregate description** | `aggregate_description` field | `source["aggregate_description"] = "demographics"` | `verify-california.py --ab2013-aggregate-desc` |

### Section 3110(b)(9): Data Processing

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **Processing description** | `processing_description` field | `source["processing"] = ["cleaned", "deduplicated"]` | `verify-california.py --ab2013-processing` |
| **Modification details** | `modifications` field | `source["modifications"] = ["tokenized", "filtered"]` | `verify-california.py --ab2013-modifications` |

### Section 3110(b)(10): Collection Time Period

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **Collection period** | `collection_period` field | `source["collection_period"] = "2020-2024"` | `verify-california.py --ab2013-period` |
| **Ongoing collection** | `ongoing_collection` field | `source["ongoing_collection"] = True` | `verify-california.py --ab2013-ongoing` |

### Section 3110(b)(11): First Use Date

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **First use date** | `first_use_date` field | `source["first_use_date"] = "2023-06-01"` | `verify-california.py --ab2013-first-use` |

### Section 3110(b)(12): Synthetic Data

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **Contains synthetic data** | `contains_synthetic_data` field | `source["contains_synthetic_data"] = True` | `verify-california.py --ab2013-synthetic` |
| **Synthetic data description** | `synthetic_description` field | `source["synthetic_description"] = "augmented with GPT-4"` | `verify-california.py --ab2013-synthetic-desc` |
| **Ongoing synthetic generation** | `ongoing_synthetic` field | `source["ongoing_synthetic"] = True` | `verify-california.py --ab2013-synthetic-ongoing` |

## 🔧 Implementation

### Training Data Transparency Tracker

```python
from jep.us.california import DataTransparencyTracker

tracker = DataTransparencyTracker(
    company_name="Generative AI Inc.",
    system_name="Text-Gen-v2",
    system_version="2.1.0",
    system_description="Large language model for text generation",
    release_date=time.time(),
    documentation_url="https://genai.com/transparency"
)

# § 3110(a): Post training data summary online
disclosure = tracker.disclose_training_data({
    "system_name": "Text-Gen-v2",
    "system_version": "2.1.0",
    "release_date": "2026-01-15",
    "disclosure_date": time.time(),
    "documentation_url": "https://genai.com/transparency",
    "datasets": [
        {
            # § 3110(b)(1): Data sources and owners
            "source": "Common Crawl",
            "source_url": "https://commoncrawl.org",
            "owner": "Common Crawl Foundation",
            "owner_type": "non-profit",
            
            # § 3110(b)(2): How data furthers system purpose
            "purpose_alignment": "Provides diverse web text for language understanding",
            
            # § 3110(b)(3): Number of data points
            "data_points_exact": 250_000_000_000,
            "data_points_unit": "tokens",
            
            # § 3110(b)(4): Data type description
            "data_types": ["text", "html", "metadata"],
            "annotation_types": ["none"],
            "characteristics": ["web crawl", "multi-lingual", "diverse domains"],
            
            # § 3110(b)(5): Intellectual Property status
            "copyright_status": "may contain copyrighted material",
            "trademark_status": "may contain trademarks",
            "patent_status": "none",
            "public_domain": False,
            "ip_explanation": "Common Crawl data may include copyrighted web pages. Use is believed to be fair use for training.",
            
            # § 3110(b)(6): Commercial arrangements
            "purchased": False,
            "licensed": False,
            "license_terms": "Public domain crawl data",
            
            # § 3110(b)(7): Personal information
            "contains_personal_info": True,
            "pii_categories": ["names", "email addresses", "IP addresses"],
            "pii_handling": "Data may contain PII; no specific filtering applied",
            
            # § 3110(b)(8): Aggregate consumer information
            "contains_aggregate_info": False,
            "aggregate_description": None,
            
            # § 3110(b)(9): Data processing
            "processing_description": [
                "HTML tag removal",
                "language filtering",
                "deduplication",
                "tokenization"
            ],
            "modifications": [
                "Text extracted from HTML",
                "Non-English content filtered (target: English)",
                "Near-duplicate documents removed"
            ],
            
            # § 3110(b)(10): Time period of collection
            "collection_period": "2020-2024",
            "ongoing_collection": False,
            
            # § 3110(b)(11): Date first used in development
            "first_use_date": "2023-01-15",
            
            # § 3110(b)(12): Synthetic data
            "contains_synthetic_data": False,
            "synthetic_description": None,
            "ongoing_synthetic": False
        },
        {
            "source": "GitHub Code",
            "source_url": "https://github.com",
            "owner": "Various open source developers",
            "owner_type": "public",
            "purpose_alignment": "Provides code examples for code generation capabilities",
            "data_points_exact": 50_000_000,
            "data_points_unit": "files",
            "data_types": ["code", "comments", "documentation"],
            "annotation_types": ["language labels", "license info"],
            "copyright_status": "various open source licenses",
            "trademark_status": "may contain trademarks",
            "purchased": False,
            "licensed": True,
            "license_terms": "MIT, Apache 2.0, GPL, etc.",
            "contains_personal_info": False,
            "processing_description": ["license filtering", "deduplication"],
            "collection_period": "2015-2024",
            "first_use_date": "2023-03-01"
        }
    ],
    "synthetic_data_summary": {
        "contains_synthetic_data": True,
        "synthetic_description": "Data augmentation using GPT-4 for instruction tuning",
        "synthetic_proportion": "5% of training data",
        "ongoing_synthetic": True,
        "synthetic_methods": ["prompt-based generation", "self-instruct"]
    },
    "overall_summary": "Text-Gen-v2 was trained on a combination of public web crawl data (Common Crawl) and open source code repositories. Approximately 5% of training data was synthetically generated for instruction tuning purposes. Data selection was focused on English-language content, which may impact performance on other languages. Training data may include personal information from public sources."
})

print(f"Disclosure ID: {disclosure['disclosure_id']}")
print(f"Documentation URL: {disclosure['documentation_url']}")
print(f"Datasets disclosed: {len(disclosure['datasets'])}")
```

### Complete Disclosure Examples

#### OpenAI-Style Disclosure (ChatGPT)

```python
# Example: OpenAI ChatGPT disclosure
openai_disclosure = tracker.disclose_training_data({
    "system_name": "ChatGPT",
    "system_version": "GPT-4",
    "release_date": "2023-03-14",
    "disclosure_date": "2026-01-01",
    "documentation_url": "https://openai.com/transparency",
    "datasets": [
        {
            "source": "Common Crawl",
            "owner": "Public",
            "data_points_range": "hundreds of billions of tokens",
            "data_types": ["web text"],
            "copyright_status": "may contain copyrighted material",
            "purchased": False,
            "licensed": False,
            "contains_personal_info": True,
            "collection_period": "2020-2023"
        },
        {
            "source": "Books2",
            "owner": "Various publishers",
            "data_points_range": "tens of billions of tokens",
            "data_types": ["books", "academic papers"],
            "copyright_status": "copyrighted",
            "purchased": True,
            "licensed": True,
            "contains_personal_info": False,
            "collection_period": "1960-2022"
        },
        {
            "source": "Wikipedia",
            "owner": "Wikimedia Foundation",
            "data_points_exact": 6_000_000,
            "data_types": ["encyclopedic text"],
            "copyright_status": "CC BY-SA",
            "purchased": False,
            "licensed": True,
            "license_terms": "CC BY-SA",
            "contains_personal_info": True,
            "collection_period": "2023"
        }
    ]
})
```

#### Anthropic-Style Disclosure (Claude)

```python
# Example: Anthropic Claude disclosure
anthropic_disclosure = tracker.disclose_training_data({
    "system_name": "Claude",
    "system_version": "3.5 Sonnet",
    "release_date": "2024-06-20",
    "disclosure_date": "2026-01-01",
    "documentation_url": "https://anthropic.com/transparency",
    "datasets": [
        {
            "source": "Public web crawl",
            "owner": "Various",
            "data_points_exact": 500_000_000,
            "data_types": ["text"],
            "copyright_status": "may include copyrighted material",
            "purchased": False,
            "licensed": False,
            "contains_personal_info": True,
            "collection_period": "2019-2023"
        },
        {
            "source": "Instruction tuning dataset",
            "owner": "Anthropic",
            "data_points_exact": 10_000_000,
            "data_types": ["prompt-response pairs"],
            "copyright_status": "proprietary",
            "purchased": False,
            "licensed": False,
            "contains_personal_info": False,
            "contains_synthetic_data": True,
            "synthetic_description": "Generated using Constitutional AI process",
            "collection_period": "2023-2024"
        }
    ]
})
```

## 🔍 Verification

```bash
# Run AB 2013 compliance verification
python tests/verify-california.py --ab2013

# Output:
# ========================================
# AB 2013 TRAINING DATA TRANSPARENCY ACT
# ========================================
# ✅ § 3110(a): Publicly available summary
# ✅ § 3110(b)(1): Data sources and owners
# ✅ § 3110(b)(2): Purpose alignment
# ✅ § 3110(b)(3): Number of data points
# ✅ § 3110(b)(4): Data type description
# ✅ § 3110(b)(5): IP status
# ✅ § 3110(b)(6): Commercial arrangements
# ✅ § 3110(b)(7): Personal information
# ✅ § 3110(b)(8): Aggregate consumer information
# ✅ § 3110(b)(9): Data processing
# ✅ § 3110(b)(10): Collection period
# ✅ § 3110(b)(11): First use date
# ✅ § 3110(b)(12): Synthetic data
# ✅ § 3110(c): Understandable summary
# ========================================
# FULL COMPLIANCE VERIFIED
# ========================================
```

## ⚖️ Enforcement

AB 2013 is enforced through California's **Unfair Competition Law (UCL)** , Business & Professions Code § 17200. Violations can result in:

- Injunctive relief (court order to comply)
- Restitution to affected consumers
- Civil penalties up to **$2,500 per violation**
- Attorney's fees

While there is no specific penalty amount in the statute, the UCL allows for civil penalties of up to $2,500 per violation .

## 📚 References

- [Full Text of AB 2013](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240AB2013)
- [California Unfair Competition Law (UCL), Bus. & Prof. Code § 17200](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=17200)
- [California Attorney General AI Enforcement](https://oag.ca.gov/)

## 📬 Contact

For AB 2013-specific inquiries:
- **Email**: ab2013@humanjudgment.org
- **GitHub**: [hjs-spec/jep-us-solutions](https://github.com/hjs-spec/jep-us-solutions)

---

*Last Updated: March 2026*
*Supporting transparency in generative AI training data*
```
