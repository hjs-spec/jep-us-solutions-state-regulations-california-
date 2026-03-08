# JEP Mapping to California SB 942 (California AI Transparency Act)

**Detailed Section-by-Section Mapping with Code Examples and Verification Methods**

## 📋 Overview

This document provides a comprehensive mapping between the **Judgment Event Protocol (JEP)** and California's **AI Transparency Act (SB 942)** , which becomes operative on **August 2, 2026** (aligned with EU AI Act Article 50) .

The law applies to providers of AI systems that generate or manipulate image, video, or audio content and have **1 million or more monthly users** .

---

## 📊 Article 1: General Provisions

### Section 22757.1: Definitions

| Term | Statutory Definition | JEP Implementation |
|------|---------------------|-------------------|
| **§ 22757.1(a)** - AI system | Machine-based system that can generate or manipulate image, video, or audio content | `content_types` parameter |
| **§ 22757.1(b)** - Covered provider | Person with 1M+ monthly users globally | `monthly_users` tracking |
| **§ 22757.1(c)** - Image, video, audio content | Visual or audio content, or combination | `detection_capabilities` |
| **§ 22757.1(d)** - System provenance data | Data identifying provider, system, time, unique ID | `latent_disclosure` structure |

---

## 📊 Article 2: AI Detection Tool

### Section 22757.2(a): Free AI Detection Tool Requirements

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 22757.2(a)(1)** - Assess whether content was AI-generated or manipulated | `detect_content_origin()` | `tool.detect(content)` | `verify-california.py --sb942-a1` |
| **§ 22757.2(a)(2)** - Output system provenance data | `get_system_provenance()` | `tool.get_provenance()` | `verify-california.py --sb942-a2` |
| **§ 22757.2(a)(3)** - Not output personal provenance data | `strip_personal_data()` | `tool.safe_output()` | `verify-california.py --sb942-a3` |
| **§ 22757.2(a)(4)** - Make tool publicly accessible | `deploy_detection_tool()` | `tool.deploy_public()` | `verify-california.py --sb942-a4` |
| **§ 22757.2(a)(5)** - Allow submission by URL | `detect_from_url()` | `tool.detect_url(url)` | `verify-california.py --sb942-a5` |
| **§ 22757.2(a)(6)** - Allow submission by API | `create_api_endpoint()` | `tool.create_api()` | `verify-california.py --sb942-a6` |

**Code Example:**
```python
from jep.us.california import ContentTransparencyTracker

tracker = ContentTransparencyTracker(
    company_name="AI Media Corp",
    monthly_users=2_500_000
)

# § 22757.2(a)(1)-(6): Complete detection tool implementation
detection_tool = tracker.deploy_detection_tool({
    "tool_name": "AIDetect Pro",
    "version": "1.0.0",
    
    # § 22757.2(a)(1): Content origin assessment
    "detection_capabilities": ["image", "video", "audio"],
    "supported_formats": ["jpg", "png", "mp4", "mp3", "wav"],
    "detection_methods": ["watermark_detection", "frequency_analysis", "neural_classifier"],
    
    # § 22757.2(a)(2): System provenance output
    "provenance_output": {
        "provider_name": "AI Media Corp",
        "system_version": "2.1.0",
        "timestamp_format": "ISO 8601",
        "unique_id_format": "UUIDv7"
    },
    
    # § 22757.2(a)(3): No personal data
    "privacy_protections": {
        "strip_personal_data": True,
        "no_pii_output": True,
        "no_data_retention": True
    },
    
    # § 22757.2(a)(4): Public accessibility
    "web_interface": "https://aimedia.com/detect",
    "rate_limit": "1000 requests/hour",
    "uptime_sla": "99.9%",
    
    # § 22757.2(a)(5): URL submission
    "url_support": {
        "enabled": True,
        "max_urls_per_request": 10,
        "timeout_seconds": 30,
        "supported_protocols": ["https"]
    },
    
    # § 22757.2(a)(6): API support
    "api_support": {
        "rest_api": True,
        "endpoint": "https://api.aimedia.com/v1/detect",
        "authentication": "optional",
        "sdk_available": ["python", "javascript", "java"],
        "documentation_url": "https://docs.aimedia.com/api"
    }
})

# Usage example: URL submission
result = tracker.detect_from_url(
    url="https://example.com/image.jpg",
    content_type="image"
)

# Output includes provenance if detected
assert "provider_name" in result or "ai_generated" in result

# No personal data in output
assert "user_id" not in result
assert "email" not in result
assert "ip_address" not in result
```

