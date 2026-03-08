# JEP Mapping to California AB 2013 (Generative AI Training Data Transparency Act)

**Detailed Section-by-Section Mapping with Code Examples and Verification Methods**

## 📋 Overview

This document provides a comprehensive mapping between the **Judgment Event Protocol (JEP)** and California's **Generative AI Training Data Transparency Act (AB 2013)** , which took effect **January 1, 2026**.

The law applies to any generative AI system made available to the public, requiring developers to disclose detailed summaries of their training datasets .

---

## 📊 Section 3110: Training Data Transparency

### Section 3110(a): Public Availability Requirement

Developers must post or make available a summary of the training data used to build the AI system.

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 3110(a)** - Publicly available summary | `disclose_training_data()` | `tracker.disclose_training_data()` | `verify-california.py --ab2013-a` |
| **§ 3110(a)** - Posted online | `documentation_url` field | `disclosure["url"] = "https://..."` | `verify-california.py --ab2013-url` |

**Code Example:**
```python
from jep.us.california import DataTransparencyTracker

tracker = DataTransparencyTracker(
    company_name="GenAI Corp",
    system_name="TextGen-v2"
)

disclosure = tracker.disclose_training_data({
    "system_name": "TextGen-v2",
    "system_version": "2.1.0",
    "release_date": "2026-01-15",
    "disclosure_date": time.time(),
    "documentation_url": "https://genai.com/transparency",
    "datasets": []
})

assert disclosure["documentation_url"] is not None
assert disclosure["disclosure_date"] <= time.time()
```

---

### Section 3110(b)(1): Data Sources and Owners

Identify the sources of data used to train the AI system, including the owners of the data.

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 3110(b)(1)** - Source identification | `source` field | `dataset["source"] = "Common Crawl"` | `verify-california.py --ab2013-b1-source` |
| **§ 3110(b)(1)** - Source URL | `source_url` field | `dataset["source_url"] = "https://..."` | `verify-california.py --ab2013-b1-url` |
| **§ 3110(b)(1)** - Owner identification | `owner` field | `dataset["owner"] = "Common Crawl Foundation"` | `verify-california.py --ab2013-b1-owner` |
| **§ 3110(b)(1)** - Owner type | `owner_type` field | `dataset["owner_type"] = "non-profit"` | `verify-california.py --ab2013-b1-type` |

**Code Example:**
```python
dataset = {
    # § 3110(b)(1): Complete source and owner information
    "source": "Common Crawl",
    "source_url": "https://commoncrawl.org",
    "owner": "Common Crawl Foundation",
    "owner_type": "non-profit",
    "owner_contact": "info@commoncrawl.org",
    "owner_jurisdiction": "United States"
}

# Multiple sources must be listed separately
disclosure = tracker.disclose_training_data({
    "datasets": [
        {
            "source": "Common Crawl",
            "source_url": "https://commoncrawl.org",
            "owner": "Common Crawl Foundation"
        },
        {
            "source": "GitHub",
            "source_url": "https://github.com",
            "owner": "Various open source developers"
        },
        {
            "source": "BooksCorpus",
            "owner": "University of Toronto"
        }
    ]
})

assert len(disclosure["datasets"]) == 3
```

---

### Section 3110(b)(2): How Data Furthers System Purpose

Describe how the data furthers the intended purpose of the AI system.

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 3110(b)(2)** - Purpose alignment | `purpose_alignment` field | `dataset["purpose_alignment"] = "Language understanding"` | `verify-california.py --ab2013-b2` |

**Code Example:**
```python
dataset = {
    "source": "Common Crawl",
    "purpose_alignment": "Provides diverse web text to train language understanding and generation capabilities",
    "specific_contribution": "Enables model to understand contemporary writing styles, factual knowledge, and discourse patterns"
}
```

---

### Section 3110(b)(3): Number of Data Points

Disclose the number of data points in the dataset, which can be an exact number or a reasonable estimate.

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 3110(b)(3)** - Exact count | `data_points_exact` field | `dataset["data_points_exact"] = 250000000` | `verify-california.py --ab2013-b3-exact` |
| **§ 3110(b)(3)** - Range or estimate | `data_points_range` field | `dataset["data_points_range"] = "200-300M"` | `verify-california.py --ab2013-b3-range` |
| **§ 3110(b)(3)** - Unit of measurement | `data_points_unit` field | `dataset["data_points_unit"] = "tokens"` | `verify-california.py --ab2013-b3-unit` |

