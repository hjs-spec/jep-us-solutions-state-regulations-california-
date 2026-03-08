# 🇨🇦 California SB 942: California AI Transparency Act

**Complete JEP Implementation for AI Content Watermarking and Detection**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/downloads/)
[![Effective Date](https://img.shields.io/badge/Effective-January%201%2C%202026-red)](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240SB942)
[![Operative Date](https://img.shields.io/badge/Operative-August%202%2C%202026-orange)](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240SB942)

## 📋 Overview

The **California AI Transparency Act (SB 942)** , signed into law on September 19, 2024, establishes groundbreaking requirements for AI content transparency, including mandatory watermarks and free AI detection tools . The law originally took effect **January 1, 2026**, but has been delayed to become operative on **August 2, 2026**, aligning with the EU AI Act Article 50 .

### Key Dates

| Date | Significance |
|------|--------------|
| **September 19, 2024** | Bill signed into law |
| **January 1, 2026** | Original effective date |
| **August 2, 2026** | **New operative date** (aligned with EU AI Act) |

### Applicability Thresholds

| Criteria | Threshold | Notes |
|----------|-----------|-------|
| **Monthly Users** | ≥ 1,000,000 monthly visitors or users | Counted globally, not just California  |
| **Public Accessibility** | Publicly accessible within California | Applies regardless of provider location |
| **Content Types** | Image, video, audio, or combinations | **Does not apply to text-only content**  |
| **Exceptions** | Video games, TV, streaming, movies | Non-user-generated entertainment excluded  |

## 🎯 Key Requirements

| Section | Requirement | Deadline | Penalty |
|---------|-------------|----------|---------|
| **§ 22757.2(a)** | Free AI Detection Tool | Aug 2, 2026 | $5,000/violation |
| **§ 22757.2(b)** | User Feedback Collection | Aug 2, 2026 | $5,000/violation |
| **§ 22757.3(a)** | Manifest Disclosure (Optional) | Aug 2, 2026 | $5,000/violation |
| **§ 22757.3(b)** | Latent Disclosure (Mandatory) | Aug 2, 2026 | $5,000/violation |
| **§ 22757.3(c)** | Licensee Contract Requirements | Aug 2, 2026 | License revocation + penalties |
| **§ 22757.2(c)** | Privacy Protections | Aug 2, 2026 | $5,000/violation |

## 📊 Detailed Requirements Mapping

### Section 22757.2(a): AI Detection Tool

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 22757.2(a)(1)** - Assess content origin | `detect_content_origin()` | `tool.detect(content)` | `verify-california.py --sb942-detect` |
| **§ 22757.2(a)(2)** - Output system provenance data | `get_system_provenance()` | `tool.get_provenance()` | `verify-california.py --sb942-provenance` |
| **§ 22757.2(a)(3)** - No personal provenance data | `strip_personal_data()` | `tool.safe_output()` | `verify-california.py --sb942-privacy` |
| **§ 22757.2(a)(4)** - Publicly accessible | `deploy_detection_tool()` | `tool.deploy_public()` | `verify-california.py --sb942-public` |
| **§ 22757.2(a)(5)** - URL submission support | `detect_from_url()` | `tool.detect_url(url)` | `verify-california.py --sb942-url` |
| **§ 22757.2(a)(6)** - API support | `create_api_endpoint()` | `tool.create_api()` | `verify-california.py --sb942-api` |

**Code Example:**
```python
from jep.us.california import ContentTransparencyTracker

tracker = ContentTransparencyTracker(
    company_name="AI Media Corp",
    monthly_users=2_500_000,  # >1M threshold
    content_types=["image", "video", "audio"]
)

# § 22757.2(a): Deploy free AI detection tool
detection_tool = tracker.deploy_detection_tool({
    "tool_name": "AIDetect Pro",
    "version": "1.0.0",
    "endpoint_url": "https://api.aimedia.com/detect",
    "web_interface": "https://aimedia.com/detect",
    
    # § 22757.2(a)(1): Content origin assessment
    "detection_capabilities": ["image", "video", "audio"],
    "supported_formats": ["jpg", "png", "mp4", "mp3", "wav"],
    "accuracy_metrics": {
        "image": 0.98,
        "video": 0.95,
        "audio": 0.94
    },
    
    # § 22757.2(a)(2): System provenance output
    "provenance_output": {
        "provider_name": True,
        "system_version": True,
        "timestamp": True,
        "unique_id": True
    },
    
    # § 22757.2(a)(3): No personal data
    "privacy_protections": {
        "strip_personal_data": True,
        "no_data_retention": True,
        "no_pii_output": True
    },
    
    # § 22757.2(a)(4): Public accessibility
    "public_access": {
        "rate_limit": "1000 requests/hour",
        "authentication": "optional",
        "uptime_sla": "99.9%"
    },
    
    # § 22757.2(a)(5): URL submission
    "url_support": {
        "enabled": True,
        "max_urls_per_request": 10,
        "timeout_seconds": 30
    },
    
    # § 22757.2(a)(6): API support
    "api_support": {
        "rest_api": True,
        "graphql": False,
        "sdk_available": ["python", "javascript", "java"],
        "documentation_url": "https://docs.aimedia.com/api"
    },
    
    "deployment_date": time.time()
})

print(f"Detection Tool URL: {detection_tool['web_interface']}")
print(f"API Endpoint: {detection_tool['api_support']['rest_api']}")
```

### Section 22757.2(b): User Feedback Collection

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 22757.2(b)** - Collect user feedback | `collect_user_feedback()` | `tracker.collect_feedback()` | `verify-california.py --sb942-feedback` |
| **§ 22757.2(b)** - Incorporate feedback | `update_detection_tool()` | `tracker.update_tool()` | `verify-california.py --sb942-update` |

**Code Example:**
```python
# § 22757.2(b): User feedback system
feedback_system = tracker.create_feedback_system({
    "feedback_id": f"FB-{int(time.time())}",
    "collection_methods": ["in-app", "email", "web_form"],
    "feedback_categories": [
        "false_positive",
        "false_negative",
        "accuracy_issue",
        "feature_request"
    ],
    "retention_policy": "90 days",
    "opt_in_required": True,
    "anonymized": True
})

# Collect feedback
feedback = tracker.collect_feedback({
    "feedback_id": "FB-2026-001",
    "user_id": "USER-123",
    "timestamp": time.time(),
    "category": "false_positive",
    "description": "Tool flagged human-created image as AI-generated",
    "content_hash": hashlib.sha256(content).hexdigest(),
    "accuracy_rating": 3,
    "opt_in_contact": "user@example.com"
})

# Incorporate feedback into tool updates
update = tracker.update_detection_tool({
    "update_id": "UPD-2026-001",
    "feedback_ids": ["FB-2026-001", "FB-2026-002"],
    "improvements": [
        "Improved image detection algorithm",
        "Reduced false positive rate by 15%"
    ],
    "new_version": "1.0.1",
    "release_date": time.time()
})
```

### Section 22757.2(c): Privacy Protections

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 22757.2(c)(1)** - No personal info collection | `privacy_policy` | `tool.no_pii_collection()` | `verify-california.py --sb942-no-collect` |
| **§ 22757.2(c)(1)(B)** - Opt-in for feedback contact | `opt_in_contact()` | `tracker.opt_in_contact()` | `verify-california.py --sb942-optin` |
| **§ 22757.2(c)(2)** - Content retention limited | `auto_delete_content()` | `tool.set_retention()` | `verify-california.py --sb942-retention` |
| **§ 22757.2(c)(3)** - No personal provenance retention | `no_personal_provenance()` | `tool.strip_provenance()` | `verify-california.py --sb942-no-provenance` |

**Code Example:**
```python
# § 22757.2(c): Privacy compliance
privacy_config = tracker.configure_privacy({
    "personal_info_collection": False,
    "feedback_opt_in": {
        "enabled": True,
        "method": "checkbox",
        "disclosure": "Contact info used only for tool improvement"
    },
    "content_retention": {
        "max_duration_seconds": 3600,  # 1 hour
        "auto_delete": True,
        "deletion_confirmation": True
    },
    "provenance_handling": {
        "strip_personal_data": True,
        "retain_system_data": True,
        "retention_days": 30
    },
    "data_processing_agreement": "DPA-2026-001",
    "ccpa_compliant": True,
    "privacy_policy_url": "https://aimedia.com/privacy"
})

# Verify privacy compliance
assert privacy_config["personal_info_collection"] == False
assert privacy_config["content_retention"]["max_duration_seconds"] <= 3600
```

### Section 22757.3(a): Manifest Disclosure (Optional)

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 22757.3(a)(1)** - Identify as AI-generated | `manifest_identifier` field | `disclosure["identifier"] = "AI-Generated"` | `verify-california.py --sb942-manifest-id` |
| **§ 22757.3(a)(2)** - Clear and conspicuous | `manifest_format` field | `disclosure["format"] = "watermark"` | `verify-california.py --sb942-manifest-clear` |
| **§ 22757.3(a)(3)** - Permanent/difficult to remove | `manifest_permanence` field | `disclosure["permanence"] = "extraordinarily_difficult"` | `verify-california.py --sb942-manifest-permanent` |

**Code Example:**
```python
# § 22757.3(a): Offer manifest disclosure option
manifest_option = tracker.create_manifest_disclosure_option({
    "option_name": "AI Watermark",
    "default": "off",
    "user_control": "toggle",
    "disclosure_types": ["image", "video", "audio"],
    
    # § 22757.3(a)(1): AI-generated identifier
    "identifier": {
        "text": "AI-Generated",
        "logo": "🤖",
        "placement": "corner"
    },
    
    # § 22757.3(a)(2): Clear and conspicuous
    "format": {
        "type": "visible_watermark",
        "opacity": "0.8",
        "size": "medium",
        "contrast": "high"
    },
    
    # § 22757.3(a)(3): Permanent/difficult to remove
    "permanence": {
        "level": "extraordinarily_difficult",
        "method": "frequency_domain_embedding",
        "removal_detection": True
    },
    
    "preview_url": "https://aimedia.com/watermark-preview",
    "documentation_url": "https://aimedia.com/watermark-docs"
})

# User applies manifest disclosure
watermarked_content = tracker.apply_manifest_disclosure(
    content=original_image,
    content_type="image",
    user_id="USER-123",
    options={
        "identifier": "AI-Generated",
        "placement": "bottom_right",
        "opacity": 0.8
    }
)
```

### Section 22757.3(b): Latent Disclosure (Mandatory)

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 22757.3(b)(1)(A)** - Provider name | `provider_name` field | `disclosure["provider"] = "AI Media Corp"` | `verify-california.py --sb942-latent-provider` |
| **§ 22757.3(b)(1)(B)** - System name/version | `system_info` field | `disclosure["system"] = "GenAI v2.1"` | `verify-california.py --sb942-latent-system` |
| **§ 22757.3(b)(1)(C)** - Time and date | `timestamp` field | `disclosure["timestamp"] = time.time()` | `verify-california.py --sb942-latent-time` |
| **§ 22757.3(b)(1)(D)** - Unique identifier | `unique_id` field | `disclosure["unique_id"] = uuid7()` | `verify-california.py --sb942-latent-id` |
| **§ 22757.3(b)(2)** - Detectable by AI detection tool | `detectable_by_tool` field | `disclosure["detectable"] = True` | `verify-california.py --sb942-latent-detectable` |
| **§ 22757.3(b)(3)** - Industry standards | `industry_standards` field | `disclosure["standards"] = ["C2PA", "ISO"]` | `verify-california.py --sb942-latent-standards` |
| **§ 22757.3(b)(4)** - Permanent/difficult to remove | `latent_permanence` field | `disclosure["permanence"] = "extraordinarily_difficult"` | `verify-california.py --sb942-latent-permanent` |

**Code Example:**
```python
# § 22757.3(b): Mandatory latent disclosure
latent_disclosure = tracker.embed_latent_disclosure({
    "content_id": f"CONTENT-{int(time.time())}",
    "content_type": "image",
    
    # § 22757.3(b)(1)(A): Provider name
    "provider": {
        "name": "AI Media Corp",
        "url": "https://aimedia.com",
        "contact": "compliance@aimedia.com"
    },
    
    # § 22757.3(b)(1)(B): System name and version
    "system": {
        "name": "ImageGen Pro",
        "version": "2.1.0",
        "model_id": "img-gen-v2-1"
    },
    
    # § 22757.3(b)(1)(C): Time and date
    "timestamp": {
        "created": time.time(),
        "timezone": "UTC",
        "format": "ISO 8601"
    },
    
    # § 22757.3(b)(1)(D): Unique identifier
    "unique_id": tracker._generate_uuid7(),
    
    # § 22757.3(b)(2): Detectable by detection tool
    "detectable": {
        "by_provider_tool": True,
        "detection_method": "provenance_extraction",
        "confidence": 0.99
    },
    
    # § 22757.3(b)(3): Industry standards
    "industry_standards": {
        "c2pa": True,
        "iso_iec_27050": True,
        "w3c_credentials": True
    },
    
    # § 22757.3(b)(4): Permanent/difficult to remove
    "permanence": {
        "level": "extraordinarily_difficult",
        "method": "steganographic_embedding",
        "robustness": "high",
        "removal_detection": True
    },
    
    # Optional: Link to permanent website
    "link": {
        "url": f"https://verify.aimedia.com/content/{unique_id}",
        "permanent": True,
        "includes_all_info": True
    }
})

# Embed into content
watermarked_content = tracker.embed_into_content(
    content=original_content,
    disclosure=latent_disclosure,
    content_type="image"
)

# Verify latent disclosure
assert tracker.verify_latent_disclosure(watermarked_content)["valid"] == True
```

### Section 22757.3(c): Licensee Requirements

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 22757.3(c)(1)** - Contract require maintenance | `license_contract_clause()` | `tracker.add_license_clause()` | `verify-california.py --sb942-license-clause` |
| **§ 22757.3(c)(2)** - Revoke license within 96 hours | `revoke_license()` | `tracker.revoke_license()` | `verify-california.py --sb942-revoke` |
| **§ 22757.3(c)(3)** - Licensee cease use | `cease_use_notice()` | `tracker.notify_cease_use()` | `verify-california.py --sb942-cease` |

**Code Example:**
```python
# § 22757.3(c)(1): License contract requirements
license_agreement = tracker.create_license_agreement({
    "license_id": f"LIC-{int(time.time())}",
    "licensee": "Third-Party Corp",
    "effective_date": time.time(),
    "termination_date": time.time() + 31536000,  # 1 year
    
    # Contract clause requiring latent disclosure maintenance
    "latent_disclosure_clause": {
        "required": True,
        "maintenance_obligation": "Licensee must maintain all latent disclosure capabilities",
        "modification_restriction": "No modifications that disable latent disclosures",
        "audit_rights": "Provider may audit quarterly"
    },
    
    "reporting_requirements": {
        "frequency": "monthly",
        "method": "compliance_report",
        "due_within_days": 30
    }
})

# § 22757.3(c)(2): Monitor for modifications
monitoring = tracker.monitor_licensee_compliance({
    "license_id": license_agreement["license_id"],
    "monitoring_frequency": "continuous",
    "detection_method": "content_sampling",
    "sample_rate": 0.01  # 1% of content
})

# If modification detected, revoke within 96 hours
if monitoring["modification_detected"]:
    revocation = tracker.revoke_license({
        "license_id": license_agreement["license_id"],
        "revocation_reason": "Licensee disabled latent disclosure capabilities",
        "discovery_time": monitoring["detection_time"],
        "revocation_time": time.time(),
        "compliance_96_hours": (time.time() - monitoring["detection_time"]) <= 345600,  # 96 hours
        "notification_sent": True,
        "notification_method": ["email", "certified_mail"]
    })
    
    # § 22757.3(c)(3): Notice to cease use
    cease_notice = tracker.notify_cease_use({
        "license_id": license_agreement["license_id"],
        "notice_time": time.time(),
        "effective_immediately": True,
        "consequences": "Continued use may result in legal action",
        "proof_of_delivery": "signed_receipt.pdf"
    })
    
    assert revocation["compliance_96_hours"] == True
```

### Section 22757.4: Penalties and Enforcement

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 22757.4(a)** - Civil penalty $5,000/violation | `track_violations()` | `tracker.log_violation()` | `verify-california.py --sb942-penalty` |
| **§ 22757.4(b)** - Each day = discrete violation | `daily_violation_count()` | `tracker.count_daily()` | `verify-california.py --sb942-daily` |
| **§ 22757.4(c)** - Injunctive relief for licensees | `prepare_injunction()` | `tracker.injunction_request()` | `verify-california.py --sb942-injunction` |

**Code Example:**
```python
# Track violations for compliance reporting
violation_log = tracker.log_violation({
    "violation_id": f"VIO-{int(time.time())}",
    "date": time.time(),
    "type": "missing_latent_disclosure",
    "description": "Content generated without required latent disclosure",
    "affected_content_ids": ["CONTENT-001", "CONTENT-002"],
    "days_in_violation": 3,
    "estimated_penalty": 3 * 5000,  # $15,000
    "remediated": False,
    "remediation_deadline": time.time() + 259200  # 3 days
})

# Daily violation counting
daily_count = tracker.count_daily_violations(date="2026-08-15")
assert daily_count["total_violations"] * 5000 == daily_count["estimated_penalty"]
```

## 🔍 Verification

```bash
# Run SB 942 compliance verification
python tests/verify-california.py --sb942

# Output:
# ========================================
# SB 942 AI TRANSPARENCY ACT COMPLIANCE
# ========================================
# ✅ § 22757.2(a): Free AI Detection Tool
#   - Content origin assessment
#   - System provenance output
#   - No personal data
#   - Publicly accessible
#   - URL submission support
#   - API support
#
# ✅ § 22757.2(b): User Feedback Collection
#   - Feedback system implemented
#   - Updates incorporate feedback
#
# ✅ § 22757.2(c): Privacy Protections
#   - No personal info collection
#   - Feedback opt-in only
#   - Limited content retention
#   - No personal provenance retention
#
# ✅ § 22757.3(a): Manifest Disclosure (Optional)
#   - AI-generated identifier
#   - Clear and conspicuous
#   - Extraordinarily difficult to remove
#
# ✅ § 22757.3(b): Latent Disclosure (Mandatory)
#   - Provider name
#   - System name/version
#   - Timestamp
#   - Unique identifier
#   - Detectable by tool
#   - Industry standards compliant
#   - Extraordinarily difficult to remove
#
# ✅ § 22757.3(c): Licensee Requirements
#   - Contract clauses present
#   - 96-hour revocation capability
#   - Cease use notification
#
# ========================================
# ✅ FULL COMPLIANCE VERIFIED
# ========================================
```

## ⚖️ Penalties and Enforcement

| Violation | Penalty | JEP Mitigation |
|-----------|---------|----------------|
| **Missing detection tool** | $5,000 per day | Automated tool deployment |
| **Missing latent disclosure** | $5,000 per day | Mandatory embedding |
| **Privacy violation** | $5,000 per day | Privacy-by-design architecture |
| **Licensee non-compliance** | $5,000 per day + license revocation | Automated monitoring + 96h revocation |
| **Each day in violation** | Counts as separate violation | Daily compliance checks |

**Enforcement authorities** :
- California Attorney General
- City attorneys
- County counsels

## 📚 References

- [Full Text of SB 942](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240SB942) 
- [California Business and Professions Code § 22757 et seq.](https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=BPC&division=8.&title=&part=&chapter=25.&article=) 
- [California Attorney General AI Enforcement](https://oag.ca.gov/)

## 📬 Contact

For SB 942-specific inquiries:
- **Email**: sb942@humanjudgment.org
- **GitHub**: [hjs-spec/jep-us-solutions](https://github.com/hjs-spec/jep-us-solutions)

---

*Last Updated: March 2026*
*Operative Date: August 2, 2026 (aligned with EU AI Act Article 50)*
```