---

### Section 22757.2(b): User Feedback Collection

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 22757.2(b)** - Collect user feedback | `collect_user_feedback()` | `tracker.collect_feedback()` | `verify-california.py --sb942-b` |
| **§ 22757.2(b)** - Incorporate feedback into tool | `update_detection_tool()` | `tracker.update_tool()` | `verify-california.py --sb942-b-update` |

**Code Example:**
```python
# § 22757.2(b): User feedback system
feedback_system = tracker.create_feedback_system({
    "feedback_id": f"FB-{int(time.time())}",
    "collection_methods": ["in-app", "web_form", "email"],
    "feedback_categories": [
        "false_positive",
        "false_negative",
        "accuracy_issue",
        "feature_request"
    ],
    "retention_policy": "90 days",
    "anonymized": True
})

# Collect feedback
feedback = tracker.collect_feedback({
    "feedback_id": "FB-2026-001",
    "timestamp": time.time(),
    "category": "false_positive",
    "description": "Tool flagged human-created image as AI-generated",
    "content_hash": hashlib.sha256(content).hexdigest(),
    "accuracy_rating": 3,
    "suggested_improvement": "Better detection of human art styles"
})

# Incorporate feedback into tool update
update = tracker.update_detection_tool({
    "update_id": "UPD-2026-001",
    "feedback_ids": ["FB-2026-001", "FB-2026-002"],
    "improvements": [
        "Enhanced detection algorithm for artistic content",
        "Reduced false positive rate by 15%"
    ],
    "new_version": "1.1.0",
    "release_date": time.time(),
    "performance_metrics_after": {
        "false_positive_rate": 0.03,
        "accuracy": 0.97
    }
})
```

---

### Section 22757.2(c): Privacy Protections

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 22757.2(c)(1)** - Not collect personal information | `privacy_policy` | `tool.set_no_pii()` | `verify-california.py --sb942-c1` |
| **§ 22757.2(c)(1)(B)** - Opt-in for feedback contact | `opt_in_contact()` | `tracker.opt_in_contact()` | `verify-california.py --sb942-c1b` |
| **§ 22757.2(c)(2)** - Limited content retention | `set_retention_policy()` | `tool.set_retention(seconds)` | `verify-california.py --sb942-c2` |
| **§ 22757.2(c)(3)** - Not retain personal provenance | `strip_provenance_data()` | `tool.strip_provenance()` | `verify-california.py --sb942-c3` |

**Code Example:**
```python
# § 22757.2(c): Complete privacy configuration
privacy_config = tracker.configure_privacy({
    # § 22757.2(c)(1): No personal information collection
    "collect_personal_info": False,
    "collect_contact_info": False,
    "collect_usage_data": False,
    "anonymize_all": True,
    
    # § 22757.2(c)(1)(B): Feedback opt-in only
    "feedback_opt_in": {
        "enabled": True,
        "method": "explicit_checkbox",
        "disclosure": "Contact info used only for tool improvement",
        "retention_days": 90,
        "right_to_delete": True
    },
    
    # § 22757.2(c)(2): Limited content retention
    "content_retention": {
        "analysis_retention_seconds": 3600,  # 1 hour
        "auto_delete": True,
        "deletion_confirmation": True,
        "retention_policy_url": "https://aimedia.com/privacy"
    },
    
    # § 22757.2(c)(3): No personal provenance retention
    "provenance_handling": {
        "strip_personal_data": True,
        "retain_system_data": True,
        "retention_days": 30,
        "aggregate_only": True
    },
    
    "ccpa_compliant": True,
    "gdpr_compliant": True,
    "privacy_policy_url": "https://aimedia.com/privacy",
    "data_protection_officer": "dpo@aimedia.com"
})

# Verify compliance
assert privacy_config["collect_personal_info"] == False
assert privacy_config["content_retention"]["analysis_retention_seconds"] <= 3600
assert privacy_config["provenance_handling"]["strip_personal_data"] == True
```