**Code Example:**
```python
# Exact count
dataset_exact = {
    "source": "Wikipedia",
    "data_points_exact": 6000000,
    "data_points_unit": "articles"
}

# Range estimate
dataset_range = {
    "source": "Common Crawl",
    "data_points_range": "200-300 billion",
    "data_points_unit": "tokens"
}

assert dataset_exact["data_points_exact"] > 0
assert "billion" in dataset_range["data_points_range"]
```

---

### Section 3110(b)(4): Data Type Description

Describe the type of data, including whether it is text, image, video, audio, or another form of data, and any characteristics or features of the data, including whether it contains annotations or labels.

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 3110(b)(4)** - Data type | `data_types` field | `dataset["data_types"] = ["text", "code"]` | `verify-california.py --ab2013-b4-types` |
| **§ 3110(b)(4)** - Annotation description | `annotation_types` field | `dataset["annotation_types"] = ["labels"]` | `verify-california.py --ab2013-b4-annotations` |
| **§ 3110(b)(4)** - Characteristics | `characteristics` field | `dataset["characteristics"] = ["QA pairs"]` | `verify-california.py --ab2013-b4-characteristics` |
| **§ 3110(b)(4)** - Modalities | `modalities` field | `dataset["modalities"] = ["text", "image"]` | `verify-california.py --ab2013-b4-modalities` |

**Code Example:**
```python
dataset = {
    "source": "Instruction Tuning Dataset",
    "data_types": ["text", "code"],
    "modalities": ["text"],
    "annotation_types": [
        {
            "type": "instruction",
            "description": "User instruction or prompt",
            "coverage": "100%"
        },
        {
            "type": "response",
            "description": "Expected model response",
            "coverage": "100%"
        },
        {
            "type": "safety_rating",
            "description": "Safety classification",
            "coverage": "60%"
        }
    ],
    "characteristics": [
        "Question-answer pairs",
        "Multi-turn conversations",
        "Code generation examples",
        "Reasoning chains"
    ],
    "languages": ["en", "es", "zh"],
    "quality_metrics": {
        "fluency": "4.5/5",
        "relevance": "4.3/5",
        "safety": "reviewed"
    }
}

assert "text" in dataset["data_types"]
assert len(dataset["annotation_types"]) > 0
```

---

### Section 3110(b)(5): Intellectual Property Status

Describe the intellectual property status of the data, including whether the data is subject to copyright, trademark, or patent, or is in the public domain.

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 3110(b)(5)** - Copyright status | `copyright_status` field | `dataset["copyright_status"] = "may contain copyrighted"` | `verify-california.py --ab2013-b5-copyright` |
| **§ 3110(b)(5)** - Trademark status | `trademark_status` field | `dataset["trademark_status"] = "may contain trademarks"` | `verify-california.py --ab2013-b5-trademark` |
| **§ 3110(b)(5)** - Patent status | `patent_status` field | `dataset["patent_status"] = "none"` | `verify-california.py --ab2013-b5-patent` |
| **§ 3110(b)(5)** - Public domain | `public_domain` field | `dataset["public_domain"] = True` | `verify-california.py --ab2013-b5-public` |
| **§ 3110(b)(5)** - Explanation | `ip_explanation` field | `dataset["ip_explanation"] = "..."` | `verify-california.py --ab2013-b5-explanation` |

**Code Example:**
```python
dataset = {
    "source": "Common Crawl",
    "copyright_status": "may contain copyrighted material",
    "trademark_status": "may contain trademarks",
    "patent_status": "none",
    "public_domain": False,
    "ip_explanation": "Common Crawl data may include copyrighted web pages. Use is believed to be fair use for training under 17 U.S.C. § 107.",
    "ip_disclaimer": "Developers should consult their legal counsel regarding use of copyrighted materials."
}

# Public domain dataset
public_domain_dataset = {
    "source": "Project Gutenberg",
    "copyright_status": "public domain",
    "public_domain": True,
    "ip_explanation": "All works are in the public domain under U.S. copyright law"
}
```

---

### Section 3110(b)(6): Commercial Arrangements

