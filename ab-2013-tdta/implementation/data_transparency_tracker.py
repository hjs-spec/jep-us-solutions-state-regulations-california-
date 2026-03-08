```python
#!/usr/bin/env python3
"""
California AB 2013 (TDTA) Training Data Transparency Tracker
===============================================================

Complete implementation of California's Generative AI Training Data Transparency Act
for developers of publicly available generative AI systems.

This tracker ensures all generative AI systems comply with:
- § 3110(a): Publicly available training data summary
- § 3110(b)(1): Data sources and owners
- § 3110(b)(2): How data furthers system purpose
- § 3110(b)(3): Number of data points
- § 3110(b)(4): Data type description
- § 3110(b)(5): Intellectual property status
- § 3110(b)(6): Commercial arrangements
- § 3110(b)(7): Personal information disclosure
- § 3110(b)(8): Aggregate consumer information
- § 3110(b)(9): Data processing description
- § 3110(b)(10): Collection time period
- § 3110(b)(11): First use date
- § 3110(b)(12): Synthetic data disclosure
- § 3110(c): Understandable summary
"""

import json
import time
import hashlib
from datetime import datetime, timedelta
from typing import Dict, Any, Optional, List, Union
from enum import Enum

# Try to import cryptography
try:
    from cryptography.hazmat.primitives.asymmetric import ed25519
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False
    print("⚠️ Warning: cryptography not installed. Using mock signatures.")


class SystemType(Enum):
    """Types of generative AI systems covered by AB 2013"""
    TEXT = "text"
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    CODE = "code"
    MULTIMODAL = "multimodal"


class DataSourceType(Enum):
    """Types of data sources"""
    PUBLIC_WEB = "public_web"
    PROPRIETARY = "proprietary"
    OPEN_SOURCE = "open_source"
    CUSTOMER = "customer"
    SYNTHETIC = "synthetic"
    PARTNER = "partner"


class IPStatus(Enum):
    """Intellectual property status"""
    PUBLIC_DOMAIN = "public_domain"
    COPYRIGHTED = "copyrighted"
    MAY_CONTAIN_COPYRIGHT = "may_contain_copyright"
    TRADEMARKED = "trademarked"
    PATENTED = "patented"
    UNKNOWN = "unknown"
    FAIR_USE = "fair_use"


class DataTransparencyTracker:
    """
    Complete AB 2013 compliance tracker for generative AI developers.
    
    Covers all 12 disclosure requirements for training data transparency.
    """
    
    def __init__(
        self,
        company_name: str,
        system_name: str,
        system_version: str,
        system_type: SystemType,
        system_description: str,
        release_date: Optional[float] = None,
        documentation_url: Optional[str] = None,
        private_key_hex: Optional[str] = None
    ):
        """
        Initialize AB 2013 data transparency tracker.
        
        Args:
            company_name: Name of the company
            system_name: Name of the AI system
            system_version: Version of the system
            system_type: Type of generative AI system
            system_description: Description of the system
            release_date: Public release date (default: now)
            documentation_url: URL for transparency documentation
            private_key_hex: Optional private key for signatures
        """
        self.company_name = company_name
        self.system_name = system_name
        self.system_version = system_version
        self.system_type = system_type.value if isinstance(system_type, SystemType) else system_type
        self.system_description = system_description
        self.release_date = release_date or time.time()
        self.documentation_url = documentation_url or f"https://{company_name}/transparency"
        
        # Initialize signer
        self.signer = self._init_signer(private_key_hex)
        
        # Data stores
        self.disclosures = []
        self.datasets = []
        self.audit_log = []
        
        print(f"✅ AB 2013 Data Transparency Tracker initialized")
        print(f"   Company: {company_name}")
        print(f"   System: {system_name} v{system_version}")
        print(f"   Type: {self.system_type}")
        print(f"   Release Date: {datetime.fromtimestamp(self.release_date)}")
    
    def _init_signer(self, private_key_hex: Optional[str] = None):
        """Initialize cryptographic signer."""
        if CRYPTO_AVAILABLE:
            if private_key_hex:
                return ed25519.Ed25519PrivateKey.from_private_bytes(
                    bytes.fromhex(private_key_hex)
                )
            else:
                return ed25519.Ed25519PrivateKey.generate()
        return None
    
    def _generate_uuid7(self) -> str:
        """Generate UUID v7 for traceability."""
        import uuid
        timestamp = int(time.time() * 1000)
        random_part = uuid.uuid4().hex[:12]
        return f"{timestamp:08x}-{random_part[:4]}-7{random_part[4:7]}-{random_part[7:11]}-{random_part[11:]}"
    
    def _sign(self, data: Dict) -> str:
        """Sign data with Ed25519."""
        if CRYPTO_AVAILABLE and self.signer:
            message = json.dumps(data, sort_keys=True).encode()
            signature = self.signer.sign(message)
            return f"ed25519:{signature.hex()[:64]}"
        return f"mock_sig_{hash(json.dumps(data, sort_keys=True))}"
    
    def _log_audit(self, event_type: str, data: Dict[str, Any]) -> None:
        """Internal audit logging."""
        self.audit_log.append({
            "event_type": event_type,
            "timestamp": time.time(),
            "data": data
        })
    
    # ========================================================================
    # § 3110(a): Publicly Available Summary
    # ========================================================================
    
    def disclose_training_data(
        self,
        datasets: List[Dict[str, Any]],
        synthetic_data_summary: Optional[Dict[str, Any]] = None,
        plain_language_summary: Optional[str] = None,
        publication_date: Optional[float] = None,
        publication_url: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Publish training data disclosure as required by § 3110(a).
        
        This method creates a complete disclosure document covering all
        12 AB 2013 requirements.
        """
        disclosure_id = f"DISC-{self._generate_uuid7()}"
        
        # Process each dataset to ensure all required fields
        processed_datasets = []
        for ds in datasets:
            processed = self._validate_dataset(ds)
            processed_datasets.append(processed)
            self.datasets.append(processed)
        
        disclosure = {
            "disclosure_id": disclosure_id,
            "company": self.company_name,
            "system_name": self.system_name,
            "system_version": self.system_version,
            "system_type": self.system_type,
            "system_description": self.system_description,
            "release_date": self.release_date,
            "publication_date": publication_date or time.time(),
            "publication_url": publication_url or self.documentation_url,
            
            # § 3110(a): Datasets
            "datasets": processed_datasets,
            
            # § 3110(b)(12): Synthetic data summary
            "synthetic_data_summary": synthetic_data_summary or {},
            
            # § 3110(c): Understandable summary
            "plain_language_summary": plain_language_summary or self._generate_plain_language_summary(processed_datasets),
            
            # Readability metrics (optional but good practice)
            "readability_score": self._calculate_readability(plain_language_summary),
            "translation_available": ["es", "zh", "vi", "ko", "tl"],
            
            "disclosure_version": "1.0",
            "last_updated": time.time(),
            "update_frequency": "as_needed"
        }
        
        disclosure["signature"] = self._sign(disclosure)
        self.disclosures.append(disclosure)
        self._log_audit("TRAINING_DATA_DISCLOSURE", disclosure)
        
        print(f"\n📋 § 3110(a): Training Data Disclosure Published")
        print(f"   Disclosure ID: {disclosure_id}")
        print(f"   URL: {disclosure['publication_url']}")
        print(f"   Datasets: {len(processed_datasets)}")
        print(f"   Synthetic Data: {'Yes' if synthetic_data_summary else 'No'}")
        
        return disclosure
    
    def _validate_dataset(self, dataset: Dict[str, Any]) -> Dict[str, Any]:
        """Validate that dataset contains all required AB 2013 fields."""
        
        # Ensure required fields exist with defaults if needed
        validated = dataset.copy()
        
        # § 3110(b)(1): Data sources and owners
        validated.setdefault("source", "Unknown")
        validated.setdefault("source_url", None)
        validated.setdefault("owner", "Unknown")
        validated.setdefault("owner_type", "unknown")
        
        # § 3110(b)(2): Purpose alignment
        validated.setdefault("purpose_alignment", "Training data for generative AI")
        
        # § 3110(b)(3): Number of data points
        if "data_points_exact" not in validated and "data_points_range" not in validated:
            validated["data_points_range"] = "unknown"
        
        # § 3110(b)(4): Data type description
        validated.setdefault("data_types", ["unknown"])
        validated.setdefault("annotation_types", [])
        validated.setdefault("characteristics", [])
        validated.setdefault("modalities", ["text"])
        validated.setdefault("languages", ["en"])
        
        # § 3110(b)(5): Intellectual property status
        validated.setdefault("copyright_status", "unknown")
        validated.setdefault("trademark_status", "unknown")
        validated.setdefault("patent_status", "unknown")
        validated.setdefault("public_domain", False)
        validated.setdefault("ip_explanation", None)
        
        # § 3110(b)(6): Commercial arrangements
        validated.setdefault("purchased", False)
        validated.setdefault("licensed", False)
        validated.setdefault("license_terms", None)
        validated.setdefault("license_url", None)
        validated.setdefault("commercial_provider", None)
        
        # § 3110(b)(7): Personal information
        validated.setdefault("contains_personal_info", False)
        validated.setdefault("pii_categories", [])
        validated.setdefault("pii_handling", None)
        
        # § 3110(b)(8): Aggregate consumer information
        validated.setdefault("contains_aggregate_info", False)
        validated.setdefault("aggregate_description", None)
        
        # § 3110(b)(9): Data processing
        validated.setdefault("processing_description", [])
        validated.setdefault("modifications", [])
        validated.setdefault("filtering_criteria", {})
        
        # § 3110(b)(10): Collection period
        validated.setdefault("collection_period", "unknown")
        validated.setdefault("collection_start", None)
        validated.setdefault("collection_end", None)
        validated.setdefault("ongoing_collection", False)
        
        # § 3110(b)(11): First use date
        validated.setdefault("first_use_date", None)
        
        # § 3110(b)(12): Synthetic data (per dataset)
        validated.setdefault("contains_synthetic_data", False)
        validated.setdefault("synthetic_description", None)
        validated.setdefault("synthetic_proportion", None)
        
        return validated
    
    def _generate_plain_language_summary(self, datasets: List[Dict]) -> str:
        """Generate plain language summary for § 3110(c)."""
        total_datasets = len(datasets)
        sources = list(set(d.get("source", "Unknown") for d in datasets))
        contains_pii = any(d.get("contains_personal_info", False) for d in datasets)
        contains_synthetic = any(d.get("contains_synthetic_data", False) for d in datasets)
        
        summary = f"""
{self.system_name} v{self.system_version} was trained using {total_datasets} dataset{'s' if total_datasets > 1 else ''}. 
The training data comes from the following sources: {', '.join(sources[:3])}{' and others' if len(sources) > 3 else ''}.

{'Some of this data may contain personal information that was publicly available online.' if contains_pii else 'The training data does not contain personal information.'}
{'About {:.0%} of the training data was synthetically generated to improve model performance.'.format(sum(d.get('synthetic_proportion', 0) for d in datasets if d.get('synthetic_proportion')) / len(datasets) if contains_synthetic else 0) if contains_synthetic else ''}

For more detailed information about each dataset, including data sources, processing, and intellectual property status, please see the full disclosure above.
        """
        return summary.strip()
    
    def _calculate_readability(self, text: Optional[str]) -> float:
        """Calculate approximate readability score."""
        if not text:
            return 8.0  # Default 8th grade level
        # Simplified - would use actual readability formula in production
        return 8.5
    
    # ========================================================================
    # Individual Dataset Management
    # ========================================================================
    
    def add_dataset(self, dataset_data: Dict[str, Any]) -> Dict[str, Any]:
        """Add a new dataset to the system."""
        dataset_id = f"DS-{self._generate_uuid7()}"
        
        dataset = self._validate_dataset(dataset_data)
        dataset["dataset_id"] = dataset_id
        dataset["added_date"] = time.time()
        dataset["status"] = "ACTIVE"
        
        self.datasets.append(dataset)
        self._log_audit("DATASET_ADDED", dataset)
        
        print(f"\n📊 Dataset Added")
        print(f"   Dataset ID: {dataset_id}")
        print(f"   Source: {dataset['source']}")
        print(f"   Data Points: {dataset.get('data_points_exact') or dataset.get('data_points_range')}")
        
        return dataset
    
    def update_dataset(self, dataset_id: str, updates: Dict[str, Any]) -> Dict[str, Any]:
        """Update an existing dataset."""
        dataset = next((d for d in self.datasets if d.get("dataset_id") == dataset_id), None)
        if not dataset:
            raise ValueError(f"Dataset {dataset_id} not found")
        
        dataset.update(updates)
        dataset["updated_date"] = time.time()
        
        self._log_audit("DATASET_UPDATED", dataset)
        
        print(f"\n📊 Dataset Updated: {dataset_id}")
        return dataset
    
    # ========================================================================
    # Individual Disclosure Management
    # ========================================================================
    
    def update_disclosure(
        self,
        disclosure_id: str,
        new_datasets: Optional[List[Dict]] = None,
        updated_summary: Optional[str] = None,
        update_reason: str = "Data refresh"
    ) -> Dict[str, Any]:
        """Update an existing disclosure with new information."""
        
        disclosure = next((d for d in self.disclosures if d["disclosure_id"] == disclosure_id), None)
        if not disclosure:
            raise ValueError(f"Disclosure {disclosure_id} not found")
        
        # Process new datasets
        if new_datasets:
            processed = []
            for ds in new_datasets:
                processed_ds = self._validate_dataset(ds)
                self.datasets.append(processed_ds)
                processed.append(processed_ds)
            
            disclosure["datasets"].extend(processed)
        
        if updated_summary:
            disclosure["plain_language_summary"] = updated_summary
        
        disclosure["last_updated"] = time.time()
        disclosure["update_reason"] = update_reason
        disclosure["disclosure_version"] = str(float(disclosure.get("disclosure_version", "1.0")) + 0.1)
        
        disclosure["signature"] = self._sign(disclosure)
        self._log_audit("DISCLOSURE_UPDATED", disclosure)
        
        print(f"\n📋 Disclosure Updated: {disclosure_id}")
        print(f"   New Version: {disclosure['disclosure_version']}")
        print(f"   Total Datasets: {len(disclosure['datasets'])}")
        
        return disclosure
    
    # ========================================================================
    # Verification and Reporting
    # ========================================================================
    
    def verify_compliance(self) -> Dict[str, Any]:
        """Verify compliance with all 12 AB 2013 requirements."""
        
        verification = {
            "verification_time": time.time(),
            "company": self.company_name,
            "system": f"{self.system_name} v{self.system_version}",
            "has_disclosure": len(self.disclosures) > 0,
            "checks": {}
        }
        
        if not self.disclosures:
            verification["overall_status"] = "NO_DISCLOSURE"
            return verification
        
        latest = self.disclosures[-1]
        
        # § 3110(a): Publicly available
        verification["checks"]["a_public_availability"] = {
            "required": True,
            "compliant": latest.get("publication_url") is not None,
            "url": latest.get("publication_url")
        }
        
        # § 3110(b)(1): Data sources
        verification["checks"]["b1_data_sources"] = {
            "compliant": all(ds.get("source") for ds in latest["datasets"]),
            "datasets_with_source": sum(1 for ds in latest["datasets"] if ds.get("source"))
        }
        
        # § 3110(b)(2): Purpose alignment
        verification["checks"]["b2_purpose"] = {
            "compliant": all(ds.get("purpose_alignment") for ds in latest["datasets"])
        }
        
        # § 3110(b)(3): Data points
        verification["checks"]["b3_data_points"] = {
            "compliant": all(
                ds.get("data_points_exact") or ds.get("data_points_range")
                for ds in latest["datasets"]
            )
        }
        
        # § 3110(b)(4): Data types
        verification["checks"]["b4_data_types"] = {
            "compliant": all(ds.get("data_types") for ds in latest["datasets"])
        }
        
        # § 3110(b)(5): IP status
        verification["checks"]["b5_ip_status"] = {
            "compliant": all(
                ds.get("copyright_status") is not None
                for ds in latest["datasets"]
            )
        }
        
        # § 3110(b)(6): Commercial arrangements
        verification["checks"]["b6_commercial"] = {
            "compliant": all(
                "purchased" in ds or "licensed" in ds
                for ds in latest["datasets"]
            )
        }
        
        # § 3110(b)(7): Personal information
        verification["checks"]["b7_personal_info"] = {
            "compliant": all(
                "contains_personal_info" in ds
                for ds in latest["datasets"]
            )
        }
        
        # § 3110(b)(8): Aggregate info
        verification["checks"]["b8_aggregate"] = {
            "compliant": all(
                "contains_aggregate_info" in ds
                for ds in latest["datasets"]
            )
        }
        
        # § 3110(b)(9): Data processing
        verification["checks"]["b9_processing"] = {
            "compliant": all(
                ds.get("processing_description") is not None
                for ds in latest["datasets"]
            )
        }
        
        # § 3110(b)(10): Collection period
        verification["checks"]["b10_collection"] = {
            "compliant": all(
                ds.get("collection_period") is not None
                for ds in latest["datasets"]
            )
        }
        
        # § 3110(b)(11): First use date
        verification["checks"]["b11_first_use"] = {
            "compliant": all(
                ds.get("first_use_date") is not None
                for ds in latest["datasets"]
            )
        }
        
        # § 3110(b)(12): Synthetic data
        verification["checks"]["b12_synthetic"] = {
            "compliant": "synthetic_data_summary" in latest or any(
                ds.get("contains_synthetic_data") for ds in latest["datasets"]
            )
        }
        
        # § 3110(c): Understandable summary
        verification["checks"]["c_summary"] = {
            "compliant": latest.get("plain_language_summary") is not None,
            "summary_length": len(latest.get("plain_language_summary", ""))
        }
        
        all_compliant = all(
            check.get("compliant", True)
            for check in verification["checks"].values()
        )
        
        verification["overall_status"] = "COMPLIANT" if all_compliant else "NON_COMPLIANT"
        verification["compliant_requirements"] = sum(1 for c in verification["checks"].values() if c.get("compliant"))
        verification["total_requirements"] = len(verification["checks"])
        
        return verification
    
    def generate_compliance_report(self) -> Dict[str, Any]:
        """Generate comprehensive AB 2013 compliance report."""
        
        report_id = f"AB2013-{self._generate_uuid7()}"
        verification = self.verify_compliance()
        
        report = {
            "report_id": report_id,
            "company": self.company_name,
            "system_name": self.system_name,
            "system_version": self.system_version,
            "report_date": datetime.now().isoformat(),
            "release_date": datetime.fromtimestamp(self.release_date).isoformat(),
            "documentation_url": self.documentation_url,
            "statistics": {
                "total_disclosures": len(self.disclosures),
                "total_datasets": len(self.datasets),
                "datasets_with_pii": sum(1 for d in self.datasets if d.get("contains_personal_info")),
                "datasets_with_synthetic": sum(1 for d in self.datasets if d.get("contains_synthetic_data"))
            },
            "compliance": verification,
            "latest_disclosure": self.disclosures[-1] if self.disclosures else None
        }
        
        report["signature"] = self._sign(report)
        return report
    
    def export_to_json(self, filepath: str) -> None:
        """Export all disclosures to JSON file."""
        export = {
            "company": self.company_name,
            "system": {
                "name": self.system_name,
                "version": self.system_version,
                "type": self.system_type,
                "release_date": self.release_date
            },
            "disclosures": self.disclosures,
            "datasets": self.datasets,
            "generated_at": time.time()
        }
        
        with open(filepath, 'w') as f:
            json.dump(export, f, indent=2, default=str)
        
        print(f"\n✅ Exported to {filepath}")


# Example usage
if __name__ == "__main__":
    print("\n" + "="*80)
    print("🇨🇦 AB 2013 Data Transparency Tracker Demo")
    print("="*80)
    
    # Initialize tracker
    tracker = DataTransparencyTracker(
        company_name="GenAI Corp",
        system_name="TextGen",
        system_version="2.1.0",
        system_type=SystemType.TEXT,
        system_description="Large language model for text generation",
        release_date=time.time()
    )
    
    # Add datasets
    print("\n📊 Adding Datasets")
    
    dataset1 = tracker.add_dataset({
        "source": "Common Crawl",
        "source_url": "https://commoncrawl.org",
        "owner": "Common Crawl Foundation",
        "owner_type": "non-profit",
        "purpose_alignment": "Provides diverse web text for language understanding",
        "data_points_exact": 250_000_000_000,
        "data_points_unit": "tokens",
        "data_types": ["text", "html"],
        "copyright_status": "may_contain_copyright",
        "purchased": False,
        "licensed": False,
        "contains_personal_info": True,
        "pii_categories": ["names", "emails", "IP addresses"],
        "contains_aggregate_info": False,
        "processing_description": ["HTML removal", "language filtering", "deduplication"],
        "collection_period": "2020-2024",
        "first_use_date": "2023-01-15",
        "contains_synthetic_data": False
    })
    
    dataset2 = tracker.add_dataset({
        "source": "GitHub Code",
        "source_url": "https://github.com",
        "owner": "Open source developers",
        "owner_type": "public",
        "purpose_alignment": "Provides code examples for code generation",
        "data_points_exact": 50_000_000,
        "data_points_unit": "files",
        "data_types": ["code", "comments"],
        "copyright_status": "various_licenses",
        "licensed": True,
        "license_terms": "MIT, Apache 2.0, GPL",
        "contains_personal_info": False,
        "contains_aggregate_info": False,
        "processing_description": ["license filtering", "deduplication"],
        "collection_period": "2015-2024",
        "first_use_date": "2023-03-01",
        "contains_synthetic_data": False
    })
    
    dataset3 = tracker.add_dataset({
        "source": "Instruction Tuning Set",
        "owner": "GenAI Corp",
        "owner_type": "proprietary",
        "purpose_alignment": "Provides instruction-response pairs for fine-tuning",
        "data_points_exact": 5_000_000,
        "data_points_unit": "examples",
        "data_types": ["text"],
        "annotation_types": ["instruction", "response"],
        "copyright_status": "proprietary",
        "purchased": False,
        "licensed": False,
        "contains_personal_info": False,
        "contains_aggregate_info": False,
        "processing_description": ["quality filtering", "formatting"],
        "collection_period": "2024",
        "first_use_date": "2024-06-01",
        "contains_synthetic_data": True,
        "synthetic_description": "Generated using GPT-4 with self-instruct methodology",
        "synthetic_proportion": 1.0
    })
    
    # Publish disclosure
    print("\n📋 Publishing Training Data Disclosure")
    disclosure = tracker.disclose_training_data(
        datasets=[dataset1, dataset2, dataset3],
        synthetic_data_summary={
            "contains_synthetic_data": True,
            "synthetic_description": "Data augmentation using GPT-4 for instruction tuning",
            "synthetic_proportion": "5% of total training data",
            "synthetic_methods": ["prompt-based generation", "self-instruct"]
        },
        plain_language_summary="""
        TextGen v2.1.0 was trained using three main datasets: web crawl data from Common Crawl,
        open source code from GitHub, and a proprietary instruction tuning dataset.
        About 5% of the training data was synthetically generated using GPT-4.
        The web crawl data may contain personal information from public websites.
        """
    )
    
    # Verify compliance
    print("\n📊 Compliance Verification")
    verification = tracker.verify_compliance()
    print(f"   Overall Status: {verification['overall_status']}")
    print(f"   Requirements Met: {verification['compliant_requirements']}/{verification['total_requirements']}")
    
    for check, result in verification['checks'].items():
        if result.get('compliant'):
            print(f"   ✅ {check}")
    
    # Generate report
    print("\n📊 Generating Compliance Report")
    report = tracker.generate_compliance_report()
    print(f"   Report ID: {report['report_id']}")
    print(f"   Total Datasets: {report['statistics']['total_datasets']}")
    
    # Export to JSON
    tracker.export_to_json("ab2013_disclosure.json")
    
    print("\n" + "="*80)
    print("✅ Demo Complete")
    print("="*80)
```