---

## 📊 Article 3: Disclosure Requirements

### Section 22757.3(a): Manifest Disclosure Option

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 22757.3(a)(1)** - Identify as AI-generated | `manifest_identifier` field | `disclosure["identifier"] = "AI-Generated"` | `verify-california.py --sb942-a1` |
| **§ 22757.3(a)(2)** - Clear and conspicuous | `manifest_format` field | `disclosure["format"] = "visible_watermark"` | `verify-california.py --sb942-a2` |
| **§ 22757.3(a)(3)** - Permanent/difficult to remove | `manifest_permanence` field | `disclosure["permanence"] = "extraordinarily_difficult"` | `verify-california.py --sb942-a3` |

**Code Example:**
```python
# § 22757.3(a): Manifest disclosure option
manifest_option = tracker.create_manifest_disclosure_option({
    "option_name": "AI Content Watermark",
    "default": "off",
    "user_control": "toggle",
    "disclosure_types": ["image", "video", "audio"],
    
    # § 22757.3(a)(1): AI-generated identifier
    "identifier": {
        "text": "AI-Generated",
        "logo": "🤖",
        "icon": "ai_icon.svg",
        "placement_options": ["corner", "overlay", "border"]
    },
    
    # § 22757.3(a)(2): Clear and conspicuous
    "format": {
        "type": "visible_watermark",
        "opacity_range": [0.7, 0.9],
        "size": "medium",
        "contrast": "high",
        "color": "#FF0000"
    },
    
    # § 22757.3(a)(3): Permanent/difficult to remove
    "permanence": {
        "level": "extraordinarily_difficult",
        "method": "frequency_domain_embedding",
        "removal_detection": True,
        "robustness_tested": True,
        "testing_results": {
            "crop_removal": "failed",
            "filter_removal": "failed",
            "compression_removal": "failed"
        }
    },
    
    "preview_url": "https://aimedia.com/watermark-preview",
    "documentation_url": "https://aimedia.com/watermark-docs"
})

# User applies manifest disclosure
watermarked_content = tracker.apply_manifest_disclosure({
    "content_id": "IMG-2026-001",
    "content_type": "image",
    "original_content": original_image,
    "user_id": "USER-123",
    "options": {
        "identifier_text": "AI-Generated",
        "placement": "bottom_right",
        "opacity": 0.8,
        "size": "medium"
    }
})

# Verify manifest disclosure is present
detection_result = tracker.detect_manifest_disclosure(watermarked_content)
assert detection_result["has_manifest"] == True
assert detection_result["identifier"] == "AI-Generated"
```

---

### Section 22757.3(b): Latent Disclosure (Mandatory)

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 22757.3(b)(1)(A)** - Provider name | `provider_name` field | `disclosure["provider"] = "AI Media Corp"` | `verify-california.py --sb942-b1a` |
| **§ 22757.3(b)(1)(B)** - System name/version | `system_info` field | `disclosure["system"] = "ImageGen v2.1"` | `verify-california.py --sb942-b1b` |
| **§ 22757.3(b)(1)(C)** - Time and date | `timestamp` field | `disclosure["timestamp"] = time.time()` | `verify-california.py --sb942-b1c` |
| **§ 22757.3(b)(1)(D)** - Unique identifier | `unique_id` field | `disclosure["unique_id"] = uuid7()` | `verify-california.py --sb942-b1d` |
| **§ 22757.3(b)(2)** - Detectable by AI detection tool | `detectable_by_tool` field | `disclosure["detectable"] = True` | `verify-california.py --sb942-b2` |
| **§ 22757.3(b)(3)** - Industry standards | `industry_standards` field | `disclosure["standards"] = ["C2PA", "ISO"]` | `verify-california.py --sb942-b3` |
| **§ 22757.3(b)(4)** - Permanent/difficult to remove | `latent_permanence` field | `disclosure["permanence"] = "extraordinarily_difficult"` | `verify-california.py --sb942-b4` |