Disclose whether the data was purchased, licensed, or otherwise acquired through a commercial arrangement.

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 3110(b)(6)** - Purchased | `purchased` field | `dataset["purchased"] = True` | `verify-california.py --ab2013-b6-purchased` |
| **§ 3110(b)(6)** - Licensed | `licensed` field | `dataset["licensed"] = True` | `verify-california.py --ab2013-b6-licensed` |
| **§ 3110(b)(6)** - License terms | `license_terms` field | `dataset["license_terms"] = "CC BY-SA 4.0"` | `verify-california.py --ab2013-b6-license` |
| **§ 3110(b)(6)** - License URL | `license_url` field | `dataset["license_url"] = "https://..."` | `verify-california.py --ab2013-b6-url` |
| **§ 3110(b)(6)** - Commercial provider | `commercial_provider` field | `dataset["commercial_provider"] = "Acme Data Corp"` | `verify-california.py --ab2013-b6-provider` |

**Code Example:**
```python
# Purchased dataset
purchased_dataset = {
    "source": "Financial News Corpus",
    "purchased": True,
    "commercial_provider": "Reuters Data",
    "purchase_price": "undisclosed",
    "purchase_date": "2024-06-01"
}

# Licensed dataset
licensed_dataset = {
    "source": "Wikipedia",
    "licensed": True,
    "license_terms": "CC BY-SA 4.0",
    "license_url": "https://creativecommons.org/licenses/by-sa/4.0/",
    "license_restrictions": "Attribution required, share-alike"
}

# Free public dataset
public_dataset = {
    "source": "Common Crawl",
    "purchased": False,
    "licensed": False,
    "license_terms": "Public domain crawl data"
}
```

---

### Section 3110(b)(7): Personal Information

Disclose whether the data contains personal information as defined in the California Consumer Privacy Act (CCPA).

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 3110(b)(7)** - Contains personal info | `contains_personal_info` field | `dataset["contains_personal_info"] = True` | `verify-california.py --ab2013-b7-contains` |
| **§ 3110(b)(7)** - PII categories | `pii_categories` field | `dataset["pii_categories"] = ["names", "emails"]` | `verify-california.py --ab2013-b7-categories` |
| **§ 3110(b)(7)** - PII handling | `pii_handling` field | `dataset["pii_handling"] = "not filtered"` | `verify-california.py --ab2013-b7-handling` |

**Code Example:**
```python
dataset = {
    "source": "Common Crawl",
    "contains_personal_info": True,
    "pii_categories": [
        "names",
        "email addresses",
        "IP addresses",
        "physical addresses",
        "phone numbers"
    ],
    "pii_handling": "Data may contain PII from public web pages; no specific filtering or redaction applied",
    "ccpa_compliance": "Training on PII may require CCPA compliance",
    "ccpa_explanation": "Data subjects have rights under CCPA; developers should implement appropriate safeguards"
}

# Dataset with no PII
clean_dataset = {
    "source": "Synthetic QA Pairs",
    "contains_personal_info": False,
    "pii_categories": [],
    "pii_handling": "N/A - synthetic data only"
}
```

---

### Section 3110(b)(8): Aggregate Consumer Information

Disclose whether the data contains aggregate consumer information as defined in the CCPA.

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 3110(b)(8)** - Contains aggregate info | `contains_aggregate_info` field | `dataset["contains_aggregate_info"] = True` | `verify-california.py --ab2013-b8-contains` |
| **§ 3110(b)(8)** - Aggregate description | `aggregate_description` field | `dataset["aggregate_description"] = "demographics"` | `verify-california.py --ab2013-b8-description` |

**Code Example:**
```python
dataset = {
    "source": "Consumer Survey Data",
    "contains_aggregate_info": True,
    "aggregate_description": "Aggregated demographic information including age ranges, income brackets, and geographic regions",
    "aggregation_method": "K-anonymity applied",
    "cell_suppression": True
}
```

---

### Section 3110(b)(9): Data Processing

Describe the extent to which the data was modified, including any cleaning, filtering, or other processing.

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 3110(b)(9)** - Processing description | `processing_description` field | `dataset["processing"] = ["cleaned", "deduplicated"]` | `verify-california.py --ab2013-b9-processing` |
| **§ 3110(b)(9)** - Modifications | `modifications` field | `dataset["modifications"] = ["tokenized"]` | `verify-california.py --ab2013-b9-modifications` |
| **§ 3110(b)(9)** - Filtering criteria | `filtering_criteria` field | `dataset["filtering"] = ["toxic content removed"]` | `verify-california.py --ab2013-b9-filtering` |