**Code Example:**
```python
# § 22757.3(b): Complete latent disclosure implementation
def embed_latent_disclosure(content, content_type, provider_info):
    """Embed mandatory latent disclosure into content."""
    
    # Generate unique ID (UUIDv7 for timestamp ordering)
    unique_id = tracker._generate_uuid7()
    
    # § 22757.3(b)(1)(A)-(D): Core disclosure data
    disclosure_data = {
        # § 22757.3(b)(1)(A): Provider name
        "provider": provider_info["name"],
        
        # § 22757.3(b)(1)(B): System name and version
        "system": provider_info["system"],
        "version": provider_info["version"],
        
        # § 22757.3(b)(1)(C): Time and date
        "timestamp": time.time(),
        "timestamp_iso": datetime.now().isoformat(),
        
        # § 22757.3(b)(1)(D): Unique identifier
        "unique_id": unique_id,
        
        # Additional: URL for verification (optional but recommended)
        "verify_url": f"https://verify.aimedia.com/content/{unique_id}"
    }
    
    # § 22757.3(b)(2): Ensure detectable by detection tool
    # Use steganographic embedding for images
    if content_type == "image":
        watermarked = embed_in_image(content, disclosure_data)
    elif content_type == "video":
        watermarked = embed_in_video(content, disclosure_data)
    elif content_type == "audio":
        watermarked = embed_in_audio(content, disclosure_data)
    
    # § 22757.3(b)(3): Industry standards compliance
    standards_compliance = {
        "c2pa": True,  # Coalition for Content Provenance and Authenticity
        "iso_iec_27050": True,
        "w3c_credentials": True
    }
    
    # § 22757.3(b)(4): Permanent/difficult to remove
    permanence = {
        "level": "extraordinarily_difficult",
        "method": "frequency_domain_embedding",
        "robustness_tests": {
            "compression": "survives 90% quality JPEG",
            "resize": "survives 50% scaling",
            "crop": "recoverable from 75% crop",
            "filter": "survives common filters"
        }
    }
    
    # Store mapping for detection tool
    tracker.register_content({
        "unique_id": unique_id,
        "provider": provider_info["name"],
        "timestamp": time.time(),
        "content_hash": hashlib.sha256(content).hexdigest()
    })
    
    return watermarked

# Usage example
watermarked = embed_latent_disclosure(
    content=original_image,
    content_type="image",
    provider_info={
        "name": "AI Media Corp",
        "system": "ImageGen Pro",
        "version": "2.1.0"
    }
)

# Detection tool can extract disclosure
detection_result = tracker.detect_latent_disclosure(watermarked)
assert detection_result["provider"] == "AI Media Corp"
assert detection_result["unique_id"] is not None
assert detection_result["timestamp"] > 0

# Optional: Provide permanent link (as allowed by § 22757.3(b))
permanent_link = f"https://verify.aimedia.com/content/{detection_result['unique_id']}"
print(f"Verify at: {permanent_link}")
```

---

### Section 22757.3(c): Licensee Requirements

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 22757.3(c)(1)** - Contract require maintenance | `license_contract_clause()` | `tracker.add_license_clause()` | `verify-california.py --sb942-c1` |
| **§ 22757.3(c)(2)** - Revoke license within 96 hours | `revoke_license()` | `tracker.revoke_license()` | `verify-california.py --sb942-c2` |
| **§ 22757.3(c)(3)** - Licensee cease use | `cease_use_notice()` | `tracker.notify_cease_use()` | `verify-california.py --sb942-c3` |