**Code Example:**
```python
dataset = {
    "source": "Common Crawl",
    "processing_description": [
        "HTML tag removal",
        "Language filtering (target: English)",
        "Near-deduplication",
        "Quality filtering",
        "Toxic content filtering"
    ],
    "modifications": [
        "Text extracted from HTML",
        "Non-English documents removed (retained ~30% of original)",
        "Duplicate documents removed (retained ~60% after dedup)",
        "Low-quality documents filtered (perplexity threshold)"
    ],
    "filtering_criteria": {
        "language": "English (>90% probability)",
        "quality": "Perplexity < 50",
        "safety": "Toxic content probability < 0.5",
        "length": "> 50 tokens"
    },
    "processing_software": "Custom pipeline using Spark, HuggingFace",
    "processing_date": "2024-2025"
}
```

---

### Section 3110(b)(10): Time Period of Collection

Disclose the time period during which the data was collected.

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 3110(b)(10)** - Collection period | `collection_period` field | `dataset["collection_period"] = "2020-2024"` | `verify-california.py --ab2013-b10-period` |
| **§ 3110(b)(10)** - Start date | `collection_start` field | `dataset["collection_start"] = "2020-01-01"` | `verify-california.py --ab2013-b10-start` |
| **§ 3110(b)(10)** - End date | `collection_end` field | `dataset["collection_end"] = "2024-12-31"` | `verify-california.py --ab2013-b10-end` |
| **§ 3110(b)(10)** - Ongoing collection | `ongoing_collection` field | `dataset["ongoing_collection"] = True` | `verify-california.py --ab2013-b10-ongoing` |

**Code Example:**
```python
# Completed collection
dataset = {
    "source": "Common Crawl",
    "collection_period": "2020-2024",
    "collection_start": "2020-01-01",
    "collection_end": "2024-12-31"
}

# Ongoing collection
ongoing_dataset = {
    "source": "Real-time API data",
    "collection_period": "2023-present",
    "collection_start": "2023-06-01",
    "ongoing_collection": True,
    "update_frequency": "daily"
}
```

---

### Section 3110(b)(11): First Use Date

Disclose the date on which the data was first used in the development of the AI system.

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 3110(b)(11)** - First use date | `first_use_date` field | `dataset["first_use_date"] = "2023-06-01"` | `verify-california.py --ab2013-b11` |

**Code Example:**
```python
dataset = {
    "source": "Common Crawl",
    "first_use_date": "2023-06-15",
    "first_use_context": "Initial model pre-training"
}

assert dataset["first_use_date"] >= "2023-01-01"
```

---

### Section 3110(b)(12): Synthetic Data

Disclose whether synthetic data was used in training, and if so, a description of the synthetic data generation process.

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 3110(b)(12)** - Contains synthetic data | `contains_synthetic_data` field | `dataset["contains_synthetic_data"] = True` | `verify-california.py --ab2013-b12-contains` |
| **§ 3110(b)(12)** - Synthetic description | `synthetic_description` field | `dataset["synthetic_description"] = "GPT-4 generated"` | `verify-california.py --ab2013-b12-description` |
| **§ 3110(b)(12)** - Synthetic proportion | `synthetic_proportion` field | `dataset["synthetic_proportion"] = "5%"` | `verify-california.py --ab2013-b12-proportion` |
| **§ 3110(b)(12)** - Ongoing synthetic | `ongoing_synthetic` field | `dataset["ongoing_synthetic"] = True` | `verify-california.py --ab2013-b12-ongoing` |
| **§ 3110(b)(12)** - Generation method | `synthetic_methods` field | `dataset["synthetic_methods"] = ["prompt-based"]` | `verify-california.py --ab2013-b12-methods` |

**Code Example:**
```python
# Overall synthetic data summary
disclosure = {
    "system_name": "TextGen-v2",
    "synthetic_data_summary": {
        "contains_synthetic_data": True,
        "synthetic_description": "Data augmentation using GPT-4 for instruction tuning and self-instruct",
        "synthetic_proportion": "5% of total training data",
        "synthetic_datasets": [
            {
                "name": "Instruction Tuning Set",
                "size": "2M examples",
                "method": "Self-instruct with GPT-4",
                "seed_data": "200 human-written examples"
            },
            {
                "name": "Code Generation Examples",
                "size": "1M examples",
                "method": "Synthetic code generation",
                "seed_data": "Open source repositories"
            }
        ],
        "ongoing_synthetic": True,
        "synthetic_methods": [
            "prompt-based generation",
            "self-instruct",
            "back-translation"
        ],
        "quality_control": "Human validation of 5% of samples",
        "validation_results": "98% acceptable quality"
    }
}

# Dataset-level synthetic disclosure
dataset = {
    "source": "Instruction Tuning Set",
    "contains_synthetic_data": True,
    "synthetic_description": "Generated using GPT-4 with self-instruct methodology",
    "synthetic_proportion": "100%",
    "generation_prompt": "Create a question-answer pair about [topic]",
    "seed_data": "200 human-written examples",
    "quality_filter": "Min response length 10 tokens, safety filters applied"
}
```

---

### Section 3110(c): Understandable Summary

The summary must be written in plain language that is understandable to the average person.

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 3110(c)** - Plain language summary | `plain_language_summary` field | `disclosure["summary"] = "We used..."` | `verify-california.py --ab2013-c` |

**Code Example:**
```python
disclosure = {
    "system_name": "TextGen-v2",
    "plain_language_summary": """
    TextGen-v2 was trained using a combination of public web data and open source code. 
    The largest dataset is Common Crawl, which contains text from hundreds of millions of 
    web pages collected between 2020 and 2024. This web data may include personal information 
    that was publicly available online. We also used code from public GitHub repositories 
    to improve code generation capabilities. About 5% of the training data was synthetically 
    generated using GPT-4 to create instruction-response pairs.
    
    We processed the data by removing HTML tags, filtering out non-English content, 
    removing near-duplicate documents, and filtering for quality. The web data may contain 
    copyrighted material; we believe our use is fair use for machine learning training.
    """,
    "readability_score": "8th grade level",
    "translation_available": ["es", "zh", "vi"]
}
```

---

## ✅ Complete Verification

```bash
# Run complete AB 2013 compliance verification
python tests/verify-california.py --ab2013 --verbose

# Output:
# ========================================
# AB 2013 TRAINING DATA TRANSPARENCY ACT
# ========================================
#
# 📋 Section 3110(a): Public Availability
#   ✅ Summary publicly accessible
#   ✅ Documentation URL provided
#
# 📋 Section 3110(b)(1): Data Sources
#   ✅ All sources identified
#   ✅ Owners disclosed
#
# 📋 Section 3110(b)(2): Purpose Alignment
#   ✅ Purpose descriptions provided
#
# 📋 Section 3110(b)(3): Data Points
#   ✅ Counts provided (exact or range)
#
# 📋 Section 3110(b)(4): Data Types
#   ✅ Types described
#   ✅ Annotations disclosed
#
# 📋 Section 3110(b)(5): IP Status
#   ✅ Copyright status disclosed
#   ✅ IP explanation provided
#
# 📋 Section 3110(b)(6): Commercial Arrangements
#   ✅ Purchase/license status disclosed
#
# 📋 Section 3110(b)(7): Personal Information
#   ✅ PII presence disclosed
#   ✅ Categories identified
#
# 📋 Section 3110(b)(8): Aggregate Info
#   ✅ Aggregate info status disclosed
#
# 📋 Section 3110(b)(9): Data Processing
#   ✅ Processing steps described
#
# 📋 Section 3110(b)(10): Collection Period
#   ✅ Time periods provided
#
# 📋 Section 3110(b)(11): First Use Date
#   ✅ First use dates provided
#
# 📋 Section 3110(b)(12): Synthetic Data
#   ✅ Synthetic data status disclosed
#   ✅ Generation methods described
#
# 📋 Section 3110(c): Understandable Summary
#   ✅ Plain language summary provided
#
# ========================================
# ✅ FULL COMPLIANCE VERIFIED
# ========================================
```

## ⚖️ UCL Enforcement

AB 2013 is enforced through California's **Unfair Competition Law (UCL)** , Business & Professions Code § 17200 . Violations can result in:

| Remedy | Description | Maximum |
|--------|-------------|---------|
| **Injunctive relief** | Court order to comply | N/A |
| **Restitution** | Return money to affected consumers | Full amount |
| **Civil penalties** | Per violation fines | $2,500 per violation |
| **Attorney's fees** | Plaintiff's legal costs | Full amount |

## 📚 References

- [Full Text of AB 2013](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240AB2013)
- [California Unfair Competition Law, Bus. & Prof. Code § 17200](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=17200)
- [California Attorney General AI Enforcement](https://oag.ca.gov/)

## 📬 Contact

For AB 2013-specific inquiries:
- **Email**: ab2013@humanjudgment.org
- **GitHub**: [hjs-spec/jep-us-solutions](https://github.com/hjs-spec/jep-us-solutions)

---

*Last Updated: March 2026*
```