**Code Example:**
```python
# § 22757.3(c)(1): License contract with required clauses
license_agreement = tracker.create_license_agreement({
    "license_id": f"LIC-{int(time.time())}",
    "licensee": "Third-Party Corp",
    "effective_date": time.time(),
    "termination_date": time.time() + 31536000,  # 1 year
    
    # Required clause: maintain latent disclosure capabilities
    "latent_disclosure_clause": {
        "required": True,
        "obligation": "Licensee must maintain all latent disclosure capabilities",
        "modification_prohibition": "No modifications that disable latent disclosures",
        "audit_rights": "Provider may audit quarterly",
        "audit_notice": "7 days",
        "remedy_period": "30 days"
    },
    
    # Required clause: compliance reporting
    "reporting_requirements": {
        "frequency": "monthly",
        "method": "compliance_report",
        "due_within_days": 30,
        "report_format": "JSON",
        "include_metrics": ["content_count", "disclosure_rate", "violations"]
    },
    
    # Required clause: penalties for non-compliance
    "penalties": {
        "first_violation": "warning",
        "second_violation": "$10,000 fine",
        "third_violation": "license_revocation"
    }
})

# § 22757.3(c)(2): Monitor and revoke within 96 hours
monitoring_system = tracker.monitor_licensee_compliance({
    "license_id": license_agreement["license_id"],
    "monitoring_frequency": "continuous",
    "detection_method": "content_sampling",
    "sample_rate": 0.01,  # 1% of content
    "alert_threshold": 0.001  # 0.1% violation rate
})

# Simulate detection of non-compliance
if monitoring_system.detect_violation():
    violation = {
        "license_id": license_agreement["license_id"],
        "violation_id": f"VIO-{int(time.time())}",
        "detection_time": time.time(),
        "violation_type": "missing_latent_disclosure",
        "evidence": ["content_001.jpg", "content_002.mp4"],
        "severity": "high"
    }
    
    # § 22757.3(c)(2): Revoke within 96 hours
    revocation_deadline = violation["detection_time"] + 345600  # 96 hours
    current_time = time.time()
    
    if current_time <= revocation_deadline:
        revocation = tracker.revoke_license({
            "license_id": license_agreement["license_id"],
            "revocation_reason": violation["violation_type"],
            "detection_time": violation["detection_time"],
            "revocation_time": current_time,
            "compliant_96_hours": True,
            "notification_sent": True
        })
        
        # § 22757.3(c)(3): Notice to cease use
        cease_notice = tracker.notify_cease_use({
            "license_id": license_agreement["license_id"],
            "notice_time": current_time,
            "effective_immediately": True,
            "consequences": "Continued use may result in legal action under Bus. & Prof. Code § 22757.4",
            "proof_of_delivery": "email_receipt.pdf",
            "copy_to_attorney_general": True
        })
        
        assert revocation["compliant_96_hours"] == True
```

---

## 📊 Article 4: Penalties and Enforcement

### Section 22757.4: Penalties

| Requirement | JEP Implementation | Code Example | Verification |
|-------------|-------------------|--------------|--------------|
| **§ 22757.4(a)** - Civil penalty $5,000/violation | `track_violations()` | `tracker.log_violation()` | `verify-california.py --sb942-penalty` |
| **§ 22757.4(b)** - Each day = discrete violation | `daily_violation_count()` | `tracker.count_daily()` | `verify-california.py --sb942-daily` |
| **§ 22757.4(c)** - Injunctive relief for licensees | `prepare_injunction()` | `tracker.injunction_request()` | `verify-california.py --sb942-injunction` |

**Code Example:**
```python
# Track violations for compliance
violation_tracking = tracker.initialize_violation_tracking({
    "tracking_id": f"TRACK-{int(time.time())}",
    "start_date": "2026-08-02",  # Operative date
    "alert_on_violation": True,
    "daily_report": True
})

# Log a violation
violation = tracker.log_violation({
    "violation_id": f"VIO-{int(time.time())}",
    "date": time.time(),
    "type": "missing_latent_disclosure",
    "description": "Content generated without required latent disclosure",
    "affected_content_ids": ["CONTENT-001", "CONTENT-002"],
    "affected_users": 15000,
    "days_in_violation": 3,
    "estimated_penalty": 3 * 5000,  # $15,000
    "remediated": False,
    "remediation_deadline": time.time() + 259200  # 3 days
})

# Count daily violations for reporting
daily_report = tracker.generate_daily_violation_report({
    "date": "2026-08-15",
    "include_penalty_calculation": True
})

print(f"Daily Report: {daily_report}")
print(f"Total Violations: {daily_report['total_violations']}")
print(f"Estimated Penalty: ${daily_report['total_violations'] * 5000}")

# § 22757.4(c): Prepare for injunctive relief if needed
if daily_report['total_violations'] > 10:
    injunction_package = tracker.prepare_injunction_request({
        "licensee": "Non-Compliant Corp",
        "violations": daily_report['violations'],
        "total_days": daily_report['total_days'],
        "total_penalty": daily_report['total_violations'] * 5000,
        "evidence_files": daily_report['evidence'],
        "request_to": "California Attorney General",
        "filing_date": time.time() + 86400  # Tomorrow
    })
```

---

## ✅ Complete Verification

```bash
# Run SB 942 compliance verification
python tests/verify-california.py --sb942 --verbose

# Output:
# ========================================
# SB 942 AI TRANSPARENCY ACT COMPLIANCE
# ========================================
#
# 📋 Section 22757.2(a): Detection Tool
#   ✅ (1) Content origin assessment
#   ✅ (2) System provenance output
#   ✅ (3) No personal provenance data
#   ✅ (4) Publicly accessible
#   ✅ (5) URL submission
#   ✅ (6) API support
#
# 📋 Section 22757.2(b): Feedback Collection
#   ✅ Feedback system implemented
#   ✅ Tool updates incorporate feedback
#
# 📋 Section 22757.2(c): Privacy Protections
#   ✅ (1) No personal info collection
#   ✅ (1)(B) Feedback opt-in only
#   ✅ (2) Limited content retention
#   ✅ (3) No personal provenance retention
#
# 📋 Section 22757.3(a): Manifest Disclosure
#   ✅ (1) AI-generated identifier
#   ✅ (2) Clear and conspicuous
#   ✅ (3) Extraordinarily difficult to remove
#
# 📋 Section 22757.3(b): Latent Disclosure
#   ✅ (1)(A) Provider name
#   ✅ (1)(B) System name/version
#   ✅ (1)(C) Time and date
#   ✅ (1)(D) Unique identifier
#   ✅ (2) Detectable by tool
#   ✅ (3) Industry standards compliant
#   ✅ (4) Extraordinarily difficult to remove
#
# 📋 Section 22757.3(c): Licensee Requirements
#   ✅ (1) Contract clauses present
#   ✅ (2) 96-hour revocation capability
#   ✅ (3) Cease use notification
#
# 📋 Section 22757.4: Penalties
#   ✅ Violation tracking
#   ✅ Daily counting
#   ✅ Injunction preparation
#
# ========================================
# ✅ FULL COMPLIANCE VERIFIED
# ========================================
```

## ⚖️ Penalty Calculation Examples

| Scenario | Daily Violations | Days | Total Penalty |
|----------|-----------------|------|---------------|
| Missing detection tool | 1 | 30 | $150,000 |
| Missing latent disclosure | 100 content pieces | 1 | $500,000 |
| Licensee non-compliance | 1 licensee | 5 | $25,000 |
| Privacy violation | 1 | 7 | $35,000 |

## 📚 References

- [Full Text of SB 942](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240SB942)
- [California Business and Professions Code § 22757 et seq.](https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=BPC&division=8.&title=&part=&chapter=25.&article=)
- [California Attorney General AI Enforcement](https://oag.ca.gov/)

## 📬 Contact

For SB 942-specific inquiries:
- **Email**: signal@humanjudgment.org
- **GitHub**: [hjs-spec/jep-us-solutions](https://github.com/hjs-spec/jep-us-solutions)

---

*Last Updated: March 2026*
*Operative Date: August 2, 2026*
```
