from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Type, Union
from xsdata.models.datatype import XmlDate, XmlPeriod, XmlTime


class AccessRuleValue(Enum):
    READ = "read"
    WRITE = "write"
    CHANGE_PERMISSION = "changePermission"
    ALL = "all"


class AccessTypeOrder(Enum):
    ALLOW_FIRST = "allowFirst"
    DENY_FIRST = "denyFirst"


@dataclass
class AccuracyQuantitativeAttributeAccuracyAssessment:
    class Meta:
        global_type = False

    attribute_accuracy_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "attributeAccuracyValue",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    attribute_accuracy_explanation: Optional[str] = field(
        default=None,
        metadata={
            "name": "attributeAccuracyExplanation",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class AttributeTypeMissingValueCode:
    class Meta:
        global_type = False

    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    code_explanation: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeExplanation",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class AttributeTypeStorageType:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    type_system: str = field(
        default="http://www.w3.org/2001/XMLSchema-datatypes",
        metadata={
            "name": "typeSystem",
            "type": "Attribute",
        }
    )


@dataclass
class BoundsDateGroupBoundsMaximum:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    exclusive: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class BoundsDateGroupBoundsMinimum:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    exclusive: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class BoundsGroupBoundsMaximum:
    class Meta:
        global_type = False

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    exclusive: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class BoundsGroupBoundsMinimum:
    class Meta:
        global_type = False

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    exclusive: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class NonNumericDomainTypeEnumeratedDomainCodeDefinition:
    class Meta:
        global_type = False

    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    definition: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


class NonNumericDomainTypeEnumeratedDomainEnforced(Enum):
    YES = "yes"
    NO = "no"


@dataclass
class NonNumericDomainTypeEnumeratedDomainEntityCodeList:
    class Meta:
        global_type = False

    entity_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityReference",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    value_attribute_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "valueAttributeReference",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    definition_attribute_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "definitionAttributeReference",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    order_attribute_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "orderAttributeReference",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class NonNumericDomainTypeTextDomain:
    class Meta:
        global_type = False

    definition: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    pattern: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


class NumberType(Enum):
    NATURAL = "natural"
    WHOLE = "whole"
    INTEGER = "integer"
    REAL = "real"


class CardinalityChildOccurancesTypeValue(Enum):
    MANY = "many"


@dataclass
class ConstraintTypeCheckConstraint:
    class Meta:
        global_type = False

    constraint_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "constraintName",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    constraint_description: Optional[object] = field(
        default=None,
        metadata={
            "name": "constraintDescription",
            "type": "Element",
            "namespace": "",
        }
    )
    check_condition: Optional[str] = field(
        default=None,
        metadata={
            "name": "checkCondition",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ConstraintTypeJoinConditionReferencedKey:
    class Meta:
        global_type = False

    attribute_reference: List[str] = field(
        default_factory=list,
        metadata={
            "name": "attributeReference",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class ConstraintTypeNotNullConstraintKey:
    class Meta:
        global_type = False

    attribute_reference: List[str] = field(
        default_factory=list,
        metadata={
            "name": "attributeReference",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class ConstraintTypePrimaryKeyKey:
    class Meta:
        global_type = False

    attribute_reference: List[str] = field(
        default_factory=list,
        metadata={
            "name": "attributeReference",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class ConstraintTypeUniqueKeyKey:
    class Meta:
        global_type = False

    attribute_reference: List[str] = field(
        default_factory=list,
        metadata={
            "name": "attributeReference",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


class ForeignKeyGroupCardinalityParentOccurences(Enum):
    VALUE_0 = 0
    VALUE_1 = 1


@dataclass
class ForeignKeyGroupKey:
    class Meta:
        global_type = False

    attribute_reference: List[str] = field(
        default_factory=list,
        metadata={
            "name": "attributeReference",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


class ForeignKeyGroupRelationshipType(Enum):
    IDENTIFYING = "identifying"
    NON_IDENTIFYING = "non-identifying"


@dataclass
class GringPointType:
    class Meta:
        name = "GRingPointType"
        target_namespace = "eml://ecoinformatics.org/coverage-2.1.1"

    g_ring_latitude: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "gRingLatitude",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("-90.0"),
            "max_inclusive": Decimal("90.0"),
        }
    )
    g_ring_longitude: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "gRingLongitude",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("-180.0"),
            "max_inclusive": Decimal("180.0"),
        }
    )


@dataclass
class SingleDateTimeTypeAlternativeTimeScale:
    class Meta:
        global_type = False

    time_scale_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "timeScaleName",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    time_scale_age_estimate: Optional[str] = field(
        default=None,
        metadata={
            "name": "timeScaleAgeEstimate",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    time_scale_age_uncertainty: Optional[str] = field(
        default=None,
        metadata={
            "name": "timeScaleAgeUncertainty",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    time_scale_age_explanation: Optional[str] = field(
        default=None,
        metadata={
            "name": "timeScaleAgeExplanation",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    time_scale_citation: List["CitationType"] = field(
        default_factory=list,
        metadata={
            "name": "timeScaleCitation",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TaxonomicClassificationType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/coverage-2.1.1"

    taxon_rank_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "taxonRankName",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    taxon_rank_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "taxonRankValue",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    common_name: List[str] = field(
        default_factory=list,
        metadata={
            "name": "commonName",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    taxonomic_classification: List["TaxonomicClassificationType"] = field(
        default_factory=list,
        metadata={
            "name": "taxonomicClassification",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TaxonomicCoverageTaxonomicSystemClassificationSystem:
    class Meta:
        global_type = False

    classification_system_citation: Optional["CitationType"] = field(
        default=None,
        metadata={
            "name": "classificationSystemCitation",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    classification_system_modifications: Optional[str] = field(
        default=None,
        metadata={
            "name": "classificationSystemModifications",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


class DataTableTypeCaseSensitive(Enum):
    YES = "yes"
    NO = "no"


class MaintUpFreqType(Enum):
    ANNUALLY = "annually"
    AS_NEEDED = "asNeeded"
    BIANNUALLY = "biannually"
    CONTINUALLY = "continually"
    DAILY = "daily"
    IRREGULAR = "irregular"
    MONTHLY = "monthly"
    NOT_PLANNED = "notPlanned"
    WEEKLY = "weekly"
    UNKOWN = "unkown"
    OTHER_MAINTENANCE_PERIOD = "otherMaintenancePeriod"


@dataclass
class MaintenanceTypeChangeHistory:
    class Meta:
        global_type = False

    change_scope: Optional[str] = field(
        default=None,
        metadata={
            "name": "changeScope",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    old_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "oldValue",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    change_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "changeDate",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class Lineage:
    class Meta:
        name = "lineage"
        namespace = "eml://ecoinformatics.org/documentation-2.1.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Module:
    class Meta:
        name = "module"
        namespace = "eml://ecoinformatics.org/documentation-2.1.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Summary:
    class Meta:
        name = "summary"
        namespace = "eml://ecoinformatics.org/documentation-2.1.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Tooltip:
    class Meta:
        name = "tooltip"
        namespace = "eml://ecoinformatics.org/documentation-2.1.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class EmlAdditionalMetadataMetadata:
    class Meta:
        global_type = False

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class EntityGroupAlternateIdentifier:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    system: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class ResponsiblePartyPhone:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    phonetype: str = field(
        default="voice",
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ResponsiblePartyUserId:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    directory: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class RoleTypeValue(Enum):
    CONTENT_PROVIDER = "contentProvider"
    CUSTODIAN_STEWARD = "custodianSteward"
    OWNER = "owner"
    USER = "user"
    DISTRIBUTOR = "distributor"
    METADATA_PROVIDER = "metadataProvider"
    ORIGINATOR = "originator"
    POINT_OF_CONTACT = "pointOfContact"
    PRINCIPAL_INVESTIGATOR = "principalInvestigator"
    PROCESSOR = "processor"
    PUBLISHER = "publisher"
    AUTHOR = "author"
    EDITOR = "editor"


@dataclass
class PhysicalTypeAuthentication:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    method: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class PhysicalTypeDataFormatBinaryRasterFormatMultiBand:
    class Meta:
        global_type = False

    nbands: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    layout: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


class PhysicalTypeDataFormatBinaryRasterFormatRowColumnOrientation(Enum):
    COLUMN = "column"
    ROW = "row"


class PhysicalTypeDataFormatTextFormatAttributeOrientation(Enum):
    COLUMN = "column"
    ROW = "row"


class PhysicalTypeDataFormatTextFormatComplexTextDelimitedCollapseDelimiters(Enum):
    YES = "yes"
    NO = "no"


@dataclass
class PhysicalTypeDataFormatTextFormatComplexTextFixed:
    class Meta:
        global_type = False

    field_width: Optional[int] = field(
        default=None,
        metadata={
            "name": "fieldWidth",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    line_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "lineNumber",
            "type": "Element",
            "namespace": "",
        }
    )
    field_start_column: Optional[int] = field(
        default=None,
        metadata={
            "name": "fieldStartColumn",
            "type": "Element",
            "namespace": "",
        }
    )


class PhysicalTypeDataFormatTextFormatSimpleDelimitedCollapseDelimiters(Enum):
    YES = "yes"
    NO = "no"


@dataclass
class PhysicalTypeSize:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    unit: str = field(
        default="byte",
        metadata={
            "type": "Attribute",
        }
    )


class DescriptorTypeValue(Enum):
    CLIMATE = "climate"
    HYDROLOGY = "hydrology"
    SOILS = "soils"
    GEOLOGY = "geology"
    DISTURBANCE = "disturbance"
    BAILEY = "bailey"
    BIOME = "biome"


@dataclass
class ResearchProjectTypeStudyAreaDescriptionDescriptorDescriptorValue:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    name_or_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ConnectionDefinitionTypeParameterDefinition:
    class Meta:
        global_type = False

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    definition: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    default_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "defaultValue",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class ConnectionDefinitionTypeSchemeName:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    system: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class ConnectionTypeParameter:
    class Meta:
        global_type = False

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


class FunctionType(Enum):
    DOWNLOAD = "download"
    INFORMATION = "information"


@dataclass
class InlineType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/resource-2.1.1"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


class KeyTypeCode(Enum):
    PLACE = "place"
    STRATUM = "stratum"
    TEMPORAL = "temporal"
    THEME = "theme"
    TAXONOMIC = "taxonomic"


@dataclass
class OfflineType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/resource-2.1.1"

    medium_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "mediumName",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    medium_density: Optional[str] = field(
        default=None,
        metadata={
            "name": "mediumDensity",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    medium_density_units: Optional[str] = field(
        default=None,
        metadata={
            "name": "mediumDensityUnits",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    medium_volume: Optional[str] = field(
        default=None,
        metadata={
            "name": "mediumVolume",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    medium_format: List[str] = field(
        default_factory=list,
        metadata={
            "name": "mediumFormat",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    medium_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "mediumNote",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class ReferencesGroupReferences:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    system: List[str] = field(
        default_factory=lambda: [
            "document",
        ],
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class ResourceGroupAlternateIdentifier:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    system: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )


class ScopeType(Enum):
    SYSTEM = "system"
    DOCUMENT = "document"


class Action(Enum):
    INSTALL = "install"
    ASSERT = "assert"


@dataclass
class SoftwareTypeImplementationLanguage:
    class Meta:
        global_type = False

    language_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "LanguageValue",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    language_code_standard: Optional[str] = field(
        default=None,
        metadata={
            "name": "LanguageCodeStandard",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


class CellGeometryType(Enum):
    PIXEL = "pixel"
    MATRIX = "matrix"


@dataclass
class DataQualityQuantitativeAccuracyReport1:
    class Meta:
        global_type = False

    quantitative_accuracy_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "quantitativeAccuracyValue",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    quantitative_accuracy_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "quantitativeAccuracyMethod",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


class ImagingConditionCode(Enum):
    BLURREDIMAGE = "blurredimage"
    CLOUD = "cloud"
    DEGRADING_OBLIQUITY = "degradingObliquity"
    FOG = "fog"
    HEAVY_SMOKEOR_DUST = "heavySmokeorDust"
    NIGHT = "night"
    RAIN = "rain"
    SEMI_DARKNESS = "semiDarkness"
    SHADOW = "shadow"
    SNOW = "snow"
    TERRAIN_MASKING = "terrainMasking"


@dataclass
class SpatialRasterTypeGeoreferenceInfoBilinearFit:
    class Meta:
        global_type = False

    x_intercept: Optional[float] = field(
        default=None,
        metadata={
            "name": "xIntercept",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    x_slope: Optional[float] = field(
        default=None,
        metadata={
            "name": "xSlope",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    y_intercept: Optional[float] = field(
        default=None,
        metadata={
            "name": "yIntercept",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    y_slope: Optional[float] = field(
        default=None,
        metadata={
            "name": "ySlope",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


class SpatialRasterTypeGeoreferenceInfoControlPointPointInPixel(Enum):
    UPPER_LEFT = "upperLeft"
    UPPER_RIGHT = "upperRight"
    LOWER_RIGHT = "lowerRight"
    LOWER_LEFT = "lowerLeft"
    CENTER = "center"


class SpatialRasterTypeGeoreferenceInfoCornerPointPointInPixel(Enum):
    UPPER_LEFT = "upperLeft"
    UPPER_RIGHT = "upperRight"
    LOWER_RIGHT = "lowerRight"
    LOWER_LEFT = "lowerLeft"
    CENTER = "center"


class RasterOriginType(Enum):
    UPPER_LEFT = "Upper Left"
    LOWER_LEFT = "Lower Left"
    UPPER_RIGHT = "Upper Right"
    LOWER_RIGHT = "Lower Right"


class SpatialReferenceTypeHorizCoordSysName(Enum):
    GCS_ABIDJAN_1987 = "GCS_Abidjan_1987"
    GCS_ACCRA = "GCS_Accra"
    GCS_ADINDAN = "GCS_Adindan"
    GCS_AFGOOYE = "GCS_Afgooye"
    GCS_AGADEZ = "GCS_Agadez"
    GCS_AIN_EL_ABD_1970 = "GCS_Ain_el_Abd_1970"
    GCS_ARC_1950 = "GCS_Arc_1950"
    GCS_ARC_1960 = "GCS_Arc_1960"
    GCS_AYABELLE = "GCS_Ayabelle"
    GCS_BEDUARAM = "GCS_Beduaram"
    GCS_BISSAU = "GCS_Bissau"
    GCS_CAMACUPA = "GCS_Camacupa"
    GCS_CAPE = "GCS_Cape"
    GCS_CARTHAGE_DEGREE = "GCS_Carthage_Degree"
    GCS_CARTHAGE_PARIS = "GCS_Carthage_Paris"
    GCS_CARTHAGE = "GCS_Carthage"
    GCS_CONAKRY_1905 = "GCS_Conakry_1905"
    GCS_COTE_D_IVOIRE = "GCS_Cote_d_Ivoire"
    GCS_DABOLA = "GCS_Dabola"
    GCS_DOUALA = "GCS_Douala"
    GCS_EGYPT_1907 = "GCS_Egypt_1907"
    GCS_EUROPEAN_1950 = "GCS_European_1950"
    GCS_EUROPEAN_LIBYAN_DATUM_1979 = "GCS_European_Libyan_Datum_1979"
    GCS_GAROUA = "GCS_Garoua"
    GCS_HARTEBEESTHOEK_1994 = "GCS_Hartebeesthoek_1994"
    GCS_KUWAIT_OIL_COMPANY = "GCS_Kuwait_Oil_Company"
    GCS_KUDAMS = "GCS_KUDAMS"
    GCS_LEIGON = "GCS_Leigon"
    GCS_LIBERIA_1964 = "GCS_Liberia_1964"
    GCS_LOCODJO_1965 = "GCS_Locodjo_1965"
    GCS_LOME = "GCS_Lome"
    GCS_MPORALOKO = "GCS_Mporaloko"
    GCS_MADZANSUA = "GCS_Madzansua"
    GCS_MAHE_1971 = "GCS_Mahe_1971"
    GCS_MALONGO_1987 = "GCS_Malongo_1987"
    GCS_MANOCA = "GCS_Manoca"
    GCS_MASSAWA = "GCS_Massawa"
    GCS_MERCHICH_DEGREE = "GCS_Merchich_Degree"
    GCS_MERCHICH = "GCS_Merchich"
    GCS_MHAST = "GCS_Mhast"
    GCS_MINNA = "GCS_Minna"
    GCS_MOZNET = "GCS_Moznet"
    GCS_NAHRWAN_1967 = "GCS_Nahrwan_1967"
    GCS_NGN = "GCS_NGN"
    GCS_NORD_SAHARA_1959 = "GCS_Nord_Sahara_1959"
    GCS_OBSERVATARIO = "GCS_Observatario"
    GCS_OMAN = "GCS_Oman"
    GCS_PALESTINE_1923 = "GCS_Palestine_1923"
    GCS_PDO_1993 = "GCS_PDO_1993"
    GCS_POINT_58 = "GCS_Point_58"
    GCS_POINTE_NOIRE = "GCS_Pointe_Noire"
    GCS_QATAR_1948 = "GCS_Qatar_1948"
    GCS_QATAR = "GCS_Qatar"
    GCS_SCHWARZECK = "GCS_Schwarzeck"
    GCS_SIERRA_LEONE_1924 = "GCS_Sierra_Leone_1924"
    GCS_SIERRA_LEONE_1960 = "GCS_Sierra_Leone_1960"
    GCS_SIERRA_LEONE_1968 = "GCS_Sierra_Leone_1968"
    GCS_SOUTH_YEMEN = "GCS_South_Yemen"
    GCS_SUDAN = "GCS_Sudan"
    GCS_TANANARIVE_1925_PARIS = "GCS_Tananarive_1925_Paris"
    GCS_TANANARIVE_1925 = "GCS_Tananarive_1925"
    GCS_TETE = "GCS_Tete"
    GCS_TRUCIAL_COAST_1948 = "GCS_Trucial_Coast_1948"
    GCS_VOIROL_1875_DEGREE = "GCS_Voirol_1875_Degree"
    GCS_VOIROL_1875_PARIS = "GCS_Voirol_1875_Paris"
    GCS_VOIROL_1875 = "GCS_Voirol_1875"
    GCS_VOIROL_UNIFIE_1960_DEGREE = "GCS_Voirol_Unifie_1960_Degree"
    GCS_VOIROL_UNIFIE_1960_PARIS = "GCS_Voirol_Unifie_1960_Paris"
    GCS_VOIROL_UNIFIE_1960 = "GCS_Voirol_Unifie_1960"
    GCS_YEMEN_NGN_1996 = "GCS_Yemen_NGN_1996"
    GCS_YOFF = "GCS_Yoff"
    GCS_CAMP_AREA = "GCS_Camp_Area"
    GCS_DECEPTION_ISLAND = "GCS_Deception_Island"
    GCS_BATAVIA_JAKARTA = "GCS_Batavia_Jakarta"
    GCS_BATAVIA = "GCS_Batavia"
    GCS_BEIJING_1954 = "GCS_Beijing_1954"
    GCS_BUKIT_RIMPAH = "GCS_Bukit_Rimpah"
    GCS_DEIR_EZ_ZOR = "GCS_Deir_ez_Zor"
    GCS_EUROPEAN_1950_ED77 = "GCS_European_1950_ED77"
    GCS_EVEREST_DEF_1962 = "GCS_Everest_def_1962"
    GCS_EVEREST_DEF_1967 = "GCS_Everest_def_1967"
    GCS_EVEREST_DEF_1975 = "GCS_Everest_def_1975"
    GCS_EVEREST_BANGLADESH = "GCS_Everest_Bangladesh"
    GCS_EVEREST_INDIA_NEPAL = "GCS_Everest_India_Nepal"
    GCS_EVEREST_1830 = "GCS_Everest_1830"
    GCS_EVEREST_MODIFIED = "GCS_Everest_Modified"
    GCS_FAHUD = "GCS_Fahud"
    GCS_FD_1958 = "GCS_FD_1958"
    GCS_GANDAJIKA_1970 = "GCS_Gandajika_1970"
    GCS_GUNUNG_SEGARA = "GCS_Gunung_Segara"
    GCS_HANOI_1972 = "GCS_Hanoi_1972"
    GCS_HERAT_NORTH = "GCS_Herat_North"
    GCS_HONG_KONG_1963 = "GCS_Hong_Kong_1963"
    GCS_HONG_KONG_1980 = "GCS_Hong_Kong_1980"
    GCS_HU_TZU_SHAN = "GCS_Hu_Tzu_Shan"
    GCS_INDIAN_1954 = "GCS_Indian_1954"
    GCS_INDIAN_1960 = "GCS_Indian_1960"
    GCS_INDIAN_1975 = "GCS_Indian_1975"
    GCS_INDONESIAN_1974 = "GCS_Indonesian_1974"
    GCS_ISRAEL = "GCS_Israel"
    GCS_JGD_2000 = "GCS_JGD_2000"
    GCS_KALIANPUR_1880 = "GCS_Kalianpur_1880"
    GCS_KALIANPUR_1937 = "GCS_Kalianpur_1937"
    GCS_KALIANPUR_1962 = "GCS_Kalianpur_1962"
    GCS_KALIANPUR_1975 = "GCS_Kalianpur_1975"
    GCS_KANDAWALA = "GCS_Kandawala"
    GCS_KERTAU = "GCS_Kertau"
    GCS_KOREAN_DATUM_1985 = "GCS_Korean_Datum_1985"
    GCS_KOREAN_DATUM_1995 = "GCS_Korean_Datum_1995"
    GCS_LUZON_1911 = "GCS_Luzon_1911"
    GCS_MAKASSAR_JAKARTA = "GCS_Makassar_Jakarta"
    GCS_MAKASSAR = "GCS_Makassar"
    GCS_PADANG_1884_JAKARTA = "GCS_Padang_1884_Jakarta"
    GCS_PADANG_1884 = "GCS_Padang_1884"
    GCS_PULKOVO_1942 = "GCS_Pulkovo_1942"
    GCS_PULKOVO_1995 = "GCS_Pulkovo_1995"
    GCS_RASSADIRAN = "GCS_Rassadiran"
    GCS_SAMBOJA = "GCS_Samboja"
    GCS_SEGORA = "GCS_Segora"
    GCS_SERINDUNG = "GCS_Serindung"
    GCS_SOUTH_ASIA_SINGAPORE = "GCS_South_Asia_Singapore"
    GCS_TIMBALAI_1948 = "GCS_Timbalai_1948"
    GCS_TOKYO = "GCS_Tokyo"
    GCS_AUSTRALIAN_1966 = "GCS_Australian_1966"
    GCS_AUSTRALIAN_1984 = "GCS_Australian_1984"
    GCS_GDA_1994 = "GCS_GDA_1994"
    GCS_NEW_ZEALAND_1949 = "GCS_New_Zealand_1949"
    GCS_NZGD_2000 = "GCS_NZGD_2000"
    GCS_AMERSFOORT = "GCS_Amersfoort"
    GCS_ATF_PARIS = "GCS_ATF_Paris"
    GCS_BELGE_1950_BRUSSELS = "GCS_Belge_1950_Brussels"
    GCS_BELGE_1972 = "GCS_Belge_1972"
    GCS_BERN_1898_BERN = "GCS_Bern_1898_Bern"
    GCS_BERN_1898 = "GCS_Bern_1898"
    GCS_BERN_1938 = "GCS_Bern_1938"
    GCS_CH1903 = "GCS_CH1903+"
    GCS_CH1903_1 = "GCS_CH1903"
    GCS_DATUM_73 = "GCS_Datum_73"
    GCS_DATUM_LISBOA_BESSEL = "GCS_Datum_Lisboa_Bessel"
    GCS_DEALUL_PISCULUI_1933 = "GCS_Dealul_Piscului_1933"
    GCS_DEALUL_PISCULUI_1970 = "GCS_Dealul_Piscului_1970"
    GCS_DEUTSCHE_HAUPTDREIECKSNETZ = "GCS_Deutsche_Hauptdreiecksnetz"
    GCS_ESTONIA_1937 = "GCS_Estonia_1937"
    GCS_ESTONIA_1992 = "GCS_Estonia_1992"
    GCS_ETRF_1989 = "GCS_ETRF_1989"
    GCS_EUROPEAN_1979 = "GCS_European_1979"
    GCS_EUROPEAN_1987 = "GCS_European_1987"
    GCS_GREEK_ATHENS = "GCS_Greek_Athens"
    GCS_GREEK = "GCS_Greek"
    GCS_HERMANNSKOGEL = "GCS_Hermannskogel"
    GCS_HJORSEY_1955 = "GCS_Hjorsey_1955"
    GCS_HUNGARIAN_1972 = "GCS_Hungarian_1972"
    GCS_IRENET95 = "GCS_IRENET95"
    GCS_KKJ = "GCS_KKJ"
    GCS_LISBON_LISBON = "GCS_Lisbon_Lisbon"
    GCS_LISBON = "GCS_Lisbon"
    GCS_LKS_1994 = "GCS_LKS_1994"
    GCS_MADRID_1870_MADRID = "GCS_Madrid_1870_Madrid"
    GCS_MGI_FERRO = "GCS_MGI_Ferro"
    GCS_MGI = "GCS_MGI"
    GCS_MONTE_MARIO_ROME = "GCS_Monte_Mario_Rome"
    GCS_MONTE_MARIO = "GCS_Monte_Mario"
    GCS_NGO_1948_OSLO = "GCS_NGO_1948_Oslo"
    GCS_NGO_1948 = "GCS_NGO_1948"
    GCS_NORD_DE_GUERRE_PARIS = "GCS_Nord_de_Guerre_Paris"
    GCS_NTF = "GCS_NTF"
    GCS_NTF_PARIS = "GCS_NTF_Paris"
    GCS_OS_SN_1980 = "GCS_OS_SN_1980"
    GCS_OSGB_1936 = "GCS_OSGB_1936"
    GCS_OSGB_1970_SN = "GCS_OSGB_1970_SN"
    GCS_QORNOQ = "GCS_Qornoq"
    GCS_BELGE_1950 = "GCS_Belge_1950"
    GCS_RGF_1993 = "GCS_RGF_1993"
    GCS_RT_1990 = "GCS_RT_1990"
    GCS_RT38_STOCKHOLM = "GCS_RT38_Stockholm"
    GCS_RT38 = "GCS_RT38"
    GCS_S42_HUNGARY = "GCS_S42_Hungary"
    GCS_S_JTSK = "GCS_S_JTSK"
    GCS_SWISS_TRF_1995 = "GCS_Swiss_TRF_1995"
    GCS_TM65 = "GCS_TM65"
    GCS_TM75 = "GCS_TM75"
    GCS_ALASKAN_ISLANDS = "GCS_Alaskan_Islands"
    GCS_AMERICAN_SAMOA_1962 = "GCS_American_Samoa_1962"
    GCS_ATS_1977 = "GCS_ATS_1977"
    GCS_BARBADOS = "GCS_Barbados"
    GCS_BERMUDA_1957 = "GCS_Bermuda_1957"
    GCS_CAPE_CANAVERAL = "GCS_Cape_Canaveral"
    GCS_GUAM_1963 = "GCS_Guam_1963"
    GCS_JAMAICA_1875 = "GCS_Jamaica_1875"
    GCS_JAMAICA_1969 = "GCS_Jamaica_1969"
    GCS_NAD_1927_CGQ77 = "GCS_NAD_1927_CGQ77"
    GCS_NAD_1927_DEFINITION_1976 = "GCS_NAD_1927_Definition_1976"
    GCS_NORTH_AMERICAN_MICHIGAN = "GCS_North_American_Michigan"
    GCS_NORTH_AMERICAN_1983_CSRS98 = "GCS_North_American_1983_CSRS98"
    GCS_NORTH_AMERICAN_1983_HARN = "GCS_North_American_1983_HARN"
    GCS_NORTH_AMERICAN_1927 = "GCS_North_American_1927"
    GCS_NORTH_AMERICAN_1983 = "GCS_North_American_1983"
    GCS_OLD_HAWAIIAN = "GCS_Old_Hawaiian"
    GCS_PUERTO_RICO = "GCS_Puerto_Rico"
    GCS_ST_GEORGE_ISLAND = "GCS_St_George_Island"
    GCS_ST_LAWRENCE_ISLAND = "GCS_St_Lawrence_Island"
    GCS_ST_PAUL_ISLAND = "GCS_St_Paul_Island"
    GCS_ANGUILLA_1957 = "GCS_Anguilla_1957"
    GCS_ANNA_1_1965 = "GCS_Anna_1_1965"
    GCS_ANTIGUA_1943 = "GCS_Antigua_1943"
    GCS_ASCENSION_ISLAND_1958 = "GCS_Ascension_Island_1958"
    GCS_BEACON_E_1945 = "GCS_Beacon_E_1945"
    GCS_DOS_71_4 = "GCS_DOS_71_4"
    GCS_ASTRO_1952 = "GCS_Astro_1952"
    GCS_BAB_SOUTH = "GCS_Bab_South"
    GCS_BARBADOS_1938 = "GCS_Barbados_1938"
    GCS_BELLEVUE_IGN = "GCS_Bellevue_IGN"
    GCS_CANTON_1966 = "GCS_Canton_1966"
    GCS_CHATHAM_ISLAND_1971 = "GCS_Chatham_Island_1971"
    GCS_DOMINICA_1945 = "GCS_Dominica_1945"
    GCS_DOS_1968 = "GCS_DOS_1968"
    GCS_EASTER_ISLAND_1967 = "GCS_Easter_Island_1967"
    GCS_FORT_THOMAS_1955 = "GCS_Fort_Thomas_1955"
    GCS_GAN_1970 = "GCS_Gan_1970"
    GCS_GRACIOSA_BASE_SW_1948 = "GCS_Graciosa_Base_SW_1948"
    GCS_GRENADA_1953 = "GCS_Grenada_1953"
    GCS_GUX_1 = "GCS_GUX_1"
    GCS_ISTS_061_1968 = "GCS_ISTS_061_1968"
    GCS_ISTS_073_1969 = "GCS_ISTS_073_1969"
    GCS_JOHNSTON_ISLAND_1961 = "GCS_Johnston_Island_1961"
    GCS_KERGUELEN_ISLAND_1949 = "GCS_Kerguelen_Island_1949"
    GCS_KUSAIE_1951 = "GCS_Kusaie_1951"
    GCS_LC5_1961 = "GCS_LC5_1961"
    GCS_MAJURO = "GCS_Majuro"
    GCS_MIDWAY_1961 = "GCS_Midway_1961"
    GCS_MONTSERRAT_1958 = "GCS_Montserrat_1958"
    GCS_OBSERV_METEOROLOGICO_1939 = "GCS_Observ_Meteorologico_1939"
    GCS_PICO_DE_LAS_NIEVES = "GCS_Pico_de_Las_Nieves"
    GCS_PITCAIRN_1967 = "GCS_Pitcairn_1967"
    GCS_POHNPEI = "GCS_Pohnpei"
    GCS_PORTO_SANTO_1936 = "GCS_Porto_Santo_1936"
    GCS_REUNION = "GCS_Reunion"
    GCS_SANTO_DOS_1965 = "GCS_Santo_DOS_1965"
    GCS_SAO_BRAZ = "GCS_Sao_Braz"
    GCS_SAPPER_HILL_1943 = "GCS_Sapper_Hill_1943"
    GCS_SELVAGEM_GRANDE_1938 = "GCS_Selvagem_Grande_1938"
    GCS_ST_KITTS_1955 = "GCS_St_Kitts_1955"
    GCS_ST_LUCIA_1955 = "GCS_St_Lucia_1955"
    GCS_ST_VINCENT_1945 = "GCS_St_Vincent_1945"
    GCS_TERN_ISLAND_1961 = "GCS_Tern_Island_1961"
    GCS_TRISTAN_1968 = "GCS_Tristan_1968"
    GCS_VITI_LEVU_1916 = "GCS_Viti_Levu_1916"
    GCS_WAKE_ISLAND_1952 = "GCS_Wake_Island_1952"
    GCS_WAKE_ENIWETOK_1960 = "GCS_Wake_Eniwetok_1960"
    GCS_ARATU = "GCS_Aratu"
    GCS_BOGOTA_BOGOTA = "GCS_Bogota_Bogota"
    GCS_BOGOTA = "GCS_Bogota"
    GCS_CAMPO_INCHAUSPE = "GCS_Campo_Inchauspe"
    GCS_CHOS_MALAL_1914 = "GCS_Chos_Malal_1914"
    GCS_CHUA = "GCS_Chua"
    GCS_CORREGO_ALEGRE = "GCS_Corrego_Alegre"
    GCS_GUYANE_FRANCAISE = "GCS_Guyane_Francaise"
    GCS_HITO_XVIII_1963 = "GCS_Hito_XVIII_1963"
    GCS_LA_CANOA = "GCS_La_Canoa"
    GCS_LAKE = "GCS_Lake"
    GCS_LOMA_QUINTANA = "GCS_Loma_Quintana"
    GCS_MOUNT_DILLON = "GCS_Mount_Dillon"
    GCS_NAPARIMA_1955 = "GCS_Naparima_1955"
    GCS_NAPARIMA_1972 = "GCS_Naparima_1972"
    GCS_PAMPA_DEL_CASTILLO = "GCS_Pampa_del_Castillo"
    GCS_POSGAR = "GCS_POSGAR"
    GCS_REGVEN = "GCS_REGVEN"
    GCS_SIRGAS = "GCS_SIRGAS"
    GCS_SOUTH_AMERICAN_1969 = "GCS_South_American_1969"
    GCS_TRINIDAD_1903 = "GCS_Trinidad_1903"
    GCS_YACARE = "GCS_Yacare"
    GCS_ZANDERIJ = "GCS_Zanderij"
    GCS_AIRY_1830 = "GCS_Airy_1830"
    GCS_AIRY_MODIFIED = "GCS_Airy_Modified"
    GCS_AUSTRALIAN = "GCS_Australian"
    GCS_SPHERE_ARC_INFO = "GCS_Sphere_ARC_INFO"
    GCS_SPHERE = "GCS_Sphere"
    GCS_BESSEL_1841 = "GCS_Bessel_1841"
    GCS_BESSEL_MODIFIED = "GCS_Bessel_Modified"
    GCS_BESSEL_NAMIBIA = "GCS_Bessel_Namibia"
    GCS_CLARKE_1858 = "GCS_Clarke_1858"
    GCS_CLARKE_1866_MICHIGAN = "GCS_Clarke_1866_Michigan"
    GCS_CLARKE_1866 = "GCS_Clarke_1866"
    GCS_CLARKE_1880_ARC = "GCS_Clarke_1880_Arc"
    GCS_CLARKE_1880_BENOIT = "GCS_Clarke_1880_Benoit"
    GCS_CLARKE_1880_IGN = "GCS_Clarke_1880_IGN"
    GCS_CLARKE_1880_RGS = "GCS_Clarke_1880_RGS"
    GCS_CLARKE_1880_SGA = "GCS_Clarke_1880_SGA"
    GCS_CLARKE_1880 = "GCS_Clarke_1880"
    GCS_EVEREST_MODIFIED_1969 = "GCS_Everest_Modified_1969"
    GCS_FISCHER_1960 = "GCS_Fischer_1960"
    GCS_FISCHER_1968 = "GCS_Fischer_1968"
    GCS_FISCHER_MODIFIED = "GCS_Fischer_Modified"
    GCS_GEM_10_C = "GCS_GEM_10C"
    GCS_GRS_1967 = "GCS_GRS_1967"
    GCS_GRS_1980 = "GCS_GRS_1980"
    GCS_HELMERT_1906 = "GCS_Helmert_1906"
    GCS_HOUGH_1960 = "GCS_Hough_1960"
    GCS_INDONESIAN = "GCS_Indonesian"
    GCS_INTERNATIONAL_1924 = "GCS_International_1924"
    GCS_INTERNATIONAL_1967 = "GCS_International_1967"
    GCS_KRASOVSKY_1940 = "GCS_Krasovsky_1940"
    GCS_OSU_86_F = "GCS_OSU_86F"
    GCS_OSU_91_A = "GCS_OSU_91A"
    GCS_PLESSIS_1817 = "GCS_Plessis_1817"
    GCS_STRUVE_1860 = "GCS_Struve_1860"
    GCS_NWL_9_D = "GCS_NWL_9D"
    GCS_WALBECK = "GCS_Walbeck"
    GCS_WAR_OFFICE = "GCS_War_Office"
    GCS_WGS_1966 = "GCS_WGS_1966"
    GCS_NSWC_9_Z_2 = "GCS_NSWC_9Z_2"
    GCS_WGS_1972_BE = "GCS_WGS_1972_BE"
    GCS_WGS_1972 = "GCS_WGS_1972"
    GCS_WGS_1984 = "GCS_WGS_1984"
    AFRICA_ALBERS_EQUAL_AREA_CONIC = "Africa_Albers_Equal_Area_Conic"
    AFRICA_EQUIDISTANT_CONIC = "Africa_Equidistant_Conic"
    AFRICA_LAMBERT_CONFORMAL_CONIC = "Africa_Lambert_Conformal_Conic"
    AFRICA_SINUSOIDAL = "Africa_Sinusoidal"
    ASIA_LAMBERT_CONFORMAL_CONIC = "Asia_Lambert_Conformal_Conic"
    ASIA_NORTH_ALBERS_EQUAL_AREA_CONIC = "Asia_North_Albers_Equal_Area_Conic"
    ASIA_NORTH_EQUIDISTANT_CONIC = "Asia_North_Equidistant_Conic"
    ASIA_NORTH_LAMBERT_CONFORMAL_CONIC = "Asia_North_Lambert_Conformal_Conic"
    ASIA_SOUTH_ALBERS_EQUAL_AREA_CONIC = "Asia_South_Albers_Equal_Area_Conic"
    ASIA_SOUTH_EQUIDISTANT_CONIC = "Asia_South_Equidistant_Conic"
    ASIA_SOUTH_LAMBERT_CONFORMAL_CONIC = "Asia_South_Lambert_Conformal_Conic"
    EUROPE_ALBERS_EQUAL_AREA_CONIC = "Europe_Albers_Equal_Area_Conic"
    EUROPE_EQUIDISTANT_CONIC = "Europe_Equidistant_Conic"
    EUROPE_LAMBERT_CONFORMAL_CONIC = "Europe_Lambert_Conformal_Conic"
    ALASKA_ALBERS_EQUAL_AREA_CONIC = "Alaska_Albers_Equal_Area_Conic"
    CANADA_ALBERS_EQUAL_AREA_CONIC = "Canada_Albers_Equal_Area_Conic"
    CANADA_LAMBERT_CONFORMAL_CONIC = "Canada_Lambert_Conformal_Conic"
    HAWAII_ALBERS_EQUAL_AREA_CONIC = "Hawaii_Albers_Equal_Area_Conic"
    NORTH_AMERICA_ALBERS_EQUAL_AREA_CONIC = "North_America_Albers_Equal_Area_Conic"
    NORTH_AMERICA_EQUIDISTANT_CONIC = "North_America_Equidistant_Conic"
    NORTH_AMERICA_LAMBERT_CONFORMAL_CONIC = "North_America_Lambert_Conformal_Conic"
    USA_CONTIGUOUS_ALBERS_EQUAL_AREA_CONIC_USGS_VERSION = "USA_Contiguous_Albers_Equal_Area_Conic_USGS_version"
    USA_CONTIGUOUS_ALBERS_EQUAL_AREA_CONIC = "USA_Contiguous_Albers_Equal_Area_Conic"
    USA_CONTIGUOUS_EQUIDISTANT_CONIC = "USA_Contiguous_Equidistant_Conic"
    USA_CONTIGUOUS_LAMBERT_CONFORMAL_CONIC = "USA_Contiguous_Lambert_Conformal_Conic"
    SOUTH_AMERICA_ALBERS_EQUAL_AREA_CONIC = "South_America_Albers_Equal_Area_Conic"
    SOUTH_AMERICA_EQUIDISTANT_CONIC = "South_America_Equidistant_Conic"
    SOUTH_AMERICA_LAMBERT_CONFORMAL_CONIC = "South_America_Lambert_Conformal_Conic"
    BEIJING_1954_GK_ZONE_13 = "Beijing_1954_GK_Zone_13"
    BEIJING_1954_GK_ZONE_13_N = "Beijing_1954_GK_Zone_13N"
    BEIJING_1954_GK_ZONE_14 = "Beijing_1954_GK_Zone_14"
    BEIJING_1954_GK_ZONE_14_N = "Beijing_1954_GK_Zone_14N"
    BEIJING_1954_GK_ZONE_15 = "Beijing_1954_GK_Zone_15"
    BEIJING_1954_GK_ZONE_15_N = "Beijing_1954_GK_Zone_15N"
    BEIJING_1954_GK_ZONE_16 = "Beijing_1954_GK_Zone_16"
    BEIJING_1954_GK_ZONE_16_N = "Beijing_1954_GK_Zone_16N"
    BEIJING_1954_GK_ZONE_17 = "Beijing_1954_GK_Zone_17"
    BEIJING_1954_GK_ZONE_17_N = "Beijing_1954_GK_Zone_17N"
    BEIJING_1954_GK_ZONE_18 = "Beijing_1954_GK_Zone_18"
    BEIJING_1954_GK_ZONE_18_N = "Beijing_1954_GK_Zone_18N"
    BEIJING_1954_GK_ZONE_19 = "Beijing_1954_GK_Zone_19"
    BEIJING_1954_GK_ZONE_19_N = "Beijing_1954_GK_Zone_19N"
    BEIJING_1954_GK_ZONE_20 = "Beijing_1954_GK_Zone_20"
    BEIJING_1954_GK_ZONE_20_N = "Beijing_1954_GK_Zone_20N"
    BEIJING_1954_GK_ZONE_21 = "Beijing_1954_GK_Zone_21"
    BEIJING_1954_GK_ZONE_21_N = "Beijing_1954_GK_Zone_21N"
    BEIJING_1954_GK_ZONE_22 = "Beijing_1954_GK_Zone_22"
    BEIJING_1954_GK_ZONE_22_N = "Beijing_1954_GK_Zone_22N"
    BEIJING_1954_GK_ZONE_23 = "Beijing_1954_GK_Zone_23"
    BEIJING_1954_GK_ZONE_23_N = "Beijing_1954_GK_Zone_23N"
    HANOI_1972_GK_ZONE_18 = "Hanoi_1972_GK_Zone_18"
    HANOI_1972_GK_ZONE_19 = "Hanoi_1972_GK_Zone_19"
    SOUTH_YEMEN_GK_ZONE_8 = "South_Yemen_GK_Zone_8"
    SOUTH_YEMEN_GK_ZONE_9 = "South_Yemen_GK_Zone_9"
    PULKOVO_1942_GK_ZONE_10 = "Pulkovo_1942_GK_Zone_10"
    PULKOVO_1942_GK_ZONE_10_N = "Pulkovo_1942_GK_Zone_10N"
    PULKOVO_1942_GK_ZONE_11 = "Pulkovo_1942_GK_Zone_11"
    PULKOVO_1942_GK_ZONE_11_N = "Pulkovo_1942_GK_Zone_11N"
    PULKOVO_1942_GK_ZONE_12 = "Pulkovo_1942_GK_Zone_12"
    PULKOVO_1942_GK_ZONE_12_N = "Pulkovo_1942_GK_Zone_12N"
    PULKOVO_1942_GK_ZONE_13 = "Pulkovo_1942_GK_Zone_13"
    PULKOVO_1942_GK_ZONE_13_N = "Pulkovo_1942_GK_Zone_13N"
    PULKOVO_1942_GK_ZONE_14 = "Pulkovo_1942_GK_Zone_14"
    PULKOVO_1942_GK_ZONE_14_N = "Pulkovo_1942_GK_Zone_14N"
    PULKOVO_1942_GK_ZONE_15 = "Pulkovo_1942_GK_Zone_15"
    PULKOVO_1942_GK_ZONE_15_N = "Pulkovo_1942_GK_Zone_15N"
    PULKOVO_1942_GK_ZONE_16 = "Pulkovo_1942_GK_Zone_16"
    PULKOVO_1942_GK_ZONE_16_N = "Pulkovo_1942_GK_Zone_16N"
    PULKOVO_1942_GK_ZONE_17 = "Pulkovo_1942_GK_Zone_17"
    PULKOVO_1942_GK_ZONE_17_N = "Pulkovo_1942_GK_Zone_17N"
    PULKOVO_1942_GK_ZONE_18 = "Pulkovo_1942_GK_Zone_18"
    PULKOVO_1942_GK_ZONE_18_N = "Pulkovo_1942_GK_Zone_18N"
    PULKOVO_1942_GK_ZONE_19 = "Pulkovo_1942_GK_Zone_19"
    PULKOVO_1942_GK_ZONE_19_N = "Pulkovo_1942_GK_Zone_19N"
    PULKOVO_1942_GK_ZONE_2 = "Pulkovo_1942_GK_Zone_2"
    PULKOVO_1942_GK_ZONE_20 = "Pulkovo_1942_GK_Zone_20"
    PULKOVO_1942_GK_ZONE_20_N = "Pulkovo_1942_GK_Zone_20N"
    PULKOVO_1942_GK_ZONE_21 = "Pulkovo_1942_GK_Zone_21"
    PULKOVO_1942_GK_ZONE_21_N = "Pulkovo_1942_GK_Zone_21N"
    PULKOVO_1942_GK_ZONE_22 = "Pulkovo_1942_GK_Zone_22"
    PULKOVO_1942_GK_ZONE_22_N = "Pulkovo_1942_GK_Zone_22N"
    PULKOVO_1942_GK_ZONE_23 = "Pulkovo_1942_GK_Zone_23"
    PULKOVO_1942_GK_ZONE_23_N = "Pulkovo_1942_GK_Zone_23N"
    PULKOVO_1942_GK_ZONE_24 = "Pulkovo_1942_GK_Zone_24"
    PULKOVO_1942_GK_ZONE_24_N = "Pulkovo_1942_GK_Zone_24N"
    PULKOVO_1942_GK_ZONE_25 = "Pulkovo_1942_GK_Zone_25"
    PULKOVO_1942_GK_ZONE_25_N = "Pulkovo_1942_GK_Zone_25N"
    PULKOVO_1942_GK_ZONE_26 = "Pulkovo_1942_GK_Zone_26"
    PULKOVO_1942_GK_ZONE_26_N = "Pulkovo_1942_GK_Zone_26N"
    PULKOVO_1942_GK_ZONE_27 = "Pulkovo_1942_GK_Zone_27"
    PULKOVO_1942_GK_ZONE_27_N = "Pulkovo_1942_GK_Zone_27N"
    PULKOVO_1942_GK_ZONE_28 = "Pulkovo_1942_GK_Zone_28"
    PULKOVO_1942_GK_ZONE_28_N = "Pulkovo_1942_GK_Zone_28N"
    PULKOVO_1942_GK_ZONE_29 = "Pulkovo_1942_GK_Zone_29"
    PULKOVO_1942_GK_ZONE_29_N = "Pulkovo_1942_GK_Zone_29N"
    PULKOVO_1942_GK_ZONE_2_N = "Pulkovo_1942_GK_Zone_2N"
    PULKOVO_1942_GK_ZONE_3 = "Pulkovo_1942_GK_Zone_3"
    PULKOVO_1942_GK_ZONE_30 = "Pulkovo_1942_GK_Zone_30"
    PULKOVO_1942_GK_ZONE_30_N = "Pulkovo_1942_GK_Zone_30N"
    PULKOVO_1942_GK_ZONE_31 = "Pulkovo_1942_GK_Zone_31"
    PULKOVO_1942_GK_ZONE_31_N = "Pulkovo_1942_GK_Zone_31N"
    PULKOVO_1942_GK_ZONE_32 = "Pulkovo_1942_GK_Zone_32"
    PULKOVO_1942_GK_ZONE_32_N = "Pulkovo_1942_GK_Zone_32N"
    PULKOVO_1942_GK_ZONE_3_N = "Pulkovo_1942_GK_Zone_3N"
    PULKOVO_1942_GK_ZONE_4 = "Pulkovo_1942_GK_Zone_4"
    PULKOVO_1942_GK_ZONE_4_N = "Pulkovo_1942_GK_Zone_4N"
    PULKOVO_1942_GK_ZONE_5 = "Pulkovo_1942_GK_Zone_5"
    PULKOVO_1942_GK_ZONE_5_N = "Pulkovo_1942_GK_Zone_5N"
    PULKOVO_1942_GK_ZONE_6 = "Pulkovo_1942_GK_Zone_6"
    PULKOVO_1942_GK_ZONE_6_N = "Pulkovo_1942_GK_Zone_6N"
    PULKOVO_1942_GK_ZONE_7 = "Pulkovo_1942_GK_Zone_7"
    PULKOVO_1942_GK_ZONE_7_N = "Pulkovo_1942_GK_Zone_7N"
    PULKOVO_1942_GK_ZONE_8 = "Pulkovo_1942_GK_Zone_8"
    PULKOVO_1942_GK_ZONE_8_N = "Pulkovo_1942_GK_Zone_8N"
    PULKOVO_1942_GK_ZONE_9 = "Pulkovo_1942_GK_Zone_9"
    PULKOVO_1942_GK_ZONE_9_N = "Pulkovo_1942_GK_Zone_9N"
    PULKOVO_1995_GK_ZONE_10 = "Pulkovo_1995_GK_Zone_10"
    PULKOVO_1995_GK_ZONE_10_N = "Pulkovo_1995_GK_Zone_10N"
    PULKOVO_1995_GK_ZONE_11 = "Pulkovo_1995_GK_Zone_11"
    PULKOVO_1995_GK_ZONE_11_N = "Pulkovo_1995_GK_Zone_11N"
    PULKOVO_1995_GK_ZONE_12 = "Pulkovo_1995_GK_Zone_12"
    PULKOVO_1995_GK_ZONE_12_N = "Pulkovo_1995_GK_Zone_12N"
    PULKOVO_1995_GK_ZONE_13 = "Pulkovo_1995_GK_Zone_13"
    PULKOVO_1995_GK_ZONE_13_N = "Pulkovo_1995_GK_Zone_13N"
    PULKOVO_1995_GK_ZONE_14 = "Pulkovo_1995_GK_Zone_14"
    PULKOVO_1995_GK_ZONE_14_N = "Pulkovo_1995_GK_Zone_14N"
    PULKOVO_1995_GK_ZONE_15 = "Pulkovo_1995_GK_Zone_15"
    PULKOVO_1995_GK_ZONE_15_N = "Pulkovo_1995_GK_Zone_15N"
    PULKOVO_1995_GK_ZONE_16 = "Pulkovo_1995_GK_Zone_16"
    PULKOVO_1995_GK_ZONE_16_N = "Pulkovo_1995_GK_Zone_16N"
    PULKOVO_1995_GK_ZONE_17 = "Pulkovo_1995_GK_Zone_17"
    PULKOVO_1995_GK_ZONE_17_N = "Pulkovo_1995_GK_Zone_17N"
    PULKOVO_1995_GK_ZONE_18 = "Pulkovo_1995_GK_Zone_18"
    PULKOVO_1995_GK_ZONE_18_N = "Pulkovo_1995_GK_Zone_18N"
    PULKOVO_1995_GK_ZONE_19 = "Pulkovo_1995_GK_Zone_19"
    PULKOVO_1995_GK_ZONE_19_N = "Pulkovo_1995_GK_Zone_19N"
    PULKOVO_1995_GK_ZONE_2 = "Pulkovo_1995_GK_Zone_2"
    PULKOVO_1995_GK_ZONE_20 = "Pulkovo_1995_GK_Zone_20"
    PULKOVO_1995_GK_ZONE_20_N = "Pulkovo_1995_GK_Zone_20N"
    PULKOVO_1995_GK_ZONE_21 = "Pulkovo_1995_GK_Zone_21"
    PULKOVO_1995_GK_ZONE_21_N = "Pulkovo_1995_GK_Zone_21N"
    PULKOVO_1995_GK_ZONE_22 = "Pulkovo_1995_GK_Zone_22"
    PULKOVO_1995_GK_ZONE_22_N = "Pulkovo_1995_GK_Zone_22N"
    PULKOVO_1995_GK_ZONE_23 = "Pulkovo_1995_GK_Zone_23"
    PULKOVO_1995_GK_ZONE_23_N = "Pulkovo_1995_GK_Zone_23N"
    PULKOVO_1995_GK_ZONE_24 = "Pulkovo_1995_GK_Zone_24"
    PULKOVO_1995_GK_ZONE_24_N = "Pulkovo_1995_GK_Zone_24N"
    PULKOVO_1995_GK_ZONE_25 = "Pulkovo_1995_GK_Zone_25"
    PULKOVO_1995_GK_ZONE_25_N = "Pulkovo_1995_GK_Zone_25N"
    PULKOVO_1995_GK_ZONE_26 = "Pulkovo_1995_GK_Zone_26"
    PULKOVO_1995_GK_ZONE_26_N = "Pulkovo_1995_GK_Zone_26N"
    PULKOVO_1995_GK_ZONE_27 = "Pulkovo_1995_GK_Zone_27"
    PULKOVO_1995_GK_ZONE_27_N = "Pulkovo_1995_GK_Zone_27N"
    PULKOVO_1995_GK_ZONE_28 = "Pulkovo_1995_GK_Zone_28"
    PULKOVO_1995_GK_ZONE_28_N = "Pulkovo_1995_GK_Zone_28N"
    PULKOVO_1995_GK_ZONE_29 = "Pulkovo_1995_GK_Zone_29"
    PULKOVO_1995_GK_ZONE_29_N = "Pulkovo_1995_GK_Zone_29N"
    PULKOVO_1995_GK_ZONE_2_N = "Pulkovo_1995_GK_Zone_2N"
    PULKOVO_1995_GK_ZONE_3 = "Pulkovo_1995_GK_Zone_3"
    PULKOVO_1995_GK_ZONE_30 = "Pulkovo_1995_GK_Zone_30"
    PULKOVO_1995_GK_ZONE_30_N = "Pulkovo_1995_GK_Zone_30N"
    PULKOVO_1995_GK_ZONE_31 = "Pulkovo_1995_GK_Zone_31"
    PULKOVO_1995_GK_ZONE_31_N = "Pulkovo_1995_GK_Zone_31N"
    PULKOVO_1995_GK_ZONE_32 = "Pulkovo_1995_GK_Zone_32"
    PULKOVO_1995_GK_ZONE_32_N = "Pulkovo_1995_GK_Zone_32N"
    PULKOVO_1995_GK_ZONE_3_N = "Pulkovo_1995_GK_Zone_3N"
    PULKOVO_1995_GK_ZONE_4 = "Pulkovo_1995_GK_Zone_4"
    PULKOVO_1995_GK_ZONE_4_N = "Pulkovo_1995_GK_Zone_4N"
    PULKOVO_1995_GK_ZONE_5 = "Pulkovo_1995_GK_Zone_5"
    PULKOVO_1995_GK_ZONE_5_N = "Pulkovo_1995_GK_Zone_5N"
    PULKOVO_1995_GK_ZONE_6 = "Pulkovo_1995_GK_Zone_6"
    PULKOVO_1995_GK_ZONE_6_N = "Pulkovo_1995_GK_Zone_6N"
    PULKOVO_1995_GK_ZONE_7 = "Pulkovo_1995_GK_Zone_7"
    PULKOVO_1995_GK_ZONE_7_N = "Pulkovo_1995_GK_Zone_7N"
    PULKOVO_1995_GK_ZONE_8 = "Pulkovo_1995_GK_Zone_8"
    PULKOVO_1995_GK_ZONE_8_N = "Pulkovo_1995_GK_Zone_8N"
    PULKOVO_1995_GK_ZONE_9 = "Pulkovo_1995_GK_Zone_9"
    PULKOVO_1995_GK_ZONE_9_N = "Pulkovo_1995_GK_Zone_9N"
    ABIDJAN_1987_TM_5_NW = "Abidjan_1987_TM_5_NW"
    ACCRA_GHANA_GRID = "Accra_Ghana_Grid"
    ACCRA_TM_1_NW = "Accra_TM_1_NW"
    SAMOA_1962_SAMOA_LAMBERT = "Samoa_1962_Samoa_Lambert"
    ANGUILLA_1957_BRITISH_WEST_INDIES_GRID = "Anguilla_1957_British_West_Indies_Grid"
    ANTIGUA_1943_BRITISH_WEST_INDIES_GRID = "Antigua_1943_British_West_Indies_Grid"
    ARGENTINA_ZONE_1 = "Argentina_Zone_1"
    ARGENTINA_ZONE_2 = "Argentina_Zone_2"
    ARGENTINA_ZONE_3 = "Argentina_Zone_3"
    ARGENTINA_ZONE_4 = "Argentina_Zone_4"
    ARGENTINA_ZONE_5 = "Argentina_Zone_5"
    ARGENTINA_ZONE_6 = "Argentina_Zone_6"
    ARGENTINA_ZONE_7 = "Argentina_Zone_7"
    AGD_1966_AMG_ZONE_48 = "AGD_1966_AMG_Zone_48"
    AGD_1966_AMG_ZONE_49 = "AGD_1966_AMG_Zone_49"
    AGD_1966_AMG_ZONE_50 = "AGD_1966_AMG_Zone_50"
    AGD_1966_AMG_ZONE_51 = "AGD_1966_AMG_Zone_51"
    AGD_1966_AMG_ZONE_52 = "AGD_1966_AMG_Zone_52"
    AGD_1966_AMG_ZONE_53 = "AGD_1966_AMG_Zone_53"
    AGD_1966_AMG_ZONE_54 = "AGD_1966_AMG_Zone_54"
    AGD_1966_AMG_ZONE_55 = "AGD_1966_AMG_Zone_55"
    AGD_1966_AMG_ZONE_56 = "AGD_1966_AMG_Zone_56"
    AGD_1966_AMG_ZONE_57 = "AGD_1966_AMG_Zone_57"
    AGD_1966_AMG_ZONE_58 = "AGD_1966_AMG_Zone_58"
    AGD_1966_VICGRID = "AGD_1966_VICGRID"
    AGD_1984_AMG_ZONE_48 = "AGD_1984_AMG_Zone_48"
    AGD_1984_AMG_ZONE_49 = "AGD_1984_AMG_Zone_49"
    AGD_1984_AMG_ZONE_50 = "AGD_1984_AMG_Zone_50"
    AGD_1984_AMG_ZONE_51 = "AGD_1984_AMG_Zone_51"
    AGD_1984_AMG_ZONE_52 = "AGD_1984_AMG_Zone_52"
    AGD_1984_AMG_ZONE_53 = "AGD_1984_AMG_Zone_53"
    AGD_1984_AMG_ZONE_54 = "AGD_1984_AMG_Zone_54"
    AGD_1984_AMG_ZONE_55 = "AGD_1984_AMG_Zone_55"
    AGD_1984_AMG_ZONE_56 = "AGD_1984_AMG_Zone_56"
    AGD_1984_AMG_ZONE_57 = "AGD_1984_AMG_Zone_57"
    AGD_1984_AMG_ZONE_58 = "AGD_1984_AMG_Zone_58"
    GDA_1994_MGA_ZONE_48 = "GDA_1994_MGA_Zone_48"
    GDA_1994_MGA_ZONE_49 = "GDA_1994_MGA_Zone_49"
    GDA_1994_MGA_ZONE_50 = "GDA_1994_MGA_Zone_50"
    GDA_1994_MGA_ZONE_51 = "GDA_1994_MGA_Zone_51"
    GDA_1994_MGA_ZONE_52 = "GDA_1994_MGA_Zone_52"
    GDA_1994_MGA_ZONE_53 = "GDA_1994_MGA_Zone_53"
    GDA_1994_MGA_ZONE_54 = "GDA_1994_MGA_Zone_54"
    GDA_1994_MGA_ZONE_55 = "GDA_1994_MGA_Zone_55"
    GDA_1994_MGA_ZONE_56 = "GDA_1994_MGA_Zone_56"
    GDA_1994_MGA_ZONE_57 = "GDA_1994_MGA_Zone_57"
    GDA_1994_MGA_ZONE_58 = "GDA_1994_MGA_Zone_58"
    GDA_1994_SOUTH_AUSTRALIA_LAMBERT = "GDA_1994_South_Australia_Lambert"
    GDA_1994_VICGRID94 = "GDA_1994_VICGRID94"
    AUSTRIA_CENTRAL_ZONE = "Austria_Central_Zone"
    AUSTRIA_EAST_ZONE = "Austria_East_Zone"
    AUSTRIA_WEST_ZONE = "Austria_West_Zone"
    BAHRAIN_STATE_GRID = "Bahrain_State_Grid"
    BARBADOS_1938_BARBADOS_GRID = "Barbados_1938_Barbados_Grid"
    BARBADOS_1938_BRITISH_WEST_INDIES_GRID = "Barbados_1938_British_West_Indies_Grid"
    BELGE_LAMBERT_1950 = "Belge_Lambert_1950"
    BELGE_LAMBERT_1972 = "Belge_Lambert_1972"
    BERN_1898_BERN_LV03_C = "Bern_1898_Bern_LV03C"
    BRITISH_NATIONAL_GRID = "British_National_Grid"
    CAMACUPA_TM_11_30_SE = "Camacupa_TM_11_30_SE"
    CAMACUPA_TM_12_SE = "Camacupa_TM_12_SE"
    ATS_1977_MTM_4_NOVA_SCOTIA = "ATS_1977_MTM_4_Nova_Scotia"
    ATS_1977_MTM_5_NOVA_SCOTIA = "ATS_1977_MTM_5_Nova_Scotia"
    ATS_1977_NEW_BRUNSWICK_STEREOGRAPHIC = "ATS_1977_New_Brunswick_Stereographic"
    NAD_1927_10_TM_AEP_FOREST = "NAD_1927_10TM_AEP_Forest"
    NAD_1927_10_TM_AEP_RESOURCE = "NAD_1927_10TM_AEP_Resource"
    NAD_1927_3_TM_111 = "NAD_1927_3TM_111"
    NAD_1927_3_TM_114 = "NAD_1927_3TM_114"
    NAD_1927_3_TM_117 = "NAD_1927_3TM_117"
    NAD_1927_3_TM_120 = "NAD_1927_3TM_120"
    NAD_1927_CGQ77_MTM_10_SCO_PQ = "NAD_1927_CGQ77_MTM_10_SCoPQ"
    NAD_1927_CGQ77_MTM_2_SCO_PQ = "NAD_1927_CGQ77_MTM_2_SCoPQ"
    NAD_1927_CGQ77_MTM_3_SCO_PQ = "NAD_1927_CGQ77_MTM_3_SCoPQ"
    NAD_1927_CGQ77_MTM_4_SCO_PQ = "NAD_1927_CGQ77_MTM_4_SCoPQ"
    NAD_1927_CGQ77_MTM_5_SCO_PQ = "NAD_1927_CGQ77_MTM_5_SCoPQ"
    NAD_1927_CGQ77_MTM_6_SCO_PQ = "NAD_1927_CGQ77_MTM_6_SCoPQ"
    NAD_1927_CGQ77_MTM_7_SCO_PQ = "NAD_1927_CGQ77_MTM_7_SCoPQ"
    NAD_1927_CGQ77_MTM_8_SCO_PQ = "NAD_1927_CGQ77_MTM_8_SCoPQ"
    NAD_1927_CGQ77_MTM_9_SCO_PQ = "NAD_1927_CGQ77_MTM_9_SCoPQ"
    NAD_1927_CGQ77_QUEBEC_LAMBERT = "NAD_1927_CGQ77_Quebec_Lambert"
    NAD_1927_CGQ77_UTM_ZONE_17_N = "NAD_1927_CGQ77_UTM_Zone_17N"
    NAD_1927_CGQ77_UTM_ZONE_18_N = "NAD_1927_CGQ77_UTM_Zone_18N"
    NAD_1927_CGQ77_UTM_ZONE_19_N = "NAD_1927_CGQ77_UTM_Zone_19N"
    NAD_1927_CGQ77_UTM_ZONE_20_N = "NAD_1927_CGQ77_UTM_Zone_20N"
    NAD_1927_CGQ77_UTM_ZONE_21_N = "NAD_1927_CGQ77_UTM_Zone_21N"
    NAD_1927_DEF_1976_MTM_10 = "NAD_1927_DEF_1976_MTM_10"
    NAD_1927_DEF_1976_MTM_11 = "NAD_1927_DEF_1976_MTM_11"
    NAD_1927_DEF_1976_MTM_12 = "NAD_1927_DEF_1976_MTM_12"
    NAD_1927_DEF_1976_MTM_13 = "NAD_1927_DEF_1976_MTM_13"
    NAD_1927_DEF_1976_MTM_14 = "NAD_1927_DEF_1976_MTM_14"
    NAD_1927_DEF_1976_MTM_15 = "NAD_1927_DEF_1976_MTM_15"
    NAD_1927_DEF_1976_MTM_16 = "NAD_1927_DEF_1976_MTM_16"
    NAD_1927_DEF_1976_MTM_17 = "NAD_1927_DEF_1976_MTM_17"
    NAD_1927_DEF_1976_MTM_8 = "NAD_1927_DEF_1976_MTM_8"
    NAD_1927_DEF_1976_MTM_9 = "NAD_1927_DEF_1976_MTM_9"
    NAD_1927_DEF_1976_UTM_ZONE_15_N = "NAD_1927_DEF_1976_UTM_Zone_15N"
    NAD_1927_DEF_1976_UTM_ZONE_16_N = "NAD_1927_DEF_1976_UTM_Zone_16N"
    NAD_1927_DEF_1976_UTM_ZONE_17_N = "NAD_1927_DEF_1976_UTM_Zone_17N"
    NAD_1927_DEF_1976_UTM_ZONE_18_N = "NAD_1927_DEF_1976_UTM_Zone_18N"
    NAD_1927_MTM_1 = "NAD_1927_MTM_1"
    NAD_1927_MTM_2 = "NAD_1927_MTM_2"
    NAD_1927_MTM_3 = "NAD_1927_MTM_3"
    NAD_1927_MTM_4 = "NAD_1927_MTM_4"
    NAD_1927_MTM_5 = "NAD_1927_MTM_5"
    NAD_1927_MTM_6 = "NAD_1927_MTM_6"
    NAD_1927_QUEBEC_LAMBERT = "NAD_1927_Quebec_Lambert"
    NAD_1983_10_TM_AEP_FOREST = "NAD_1983_10TM_AEP_Forest"
    NAD_1983_10_TM_AEP_RESOURCE = "NAD_1983_10TM_AEP_Resource"
    NAD_1983_3_TM_111 = "NAD_1983_3TM_111"
    NAD_1983_3_TM_114 = "NAD_1983_3TM_114"
    NAD_1983_3_TM_117 = "NAD_1983_3TM_117"
    NAD_1983_3_TM_120 = "NAD_1983_3TM_120"
    NAD_1983_BC_ENVIRONMENT_ALBERS = "NAD_1983_BC_Environment_Albers"
    NAD_1983_CRS98_MTM_10 = "NAD_1983_CRS98_MTM_10"
    NAD_1983_CSRS98_MTM_2_SCO_PQ = "NAD_1983_CSRS98_MTM_2_SCoPQ"
    NAD_1983_CRS98_MTM_3 = "NAD_1983_CRS98_MTM_3"
    NAD_1983_CRS98_MTM_4 = "NAD_1983_CRS98_MTM_4"
    NAD_1983_CRS98_MTM_5 = "NAD_1983_CRS98_MTM_5"
    NAD_1983_CRS98_MTM_6 = "NAD_1983_CRS98_MTM_6"
    NAD_1983_CRS98_MTM_7 = "NAD_1983_CRS98_MTM_7"
    NAD_1983_CRS98_MTM_8 = "NAD_1983_CRS98_MTM_8"
    NAD_1983_CRS98_MTM_9 = "NAD_1983_CRS98_MTM_9"
    NAD_1983_CSRS98_NEW_BRUNSWICK_STEREOGRAPHIC = "NAD_1983_CSRS98_New_Brunswick_Stereographic"
    NAD_1983_CSRS98_PRINCE_EDWARD_ISLAND = "NAD_1983_CSRS98_Prince_Edward_Island"
    NAD_1983_CSRS98_UTM_ZONE_21_N = "NAD_1983_CSRS98_UTM_Zone_21N"
    NAD_1983_CSRS98_UTM_ZONE_11_N = "NAD_1983_CSRS98_UTM_Zone_11N"
    NAD_1983_CSRS98_UTM_ZONE_12_N = "NAD_1983_CSRS98_UTM_Zone_12N"
    NAD_1983_CSRS98_UTM_ZONE_13_N = "NAD_1983_CSRS98_UTM_Zone_13N"
    NAD_1983_CSRS98_UTM_ZONE_17_N = "NAD_1983_CSRS98_UTM_Zone_17N"
    NAD_1983_CSRS98_UTM_ZONE_18_N = "NAD_1983_CSRS98_UTM_Zone_18N"
    NAD_1983_CSRS98_UTM_ZONE_19_N = "NAD_1983_CSRS98_UTM_Zone_19N"
    NAD_1983_CSRS98_UTM_ZONE_20_N = "NAD_1983_CSRS98_UTM_Zone_20N"
    NAD_1983_MTM_1 = "NAD_1983_MTM_1"
    NAD_1983_MTM_10 = "NAD_1983_MTM_10"
    NAD_1983_MTM_11 = "NAD_1983_MTM_11"
    NAD_1983_MTM_12 = "NAD_1983_MTM_12"
    NAD_1983_MTM_13 = "NAD_1983_MTM_13"
    NAD_1983_MTM_14 = "NAD_1983_MTM_14"
    NAD_1983_MTM_15 = "NAD_1983_MTM_15"
    NAD_1983_MTM_16 = "NAD_1983_MTM_16"
    NAD_1983_MTM_17 = "NAD_1983_MTM_17"
    NAD_1983_MTM_2_SCO_PQ = "NAD_1983_MTM_2_SCoPQ"
    NAD_1983_MTM_2 = "NAD_1983_MTM_2"
    NAD_1983_MTM_3 = "NAD_1983_MTM_3"
    NAD_1983_MTM_4 = "NAD_1983_MTM_4"
    NAD_1983_MTM_5 = "NAD_1983_MTM_5"
    NAD_1983_MTM_6 = "NAD_1983_MTM_6"
    NAD_1983_MTM_7 = "NAD_1983_MTM_7"
    NAD_1983_MTM_8 = "NAD_1983_MTM_8"
    NAD_1983_MTM_9 = "NAD_1983_MTM_9"
    NAD_1983_QUEBEC_LAMBERT = "NAD_1983_Quebec_Lambert"
    PRINCE_EDWARD_ISLAND_STEREOGRAPHIC = "Prince_Edward_Island_Stereographic"
    CARTHAGE_TM_11_NE = "Carthage_TM_11_NE"
    CENTRE_FRANCE = "Centre_France"
    CH1903_LV03 = "CH1903_LV03"
    CH1903_LV95 = "CH1903+_LV95"
    CHOS_MALAL_1914_ARGENTINA_2 = "Chos_Malal_1914_Argentina_2"
    COLOMBIA_BOGOTA_ZONE = "Colombia_Bogota_Zone"
    COLOMBIA_EAST_CENTRAL_ZONE = "Colombia_East_Central_Zone"
    COLOMBIA_EAST_ZONE = "Colombia_East_Zone"
    COLOMBIA_WEST_ZONE = "Colombia_West_Zone"
    CORSE = "Corse"
    DATUM_73_HAYFORD_GAUSS_IGEO_E = "Datum_73_Hayford_Gauss_IGeoE"
    DATUM_73_HAYFORD_GAUSS_IPCC = "Datum_73_Hayford_Gauss_IPCC"
    DEIR_EZ_ZOR_LEVANT_STEREOGRAPHIC = "Deir_ez_Zor_Levant_Stereographic"
    DEIR_EZ_ZOR_LEVANT_ZONE = "Deir_ez_Zor_Levant_Zone"
    DEIR_EZ_ZOR_SYRIA_LAMBERT = "Deir_ez_Zor_Syria_Lambert"
    DHDN_3_DEGREE_GAUSS_ZONE_1 = "DHDN_3_Degree_Gauss_Zone_1"
    DHDN_3_DEGREE_GAUSS_ZONE_2 = "DHDN_3_Degree_Gauss_Zone_2"
    DHDN_3_DEGREE_GAUSS_ZONE_3 = "DHDN_3_Degree_Gauss_Zone_3"
    DHDN_3_DEGREE_GAUSS_ZONE_4 = "DHDN_3_Degree_Gauss_Zone_4"
    DHDN_3_DEGREE_GAUSS_ZONE_5 = "DHDN_3_Degree_Gauss_Zone_5"
    DOMINICA_1945_BRITISH_WEST_INDIES_GRID = "Dominica_1945_British_West_Indies_Grid"
    ED_1950_TM_0_N = "ED_1950_TM_0_N"
    ED_1950_TM_5_NE = "ED_1950_TM_5_NE"
    EGYPT_BLUE_BELT = "Egypt_Blue_Belt"
    EGYPT_EXTENDED_PURPLE_BELT = "Egypt_Extended_Purple_Belt"
    EGYPT_PURPLE_BELT = "Egypt_Purple_Belt"
    EGYPT_RED_BELT = "Egypt_Red_Belt"
    ELD_1979_LIBYA_10 = "ELD_1979_Libya_10"
    ELD_1979_LIBYA_11 = "ELD_1979_Libya_11"
    ELD_1979_LIBYA_12 = "ELD_1979_Libya_12"
    ELD_1979_LIBYA_13 = "ELD_1979_Libya_13"
    ELD_1979_LIBYA_5 = "ELD_1979_Libya_5"
    ELD_1979_LIBYA_6 = "ELD_1979_Libya_6"
    ELD_1979_LIBYA_7 = "ELD_1979_Libya_7"
    ELD_1979_LIBYA_8 = "ELD_1979_Libya_8"
    ELD_1979_LIBYA_9 = "ELD_1979_Libya_9"
    ELD_1979_TM_12_NE = "ELD_1979_TM_12_NE"
    ESTONIAN_COORDINATE_SYSTEM_OF_1992 = "Estonian_Coordinate_System_of_1992"
    ETRF_1989_TM_BALTIC_1993 = "ETRF_1989_TM_Baltic_1993"
    FD_1958_IRAQ = "FD_1958_Iraq"
    FINLAND_ZONE_1 = "Finland_Zone_1"
    FINLAND_ZONE_2 = "Finland_Zone_2"
    FINLAND_ZONE_3 = "Finland_Zone_3"
    FINLAND_ZONE_4 = "Finland_Zone_4"
    FRANCE_I = "France_I"
    FRANCE_II = "France_II"
    FRANCE_III = "France_III"
    FRANCE_IV = "France_IV"
    GERMANY_ZONE_1 = "Germany_Zone_1"
    GERMANY_ZONE_2 = "Germany_Zone_2"
    GERMANY_ZONE_3 = "Germany_Zone_3"
    GERMANY_ZONE_4 = "Germany_Zone_4"
    GERMANY_ZONE_5 = "Germany_Zone_5"
    GHANA_METRE_GRID = "Ghana_Metre_Grid"
    GREEK_GRID = "Greek_Grid"
    GRENADA_1953_BRITISH_WEST_INDIES_GRID = "Grenada_1953_British_West_Indies_Grid"
    HANOI_1972_GK_106_NE = "Hanoi_1972_GK_106_NE"
    HD_1972_EGYSEGES_ORSZAGOS_VETULETI = "HD_1972_Egyseges_Orszagos_Vetuleti"
    HITO_XVIII_1963_ARGENTINA_2 = "Hito_XVIII_1963_Argentina_2"
    HONG_KONG_1980_GRID = "Hong_Kong_1980_Grid"
    INDIAN_1960_TM_106_NE = "Indian_1960_TM_106NE"
    KALIANPUR_1880_INDIA_ZONE_0 = "Kalianpur_1880_India_Zone_0"
    KALIANPUR_1880_INDIA_ZONE_I = "Kalianpur_1880_India_Zone_I"
    KALIANPUR_1880_INDIA_ZONE_IIA = "Kalianpur_1880_India_Zone_IIa"
    KALIANPUR_1880_INDIA_ZONE_IIB = "Kalianpur_1880_India_Zone_IIb"
    KALIANPUR_1880_INDIA_ZONE_III = "Kalianpur_1880_India_Zone_III"
    KALIANPUR_1880_INDIA_ZONE_IV = "Kalianpur_1880_India_Zone_IV"
    KALIANPUR_1937_INDIA_ZONE_IIB = "Kalianpur_1937_India_Zone_IIb"
    KALIANPUR_1937_UTM_ZONE_45_N = "Kalianpur_1937_UTM_Zone_45N"
    KALIANPUR_1937_UTM_ZONE_46_N = "Kalianpur_1937_UTM_Zone_46N"
    KALIANPUR_1962_INDIA_ZONE_I = "Kalianpur_1962_India_Zone_I"
    KALIANPUR_1962_INDIA_ZONE_IIA = "Kalianpur_1962_India_Zone_IIa"
    KALIANPUR_1962_UTM_ZONE_41_N = "Kalianpur_1962_UTM_Zone_41N"
    KALIANPUR_1962_UTM_ZONE_42_N = "Kalianpur_1962_UTM_Zone_42N"
    KALIANPUR_1962_UTM_ZONE_43_N = "Kalianpur_1962_UTM_Zone_43N"
    KALIANPUR_1975_INDIA_ZONE_I = "Kalianpur_1975_India_Zone_I"
    KALIANPUR_1975_INDIA_ZONE_IIA = "Kalianpur_1975_India_Zone_IIa"
    KALIANPUR_1975_INDIA_ZONE_IIB = "Kalianpur_1975_India_Zone_IIb"
    KALIANPUR_1975_INDIA_ZONE_III = "Kalianpur_1975_India_Zone_III"
    KALIANPUR_1975_INDIA_ZONE_IV = "Kalianpur_1975_India_Zone_IV"
    KALIANPUR_1975_UTM_ZONE_42_N = "Kalianpur_1975_UTM_Zone_42N"
    KALIANPUR_1975_UTM_ZONE_43_N = "Kalianpur_1975_UTM_Zone_43N"
    KALIANPUR_1975_UTM_ZONE_44_N = "Kalianpur_1975_UTM_Zone_44N"
    KALIANPUR_1975_UTM_ZONE_45_N = "Kalianpur_1975_UTM_Zone_45N"
    KALIANPUR_1975_UTM_ZONE_46_N = "Kalianpur_1975_UTM_Zone_46N"
    KALIANPUR_1975_UTM_ZONE_47_N = "Kalianpur_1975_UTM_Zone_47N"
    IRENET95_IRISH_TRANSVERSE_MERCATOR = "IRENET95_IRISH_Transverse_Mercator"
    IRISH_NATIONAL_GRID = "Irish_National_Grid"
    ISRAEL_TM_GRID = "Israel_TM_Grid"
    JAMAICA_1875_OLD_GRID = "Jamaica_1875_Old_Grid"
    JAMAICA_GRID = "Jamaica_Grid"
    JAPAN_ZONE_1 = "Japan_Zone_1"
    JAPAN_ZONE_10 = "Japan_Zone_10"
    JAPAN_ZONE_11 = "Japan_Zone_11"
    JAPAN_ZONE_12 = "Japan_Zone_12"
    JAPAN_ZONE_13 = "Japan_Zone_13"
    JAPAN_ZONE_14 = "Japan_Zone_14"
    JAPAN_ZONE_15 = "Japan_Zone_15"
    JAPAN_ZONE_16 = "Japan_Zone_16"
    JAPAN_ZONE_17 = "Japan_Zone_17"
    JAPAN_ZONE_18 = "Japan_Zone_18"
    JAPAN_ZONE_19 = "Japan_Zone_19"
    JAPAN_ZONE_2 = "Japan_Zone_2"
    JAPAN_ZONE_3 = "Japan_Zone_3"
    JAPAN_ZONE_4 = "Japan_Zone_4"
    JAPAN_ZONE_5 = "Japan_Zone_5"
    JAPAN_ZONE_6 = "Japan_Zone_6"
    JAPAN_ZONE_7 = "Japan_Zone_7"
    JAPAN_ZONE_8 = "Japan_Zone_8"
    JAPAN_ZONE_9 = "Japan_Zone_9"
    KERTAU_SINGAPORE_GRID = "Kertau_Singapore_Grid"
    KOC_LAMBERT = "KOC_Lambert"
    KOREAN_1985_KOREA_CENTRAL_BELT = "Korean_1985_Korea_Central_Belt"
    KOREAN_1985_KOREA_EAST_BELT = "Korean_1985_Korea_East_Belt"
    KOREAN_1985_KOREA_WEST_BELT = "Korean_1985_Korea_West_Belt"
    KUDAMS_KTM = "KUDAMS_KTM"
    LAKE_MARACAIBO_GRID_M1 = "Lake_Maracaibo_Grid_M1"
    LAKE_MARACAIBO_GRID_M3 = "Lake_Maracaibo_Grid_M3"
    LAKE_MARACAIBO_GRID = "Lake_Maracaibo_Grid"
    LAKE_MARACAIBO_LA_ROSA_GRID = "Lake_Maracaibo_La_Rosa_Grid"
    LIETUVOS_KOORDINACIU_SISTEMA = "Lietuvos_Koordinaciu_Sistema"
    LISBOA_BESSEL_BONNE = "Lisboa_Bessel_Bonne"
    LISBOA_HAYFORD_GAUSS_IGEO_E = "Lisboa_Hayford_Gauss_IGeoE"
    LISBOA_HAYFORD_GAUSS_IPCC = "Lisboa_Hayford_Gauss_IPCC"
    LOCODJO_1965_TM_5_NW = "Locodjo_1965_TM_5_NW"
    MADRID_1870_MADRID_SPAIN = "Madrid_1870_Madrid_Spain"
    MGI_3_DEGREE_GAUSS_ZONE_5 = "MGI_3_Degree_Gauss_Zone_5"
    MGI_3_DEGREE_GAUSS_ZONE_6 = "MGI_3_Degree_Gauss_Zone_6"
    MGI_3_DEGREE_GAUSS_ZONE_7 = "MGI_3_Degree_Gauss_Zone_7"
    MGI_3_DEGREE_GAUSS_ZONE_8 = "MGI_3_Degree_Gauss_Zone_8"
    MGI_AUSTRIA_LAMBERT = "MGI_Austria_Lambert"
    MGI_BALKANS_5 = "MGI_Balkans_5"
    MGI_BALKANS_6 = "MGI_Balkans_6"
    MGI_BALKANS_8 = "MGI_Balkans_8"
    MGI_M28 = "MGI_M28"
    MGI_M31 = "MGI_M31"
    MGI_M34 = "MGI_M34"
    MONTE_MARIO_ROME_ITALY_1 = "Monte_Mario_Rome_Italy_1"
    MONTE_MARIO_ROME_ITALY_2 = "Monte_Mario_Rome_Italy_2"
    MONTE_MARIO_ITALY_1 = "Monte_Mario_Italy_1"
    MONTE_MARIO_ITALY_2 = "Monte_Mario_Italy_2"
    MONTSERRAT_1958_BRITISH_WEST_INDIES_GRID = "Montserrat_1958_British_West_Indies_Grid"
    MOUNT_DILLON_TOBAGO_GRID = "Mount_Dillon_Tobago_Grid"
    NAD_1927_CUBA_NORTE = "NAD_1927_Cuba_Norte"
    NAD_1927_CUBA_SUR = "NAD_1927_Cuba_Sur"
    NAD_1927_GUATEMALA_NORTE = "NAD_1927_Guatemala_Norte"
    NAD_1927_GUATEMALA_SUR = "NAD_1927_Guatemala_Sur"
    NAD_1927_MICHIGAN_GEO_REF_METERS = "NAD_1927_Michigan_GeoRef_Meters"
    NAD_1927_MICHIGAN_GEO_REF_FEET_US = "NAD_1927_Michigan_GeoRef_Feet_US"
    NAD_1983_HARN_GUAM_MAP_GRID = "NAD_1983_HARN_Guam_Map_Grid"
    NAD_1983_MICHIGAN_GEO_REF_METERS = "NAD_1983_Michigan_GeoRef_Meters"
    NAD_1983_MICHIGAN_GEO_REF_FEET_US = "NAD_1983_Michigan_GeoRef_Feet_US"
    GD_1949_NEW_ZEALAND_MAP_GRID = "GD_1949_New_Zealand_Map_Grid"
    NEW_ZEALAND_NORTH_ISLAND = "New_Zealand_North_Island"
    NEW_ZEALAND_SOUTH_ISLAND = "New_Zealand_South_Island"
    NZGD_1949_AMURI_CIRCUIT = "NZGD_1949_Amuri_Circuit"
    NZGD_1949_BAY_OF_PLENTY_CIRCUIT = "NZGD_1949_Bay_of_Plenty_Circuit"
    NZGD_1949_BLUFF_CIRCUIT = "NZGD_1949_Bluff_Circuit"
    NZGD_1949_BULLER_CIRCUIT = "NZGD_1949_Buller_Circuit"
    NZGD_1949_COLLINGWOOD_CIRCUIT = "NZGD_1949_Collingwood_Circuit"
    NZGD_1949_GAWLER_CIRCUIT = "NZGD_1949_Gawler_Circuit"
    NZGD_1949_GREY_CIRCUIT = "NZGD_1949_Grey_Circuit"
    NZGD_1949_HAWKES_BAY_CIRCUIT = "NZGD_1949_Hawkes_Bay_Circuit"
    NZGD_1949_HOKITIKA_CIRCUIT = "NZGD_1949_Hokitika_Circuit"
    NZGD_1949_JACKSONS_BAY_CIRCUIT = "NZGD_1949_Jacksons_Bay_Circuit"
    NZGD_1949_KARAMEA_CIRCUIT = "NZGD_1949_Karamea_Circuit"
    NZGD_1949_LINDIS_PEAK_CIRCUIT = "NZGD_1949_Lindis_Peak_Circuit"
    NZGD_1949_MARLBOROUGH_CIRCUIT = "NZGD_1949_Marlborough_Circuit"
    NZGD_1949_MOUNT_EDEN_CIRCUIT = "NZGD_1949_Mount_Eden_Circuit"
    NZGD_1949_MOUNT_NICHOLAS_CIRCUIT = "NZGD_1949_Mount_Nicholas_Circuit"
    NZGD_1949_MOUNT_PLEASANT_CIRCUIT = "NZGD_1949_Mount_Pleasant_Circuit"
    NZGD_1949_MOUNT_YORK_CIRCUIT = "NZGD_1949_Mount_York_Circuit"
    NZGD_1949_NELSON_CIRCUIT = "NZGD_1949_Nelson_Circuit"
    NZGD_1949_NORTH_TAIERI_CIRCUIT = "NZGD_1949_North_Taieri_Circuit"
    NZGD_1949_OBSERVATION_POINT_CIRCUIT = "NZGD_1949_Observation_Point_Circuit"
    NZGD_1949_OKARITO_CIRCUIT = "NZGD_1949_Okarito_Circuit"
    NZGD_1949_POVERTY_BAY_CIRCUIT = "NZGD_1949_Poverty_Bay_Circuit"
    NZGD_1949_TARANAKI_CIRCUIT = "NZGD_1949_Taranaki_Circuit"
    NZGD_1949_TIMARU_CIRCUIT = "NZGD_1949_Timaru_Circuit"
    NZGD_1949_TUHIRANGI_CIRCUIT = "NZGD_1949_Tuhirangi_Circuit"
    NZGD_1949_UTM_ZONE_58_S = "NZGD_1949_UTM_Zone_58S"
    NZGD_1949_UTM_ZONE_59_S = "NZGD_1949_UTM_Zone_59S"
    NZGD_1949_UTM_ZONE_60_S = "NZGD_1949_UTM_Zone_60S"
    NZGD_1949_WAIRARAPA_CIRCUIT = "NZGD_1949_Wairarapa_Circuit"
    NZGD_1949_WANGANUI_CIRCUIT = "NZGD_1949_Wanganui_Circuit"
    NZGD_1949_WELLINGTON_CIRCUIT = "NZGD_1949_Wellington_Circuit"
    NZGD_2000_AMURI_CIRCUIT = "NZGD_2000_Amuri_Circuit"
    NZGD_2000_BAY_OF_PLENTY_CIRCUIT = "NZGD_2000_Bay_of_Plenty_Circuit"
    NZGD_2000_BLUFF_CIRCUIT = "NZGD_2000_Bluff_Circuit"
    NZGD_2000_BULLER_CIRCUIT = "NZGD_2000_Buller_Circuit"
    NZGD_2000_COLLINGWOOD_CIRCUIT = "NZGD_2000_Collingwood_Circuit"
    NZGD_2000_GAWLER_CIRCUIT = "NZGD_2000_Gawler_Circuit"
    NZGD_2000_GREY_CIRCUIT = "NZGD_2000_Grey_Circuit"
    NZGD_2000_HAWKES_BAY_CIRCUIT = "NZGD_2000_Hawkes_Bay_Circuit"
    NZGD_2000_HOKITIKA_CIRCUIT = "NZGD_2000_Hokitika_Circuit"
    NZGD_2000_JACKSONS_BAY_CIRCUIT = "NZGD_2000_Jacksons_Bay_Circuit"
    NZGD_2000_KARAMEA_CIRCUIT = "NZGD_2000_Karamea_Circuit"
    NZGD_2000_LINDIS_PEAK_CIRCUIT = "NZGD_2000_Lindis_Peak_Circuit"
    NZGD_2000_MARLBOROUGH_CIRCUIT = "NZGD_2000_Marlborough_Circuit"
    NZGD_2000_MOUNT_EDEN_CIRCUIT = "NZGD_2000_Mount_Eden_Circuit"
    NZGD_2000_MOUNT_NICHOLAS_CIRCUIT = "NZGD_2000_Mount_Nicholas_Circuit"
    NZGD_2000_MOUNT_PLEASANT_CIRCUIT = "NZGD_2000_Mount_Pleasant_Circuit"
    NZGD_2000_MOUNT_YORK_CIRCUIT = "NZGD_2000_Mount_York_Circuit"
    NZGD_2000_NELSON_CIRCUIT = "NZGD_2000_Nelson_Circuit"
    NZGD_2000_NORTH_TAIERI_CIRCUIT = "NZGD_2000_North_Taieri_Circuit"
    NZGD_2000_OBSERVATION_POINT_CIRCUIT = "NZGD_2000_Observation_Point_Circuit"
    NZGD_2000_OKARITO_CIRCUIT = "NZGD_2000_Okarito_Circuit"
    NZGD_2000_POVERTY_BAY_CIRCUIT = "NZGD_2000_Poverty_Bay_Circuit"
    NZGD_2000_TARANAKI_CIRCUIT = "NZGD_2000_Taranaki_Circuit"
    NZGD_2000_TIMARU_CIRCUIT = "NZGD_2000_Timaru_Circuit"
    NZGD_2000_TUHIRANGI_CIRCUIT = "NZGD_2000_Tuhirangi_Circuit"
    NZGD_2000_UTM_ZONE_58_S = "NZGD_2000_UTM_Zone_58S"
    NZGD_2000_UTM_ZONE_59_S = "NZGD_2000_UTM_Zone_59S"
    NZGD_2000_UTM_ZONE_60_S = "NZGD_2000_UTM_Zone_60S"
    NZGD_2000_WAIRARAPA_CIRCUIT = "NZGD_2000_Wairarapa_Circuit"
    NZGD_2000_WANGANUI_CIRCUIT = "NZGD_2000_Wanganui_Circuit"
    NZGD_2000_WELLINGTON_CIRCUIT = "NZGD_2000_Wellington_Circuit"
    NIGERIA_EAST_BELT = "Nigeria_East_Belt"
    NIGERIA_MID_BELT = "Nigeria_Mid_Belt"
    NIGERIA_WEST_BELT = "Nigeria_West_Belt"
    NORD_ALGERIE_DEGREE = "Nord_Algerie_Degree"
    NORD_ALGERIE_ANCIENNE_DEGREE = "Nord_Algerie_Ancienne_Degree"
    SUD_ALGERIE_ANCIENNE = "Sud_Algerie_Ancienne"
    NORD_ALGERIE = "Nord_Algerie"
    NORD_DE_GUERRE = "Nord_de_Guerre"
    NORD_FRANCE = "Nord_France"
    NORD_MAROC_DEGREE = "Nord_Maroc_Degree"
    NORD_MAROC = "Nord_Maroc"
    NORD_TUNISIE = "Nord_Tunisie"
    NGO_1948_BAERUM_KOMMUNE = "NGO_1948_Baerum_Kommune"
    NGO_1948_BERGENHALVOEN = "NGO_1948_Bergenhalvoen"
    NGO_1948_NORWAY_ZONE_1 = "NGO_1948_Norway_Zone_1"
    NGO_1948_NORWAY_ZONE_2 = "NGO_1948_Norway_Zone_2"
    NGO_1948_NORWAY_ZONE_3 = "NGO_1948_Norway_Zone_3"
    NGO_1948_NORWAY_ZONE_4 = "NGO_1948_Norway_Zone_4"
    NGO_1948_NORWAY_ZONE_5 = "NGO_1948_Norway_Zone_5"
    NGO_1948_NORWAY_ZONE_6 = "NGO_1948_Norway_Zone_6"
    NGO_1948_NORWAY_ZONE_7 = "NGO_1948_Norway_Zone_7"
    NGO_1948_NORWAY_ZONE_8 = "NGO_1948_Norway_Zone_8"
    NGO_1948_OSLO_KOMMUNE = "NGO_1948_Oslo_Kommune"
    NGO_1948_OSLO_NORWAY_ZONE_1 = "NGO_1948_Oslo_Norway_Zone_1"
    NGO_1948_OSLO_NORWAY_ZONE_2 = "NGO_1948_Oslo_Norway_Zone_2"
    NGO_1948_OSLO_NORWAY_ZONE_3 = "NGO_1948_Oslo_Norway_Zone_3"
    NGO_1948_OSLO_NORWAY_ZONE_4 = "NGO_1948_Oslo_Norway_Zone_4"
    NGO_1948_OSLO_NORWAY_ZONE_5 = "NGO_1948_Oslo_Norway_Zone_5"
    NGO_1948_OSLO_NORWAY_ZONE_6 = "NGO_1948_Oslo_Norway_Zone_6"
    NGO_1948_OSLO_NORWAY_ZONE_7 = "NGO_1948_Oslo_Norway_Zone_7"
    NGO_1948_OSLO_NORWAY_ZONE_8 = "NGO_1948_Oslo_Norway_Zone_8"
    NTF_FRANCE_I_DEGREES = "NTF_France_I_degrees"
    NTF_FRANCE_II_DEGREES = "NTF_France_II_degrees"
    NTF_FRANCE_III_DEGREES = "NTF_France_III_degrees"
    NTF_FRANCE_IV_DEGREES = "NTF_France_IV_degrees"
    PALESTINE_1923_ISRAEL_CS_GRID = "Palestine_1923_Israel_CS_Grid"
    PALESTINE_1923_PALESTINE_BELT = "Palestine_1923_Palestine_Belt"
    PALESTINE_1923_PALESTINE_GRID = "Palestine_1923_Palestine_Grid"
    PAMPA_DEL_CASTILLO_ARGENTINA_2 = "Pampa_del_Castillo_Argentina_2"
    PERU_CENTRAL_ZONE = "Peru_Central_Zone"
    PERU_EAST_ZONE = "Peru_East_Zone"
    PERU_WEST_ZONE = "Peru_West_Zone"
    PHILIPPINES_ZONE_I = "Philippines_Zone_I"
    PHILIPPINES_ZONE_II = "Philippines_Zone_II"
    PHILIPPINES_ZONE_III = "Philippines_Zone_III"
    PHILIPPINES_ZONE_IV = "Philippines_Zone_IV"
    PHILIPPINES_ZONE_V = "Philippines_Zone_V"
    PORTUGUESE_NATIONAL_GRID = "Portuguese_National_Grid"
    QATAR_1948_QATAR_GRID = "Qatar_1948_Qatar_Grid"
    QATAR_NATIONAL_GRID = "Qatar_National_Grid"
    RD_OLD = "RD_Old"
    RGF_1993_LAMBERT_93 = "RGF_1993_Lambert_93"
    RIJKSDRIEHOEKSTELSEL_NEW = "Rijksdriehoekstelsel_New"
    RT90_25_GON_W = "RT90_25_gon_W"
    S_JTSK_FERRO_KROVAK_EAST_NORTH = "S-JTSK_Ferro_Krovak_East_North"
    S_JTSK_FERRO_KROVAK = "S-JTSK_Ferro_Krovak"
    S_JTSK_KROVAK_EAST_NORTH = "S-JTSK_Krovak_East_North"
    S_JTSK_KROVAK = "S-JTSK_Krovak"
    SAD_1969_BRAZIL_POLYCONIC = "SAD_1969_Brazil_Polyconic"
    SAHARA_DEGREE = "Sahara_Degree"
    SAHARA = "Sahara"
    SIERRA_LEONE_1924_NEW_COLONY_GRID = "Sierra_Leone_1924_New_Colony_Grid"
    SIERRA_LEONE_1924_NEW_WAR_OFFICE_GRID = "Sierra_Leone_1924_New_War_Office_Grid"
    ST_KITTS_1955_BRITISH_WEST_INDIES_GRID = "St_Kitts_1955_British_West_Indies_Grid"
    ST_LUCIA_1955_BRITISH_WEST_INDIES_GRID = "St_Lucia_1955_British_West_Indies_Grid"
    ST_VINCENT_1945_BRITISH_WEST_INDIES_GRID = "St_Vincent_1945_British_West_Indies_Grid"
    STEREO_33 = "Stereo_33"
    STEREO_70 = "Stereo_70"
    SUD_ALGERIE_DEGREE = "Sud_Algerie_Degree"
    SUD_ALGERIE_ANCIENNE_DEGREE = "Sud_Algerie_Ancienne_Degree"
    SUD_ALGERIE = "Sud_Algerie"
    SUD_FRANCE = "Sud_France"
    SUD_MAROC_DEGREE = "Sud_Maroc_Degree"
    SUD_MAROC = "Sud_Maroc"
    SUD_TUNISIE = "Sud_Tunisie"
    SWEDISH_NATIONAL_GRID = "Swedish_National_Grid"
    TRINIDAD_1903_TRINIDAD_GRID = "Trinidad_1903_Trinidad_Grid"
    UWPP_1992 = "UWPP_1992"
    UWPP_2000_PAS_5 = "UWPP_2000_pas_5"
    UWPP_2000_PAS_6 = "UWPP_2000_pas_6"
    UWPP_2000_PAS_7 = "UWPP_2000_pas_7"
    UWPP_2000_PAS_8 = "UWPP_2000_pas_8"
    WGS_1972_BE_TM_106_NE = "WGS_1972_BE_TM_106_NE"
    WGS_1984_TM_36_SE = "WGS_1984_TM_36_SE"
    ZANDERIJ_SURINAME_OLD_TM = "Zanderij_Suriname_Old_TM"
    ZANDERIJ_SURINAME_TM = "Zanderij_Suriname_TM"
    ZANDERIJ_TM_54_NW = "Zanderij_TM_54_NW"
    NORTH_POLE_AZIMUTHAL_EQUIDISTANT = "North_Pole_Azimuthal_Equidistant"
    NORTH_POLE_GNOMONIC = "North_Pole_Gnomonic"
    NORTH_POLE_LAMBERT_AZIMUTHAL_EQUAL_AREA = "North_Pole_Lambert_Azimuthal_Equal_Area"
    NORTH_POLE_ORTHOGRAPHIC = "North_Pole_Orthographic"
    NORTH_POLE_STEREOGRAPHIC = "North_Pole_Stereographic"
    SOUTH_POLE_AZIMUTHAL_EQUIDISTANT = "South_Pole_Azimuthal_Equidistant"
    SOUTH_POLE_GNOMONIC = "South_Pole_Gnomonic"
    SOUTH_POLE_LAMBERT_AZIMUTHAL_EQUAL_AREA = "South_Pole_Lambert_Azimuthal_Equal_Area"
    SOUTH_POLE_ORTHOGRAPHIC = "South_Pole_Orthographic"
    SOUTH_POLE_STEREOGRAPHIC = "South_Pole_Stereographic"
    UPS_NORTH = "UPS_North"
    UPS_SOUTH = "UPS_South"
    NAD_1927_STATE_PLANE_ALABAMA_EAST_FIPS_0101 = "NAD_1927_StatePlane_Alabama_East_FIPS_0101"
    NAD_1927_STATE_PLANE_ALABAMA_WEST_FIPS_0102 = "NAD_1927_StatePlane_Alabama_West_FIPS_0102"
    NAD_1927_STATE_PLANE_ALASKA_1_FIPS_5001 = "NAD_1927_StatePlane_Alaska_1_FIPS_5001"
    NAD_1927_STATE_PLANE_ALASKA_10_FIPS_5010 = "NAD_1927_StatePlane_Alaska_10_FIPS_5010"
    NAD_1927_STATE_PLANE_ALASKA_2_FIPS_5002 = "NAD_1927_StatePlane_Alaska_2_FIPS_5002"
    NAD_1927_STATE_PLANE_ALASKA_3_FIPS_5003 = "NAD_1927_StatePlane_Alaska_3_FIPS_5003"
    NAD_1927_STATE_PLANE_ALASKA_4_FIPS_5004 = "NAD_1927_StatePlane_Alaska_4_FIPS_5004"
    NAD_1927_STATE_PLANE_ALASKA_5_FIPS_5005 = "NAD_1927_StatePlane_Alaska_5_FIPS_5005"
    NAD_1927_STATE_PLANE_ALASKA_6_FIPS_5006 = "NAD_1927_StatePlane_Alaska_6_FIPS_5006"
    NAD_1927_STATE_PLANE_ALASKA_7_FIPS_5007 = "NAD_1927_StatePlane_Alaska_7_FIPS_5007"
    NAD_1927_STATE_PLANE_ALASKA_8_FIPS_5008 = "NAD_1927_StatePlane_Alaska_8_FIPS_5008"
    NAD_1927_STATE_PLANE_ALASKA_9_FIPS_5009 = "NAD_1927_StatePlane_Alaska_9_FIPS_5009"
    NAD_1927_STATE_PLANE_ARIZONA_CENTRAL_FIPS_0202 = "NAD_1927_StatePlane_Arizona_Central_FIPS_0202"
    NAD_1927_STATE_PLANE_ARIZONA_EAST_FIPS_0201 = "NAD_1927_StatePlane_Arizona_East_FIPS_0201"
    NAD_1927_STATE_PLANE_ARIZONA_WEST_FIPS_0203 = "NAD_1927_StatePlane_Arizona_West_FIPS_0203"
    NAD_1927_STATE_PLANE_ARKANSAS_NORTH_FIPS_0301 = "NAD_1927_StatePlane_Arkansas_North_FIPS_0301"
    NAD_1927_STATE_PLANE_ARKANSAS_SOUTH_FIPS_0302 = "NAD_1927_StatePlane_Arkansas_South_FIPS_0302"
    NAD_1927_STATE_PLANE_CALIFORNIA_I_FIPS_0401 = "NAD_1927_StatePlane_California_I_FIPS_0401"
    NAD_1927_STATE_PLANE_CALIFORNIA_II_FIPS_0402 = "NAD_1927_StatePlane_California_II_FIPS_0402"
    NAD_1927_STATE_PLANE_CALIFORNIA_III_FIPS_0403 = "NAD_1927_StatePlane_California_III_FIPS_0403"
    NAD_1927_STATE_PLANE_CALIFORNIA_IV_FIPS_0404 = "NAD_1927_StatePlane_California_IV_FIPS_0404"
    NAD_1927_STATE_PLANE_CALIFORNIA_V_FIPS_0405 = "NAD_1927_StatePlane_California_V_FIPS_0405"
    NAD_1927_STATE_PLANE_CALIFORNIA_VI_FIPS_0406 = "NAD_1927_StatePlane_California_VI_FIPS_0406"
    NAD_1927_STATE_PLANE_CALIFORNIA_VII_FIPS_0407 = "NAD_1927_StatePlane_California_VII_FIPS_0407"
    NAD_1927_STATE_PLANE_COLORADO_CENTRAL_FIPS_0502 = "NAD_1927_StatePlane_Colorado_Central_FIPS_0502"
    NAD_1927_STATE_PLANE_COLORADO_NORTH_FIPS_0501 = "NAD_1927_StatePlane_Colorado_North_FIPS_0501"
    NAD_1927_STATE_PLANE_COLORADO_SOUTH_FIPS_0503 = "NAD_1927_StatePlane_Colorado_South_FIPS_0503"
    NAD_1927_STATE_PLANE_CONNECTICUT_FIPS_0600 = "NAD_1927_StatePlane_Connecticut_FIPS_0600"
    NAD_1927_STATE_PLANE_DELAWARE_FIPS_0700 = "NAD_1927_StatePlane_Delaware_FIPS_0700"
    NAD_1927_STATE_PLANE_FLORIDA_EAST_FIPS_0901 = "NAD_1927_StatePlane_Florida_East_FIPS_0901"
    NAD_1927_STATE_PLANE_FLORIDA_NORTH_FIPS_0903 = "NAD_1927_StatePlane_Florida_North_FIPS_0903"
    NAD_1927_STATE_PLANE_FLORIDA_WEST_FIPS_0902 = "NAD_1927_StatePlane_Florida_West_FIPS_0902"
    NAD_1927_STATE_PLANE_GEORGIA_EAST_FIPS_1001 = "NAD_1927_StatePlane_Georgia_East_FIPS_1001"
    NAD_1927_STATE_PLANE_GEORGIA_WEST_FIPS_1002 = "NAD_1927_StatePlane_Georgia_West_FIPS_1002"
    NAD_1927_STATE_PLANE_GUAM_FIPS_5400 = "NAD_1927_StatePlane_Guam_FIPS_5400"
    NAD_1927_STATE_PLANE_IDAHO_CENTRAL_FIPS_1102 = "NAD_1927_StatePlane_Idaho_Central_FIPS_1102"
    NAD_1927_STATE_PLANE_IDAHO_EAST_FIPS_1101 = "NAD_1927_StatePlane_Idaho_East_FIPS_1101"
    NAD_1927_STATE_PLANE_IDAHO_WEST_FIPS_1103 = "NAD_1927_StatePlane_Idaho_West_FIPS_1103"
    NAD_1927_STATE_PLANE_ILLINOIS_EAST_FIPS_1201 = "NAD_1927_StatePlane_Illinois_East_FIPS_1201"
    NAD_1927_STATE_PLANE_ILLINOIS_WEST_FIPS_1202 = "NAD_1927_StatePlane_Illinois_West_FIPS_1202"
    NAD_1927_STATE_PLANE_INDIANA_EAST_FIPS_1301 = "NAD_1927_StatePlane_Indiana_East_FIPS_1301"
    NAD_1927_STATE_PLANE_INDIANA_WEST_FIPS_1302 = "NAD_1927_StatePlane_Indiana_West_FIPS_1302"
    NAD_1927_STATE_PLANE_IOWA_NORTH_FIPS_1401 = "NAD_1927_StatePlane_Iowa_North_FIPS_1401"
    NAD_1927_STATE_PLANE_IOWA_SOUTH_FIPS_1402 = "NAD_1927_StatePlane_Iowa_South_FIPS_1402"
    NAD_1927_STATE_PLANE_KANSAS_NORTH_FIPS_1501 = "NAD_1927_StatePlane_Kansas_North_FIPS_1501"
    NAD_1927_STATE_PLANE_KANSAS_SOUTH_FIPS_1502 = "NAD_1927_StatePlane_Kansas_South_FIPS_1502"
    NAD_1927_STATE_PLANE_KENTUCKY_NORTH_FIPS_1601 = "NAD_1927_StatePlane_Kentucky_North_FIPS_1601"
    NAD_1927_STATE_PLANE_KENTUCKY_SOUTH_FIPS_1602 = "NAD_1927_StatePlane_Kentucky_South_FIPS_1602"
    NAD_1927_STATE_PLANE_LOUISIANA_NORTH_FIPS_1701 = "NAD_1927_StatePlane_Louisiana_North_FIPS_1701"
    NAD_1927_STATE_PLANE_LOUISIANA_SOUTH_FIPS_1702 = "NAD_1927_StatePlane_Louisiana_South_FIPS_1702"
    NAD_1927_STATE_PLANE_MAINE_EAST_FIPS_1801 = "NAD_1927_StatePlane_Maine_East_FIPS_1801"
    NAD_1927_STATE_PLANE_MAINE_WEST_FIPS_1802 = "NAD_1927_StatePlane_Maine_West_FIPS_1802"
    NAD_1927_STATE_PLANE_MARYLAND_FIPS_1900 = "NAD_1927_StatePlane_Maryland_FIPS_1900"
    NAD_1927_STATE_PLANE_MASSACHUSETTS_ISLAND_FIPS_2002 = "NAD_1927_StatePlane_Massachusetts_Island_FIPS_2002"
    NAD_1927_STATE_PLANE_MASSACHUSETTS_MAINLAND_FIPS_2001 = "NAD_1927_StatePlane_Massachusetts_Mainland_FIPS_2001"
    NAD_1927_STATE_PLANE_MICHIGAN_CENTRAL_FIPS_2112 = "NAD_1927_StatePlane_Michigan_Central_FIPS_2112"
    NAD_1927_STATE_PLANE_MICHIGAN_NORTH_FIPS_2111 = "NAD_1927_StatePlane_Michigan_North_FIPS_2111"
    NAD_1927_STATE_PLANE_MICHIGAN_SOUTH_FIPS_2113 = "NAD_1927_StatePlane_Michigan_South_FIPS_2113"
    NAD_1927_STATE_PLANE_MINNESOTA_CENTRAL_FIPS_2202 = "NAD_1927_StatePlane_Minnesota_Central_FIPS_2202"
    NAD_1927_STATE_PLANE_MINNESOTA_NORTH_FIPS_2201 = "NAD_1927_StatePlane_Minnesota_North_FIPS_2201"
    NAD_1927_STATE_PLANE_MINNESOTA_SOUTH_FIPS_2203 = "NAD_1927_StatePlane_Minnesota_South_FIPS_2203"
    NAD_1927_STATE_PLANE_MISSISSIPPI_EAST_FIPS_2301 = "NAD_1927_StatePlane_Mississippi_East_FIPS_2301"
    NAD_1927_STATE_PLANE_MISSISSIPPI_WEST_FIPS_2302 = "NAD_1927_StatePlane_Mississippi_West_FIPS_2302"
    NAD_1927_STATE_PLANE_MISSOURI_CENTRAL_FIPS_2402 = "NAD_1927_StatePlane_Missouri_Central_FIPS_2402"
    NAD_1927_STATE_PLANE_MISSOURI_EAST_FIPS_2401 = "NAD_1927_StatePlane_Missouri_East_FIPS_2401"
    NAD_1927_STATE_PLANE_MISSOURI_WEST_FIPS_2403 = "NAD_1927_StatePlane_Missouri_West_FIPS_2403"
    NAD_1927_STATE_PLANE_MONTANA_CENTRAL_FIPS_2502 = "NAD_1927_StatePlane_Montana_Central_FIPS_2502"
    NAD_1927_STATE_PLANE_MONTANA_NORTH_FIPS_2501 = "NAD_1927_StatePlane_Montana_North_FIPS_2501"
    NAD_1927_STATE_PLANE_MONTANA_SOUTH_FIPS_2503 = "NAD_1927_StatePlane_Montana_South_FIPS_2503"
    NAD_1927_STATE_PLANE_NEBRASKA_NORTH_FIPS_2601 = "NAD_1927_StatePlane_Nebraska_North_FIPS_2601"
    NAD_1927_STATE_PLANE_NEBRASKA_SOUTH_FIPS_2602 = "NAD_1927_StatePlane_Nebraska_South_FIPS_2602"
    NAD_1927_STATE_PLANE_NEVADA_CENTRAL_FIPS_2702 = "NAD_1927_StatePlane_Nevada_Central_FIPS_2702"
    NAD_1927_STATE_PLANE_NEVADA_EAST_FIPS_2701 = "NAD_1927_StatePlane_Nevada_East_FIPS_2701"
    NAD_1927_STATE_PLANE_NEVADA_WEST_FIPS_2703 = "NAD_1927_StatePlane_Nevada_West_FIPS_2703"
    NAD_1927_STATE_PLANE_NEW_HAMPSHIRE_FIPS_2800 = "NAD_1927_StatePlane_New_Hampshire_FIPS_2800"
    NAD_1927_STATE_PLANE_NEW_JERSEY_FIPS_2900 = "NAD_1927_StatePlane_New_Jersey_FIPS_2900"
    NAD_1927_STATE_PLANE_NEW_MEXICO_CENTRAL_FIPS_3002 = "NAD_1927_StatePlane_New_Mexico_Central_FIPS_3002"
    NAD_1927_STATE_PLANE_NEW_MEXICO_EAST_FIPS_3001 = "NAD_1927_StatePlane_New_Mexico_East_FIPS_3001"
    NAD_1927_STATE_PLANE_NEW_MEXICO_WEST_FIPS_3003 = "NAD_1927_StatePlane_New_Mexico_West_FIPS_3003"
    NAD_1927_STATE_PLANE_NEW_YORK_CENTRAL_FIPS_3102 = "NAD_1927_StatePlane_New_York_Central_FIPS_3102"
    NAD_1927_STATE_PLANE_NEW_YORK_EAST_FIPS_3101 = "NAD_1927_StatePlane_New_York_East_FIPS_3101"
    NAD_1927_STATE_PLANE_NEW_YORK_LONG_ISLAND_FIPS_3104 = "NAD_1927_StatePlane_New_York_Long_Island_FIPS_3104"
    NAD_1927_STATE_PLANE_NEW_YORK_WEST_FIPS_3103 = "NAD_1927_StatePlane_New_York_West_FIPS_3103"
    NAD_1927_STATE_PLANE_NORTH_CAROLINA_FIPS_3200 = "NAD_1927_StatePlane_North_Carolina_FIPS_3200"
    NAD_1927_STATE_PLANE_NORTH_DAKOTA_NORTH_FIPS_3301 = "NAD_1927_StatePlane_North_Dakota_North_FIPS_3301"
    NAD_1927_STATE_PLANE_NORTH_DAKOTA_SOUTH_FIPS_3302 = "NAD_1927_StatePlane_North_Dakota_South_FIPS_3302"
    NAD_1927_STATE_PLANE_OHIO_NORTH_FIPS_3401 = "NAD_1927_StatePlane_Ohio_North_FIPS_3401"
    NAD_1927_STATE_PLANE_OHIO_SOUTH_FIPS_3402 = "NAD_1927_StatePlane_Ohio_South_FIPS_3402"
    NAD_1927_STATE_PLANE_OKLAHOMA_NORTH_FIPS_3501 = "NAD_1927_StatePlane_Oklahoma_North_FIPS_3501"
    NAD_1927_STATE_PLANE_OKLAHOMA_SOUTH_FIPS_3502 = "NAD_1927_StatePlane_Oklahoma_South_FIPS_3502"
    NAD_1927_STATE_PLANE_OREGON_NORTH_FIPS_3601 = "NAD_1927_StatePlane_Oregon_North_FIPS_3601"
    NAD_1927_STATE_PLANE_OREGON_SOUTH_FIPS_3602 = "NAD_1927_StatePlane_Oregon_South_FIPS_3602"
    NAD_1927_STATE_PLANE_PENNSYLVANIA_NORTH_FIPS_3701 = "NAD_1927_StatePlane_Pennsylvania_North_FIPS_3701"
    NAD_1927_STATE_PLANE_PENNSYLVANIA_SOUTH_FIPS_3702 = "NAD_1927_StatePlane_Pennsylvania_South_FIPS_3702"
    NAD_1927_STATE_PLANE_PUERTO_RICO_FIPS_5201 = "NAD_1927_StatePlane_Puerto_Rico_FIPS_5201"
    NAD_1927_STATE_PLANE_RHODE_ISLAND_FIPS_3800 = "NAD_1927_StatePlane_Rhode_Island_FIPS_3800"
    NAD_1927_STATE_PLANE_SOUTH_CAROLINA_NORTH_FIPS_3901 = "NAD_1927_StatePlane_South_Carolina_North_FIPS_3901"
    NAD_1927_STATE_PLANE_SOUTH_CAROLINA_SOUTH_FIPS_3902 = "NAD_1927_StatePlane_South_Carolina_South_FIPS_3902"
    NAD_1927_STATE_PLANE_SOUTH_DAKOTA_NORTH_FIPS_4001 = "NAD_1927_StatePlane_South_Dakota_North_FIPS_4001"
    NAD_1927_STATE_PLANE_SOUTH_DAKOTA_SOUTH_FIPS_4002 = "NAD_1927_StatePlane_South_Dakota_South_FIPS_4002"
    NAD_1927_STATE_PLANE_TENNESSEE_FIPS_4100 = "NAD_1927_StatePlane_Tennessee_FIPS_4100"
    NAD_1927_STATE_PLANE_TEXAS_CENTRAL_FIPS_4203 = "NAD_1927_StatePlane_Texas_Central_FIPS_4203"
    NAD_1927_STATE_PLANE_TEXAS_NORTH_CENTRAL_FIPS_4202 = "NAD_1927_StatePlane_Texas_North_Central_FIPS_4202"
    NAD_1927_STATE_PLANE_TEXAS_NORTH_FIPS_4201 = "NAD_1927_StatePlane_Texas_North_FIPS_4201"
    NAD_1927_STATE_PLANE_TEXAS_SOUTH_CENTRAL_FIPS_4204 = "NAD_1927_StatePlane_Texas_South_Central_FIPS_4204"
    NAD_1927_STATE_PLANE_TEXAS_SOUTH_FIPS_4205 = "NAD_1927_StatePlane_Texas_South_FIPS_4205"
    NAD_1927_STATE_PLANE_UTAH_CENTRAL_FIPS_4302 = "NAD_1927_StatePlane_Utah_Central_FIPS_4302"
    NAD_1927_STATE_PLANE_UTAH_NORTH_FIPS_4301 = "NAD_1927_StatePlane_Utah_North_FIPS_4301"
    NAD_1927_STATE_PLANE_UTAH_SOUTH_FIPS_4303 = "NAD_1927_StatePlane_Utah_South_FIPS_4303"
    NAD_1927_STATE_PLANE_VERMONT_FIPS_3400 = "NAD_1927_StatePlane_Vermont_FIPS_3400"
    NAD_1927_STATE_PLANE_VIRGINIA_NORTH_FIPS_4501 = "NAD_1927_StatePlane_Virginia_North_FIPS_4501"
    NAD_1927_STATE_PLANE_VIRGINIA_SOUTH_FIPS_4502 = "NAD_1927_StatePlane_Virginia_South_FIPS_4502"
    NAD_1927_STATE_PLANE_WASHINGTON_NORTH_FIPS_4601 = "NAD_1927_StatePlane_Washington_North_FIPS_4601"
    NAD_1927_STATE_PLANE_WASHINGTON_SOUTH_FIPS_4602 = "NAD_1927_StatePlane_Washington_South_FIPS_4602"
    NAD_1927_STATE_PLANE_WEST_VIRGINIA_NORTH_FIPS_4701 = "NAD_1927_StatePlane_West_Virginia_North_FIPS_4701"
    NAD_1927_STATE_PLANE_WEST_VIRGINIA_SOUTH_FIPS_4702 = "NAD_1927_StatePlane_West_Virginia_South_FIPS_4702"
    NAD_1927_STATE_PLANE_WISCONSIN_CENTRAL_FIPS_4802 = "NAD_1927_StatePlane_Wisconsin_Central_FIPS_4802"
    NAD_1927_STATE_PLANE_WISCONSIN_NORTH_FIPS_4801 = "NAD_1927_StatePlane_Wisconsin_North_FIPS_4801"
    NAD_1927_STATE_PLANE_WISCONSIN_SOUTH_FIPS_4803 = "NAD_1927_StatePlane_Wisconsin_South_FIPS_4803"
    NAD_1927_STATE_PLANE_WYOMING_EAST_CENTRAL_FIPS_4902 = "NAD_1927_StatePlane_Wyoming_East_Central_FIPS_4902"
    NAD_1927_STATE_PLANE_WYOMING_EAST_FIPS_4901 = "NAD_1927_StatePlane_Wyoming_East_FIPS_4901"
    NAD_1927_STATE_PLANE_WYOMING_WEST_CENTRAL_FIPS_4903 = "NAD_1927_StatePlane_Wyoming_West_Central_FIPS_4903"
    NAD_1927_STATE_PLANE_WYOMING_WEST_FIPS_4904 = "NAD_1927_StatePlane_Wyoming_West_FIPS_4904"
    NAD_1983_STATE_PLANE_ALABAMA_EAST_FIPS_0101 = "NAD_1983_StatePlane_Alabama_East_FIPS_0101"
    NAD_1983_STATE_PLANE_ALABAMA_WEST_FIPS_0102 = "NAD_1983_StatePlane_Alabama_West_FIPS_0102"
    NAD_1983_STATE_PLANE_ALASKA_1_FIPS_5001 = "NAD_1983_StatePlane_Alaska_1_FIPS_5001"
    NAD_1983_STATE_PLANE_ALASKA_10_FIPS_5010 = "NAD_1983_StatePlane_Alaska_10_FIPS_5010"
    NAD_1983_STATE_PLANE_ALASKA_2_FIPS_5002 = "NAD_1983_StatePlane_Alaska_2_FIPS_5002"
    NAD_1983_STATE_PLANE_ALASKA_3_FIPS_5003 = "NAD_1983_StatePlane_Alaska_3_FIPS_5003"
    NAD_1983_STATE_PLANE_ALASKA_4_FIPS_5004 = "NAD_1983_StatePlane_Alaska_4_FIPS_5004"
    NAD_1983_STATE_PLANE_ALASKA_5_FIPS_5005 = "NAD_1983_StatePlane_Alaska_5_FIPS_5005"
    NAD_1983_STATE_PLANE_ALASKA_6_FIPS_5006 = "NAD_1983_StatePlane_Alaska_6_FIPS_5006"
    NAD_1983_STATE_PLANE_ALASKA_7_FIPS_5007 = "NAD_1983_StatePlane_Alaska_7_FIPS_5007"
    NAD_1983_STATE_PLANE_ALASKA_8_FIPS_5008 = "NAD_1983_StatePlane_Alaska_8_FIPS_5008"
    NAD_1983_STATE_PLANE_ALASKA_9_FIPS_5009 = "NAD_1983_StatePlane_Alaska_9_FIPS_5009"
    NAD_1983_STATE_PLANE_ARIZONA_CENTRAL_FIPS_0202 = "NAD_1983_StatePlane_Arizona_Central_FIPS_0202"
    NAD_1983_STATE_PLANE_ARIZONA_EAST_FIPS_0201 = "NAD_1983_StatePlane_Arizona_East_FIPS_0201"
    NAD_1983_STATE_PLANE_ARIZONA_WEST_FIPS_0203 = "NAD_1983_StatePlane_Arizona_West_FIPS_0203"
    NAD_1983_STATE_PLANE_ARKANSAS_NORTH_FIPS_0301 = "NAD_1983_StatePlane_Arkansas_North_FIPS_0301"
    NAD_1983_STATE_PLANE_ARKANSAS_SOUTH_FIPS_0302 = "NAD_1983_StatePlane_Arkansas_South_FIPS_0302"
    NAD_1983_STATE_PLANE_CALIFORNIA_I_FIPS_0401 = "NAD_1983_StatePlane_California_I_FIPS_0401"
    NAD_1983_STATE_PLANE_CALIFORNIA_II_FIPS_0402 = "NAD_1983_StatePlane_California_II_FIPS_0402"
    NAD_1983_STATE_PLANE_CALIFORNIA_III_FIPS_0403 = "NAD_1983_StatePlane_California_III_FIPS_0403"
    NAD_1983_STATE_PLANE_CALIFORNIA_IV_FIPS_0404 = "NAD_1983_StatePlane_California_IV_FIPS_0404"
    NAD_1983_STATE_PLANE_CALIFORNIA_V_FIPS_0405 = "NAD_1983_StatePlane_California_V_FIPS_0405"
    NAD_1983_STATE_PLANE_CALIFORNIA_VI_FIPS_0406 = "NAD_1983_StatePlane_California_VI_FIPS_0406"
    NAD_1983_STATE_PLANE_COLORADO_CENTRAL_FIPS_0502 = "NAD_1983_StatePlane_Colorado_Central_FIPS_0502"
    NAD_1983_STATE_PLANE_COLORADO_NORTH_FIPS_0501 = "NAD_1983_StatePlane_Colorado_North_FIPS_0501"
    NAD_1983_STATE_PLANE_COLORADO_SOUTH_FIPS_0503 = "NAD_1983_StatePlane_Colorado_South_FIPS_0503"
    NAD_1983_STATE_PLANE_CONNECTICUT_FIPS_0600 = "NAD_1983_StatePlane_Connecticut_FIPS_0600"
    NAD_1983_STATE_PLANE_DELAWARE_FIPS_0700 = "NAD_1983_StatePlane_Delaware_FIPS_0700"
    NAD_1983_STATE_PLANE_FLORIDA_EAST_FIPS_0901 = "NAD_1983_StatePlane_Florida_East_FIPS_0901"
    NAD_1983_STATE_PLANE_FLORIDA_NORTH_FIPS_0903 = "NAD_1983_StatePlane_Florida_North_FIPS_0903"
    NAD_1983_STATE_PLANE_FLORIDA_WEST_FIPS_0902 = "NAD_1983_StatePlane_Florida_West_FIPS_0902"
    NAD_1983_STATE_PLANE_GEORGIA_EAST_FIPS_1001 = "NAD_1983_StatePlane_Georgia_East_FIPS_1001"
    NAD_1983_STATE_PLANE_GEORGIA_WEST_FIPS_1002 = "NAD_1983_StatePlane_Georgia_West_FIPS_1002"
    NAD_1983_STATE_PLANE_GUAM_FIPS_5400 = "NAD_1983_StatePlane_Guam_FIPS_5400"
    NAD_1983_STATE_PLANE_HAWAII_1_FIPS_5101 = "NAD_1983_StatePlane_Hawaii_1_FIPS_5101"
    NAD_1983_STATE_PLANE_HAWAII_2_FIPS_5102 = "NAD_1983_StatePlane_Hawaii_2_FIPS_5102"
    NAD_1983_STATE_PLANE_HAWAII_3_FIPS_5103 = "NAD_1983_StatePlane_Hawaii_3_FIPS_5103"
    NAD_1983_STATE_PLANE_HAWAII_4_FIPS_5104 = "NAD_1983_StatePlane_Hawaii_4_FIPS_5104"
    NAD_1983_STATE_PLANE_HAWAII_5_FIPS_5105 = "NAD_1983_StatePlane_Hawaii_5_FIPS_5105"
    NAD_1983_STATE_PLANE_IDAHO_CENTRAL_FIPS_1102 = "NAD_1983_StatePlane_Idaho_Central_FIPS_1102"
    NAD_1983_STATE_PLANE_IDAHO_EAST_FIPS_1101 = "NAD_1983_StatePlane_Idaho_East_FIPS_1101"
    NAD_1983_STATE_PLANE_IDAHO_WEST_FIPS_1103 = "NAD_1983_StatePlane_Idaho_West_FIPS_1103"
    NAD_1983_STATE_PLANE_ILLINOIS_EAST_FIPS_1201 = "NAD_1983_StatePlane_Illinois_East_FIPS_1201"
    NAD_1983_STATE_PLANE_ILLINOIS_WEST_FIPS_1202 = "NAD_1983_StatePlane_Illinois_West_FIPS_1202"
    NAD_1983_STATE_PLANE_INDIANA_EAST_FIPS_1301 = "NAD_1983_StatePlane_Indiana_East_FIPS_1301"
    NAD_1983_STATE_PLANE_INDIANA_WEST_FIPS_1302 = "NAD_1983_StatePlane_Indiana_West_FIPS_1302"
    NAD_1983_STATE_PLANE_IOWA_NORTH_FIPS_1401 = "NAD_1983_StatePlane_Iowa_North_FIPS_1401"
    NAD_1983_STATE_PLANE_IOWA_SOUTH_FIPS_1402 = "NAD_1983_StatePlane_Iowa_South_FIPS_1402"
    NAD_1983_STATE_PLANE_KANSAS_NORTH_FIPS_1501 = "NAD_1983_StatePlane_Kansas_North_FIPS_1501"
    NAD_1983_STATE_PLANE_KANSAS_SOUTH_FIPS_1502 = "NAD_1983_StatePlane_Kansas_South_FIPS_1502"
    NAD_1983_STATE_PLANE_KENTUCKY_FIPS_1600 = "NAD_1983_StatePlane_Kentucky_FIPS_1600"
    NAD_1983_STATE_PLANE_KENTUCKY_NORTH_FIPS_1601 = "NAD_1983_StatePlane_Kentucky_North_FIPS_1601"
    NAD_1983_STATE_PLANE_KENTUCKY_SOUTH_FIPS_1602 = "NAD_1983_StatePlane_Kentucky_South_FIPS_1602"
    NAD_1983_STATE_PLANE_LOUISIANA_NORTH_FIPS_1701 = "NAD_1983_StatePlane_Louisiana_North_FIPS_1701"
    NAD_1983_STATE_PLANE_LOUISIANA_SOUTH_FIPS_1702 = "NAD_1983_StatePlane_Louisiana_South_FIPS_1702"
    NAD_1983_STATE_PLANE_MAINE_EAST_FIPS_1801 = "NAD_1983_StatePlane_Maine_East_FIPS_1801"
    NAD_1983_STATE_PLANE_MAINE_WEST_FIPS_1802 = "NAD_1983_StatePlane_Maine_West_FIPS_1802"
    NAD_1983_STATE_PLANE_MARYLAND_FIPS_1900 = "NAD_1983_StatePlane_Maryland_FIPS_1900"
    NAD_1983_STATE_PLANE_MASSACHUSETTS_ISLAND_FIPS_2002 = "NAD_1983_StatePlane_Massachusetts_Island_FIPS_2002"
    NAD_1983_STATE_PLANE_MASSACHUSETTS_MAINLAND_FIPS_2001 = "NAD_1983_StatePlane_Massachusetts_Mainland_FIPS_2001"
    NAD_1983_STATE_PLANE_MICHIGAN_CENTRAL_FIPS_2202 = "NAD_1983_StatePlane_Michigan_Central_FIPS_2202"
    NAD_1983_STATE_PLANE_MICHIGAN_NORTH_FIPS_2111 = "NAD_1983_StatePlane_Michigan_North_FIPS_2111"
    NAD_1983_STATE_PLANE_MICHIGAN_SOUTH_FIPS_2113 = "NAD_1983_StatePlane_Michigan_South_FIPS_2113"
    NAD_1983_STATE_PLANE_MINNESOTA_CENTRAL_FIPS_2202 = "NAD_1983_StatePlane_Minnesota_Central_FIPS_2202"
    NAD_1983_STATE_PLANE_MINNESOTA_NORTH_FIPS_2201 = "NAD_1983_StatePlane_Minnesota_North_FIPS_2201"
    NAD_1983_STATE_PLANE_MINNESOTA_SOUTH_FIPS_2203 = "NAD_1983_StatePlane_Minnesota_South_FIPS_2203"
    NAD_1983_STATE_PLANE_MISSISSIPPI_EAST_FIPS_2301 = "NAD_1983_StatePlane_Mississippi_East_FIPS_2301"
    NAD_1983_STATE_PLANE_MISSISSIPPI_WEST_FIPS_2302 = "NAD_1983_StatePlane_Mississippi_West_FIPS_2302"
    NAD_1983_STATE_PLANE_MISSOURI_CENTRAL_FIPS_2402 = "NAD_1983_StatePlane_Missouri_Central_FIPS_2402"
    NAD_1983_STATE_PLANE_MISSOURI_EAST_FIPS_2401 = "NAD_1983_StatePlane_Missouri_East_FIPS_2401"
    NAD_1983_STATE_PLANE_MISSOURI_WEST_FIPS_2403 = "NAD_1983_StatePlane_Missouri_West_FIPS_2403"
    NAD_1983_STATE_PLANE_MONTANA_FIPS_2500 = "NAD_1983_StatePlane_Montana_FIPS_2500"
    NAD_1983_STATE_PLANE_NEBRASKA_FIPS_2600 = "NAD_1983_StatePlane_Nebraska_FIPS_2600"
    NAD_1983_STATE_PLANE_NEVADA_CENTRAL_FIPS_2702 = "NAD_1983_StatePlane_Nevada_Central_FIPS_2702"
    NAD_1983_STATE_PLANE_NEVADA_EAST_FIPS_2701 = "NAD_1983_StatePlane_Nevada_East_FIPS_2701"
    NAD_1983_STATE_PLANE_NEVADA_WEST_FIPS_2703 = "NAD_1983_StatePlane_Nevada_West_FIPS_2703"
    NAD_1983_STATE_PLANE_NEW_HAMPSHIRE_FIPS_2800 = "NAD_1983_StatePlane_New_Hampshire_FIPS_2800"
    NAD_1983_STATE_PLANE_NEW_JERSEY_FIPS_2900 = "NAD_1983_StatePlane_New_Jersey_FIPS_2900"
    NAD_1983_STATE_PLANE_NEW_MEXICO_CENTRAL_FIPS_3002 = "NAD_1983_StatePlane_New_Mexico_Central_FIPS_3002"
    NAD_1983_STATE_PLANE_NEW_MEXICO_EAST_FIPS_3001 = "NAD_1983_StatePlane_New_Mexico_East_FIPS_3001"
    NAD_1983_STATE_PLANE_NEW_MEXICO_WEST_FIPS_3003 = "NAD_1983_StatePlane_New_Mexico_West_FIPS_3003"
    NAD_1983_STATE_PLANE_NEW_YORK_CENTRAL_FIPS_3102 = "NAD_1983_StatePlane_New_York_Central_FIPS_3102"
    NAD_1983_STATE_PLANE_NEW_YORK_EAST_FIPS_3101 = "NAD_1983_StatePlane_New_York_East_FIPS_3101"
    NAD_1983_STATE_PLANE_NEW_YORK_LONG_ISLAND_FIPS_3104 = "NAD_1983_StatePlane_New_York_Long_Island_FIPS_3104"
    NAD_1983_STATE_PLANE_NEW_YORK_WEST_FIPS_3103 = "NAD_1983_StatePlane_New_York_West_FIPS_3103"
    NAD_1983_STATE_PLANE_NORTH_CAROLINA_FIPS_3200 = "NAD_1983_StatePlane_North_Carolina_FIPS_3200"
    NAD_1983_STATE_PLANE_NORTH_DAKOTA_NORTH_FIPS_3301 = "NAD_1983_StatePlane_North_Dakota_North_FIPS_3301"
    NAD_1983_STATE_PLANE_NORTH_DAKOTA_SOUTH_FIPS_3302 = "NAD_1983_StatePlane_North_Dakota_South_FIPS_3302"
    NAD_1983_STATE_PLANE_OHIO_NORTH_FIPS_3401 = "NAD_1983_StatePlane_Ohio_North_FIPS_3401"
    NAD_1983_STATE_PLANE_OHIO_SOUTH_FIPS_3402 = "NAD_1983_StatePlane_Ohio_South_FIPS_3402"
    NAD_1983_STATE_PLANE_OKLAHOMA_NORTH_FIPS_3501 = "NAD_1983_StatePlane_Oklahoma_North_FIPS_3501"
    NAD_1983_STATE_PLANE_OKLAHOMA_SOUTH_FIPS_3502 = "NAD_1983_StatePlane_Oklahoma_South_FIPS_3502"
    NAD_1983_STATE_PLANE_OREGON_NORTH_FIPS_3601 = "NAD_1983_StatePlane_Oregon_North_FIPS_3601"
    NAD_1983_STATE_PLANE_OREGON_SOUTH_FIPS_3602 = "NAD_1983_StatePlane_Oregon_South_FIPS_3602"
    NAD_1983_STATE_PLANE_PENNSYLVANIA_NORTH_FIPS_3701 = "NAD_1983_StatePlane_Pennsylvania_North_FIPS_3701"
    NAD_1983_STATE_PLANE_PENNSYLVANIA_SOUTH_FIPS_3702 = "NAD_1983_StatePlane_Pennsylvania_South_FIPS_3702"
    NAD_1983_STATE_PLANE_PUERTO_RICO_VIRGIN_ISLANDS_FIPS_5200 = "NAD_1983_StatePlane_Puerto_Rico_Virgin_Islands_FIPS_5200"
    NAD_1983_STATE_PLANE_RHODE_ISLAND_FIPS_3800 = "NAD_1983_StatePlane_Rhode_Island_FIPS_3800"
    NAD_1983_STATE_PLANE_SOUTH_CAROLINA_FIPS_3900 = "NAD_1983_StatePlane_South_Carolina_FIPS_3900"
    NAD_1983_STATE_PLANE_SOUTH_DAKOTA_NORTH_FIPS_4001 = "NAD_1983_StatePlane_South_Dakota_North_FIPS_4001"
    NAD_1983_STATE_PLANE_SOUTH_DAKOTA_SOUTH_FIPS_4002 = "NAD_1983_StatePlane_South_Dakota_South_FIPS_4002"
    NAD_1983_STATE_PLANE_TENNESSEE_FIPS_4100 = "NAD_1983_StatePlane_Tennessee_FIPS_4100"
    NAD_1983_STATE_PLANE_TEXAS_CENTRAL_FIPS_4203 = "NAD_1983_StatePlane_Texas_Central_FIPS_4203"
    NAD_1983_STATE_PLANE_TEXAS_NORTH_CENTRAL_FIPS_4202 = "NAD_1983_StatePlane_Texas_North_Central_FIPS_4202"
    NAD_1983_STATE_PLANE_TEXAS_NORTH_FIPS_4201 = "NAD_1983_StatePlane_Texas_North_FIPS_4201"
    NAD_1983_STATE_PLANE_TEXAS_SOUTH_CENTRAL_FIPS_4204 = "NAD_1983_StatePlane_Texas_South_Central_FIPS_4204"
    NAD_1983_STATE_PLANE_TEXAS_SOUTH_FIPS_4205 = "NAD_1983_StatePlane_Texas_South_FIPS_4205"
    NAD_1983_STATE_PLANE_UTAH_CENTRAL_FIPS_4302 = "NAD_1983_StatePlane_Utah_Central_FIPS_4302"
    NAD_1983_STATE_PLANE_UTAH_NORTH_FIPS_4301 = "NAD_1983_StatePlane_Utah_North_FIPS_4301"
    NAD_1983_STATE_PLANE_UTAH_SOUTH_FIPS_4303 = "NAD_1983_StatePlane_Utah_South_FIPS_4303"
    NAD_1983_STATE_PLANE_VERMONT_FIPS_4400 = "NAD_1983_StatePlane_Vermont_FIPS_4400"
    NAD_1983_STATE_PLANE_VIRGINIA_NORTH_FIPS_4501 = "NAD_1983_StatePlane_Virginia_North_FIPS_4501"
    NAD_1983_STATE_PLANE_VIRGINIA_SOUTH_FIPS_4502 = "NAD_1983_StatePlane_Virginia_South_FIPS_4502"
    NAD_1983_STATE_PLANE_WASHINGTON_NORTH_FIPS_4601 = "NAD_1983_StatePlane_Washington_North_FIPS_4601"
    NAD_1983_STATE_PLANE_WASHINGTON_SOUTH_FIPS_4602 = "NAD_1983_StatePlane_Washington_South_FIPS_4602"
    NAD_1983_STATE_PLANE_WEST_VIRGINIA_NORTH_FIPS_4701 = "NAD_1983_StatePlane_West_Virginia_North_FIPS_4701"
    NAD_1983_STATE_PLANE_WEST_VIRGINIA_SOUTH_FIPS_4702 = "NAD_1983_StatePlane_West_Virginia_South_FIPS_4702"
    NAD_1983_STATE_PLANE_WISCONSIN_CENTRAL_FIPS_4802 = "NAD_1983_StatePlane_Wisconsin_Central_FIPS_4802"
    NAD_1983_STATE_PLANE_WISCONSIN_NORTH_FIPS_4801 = "NAD_1983_StatePlane_Wisconsin_North_FIPS_4801"
    NAD_1983_STATE_PLANE_WISCONSIN_SOUTH_FIPS_4803 = "NAD_1983_StatePlane_Wisconsin_South_FIPS_4803"
    NAD_1983_STATE_PLANE_WYOMING_EAST_CENTRAL_FIPS_4902 = "NAD_1983_StatePlane_Wyoming_East_Central_FIPS_4902"
    NAD_1983_STATE_PLANE_WYOMING_EAST_FIPS_4901 = "NAD_1983_StatePlane_Wyoming_East_FIPS_4901"
    NAD_1983_STATE_PLANE_WYOMING_WEST_CENTRAL_FIPS_4903 = "NAD_1983_StatePlane_Wyoming_West_Central_FIPS_4903"
    NAD_1983_STATE_PLANE_WYOMING_WEST_FIPS_4904 = "NAD_1983_StatePlane_Wyoming_West_FIPS_4904"
    NAD_1983_STATE_PLANE_ALABAMA_EAST_FIPS_0101_FEET = "NAD_1983_StatePlane_Alabama_East_FIPS_0101_Feet"
    NAD_1983_STATE_PLANE_ALABAMA_WEST_FIPS_0102_FEET = "NAD_1983_StatePlane_Alabama_West_FIPS_0102_Feet"
    NAD_1983_STATE_PLANE_ALASKA_1_FIPS_5001_FEET = "NAD_1983_StatePlane_Alaska_1_FIPS_5001_Feet"
    NAD_1983_STATE_PLANE_ALASKA_10_FIPS_5010_FEET = "NAD_1983_StatePlane_Alaska_10_FIPS_5010_Feet"
    NAD_1983_STATE_PLANE_ALASKA_2_FIPS_5002_FEET = "NAD_1983_StatePlane_Alaska_2_FIPS_5002_Feet"
    NAD_1983_STATE_PLANE_ALASKA_3_FIPS_5003_FEET = "NAD_1983_StatePlane_Alaska_3_FIPS_5003_Feet"
    NAD_1983_STATE_PLANE_ALASKA_4_FIPS_5004_FEET = "NAD_1983_StatePlane_Alaska_4_FIPS_5004_Feet"
    NAD_1983_STATE_PLANE_ALASKA_5_FIPS_5005_FEET = "NAD_1983_StatePlane_Alaska_5_FIPS_5005_Feet"
    NAD_1983_STATE_PLANE_ALASKA_6_FIPS_5006_FEET = "NAD_1983_StatePlane_Alaska_6_FIPS_5006_Feet"
    NAD_1983_STATE_PLANE_ALASKA_7_FIPS_5007_FEET = "NAD_1983_StatePlane_Alaska_7_FIPS_5007_Feet"
    NAD_1983_STATE_PLANE_ALASKA_8_FIPS_5008_FEET = "NAD_1983_StatePlane_Alaska_8_FIPS_5008_Feet"
    NAD_1983_STATE_PLANE_ALASKA_9_FIPS_5009_FEET = "NAD_1983_StatePlane_Alaska_9_FIPS_5009_Feet"
    NAD_1983_STATE_PLANE_ARIZONA_CENTRAL_FIPS_0202_FEET = "NAD_1983_StatePlane_Arizona_Central_FIPS_0202_Feet"
    NAD_1983_STATE_PLANE_ARIZONA_EAST_FIPS_0201_FEET = "NAD_1983_StatePlane_Arizona_East_FIPS_0201_Feet"
    NAD_1983_STATE_PLANE_ARIZONA_WEST_FIPS_0203_FEET = "NAD_1983_StatePlane_Arizona_West_FIPS_0203_Feet"
    NAD_1983_STATE_PLANE_ARKANSAS_NORTH_FIPS_0301_FEET = "NAD_1983_StatePlane_Arkansas_North_FIPS_0301_Feet"
    NAD_1983_STATE_PLANE_ARKANSAS_SOUTH_FIPS_0302_FEET = "NAD_1983_StatePlane_Arkansas_South_FIPS_0302_Feet"
    NAD_1983_STATE_PLANE_CALIFORNIA_I_FIPS_0401_FEET = "NAD_1983_StatePlane_California_I_FIPS_0401_Feet"
    NAD_1983_STATE_PLANE_CALIFORNIA_II_FIPS_0402_FEET = "NAD_1983_StatePlane_California_II_FIPS_0402_Feet"
    NAD_1983_STATE_PLANE_CALIFORNIA_III_FIPS_0403_FEET = "NAD_1983_StatePlane_California_III_FIPS_0403_Feet"
    NAD_1983_STATE_PLANE_CALIFORNIA_IV_FIPS_0404_FEET = "NAD_1983_StatePlane_California_IV_FIPS_0404_Feet"
    NAD_1983_STATE_PLANE_CALIFORNIA_V_FIPS_0405_FEET = "NAD_1983_StatePlane_California_V_FIPS_0405_Feet"
    NAD_1983_STATE_PLANE_CALIFORNIA_VI_FIPS_0406_FEET = "NAD_1983_StatePlane_California_VI_FIPS_0406_Feet"
    NAD_1983_STATE_PLANE_COLORADO_CENTRAL_FIPS_0502_FEET = "NAD_1983_StatePlane_Colorado_Central_FIPS_0502_Feet"
    NAD_1983_STATE_PLANE_COLORADO_NORTH_FIPS_0501_FEET = "NAD_1983_StatePlane_Colorado_North_FIPS_0501_Feet"
    NAD_1983_STATE_PLANE_COLORADO_SOUTH_FIPS_0503_FEET = "NAD_1983_StatePlane_Colorado_South_FIPS_0503_Feet"
    NAD_1983_STATE_PLANE_CONNECTICUT_FIPS_0600_FEET = "NAD_1983_StatePlane_Connecticut_FIPS_0600_Feet"
    NAD_1983_STATE_PLANE_DELAWARE_FIPS_0700_FEET = "NAD_1983_StatePlane_Delaware_FIPS_0700_Feet"
    NAD_1983_STATE_PLANE_FLORIDA_EAST_FIPS_0901_FEET = "NAD_1983_StatePlane_Florida_East_FIPS_0901_Feet"
    NAD_1983_STATE_PLANE_FLORIDA_NORTH_FIPS_0903_FEET = "NAD_1983_StatePlane_Florida_North_FIPS_0903_Feet"
    NAD_1983_STATE_PLANE_FLORIDA_WEST_FIPS_0902_FEET = "NAD_1983_StatePlane_Florida_West_FIPS_0902_Feet"
    NAD_1983_STATE_PLANE_GEORGIA_EAST_FIPS_1001_FEET = "NAD_1983_StatePlane_Georgia_East_FIPS_1001_Feet"
    NAD_1983_STATE_PLANE_GEORGIA_WEST_FIPS_1002_FEET = "NAD_1983_StatePlane_Georgia_West_FIPS_1002_Feet"
    NAD_1983_STATE_PLANE_GUAM_FIPS_5400_FEET = "NAD_1983_StatePlane_Guam_FIPS_5400_Feet"
    NAD_1983_STATE_PLANE_HAWAII_1_FIPS_5101_FEET = "NAD_1983_StatePlane_Hawaii_1_FIPS_5101_Feet"
    NAD_1983_STATE_PLANE_HAWAII_2_FIPS_5102_FEET = "NAD_1983_StatePlane_Hawaii_2_FIPS_5102_Feet"
    NAD_1983_STATE_PLANE_HAWAII_3_FIPS_5103_FEET = "NAD_1983_StatePlane_Hawaii_3_FIPS_5103_Feet"
    NAD_1983_STATE_PLANE_HAWAII_4_FIPS_5104_FEET = "NAD_1983_StatePlane_Hawaii_4_FIPS_5104_Feet"
    NAD_1983_STATE_PLANE_HAWAII_5_FIPS_5105_FEET = "NAD_1983_StatePlane_Hawaii_5_FIPS_5105_Feet"
    NAD_1983_STATE_PLANE_IDAHO_CENTRAL_FIPS_1102_FEET = "NAD_1983_StatePlane_Idaho_Central_FIPS_1102_Feet"
    NAD_1983_STATE_PLANE_IDAHO_EAST_FIPS_1101_FEET = "NAD_1983_StatePlane_Idaho_East_FIPS_1101_Feet"
    NAD_1983_STATE_PLANE_IDAHO_WEST_FIPS_1103_FEET = "NAD_1983_StatePlane_Idaho_West_FIPS_1103_Feet"
    NAD_1983_STATE_PLANE_ILLINOIS_EAST_FIPS_1201_FEET = "NAD_1983_StatePlane_Illinois_East_FIPS_1201_Feet"
    NAD_1983_STATE_PLANE_ILLINOIS_WEST_FIPS_1202_FEET = "NAD_1983_StatePlane_Illinois_West_FIPS_1202_Feet"
    NAD_1983_STATE_PLANE_INDIANA_EAST_FIPS_1301_FEET = "NAD_1983_StatePlane_Indiana_East_FIPS_1301_Feet"
    NAD_1983_STATE_PLANE_INDIANA_WEST_FIPS_1302_FEET = "NAD_1983_StatePlane_Indiana_West_FIPS_1302_Feet"
    NAD_1983_STATE_PLANE_IOWA_NORTH_FIPS_1401_FEET = "NAD_1983_StatePlane_Iowa_North_FIPS_1401_Feet"
    NAD_1983_STATE_PLANE_IOWA_SOUTH_FIPS_1402_FEET = "NAD_1983_StatePlane_Iowa_South_FIPS_1402_Feet"
    NAD_1983_STATE_PLANE_KANSAS_NORTH_FIPS_1501_FEET = "NAD_1983_StatePlane_Kansas_North_FIPS_1501_Feet"
    NAD_1983_STATE_PLANE_KANSAS_SOUTH_FIPS_1502_FEET = "NAD_1983_StatePlane_Kansas_South_FIPS_1502_Feet"
    NAD_1983_STATE_PLANE_KENTUCKY_FIPS_1600_FEET = "NAD_1983_StatePlane_Kentucky_FIPS_1600_Feet"
    NAD_1983_STATE_PLANE_KENTUCKY_NORTH_FIPS_1601_FEET = "NAD_1983_StatePlane_Kentucky_North_FIPS_1601_Feet"
    NAD_1983_STATE_PLANE_KENTUCKY_SOUTH_FIPS_1602_FEET = "NAD_1983_StatePlane_Kentucky_South_FIPS_1602_Feet"
    NAD_1983_STATE_PLANE_LOUISIANA_NORTH_FIPS_1701_FEET = "NAD_1983_StatePlane_Louisiana_North_FIPS_1701_Feet"
    NAD_1983_STATE_PLANE_LOUISIANA_SOUTH_FIPS_1702_FEET = "NAD_1983_StatePlane_Louisiana_South_FIPS_1702_Feet"
    NAD_1983_STATE_PLANE_MAINE_EAST_FIPS_1801_FEET = "NAD_1983_StatePlane_Maine_East_FIPS_1801_Feet"
    NAD_1983_STATE_PLANE_MAINE_WEST_FIPS_1802_FEET = "NAD_1983_StatePlane_Maine_West_FIPS_1802_Feet"
    NAD_1983_STATE_PLANE_MARYLAND_FIPS_1900_FEET = "NAD_1983_StatePlane_Maryland_FIPS_1900_Feet"
    NAD_1983_STATE_PLANE_MASSACHUSETTS_ISLAND_FIPS_2002_FEET = "NAD_1983_StatePlane_Massachusetts_Island_FIPS_2002_Feet"
    NAD_1983_STATE_PLANE_MASSACHUSETTS_MAINLAND_FIPS_2001_FEET = "NAD_1983_StatePlane_Massachusetts_Mainland_FIPS_2001_Feet"
    NAD_1983_STATE_PLANE_MICHIGAN_CENTRAL_FIPS_2202_FEET = "NAD_1983_StatePlane_Michigan_Central_FIPS_2202_Feet"
    NAD_1983_STATE_PLANE_MICHIGAN_NORTH_FIPS_2111_FEET = "NAD_1983_StatePlane_Michigan_North_FIPS_2111_Feet"
    NAD_1983_STATE_PLANE_MICHIGAN_SOUTH_FIPS_2113_FEET = "NAD_1983_StatePlane_Michigan_South_FIPS_2113_Feet"
    NAD_1983_STATE_PLANE_MINNESOTA_CENTRAL_FIPS_2202_FEET = "NAD_1983_StatePlane_Minnesota_Central_FIPS_2202_Feet"
    NAD_1983_STATE_PLANE_MINNESOTA_NORTH_FIPS_2201_FEET = "NAD_1983_StatePlane_Minnesota_North_FIPS_2201_Feet"
    NAD_1983_STATE_PLANE_MINNESOTA_SOUTH_FIPS_2203_FEET = "NAD_1983_StatePlane_Minnesota_South_FIPS_2203_Feet"
    NAD_1983_STATE_PLANE_MISSISSIPPI_EAST_FIPS_2301_FEET = "NAD_1983_StatePlane_Mississippi_East_FIPS_2301_Feet"
    NAD_1983_STATE_PLANE_MISSISSIPPI_WEST_FIPS_2302_FEET = "NAD_1983_StatePlane_Mississippi_West_FIPS_2302_Feet"
    NAD_1983_STATE_PLANE_MISSOURI_CENTRAL_FIPS_2402_FEET = "NAD_1983_StatePlane_Missouri_Central_FIPS_2402_Feet"
    NAD_1983_STATE_PLANE_MISSOURI_EAST_FIPS_2401_FEET = "NAD_1983_StatePlane_Missouri_East_FIPS_2401_Feet"
    NAD_1983_STATE_PLANE_MISSOURI_WEST_FIPS_2403_FEET = "NAD_1983_StatePlane_Missouri_West_FIPS_2403_Feet"
    NAD_1983_STATE_PLANE_MONTANA_FIPS_2500_FEET = "NAD_1983_StatePlane_Montana_FIPS_2500_Feet"
    NAD_1983_STATE_PLANE_NEBRASKA_FIPS_2600_FEET = "NAD_1983_StatePlane_Nebraska_FIPS_2600_Feet"
    NAD_1983_STATE_PLANE_NEVADA_CENTRAL_FIPS_2702_FEET = "NAD_1983_StatePlane_Nevada_Central_FIPS_2702_Feet"
    NAD_1983_STATE_PLANE_NEVADA_EAST_FIPS_2701_FEET = "NAD_1983_StatePlane_Nevada_East_FIPS_2701_Feet"
    NAD_1983_STATE_PLANE_NEVADA_WEST_FIPS_2703_FEET = "NAD_1983_StatePlane_Nevada_West_FIPS_2703_Feet"
    NAD_1983_STATE_PLANE_NEW_HAMPSHIRE_FIPS_2800_FEET = "NAD_1983_StatePlane_New_Hampshire_FIPS_2800_Feet"
    NAD_1983_STATE_PLANE_NEW_JERSEY_FIPS_2900_FEET = "NAD_1983_StatePlane_New_Jersey_FIPS_2900_Feet"
    NAD_1983_STATE_PLANE_NEW_MEXICO_CENTRAL_FIPS_3002_FEET = "NAD_1983_StatePlane_New_Mexico_Central_FIPS_3002_Feet"
    NAD_1983_STATE_PLANE_NEW_MEXICO_EAST_FIPS_3001_FEET = "NAD_1983_StatePlane_New_Mexico_East_FIPS_3001_Feet"
    NAD_1983_STATE_PLANE_NEW_MEXICO_WEST_FIPS_3003_FEET = "NAD_1983_StatePlane_New_Mexico_West_FIPS_3003_Feet"
    NAD_1983_STATE_PLANE_NEW_YORK_CENTRAL_FIPS_3102_FEET = "NAD_1983_StatePlane_New_York_Central_FIPS_3102_Feet"
    NAD_1983_STATE_PLANE_NEW_YORK_EAST_FIPS_3101_FEET = "NAD_1983_StatePlane_New_York_East_FIPS_3101_Feet"
    NAD_1983_STATE_PLANE_NEW_YORK_LONG_ISLAND_FIPS_3104_FEET = "NAD_1983_StatePlane_New_York_Long_Island_FIPS_3104_Feet"
    NAD_1983_STATE_PLANE_NEW_YORK_WEST_FIPS_3103_FEET = "NAD_1983_StatePlane_New_York_West_FIPS_3103_Feet"
    NAD_1983_STATE_PLANE_NORTH_CAROLINA_FIPS_3200_FEET = "NAD_1983_StatePlane_North_Carolina_FIPS_3200_Feet"
    NAD_1983_STATE_PLANE_NORTH_DAKOTA_NORTH_FIPS_3301_FEET = "NAD_1983_StatePlane_North_Dakota_North_FIPS_3301_Feet"
    NAD_1983_STATE_PLANE_NORTH_DAKOTA_SOUTH_FIPS_3302_FEET = "NAD_1983_StatePlane_North_Dakota_South_FIPS_3302_Feet"
    NAD_1983_STATE_PLANE_OHIO_NORTH_FIPS_3401_FEET = "NAD_1983_StatePlane_Ohio_North_FIPS_3401_Feet"
    NAD_1983_STATE_PLANE_OHIO_SOUTH_FIPS_3402_FEET = "NAD_1983_StatePlane_Ohio_South_FIPS_3402_Feet"
    NAD_1983_STATE_PLANE_OKLAHOMA_NORTH_FIPS_3501_FEET = "NAD_1983_StatePlane_Oklahoma_North_FIPS_3501_Feet"
    NAD_1983_STATE_PLANE_OKLAHOMA_SOUTH_FIPS_3502_FEET = "NAD_1983_StatePlane_Oklahoma_South_FIPS_3502_Feet"
    NAD_1983_STATE_PLANE_OREGON_NORTH_FIPS_3601_FEET = "NAD_1983_StatePlane_Oregon_North_FIPS_3601_Feet"
    NAD_1983_STATE_PLANE_OREGON_SOUTH_FIPS_3602_FEET = "NAD_1983_StatePlane_Oregon_South_FIPS_3602_Feet"
    NAD_1983_STATE_PLANE_PENNSYLVANIA_NORTH_FIPS_3701_FEET = "NAD_1983_StatePlane_Pennsylvania_North_FIPS_3701_Feet"
    NAD_1983_STATE_PLANE_PENNSYLVANIA_SOUTH_FIPS_3702_FEET = "NAD_1983_StatePlane_Pennsylvania_South_FIPS_3702_Feet"
    NAD_1983_STATE_PLANE_PUERTO_RICO_VIRGIN_ISLANDS_FIPS_5200_FEET = "NAD_1983_StatePlane_Puerto_Rico_Virgin_Islands_FIPS_5200_Feet"
    NAD_1983_STATE_PLANE_RHODE_ISLAND_FIPS_3800_FEET = "NAD_1983_StatePlane_Rhode_Island_FIPS_3800_Feet"
    NAD_1983_STATE_PLANE_SOUTH_CAROLINA_FIPS_3900_FEET = "NAD_1983_StatePlane_South_Carolina_FIPS_3900_Feet"
    NAD_1983_STATE_PLANE_SOUTH_DAKOTA_NORTH_FIPS_4001_FEET = "NAD_1983_StatePlane_South_Dakota_North_FIPS_4001_Feet"
    NAD_1983_STATE_PLANE_SOUTH_DAKOTA_SOUTH_FIPS_4002_FEET = "NAD_1983_StatePlane_South_Dakota_South_FIPS_4002_Feet"
    NAD_1983_STATE_PLANE_TENNESSEE_FIPS_4100_FEET = "NAD_1983_StatePlane_Tennessee_FIPS_4100_Feet"
    NAD_1983_STATE_PLANE_TEXAS_CENTRAL_FIPS_4203_FEET = "NAD_1983_StatePlane_Texas_Central_FIPS_4203_Feet"
    NAD_1983_STATE_PLANE_TEXAS_NORTH_CENTRAL_FIPS_4202_FEET = "NAD_1983_StatePlane_Texas_North_Central_FIPS_4202_Feet"
    NAD_1983_STATE_PLANE_TEXAS_NORTH_FIPS_4201_FEET = "NAD_1983_StatePlane_Texas_North_FIPS_4201_Feet"
    NAD_1983_STATE_PLANE_TEXAS_SOUTH_CENTRAL_FIPS_4204_FEET = "NAD_1983_StatePlane_Texas_South_Central_FIPS_4204_Feet"
    NAD_1983_STATE_PLANE_TEXAS_SOUTH_FIPS_4205_FEET = "NAD_1983_StatePlane_Texas_South_FIPS_4205_Feet"
    NAD_1983_STATE_PLANE_UTAH_CENTRAL_FIPS_4302_FEET = "NAD_1983_StatePlane_Utah_Central_FIPS_4302_Feet"
    NAD_1983_STATE_PLANE_UTAH_NORTH_FIPS_4301_FEET = "NAD_1983_StatePlane_Utah_North_FIPS_4301_Feet"
    NAD_1983_STATE_PLANE_UTAH_SOUTH_FIPS_4303_FEET = "NAD_1983_StatePlane_Utah_South_FIPS_4303_Feet"
    NAD_1983_STATE_PLANE_VERMONT_FIPS_4400_FEET = "NAD_1983_StatePlane_Vermont_FIPS_4400_Feet"
    NAD_1983_STATE_PLANE_VIRGINIA_NORTH_FIPS_4501_FEET = "NAD_1983_StatePlane_Virginia_North_FIPS_4501_Feet"
    NAD_1983_STATE_PLANE_VIRGINIA_SOUTH_FIPS_4502_FEET = "NAD_1983_StatePlane_Virginia_South_FIPS_4502_Feet"
    NAD_1983_STATE_PLANE_WASHINGTON_NORTH_FIPS_4601_FEET = "NAD_1983_StatePlane_Washington_North_FIPS_4601_Feet"
    NAD_1983_STATE_PLANE_WASHINGTON_SOUTH_FIPS_4602_FEET = "NAD_1983_StatePlane_Washington_South_FIPS_4602_Feet"
    NAD_1983_STATE_PLANE_WEST_VIRGINIA_NORTH_FIPS_4701_FEET = "NAD_1983_StatePlane_West_Virginia_North_FIPS_4701_Feet"
    NAD_1983_STATE_PLANE_WEST_VIRGINIA_SOUTH_FIPS_4702_FEET = "NAD_1983_StatePlane_West_Virginia_South_FIPS_4702_Feet"
    NAD_1983_STATE_PLANE_WISCONSIN_CENTRAL_FIPS_4802_FEET = "NAD_1983_StatePlane_Wisconsin_Central_FIPS_4802_Feet"
    NAD_1983_STATE_PLANE_WISCONSIN_NORTH_FIPS_4801_FEET = "NAD_1983_StatePlane_Wisconsin_North_FIPS_4801_Feet"
    NAD_1983_STATE_PLANE_WISCONSIN_SOUTH_FIPS_4803_FEET = "NAD_1983_StatePlane_Wisconsin_South_FIPS_4803_Feet"
    NAD_1983_STATE_PLANE_WYOMING_EAST_CENTRAL_FIPS_4902_FEET = "NAD_1983_StatePlane_Wyoming_East_Central_FIPS_4902_Feet"
    NAD_1983_STATE_PLANE_WYOMING_EAST_FIPS_4901_FEET = "NAD_1983_StatePlane_Wyoming_East_FIPS_4901_Feet"
    NAD_1983_STATE_PLANE_WYOMING_WEST_CENTRAL_FIPS_4903_FEET = "NAD_1983_StatePlane_Wyoming_West_Central_FIPS_4903_Feet"
    NAD_1983_STATE_PLANE_WYOMING_WEST_FIPS_4904_FEET = "NAD_1983_StatePlane_Wyoming_West_FIPS_4904_Feet"
    NAD_1983_HARN_STATE_PLANE_ALABAMA_EAST_FIPS_0101 = "NAD_1983_HARN_StatePlane_Alabama_East_FIPS_0101"
    NAD_1983_HARN_STATE_PLANE_ALABAMA_WEST_FIPS_0102 = "NAD_1983_HARN_StatePlane_Alabama_West_FIPS_0102"
    NAD_1983_HARN_STATE_PLANE_ARIZONA_CENTRAL_FIPS_0202 = "NAD_1983_HARN_StatePlane_Arizona_Central_FIPS_0202"
    NAD_1983_HARN_STATE_PLANE_ARIZONA_EAST_FIPS_0201 = "NAD_1983_HARN_StatePlane_Arizona_East_FIPS_0201"
    NAD_1983_HARN_STATE_PLANE_ARIZONA_WEST_FIPS_0203 = "NAD_1983_HARN_StatePlane_Arizona_West_FIPS_0203"
    NAD_1983_HARN_STATE_PLANE_CALIFORNIA_I_FIPS_0401 = "NAD_1983_HARN_StatePlane_California_I_FIPS_0401"
    NAD_1983_HARN_STATE_PLANE_CALIFORNIA_II_FIPS_0402 = "NAD_1983_HARN_StatePlane_California_II_FIPS_0402"
    NAD_1983_HARN_STATE_PLANE_CALIFORNIA_III_FIPS_0403 = "NAD_1983_HARN_StatePlane_California_III_FIPS_0403"
    NAD_1983_HARN_STATE_PLANE_CALIFORNIA_IV_FIPS_0404 = "NAD_1983_HARN_StatePlane_California_IV_FIPS_0404"
    NAD_1983_HARN_STATE_PLANE_CALIFORNIA_V_FIPS_0405 = "NAD_1983_HARN_StatePlane_California_V_FIPS_0405"
    NAD_1983_HARN_STATE_PLANE_CALIFORNIA_VI_FIPS_0406 = "NAD_1983_HARN_StatePlane_California_VI_FIPS_0406"
    NAD_1983_HARN_STATE_PLANE_COLORADO_CENTRAL_FIPS_0502 = "NAD_1983_HARN_StatePlane_Colorado_Central_FIPS_0502"
    NAD_1983_HARN_STATE_PLANE_COLORADO_NORTH_FIPS_0501 = "NAD_1983_HARN_StatePlane_Colorado_North_FIPS_0501"
    NAD_1983_HARN_STATE_PLANE_COLORADO_SOUTH_FIPS_0503 = "NAD_1983_HARN_StatePlane_Colorado_South_FIPS_0503"
    NAD_1983_HARN_STATE_PLANE_CONNECTICUT_FIPS_0600 = "NAD_1983_HARN_StatePlane_Connecticut_FIPS_0600"
    NAD_1983_HARN_STATE_PLANE_DELAWARE_FIPS_0700 = "NAD_1983_HARN_StatePlane_Delaware_FIPS_0700"
    NAD_1983_HARN_STATE_PLANE_FLORIDA_EAST_FIPS_0901 = "NAD_1983_HARN_StatePlane_Florida_East_FIPS_0901"
    NAD_1983_HARN_STATE_PLANE_FLORIDA_NORTH_FIPS_0903 = "NAD_1983_HARN_StatePlane_Florida_North_FIPS_0903"
    NAD_1983_HARN_STATE_PLANE_FLORIDA_WEST_FIPS_0902 = "NAD_1983_HARN_StatePlane_Florida_West_FIPS_0902"
    NAD_1983_HARN_STATE_PLANE_GEORGIA_EAST_FIPS_1001 = "NAD_1983_HARN_StatePlane_Georgia_East_FIPS_1001"
    NAD_1983_HARN_STATE_PLANE_GEORGIA_WEST_FIPS_1002 = "NAD_1983_HARN_StatePlane_Georgia_West_FIPS_1002"
    NAD_1983_HARN_STATE_PLANE_HAWAII_1_FIPS_5101 = "NAD_1983_HARN_StatePlane_Hawaii_1_FIPS_5101"
    NAD_1983_HARN_STATE_PLANE_HAWAII_2_FIPS_5102 = "NAD_1983_HARN_StatePlane_Hawaii_2_FIPS_5102"
    NAD_1983_HARN_STATE_PLANE_HAWAII_3_FIPS_5103 = "NAD_1983_HARN_StatePlane_Hawaii_3_FIPS_5103"
    NAD_1983_HARN_STATE_PLANE_HAWAII_4_FIPS_5104 = "NAD_1983_HARN_StatePlane_Hawaii_4_FIPS_5104"
    NAD_1983_HARN_STATE_PLANE_HAWAII_5_FIPS_5105 = "NAD_1983_HARN_StatePlane_Hawaii_5_FIPS_5105"
    NAD_1983_HARN_STATE_PLANE_IDAHO_CENTRAL_FIPS_1102 = "NAD_1983_HARN_StatePlane_Idaho_Central_FIPS_1102"
    NAD_1983_HARN_STATE_PLANE_IDAHO_EAST_FIPS_1101 = "NAD_1983_HARN_StatePlane_Idaho_East_FIPS_1101"
    NAD_1983_HARN_STATE_PLANE_IDAHO_WEST_FIPS_1103 = "NAD_1983_HARN_StatePlane_Idaho_West_FIPS_1103"
    NAD_1983_HARN_STATE_PLANE_ILLINOIS_EAST_FIPS_1201 = "NAD_1983_HARN_StatePlane_Illinois_East_FIPS_1201"
    NAD_1983_HARN_STATE_PLANE_ILLINOIS_WEST_FIPS_1202 = "NAD_1983_HARN_StatePlane_Illinois_West_FIPS_1202"
    NAD_1983_HARN_STATE_PLANE_INDIANA_EAST_FIPS_1301 = "NAD_1983_HARN_StatePlane_Indiana_East_FIPS_1301"
    NAD_1983_HARN_STATE_PLANE_INDIANA_WEST_FIPS_1302 = "NAD_1983_HARN_StatePlane_Indiana_West_FIPS_1302"
    NAD_1983_HARN_STATE_PLANE_KANSAS_NORTH_FIPS_1501 = "NAD_1983_HARN_StatePlane_Kansas_North_FIPS_1501"
    NAD_1983_HARN_STATE_PLANE_KANSAS_SOUTH_FIPS_1502 = "NAD_1983_HARN_StatePlane_Kansas_South_FIPS_1502"
    NAD_1983_HARN_STATE_PLANE_KENTUCKY_NORTH_FIPS_1601 = "NAD_1983_HARN_StatePlane_Kentucky_North_FIPS_1601"
    NAD_1983_HARN_STATE_PLANE_KENTUCKY_SOUTH_FIPS_1602 = "NAD_1983_HARN_StatePlane_Kentucky_South_FIPS_1602"
    NAD_1983_HARN_STATE_PLANE_LOUISIANA_NORTH_FIPS_1701 = "NAD_1983_HARN_StatePlane_Louisiana_North_FIPS_1701"
    NAD_1983_HARN_STATE_PLANE_LOUISIANA_SOUTH_FIPS_1702 = "NAD_1983_HARN_StatePlane_Louisiana_South_FIPS_1702"
    NAD_1983_HARN_STATE_PLANE_MAINE_EAST_FIPS_1801 = "NAD_1983_HARN_StatePlane_Maine_East_FIPS_1801"
    NAD_1983_HARN_STATE_PLANE_MAINE_WEST_FIPS_1802 = "NAD_1983_HARN_StatePlane_Maine_West_FIPS_1802"
    NAD_1983_HARN_STATE_PLANE_MARYLAND_FIPS_1900 = "NAD_1983_HARN_StatePlane_Maryland_FIPS_1900"
    NAD_1983_HARN_STATE_PLANE_MASSACHUSETTS_ISLAND_FIPS_2002 = "NAD_1983_HARN_StatePlane_Massachusetts_Island_FIPS_2002"
    NAD_1983_HARN_STATE_PLANE_MASSACHUSETTS_MAINLAND_FIPS_2001 = "NAD_1983_HARN_StatePlane_Massachusetts_Mainland_FIPS_2001"
    NAD_1983_HARN_STATE_PLANE_MICHIGAN_CENTRAL_FIPS_2202 = "NAD_1983_HARN_StatePlane_Michigan_Central_FIPS_2202"
    NAD_1983_HARN_STATE_PLANE_MICHIGAN_NORTH_FIPS_2111 = "NAD_1983_HARN_StatePlane_Michigan_North_FIPS_2111"
    NAD_1983_HARN_STATE_PLANE_MICHIGAN_SOUTH_FIPS_2113 = "NAD_1983_HARN_StatePlane_Michigan_South_FIPS_2113"
    NAD_1983_HARN_STATE_PLANE_MISSISSIPPI_EAST_FIPS_2301 = "NAD_1983_HARN_StatePlane_Mississippi_East_FIPS_2301"
    NAD_1983_HARN_STATE_PLANE_MISSISSIPPI_WEST_FIPS_2302 = "NAD_1983_HARN_StatePlane_Mississippi_West_FIPS_2302"
    NAD_1983_HARN_STATE_PLANE_MONTANA_FIPS_2500 = "NAD_1983_HARN_StatePlane_Montana_FIPS_2500"
    NAD_1983_HARN_STATE_PLANE_NEBRASKA_FIPS_2600 = "NAD_1983_HARN_StatePlane_Nebraska_FIPS_2600"
    NAD_1983_HARN_STATE_PLANE_NEVADA_CENTRAL_FIPS_2702 = "NAD_1983_HARN_StatePlane_Nevada_Central_FIPS_2702"
    NAD_1983_HARN_STATE_PLANE_NEVADA_EAST_FIPS_2701 = "NAD_1983_HARN_StatePlane_Nevada_East_FIPS_2701"
    NAD_1983_HARN_STATE_PLANE_NEVADA_WEST_FIPS_2703 = "NAD_1983_HARN_StatePlane_Nevada_West_FIPS_2703"
    NAD_1983_HARN_STATE_PLANE_NEW_HAMPSHIRE_FIPS_2800 = "NAD_1983_HARN_StatePlane_New_Hampshire_FIPS_2800"
    NAD_1983_HARN_STATE_PLANE_NEW_JERSEY_FIPS_2900 = "NAD_1983_HARN_StatePlane_New_Jersey_FIPS_2900"
    NAD_1983_HARN_STATE_PLANE_NEW_MEXICO_CENTRAL_FIPS_3002 = "NAD_1983_HARN_StatePlane_New_Mexico_Central_FIPS_3002"
    NAD_1983_HARN_STATE_PLANE_NEW_MEXICO_EAST_FIPS_3001 = "NAD_1983_HARN_StatePlane_New_Mexico_East_FIPS_3001"
    NAD_1983_HARN_STATE_PLANE_NEW_MEXICO_WEST_FIPS_3003 = "NAD_1983_HARN_StatePlane_New_Mexico_West_FIPS_3003"
    NAD_1983_HARN_STATE_PLANE_NEW_YORK_CENTRAL_FIPS_3102 = "NAD_1983_HARN_StatePlane_New_York_Central_FIPS_3102"
    NAD_1983_HARN_STATE_PLANE_NEW_YORK_EAST_FIPS_3101 = "NAD_1983_HARN_StatePlane_New_York_East_FIPS_3101"
    NAD_1983_HARN_STATE_PLANE_NEW_YORK_LONG_ISLAND_FIPS_3104 = "NAD_1983_HARN_StatePlane_New_York_Long_Island_FIPS_3104"
    NAD_1983_HARN_STATE_PLANE_NEW_YORK_WEST_FIPS_3103 = "NAD_1983_HARN_StatePlane_New_York_West_FIPS_3103"
    NAD_1983_HARN_STATE_PLANE_NORTH_DAKOTA_NORTH_FIPS_3301 = "NAD_1983_HARN_StatePlane_North_Dakota_North_FIPS_3301"
    NAD_1983_HARN_STATE_PLANE_NORTH_DAKOTA_SOUTH_FIPS_3302 = "NAD_1983_HARN_StatePlane_North_Dakota_South_FIPS_3302"
    NAD_1983_HARN_STATE_PLANE_OHIO_NORTH_FIPS_3401 = "NAD_1983_HARN_StatePlane_Ohio_North_FIPS_3401"
    NAD_1983_HARN_STATE_PLANE_OHIO_SOUTH_FIPS_3402 = "NAD_1983_HARN_StatePlane_Ohio_South_FIPS_3402"
    NAD_1983_HARN_STATE_PLANE_OKLAHOMA_NORTH_FIPS_3501 = "NAD_1983_HARN_StatePlane_Oklahoma_North_FIPS_3501"
    NAD_1983_HARN_STATE_PLANE_OKLAHOMA_SOUTH_FIPS_3502 = "NAD_1983_HARN_StatePlane_Oklahoma_South_FIPS_3502"
    NAD_1983_HARN_STATE_PLANE_OREGON_NORTH_FIPS_3601 = "NAD_1983_HARN_StatePlane_Oregon_North_FIPS_3601"
    NAD_1983_HARN_STATE_PLANE_OREGON_SOUTH_FIPS_3602 = "NAD_1983_HARN_StatePlane_Oregon_South_FIPS_3602"
    NAD_1983_HARN_STATE_PLANE_PUERTO_RICO_VIRGIN_ISLANDS_FIPS_5200 = "NAD_1983_HARN_StatePlane_Puerto_Rico_Virgin_Islands_FIPS_5200"
    NAD_1983_HARN_STATE_PLANE_RHODE_ISLAND_FIPS_3800 = "NAD_1983_HARN_StatePlane_Rhode_Island_FIPS_3800"
    NAD_1983_HARN_STATE_PLANE_SOUTH_DAKOTA_NORTH_FIPS_4001 = "NAD_1983_HARN_StatePlane_South_Dakota_North_FIPS_4001"
    NAD_1983_HARN_STATE_PLANE_SOUTH_DAKOTA_SOUTH_FIPS_4002 = "NAD_1983_HARN_StatePlane_South_Dakota_South_FIPS_4002"
    NAD_1983_HARN_STATE_PLANE_TENNESSEE_FIPS_4100 = "NAD_1983_HARN_StatePlane_Tennessee_FIPS_4100"
    NAD_1983_HARN_STATE_PLANE_TEXAS_CENTRAL_FIPS_4203 = "NAD_1983_HARN_StatePlane_Texas_Central_FIPS_4203"
    NAD_1983_HARN_STATE_PLANE_TEXAS_NORTH_CENTRAL_FIPS_4202 = "NAD_1983_HARN_StatePlane_Texas_North_Central_FIPS_4202"
    NAD_1983_HARN_STATE_PLANE_TEXAS_NORTH_FIPS_4201 = "NAD_1983_HARN_StatePlane_Texas_North_FIPS_4201"
    NAD_1983_HARN_STATE_PLANE_TEXAS_SOUTH_CENTRAL_FIPS_4204 = "NAD_1983_HARN_StatePlane_Texas_South_Central_FIPS_4204"
    NAD_1983_HARN_STATE_PLANE_TEXAS_SOUTH_FIPS_4205 = "NAD_1983_HARN_StatePlane_Texas_South_FIPS_4205"
    NAD_1983_HARN_STATE_PLANE_UTAH_CENTRAL_FIPS_4302 = "NAD_1983_HARN_StatePlane_Utah_Central_FIPS_4302"
    NAD_1983_HARN_STATE_PLANE_UTAH_NORTH_FIPS_4301 = "NAD_1983_HARN_StatePlane_Utah_North_FIPS_4301"
    NAD_1983_HARN_STATE_PLANE_UTAH_SOUTH_FIPS_4303 = "NAD_1983_HARN_StatePlane_Utah_South_FIPS_4303"
    NAD_1983_HARN_STATE_PLANE_VERMONT_FIPS_4400 = "NAD_1983_HARN_StatePlane_Vermont_FIPS_4400"
    NAD_1983_HARN_STATE_PLANE_VIRGINIA_NORTH_FIPS_4501 = "NAD_1983_HARN_StatePlane_Virginia_North_FIPS_4501"
    NAD_1983_HARN_STATE_PLANE_VIRGINIA_SOUTH_FIPS_4502 = "NAD_1983_HARN_StatePlane_Virginia_South_FIPS_4502"
    NAD_1983_HARN_STATE_PLANE_WASHINGTON_NORTH_FIPS_4601 = "NAD_1983_HARN_StatePlane_Washington_North_FIPS_4601"
    NAD_1983_HARN_STATE_PLANE_WASHINGTON_SOUTH_FIPS_4602 = "NAD_1983_HARN_StatePlane_Washington_South_FIPS_4602"
    NAD_1983_HARN_STATE_PLANE_WEST_VIRGINIA_NORTH_FIPS_4701 = "NAD_1983_HARN_StatePlane_West_Virginia_North_FIPS_4701"
    NAD_1983_HARN_STATE_PLANE_WEST_VIRGINIA_SOUTH_FIPS_4702 = "NAD_1983_HARN_StatePlane_West_Virginia_South_FIPS_4702"
    NAD_1983_HARN_STATE_PLANE_WISCONSIN_CENTRAL_FIPS_4802 = "NAD_1983_HARN_StatePlane_Wisconsin_Central_FIPS_4802"
    NAD_1983_HARN_STATE_PLANE_WISCONSIN_NORTH_FIPS_4801 = "NAD_1983_HARN_StatePlane_Wisconsin_North_FIPS_4801"
    NAD_1983_HARN_STATE_PLANE_WISCONSIN_SOUTH_FIPS_4803 = "NAD_1983_HARN_StatePlane_Wisconsin_South_FIPS_4803"
    NAD_1983_HARN_STATE_PLANE_WYOMING_EAST_FIPS_4901 = "NAD_1983_HARN_StatePlane_Wyoming_East_FIPS_4901"
    NAD_1983_HARN_STATE_PLANE_WYOMING_EAST_CENTRAL_FIPS_4902 = "NAD_1983_HARN_StatePlane_Wyoming_East_Central_FIPS_4902"
    NAD_1983_HARN_STATE_PLANE_WYOMING_WEST_CENTRAL_FIPS_4903 = "NAD_1983_HARN_StatePlane_Wyoming_West_Central_FIPS_4903"
    NAD_1983_HARN_STATE_PLANE_WYOMING_WEST_FIPS_4904 = "NAD_1983_HARN_StatePlane_Wyoming_West_FIPS_4904"
    AMERICAN_SAMOA_1962_STATE_PLANE_AMERICAN_SAMOA_FIPS_5300 = "American_Samoa_1962_StatePlane_American_Samoa_FIPS_5300"
    NAD_1983_HARN_UTM_ZONE_2_S = "NAD_1983_HARN_UTM_Zone_2S"
    NAD_MICHIGAN_STATE_PLANE_MICHIGAN_CENTRAL_FIPS_2112 = "NAD_Michigan_StatePlane_Michigan_Central_FIPS_2112"
    NAD_MICHIGAN_STATE_PLANE_MICHIGAN_CENTRAL_OLD_FIPS_2102 = "NAD_Michigan_StatePlane_Michigan_Central_Old_FIPS_2102"
    NAD_MICHIGAN_STATE_PLANE_MICHIGAN_EAST_OLD_FIPS_2101 = "NAD_Michigan_StatePlane_Michigan_East_Old_FIPS_2101"
    NAD_MICHIGAN_STATE_PLANE_MICHIGAN_NORTH_FIPS_2111 = "NAD_Michigan_StatePlane_Michigan_North_FIPS_2111"
    NAD_MICHIGAN_STATE_PLANE_MICHIGAN_SOUTH_FIPS_2113 = "NAD_Michigan_StatePlane_Michigan_South_FIPS_2113"
    NAD_MICHIGAN_STATE_PLANE_MICHIGAN_WEST_OLD_FIPS_2103 = "NAD_Michigan_StatePlane_Michigan_West_Old_FIPS_2103"
    OLD_HAWAIIAN_STATE_PLANE_HAWAII_1_FIPS_5101 = "Old_Hawaiian_StatePlane_Hawaii_1_FIPS_5101"
    OLD_HAWAIIAN_STATE_PLANE_HAWAII_2_FIPS_5102 = "Old_Hawaiian_StatePlane_Hawaii_2_FIPS_5102"
    OLD_HAWAIIAN_STATE_PLANE_HAWAII_3_FIPS_5103 = "Old_Hawaiian_StatePlane_Hawaii_3_FIPS_5103"
    OLD_HAWAIIAN_STATE_PLANE_HAWAII_4_FIPS_5104 = "Old_Hawaiian_StatePlane_Hawaii_4_FIPS_5104"
    OLD_HAWAIIAN_STATE_PLANE_HAWAII_5_FIPS_5105 = "Old_Hawaiian_StatePlane_Hawaii_5_FIPS_5105"
    PUERTO_RICO_STATE_PLANE_PUERTO_RICO_FIPS_5201 = "Puerto_Rico_StatePlane_Puerto_Rico_FIPS_5201"
    PUERTO_RICO_STATE_PLANE_VIRGIN_ISLANDS_ST_CROIX_FIPS_5202 = "Puerto_Rico_StatePlane_Virgin_Islands_St_Croix_FIPS_5202"
    NAD_1927_UTM_ZONE_10_N = "NAD_1927_UTM_Zone_10N"
    NAD_1927_UTM_ZONE_11_N = "NAD_1927_UTM_Zone_11N"
    NAD_1927_UTM_ZONE_12_N = "NAD_1927_UTM_Zone_12N"
    NAD_1927_UTM_ZONE_13_N = "NAD_1927_UTM_Zone_13N"
    NAD_1927_UTM_ZONE_14_N = "NAD_1927_UTM_Zone_14N"
    NAD_1927_UTM_ZONE_15_N = "NAD_1927_UTM_Zone_15N"
    NAD_1927_UTM_ZONE_16_N = "NAD_1927_UTM_Zone_16N"
    NAD_1927_UTM_ZONE_17_N = "NAD_1927_UTM_Zone_17N"
    NAD_1927_UTM_ZONE_18_N = "NAD_1927_UTM_Zone_18N"
    NAD_1927_UTM_ZONE_19_N = "NAD_1927_UTM_Zone_19N"
    NAD_1927_UTM_ZONE_20_N = "NAD_1927_UTM_Zone_20N"
    NAD_1927_UTM_ZONE_21_N = "NAD_1927_UTM_Zone_21N"
    NAD_1927_UTM_ZONE_22_N = "NAD_1927_UTM_Zone_22N"
    NAD_1927_UTM_ZONE_3_N = "NAD_1927_UTM_Zone_3N"
    NAD_1927_UTM_ZONE_4_N = "NAD_1927_UTM_Zone_4N"
    NAD_1927_UTM_ZONE_5_N = "NAD_1927_UTM_Zone_5N"
    NAD_1927_UTM_ZONE_6_N = "NAD_1927_UTM_Zone_6N"
    NAD_1927_UTM_ZONE_7_N = "NAD_1927_UTM_Zone_7N"
    NAD_1927_UTM_ZONE_8_N = "NAD_1927_UTM_Zone_8N"
    NAD_1927_UTM_ZONE_9_N = "NAD_1927_UTM_Zone_9N"
    NAD_1983_UTM_ZONE_10_N = "NAD_1983_UTM_Zone_10N"
    NAD_1983_UTM_ZONE_11_N = "NAD_1983_UTM_Zone_11N"
    NAD_1983_UTM_ZONE_12_N = "NAD_1983_UTM_Zone_12N"
    NAD_1983_UTM_ZONE_13_N = "NAD_1983_UTM_Zone_13N"
    NAD_1983_UTM_ZONE_14_N = "NAD_1983_UTM_Zone_14N"
    NAD_1983_UTM_ZONE_15_N = "NAD_1983_UTM_Zone_15N"
    NAD_1983_UTM_ZONE_16_N = "NAD_1983_UTM_Zone_16N"
    NAD_1983_UTM_ZONE_17_N = "NAD_1983_UTM_Zone_17N"
    NAD_1983_UTM_ZONE_18_N = "NAD_1983_UTM_Zone_18N"
    NAD_1983_UTM_ZONE_19_N = "NAD_1983_UTM_Zone_19N"
    NAD_1983_UTM_ZONE_20_N = "NAD_1983_UTM_Zone_20N"
    NAD_1983_UTM_ZONE_21_N = "NAD_1983_UTM_Zone_21N"
    NAD_1983_UTM_ZONE_22_N = "NAD_1983_UTM_Zone_22N"
    NAD_1983_UTM_ZONE_23_N = "NAD_1983_UTM_Zone_23N"
    NAD_1983_UTM_ZONE_3_N = "NAD_1983_UTM_Zone_3N"
    NAD_1983_UTM_ZONE_4_N = "NAD_1983_UTM_Zone_4N"
    NAD_1983_UTM_ZONE_5_N = "NAD_1983_UTM_Zone_5N"
    NAD_1983_UTM_ZONE_6_N = "NAD_1983_UTM_Zone_6N"
    NAD_1983_UTM_ZONE_7_N = "NAD_1983_UTM_Zone_7N"
    NAD_1983_UTM_ZONE_8_N = "NAD_1983_UTM_Zone_8N"
    NAD_1983_UTM_ZONE_9_N = "NAD_1983_UTM_Zone_9N"
    ABIDJAN_1987_UTM_ZONE_29_N = "Abidjan_1987_UTM_Zone_29N"
    ABIDJAN_1987_UTM_ZONE_30_N = "Abidjan_1987_UTM_Zone_30N"
    ADINDAN_UTM_ZONE_37_N = "Adindan_UTM_Zone_37N"
    ADINDAN_UTM_ZONE_38_N = "Adindan_UTM_Zone_38N"
    AFGOOYE_UTM_ZONE_38_N = "Afgooye_UTM_Zone_38N"
    AFGOOYE_UTM_ZONE_39_N = "Afgooye_UTM_Zone_39N"
    AIN_EL_ABD_UTM_ZONE_37_N = "Ain_el_Abd_UTM_Zone_37N"
    AIN_EL_ABD_UTM_ZONE_38_N = "Ain_el_Abd_UTM_Zone_38N"
    AIN_EL_ABD_UTM_ZONE_39_N = "Ain_el_Abd_UTM_Zone_39N"
    ARATU_UTM_ZONE_22_S = "Aratu_UTM_Zone_22S"
    ARATU_UTM_ZONE_23_S = "Aratu_UTM_Zone_23S"
    ARATU_UTM_ZONE_24_S = "Aratu_UTM_Zone_24S"
    ARC_1950_UTM_ZONE_34_S = "Arc_1950_UTM_Zone_34S"
    ARC_1950_UTM_ZONE_35_S = "Arc_1950_UTM_Zone_35S"
    ARC_1950_UTM_ZONE_36_S = "Arc_1950_UTM_Zone_36S"
    ARC_1960_UTM_ZONE_35_N = "Arc_1960_UTM_Zone_35N"
    ARC_1960_UTM_ZONE_35_S = "Arc_1960_UTM_Zone_35S"
    ARC_1960_UTM_ZONE_36_N = "Arc_1960_UTM_Zone_36N"
    ARC_1960_UTM_ZONE_36_S = "Arc_1960_UTM_Zone_36S"
    ARC_1960_UTM_ZONE_37_N = "Arc_1960_UTM_Zone_37N"
    ARC_1960_UTM_ZONE_37_S = "Arc_1960_UTM_Zone_37S"
    ATS_1977_UTM_ZONE_19_N = "ATS_1977_UTM_Zone_19N"
    ATS_1977_UTM_ZONE_20_N = "ATS_1977_UTM_Zone_20N"
    BATAVIA_UTM_ZONE_48_S = "Batavia_UTM_Zone_48S"
    BATAVIA_UTM_ZONE_49_S = "Batavia_UTM_Zone_49S"
    BATAVIA_UTM_ZONE_50_S = "Batavia_UTM_Zone_50S"
    BISSAU_UTM_ZONE_28_N = "Bissau_UTM_Zone_28N"
    BOGOTA_UTM_ZONE_17_N = "Bogota_UTM_Zone_17N"
    BOGOTA_UTM_ZONE_18_N = "Bogota_UTM_Zone_18N"
    CAMACUPA_UTM_ZONE_32_S = "Camacupa_UTM_Zone_32S"
    CAMACUPA_UTM_ZONE_33_S = "Camacupa_UTM_Zone_33S"
    CAPE_UTM_ZONE_34_S = "Cape_UTM_Zone_34S"
    CAPE_UTM_ZONE_35_S = "Cape_UTM_Zone_35S"
    CAPE_UTM_ZONE_36_S = "Cape_UTM_Zone_36S"
    CARTHAGE_UTM_ZONE_32_N = "Carthage_UTM_Zone_32N"
    CONAKRY_1905_UTM_ZONE_28_N = "Conakry_1905_UTM_Zone_28N"
    CONAKRY_1905_UTM_ZONE_29_N = "Conakry_1905_UTM_Zone_29N"
    CORREGO_ALEGRE_UTM_ZONE_23_S = "Corrego_Alegre_UTM_Zone_23S"
    CORREGO_ALEGRE_UTM_ZONE_24_S = "Corrego_Alegre_UTM_Zone_24S"
    DABOLA_UTM_ZONE_28_N = "Dabola_UTM_Zone_28N"
    DABOLA_UTM_ZONE_29_N = "Dabola_UTM_Zone_29N"
    DATUM_73_UTM_ZONE_29_N = "Datum_73_UTM_Zone_29N"
    DOUALA_UTM_ZONE_32_N = "Douala_UTM_Zone_32N"
    ED_1950_ED77_UTM_ZONE_38_N = "ED_1950_ED77_UTM_Zone_38N"
    ED_1950_ED77_UTM_ZONE_39_N = "ED_1950_ED77_UTM_Zone_39N"
    ED_1950_ED77_UTM_ZONE_40_N = "ED_1950_ED77_UTM_Zone_40N"
    ED_1950_ED77_UTM_ZONE_41_N = "ED_1950_ED77_UTM_Zone_41N"
    ELD_1979_UTM_ZONE_32_N = "ELD_1979_UTM_Zone_32N"
    ELD_1979_UTM_ZONE_33_N = "ELD_1979_UTM_Zone_33N"
    ELD_1979_UTM_ZONE_34_N = "ELD_1979_UTM_Zone_34N"
    ELD_1979_UTM_ZONE_35_N = "ELD_1979_UTM_Zone_35N"
    ETRF_1989_UTM_ZONE_28_N = "ETRF_1989_UTM_Zone_28N"
    ETRF_1989_UTM_ZONE_29_N = "ETRF_1989_UTM_Zone_29N"
    ETRF_1989_UTM_ZONE_30_N = "ETRF_1989_UTM_Zone_30N"
    ETRF_1989_UTM_ZONE_31_N = "ETRF_1989_UTM_Zone_31N"
    ETRF_1989_UTM_ZONE_32_N = "ETRF_1989_UTM_Zone_32N"
    ETRF_1989_UTM_ZONE_33_N = "ETRF_1989_UTM_Zone_33N"
    ETRF_1989_UTM_ZONE_34_N = "ETRF_1989_UTM_Zone_34N"
    ETRF_1989_UTM_ZONE_35_N = "ETRF_1989_UTM_Zone_35N"
    ETRF_1989_UTM_ZONE_36_N = "ETRF_1989_UTM_Zone_36N"
    ETRF_1989_UTM_ZONE_37_N = "ETRF_1989_UTM_Zone_37N"
    ETRF_1989_UTM_ZONE_38_N = "ETRF_1989_UTM_Zone_38N"
    ED_1950_UTM_ZONE_28_N = "ED_1950_UTM_Zone_28N"
    ED_1950_UTM_ZONE_29_N = "ED_1950_UTM_Zone_29N"
    ED_1950_UTM_ZONE_30_N = "ED_1950_UTM_Zone_30N"
    ED_1950_UTM_ZONE_31_N = "ED_1950_UTM_Zone_31N"
    ED_1950_UTM_ZONE_32_N = "ED_1950_UTM_Zone_32N"
    ED_1950_UTM_ZONE_33_N = "ED_1950_UTM_Zone_33N"
    ED_1950_UTM_ZONE_34_N = "ED_1950_UTM_Zone_34N"
    ED_1950_UTM_ZONE_35_N = "ED_1950_UTM_Zone_35N"
    ED_1950_UTM_ZONE_36_N = "ED_1950_UTM_Zone_36N"
    ED_1950_UTM_ZONE_37_N = "ED_1950_UTM_Zone_37N"
    ED_1950_UTM_ZONE_38_N = "ED_1950_UTM_Zone_38N"
    FAHUD_UTM_ZONE_39_N = "Fahud_UTM_Zone_39N"
    FAHUD_UTM_ZONE_40_N = "Fahud_UTM_Zone_40N"
    GAROUA_UTM_ZONE_33_N = "Garoua_UTM_Zone_33N"
    GRACIOSA_BASE_SW_1948_UTM_ZONE_26_N = "Graciosa_Base_SW_1948_UTM_Zone_26N"
    HITO_XVIII_1963_UTM_19_S = "Hito_XVIII_1963_UTM_19S"
    HONG_KONG_1980_UTM_ZONE_49_N = "Hong_Kong_1980_UTM_Zone_49N"
    HONG_KONG_1980_UTM_ZONE_50_N = "Hong_Kong_1980_UTM_Zone_50N"
    INDIAN_1954_UTM_ZONE_46_N = "Indian_1954_UTM_Zone_46N"
    INDIAN_1954_UTM_ZONE_47_N = "Indian_1954_UTM_Zone_47N"
    INDIAN_1954_UTM_ZONE_48_N = "Indian_1954_UTM_Zone_48N"
    INDIAN_1960_UTM_ZONE_48_N = "Indian_1960_UTM_Zone_48N"
    INDIAN_1960_UTM_ZONE_49_N = "Indian_1960_UTM_Zone_49N"
    INDIAN_1975_UTM_ZONE_47_N = "Indian_1975_UTM_Zone_47N"
    INDIAN_1975_UTM_ZONE_48_N = "Indian_1975_UTM_Zone_48N"
    INDONESIAN_1974_UTM_ZONE_46_N = "Indonesian_1974_UTM_Zone_46N"
    INDONESIAN_1974_UTM_ZONE_46_S = "Indonesian_1974_UTM_Zone_46S"
    INDONESIAN_1974_UTM_ZONE_47_N = "Indonesian_1974_UTM_Zone_47N"
    INDONESIAN_1974_UTM_ZONE_47_S = "Indonesian_1974_UTM_Zone_47S"
    INDONESIAN_1974_UTM_ZONE_48_N = "Indonesian_1974_UTM_Zone_48N"
    INDONESIAN_1974_UTM_ZONE_48_S = "Indonesian_1974_UTM_Zone_48S"
    INDONESIAN_1974_UTM_ZONE_49_N = "Indonesian_1974_UTM_Zone_49N"
    INDONESIAN_1974_UTM_ZONE_49_S = "Indonesian_1974_UTM_Zone_49S"
    INDONESIAN_1974_UTM_ZONE_50_N = "Indonesian_1974_UTM_Zone_50N"
    INDONESIAN_1974_UTM_ZONE_50_S = "Indonesian_1974_UTM_Zone_50S"
    INDONESIAN_1974_UTM_ZONE_51_N = "Indonesian_1974_UTM_Zone_51N"
    INDONESIAN_1974_UTM_ZONE_51_S = "Indonesian_1974_UTM_Zone_51S"
    INDONESIAN_1974_UTM_ZONE_52_N = "Indonesian_1974_UTM_Zone_52N"
    INDONESIAN_1974_UTM_ZONE_52_S = "Indonesian_1974_UTM_Zone_52S"
    INDONESIAN_1974_UTM_ZONE_53_N = "Indonesian_1974_UTM_Zone_53N"
    INDONESIAN_1974_UTM_ZONE_53_S = "Indonesian_1974_UTM_Zone_53S"
    INDONESIAN_1974_UTM_ZONE_54_S = "Indonesian_1974_UTM_Zone_54S"
    IRENET95_UTM_ZONE_29_N = "IRENET95_UTM_Zone_29N"
    KERTAU_UTM_ZONE_47_N = "Kertau_UTM_Zone_47N"
    KERTAU_UTM_ZONE_48_N = "Kertau_UTM_Zone_48N"
    LA_CANOA_UTM_ZONE_18_N = "La_Canoa_UTM_Zone_18N"
    LA_CANOA_UTM_ZONE_19_N = "La_Canoa_UTM_Zone_19N"
    LA_CANOA_UTM_ZONE_20_N = "La_Canoa_UTM_Zone_20N"
    LA_CANOA_UTM_ZONE_21_N = "La_Canoa_UTM_Zone_21N"
    LOCODJO_1965_UTM_ZONE_29_N = "Locodjo_1965_UTM_Zone_29N"
    LOCODJO_1965_UTM_ZONE_30_N = "Locodjo_1965_UTM_Zone_30N"
    LOME_UTM_ZONE_31_N = "Lome_UTM_Zone_31N"
    MPORALOKO_UTM_ZONE_32_N = "Mporaloko_UTM_Zone_32N"
    MPORALOKO_UTM_ZONE_32_S = "Mporaloko_UTM_Zone_32S"
    MALONGO_1987_UTM_ZONE_32_S = "Malongo_1987_UTM_Zone_32S"
    MASSAWA_UTM_ZONE_37_N = "Massawa_UTM_Zone_37N"
    MHAST_UTM_ZONE_32_S = "Mhast_UTM_Zone_32S"
    MINNA_UTM_ZONE_31_N = "Minna_UTM_Zone_31N"
    MINNA_UTM_ZONE_32_N = "Minna_UTM_Zone_32N"
    MOZNET_UTM_ZONE_36_S = "Moznet_UTM_Zone_36S"
    MOZNET_UTM_ZONE_37_S = "Moznet_UTM_Zone_37S"
    NAD_1927_BLM_ZONE_14_N = "NAD_1927_BLM_Zone_14N"
    NAD_1927_BLM_ZONE_15_N = "NAD_1927_BLM_Zone_15N"
    NAD_1927_BLM_ZONE_16_N = "NAD_1927_BLM_Zone_16N"
    NAD_1927_BLM_ZONE_17_N = "NAD_1927_BLM_Zone_17N"
    NAHRWAN_1967_UTM_ZONE_38_N = "Nahrwan_1967_UTM_Zone_38N"
    NAHRWAN_1967_UTM_ZONE_39_N = "Nahrwan_1967_UTM_Zone_39N"
    NAHRWAN_1967_UTM_ZONE_40_N = "Nahrwan_1967_UTM_Zone_40N"
    NAPARIMA_1955_UTM_ZONE_20_N = "Naparima_1955_UTM_Zone_20N"
    NAPARIMA_1972_UTM_ZONE_20_N = "Naparima_1972_UTM_Zone_20N"
    NGN_UTM_ZONE_38_N = "NGN_UTM_Zone_38N"
    NGN_UTM_ZONE_39_N = "NGN_UTM_Zone_39N"
    NGO_1948_UTM_ZONE_32_N = "NGO_1948_UTM_Zone_32N"
    NGO_1948_UTM_ZONE_33_N = "NGO_1948_UTM_Zone_33N"
    NGO_1948_UTM_ZONE_34_N = "NGO_1948_UTM_Zone_34N"
    NGO_1948_UTM_ZONE_35_N = "NGO_1948_UTM_Zone_35N"
    NORD_SAHARA_1959_UTM_ZONE_29_N = "Nord_Sahara_1959_UTM_Zone_29N"
    NORD_SAHARA_1959_UTM_ZONE_30_N = "Nord_Sahara_1959_UTM_Zone_30N"
    NORD_SAHARA_1959_UTM_ZONE_31_N = "Nord_Sahara_1959_UTM_Zone_31N"
    NORD_SAHARA_1959_UTM_ZONE_32_N = "Nord_Sahara_1959_UTM_Zone_32N"
    OBSERV_METEOROLOGICO_1939_UTM_ZONE_25_N = "Observ_Meteorologico_1939_UTM_Zone_25N"
    OLD_HAWAIIAN_UTM_ZONE_4_N = "Old_Hawaiian_UTM_Zone_4N"
    OLD_HAWAIIAN_UTM_ZONE_5_N = "Old_Hawaiian_UTM_Zone_5N"
    PDO_1993_UTM_ZONE_39_N = "PDO_1993_UTM_Zone_39N"
    PDO_1993_UTM_ZONE_40_N = "PDO_1993_UTM_Zone_40N"
    POINTE_NOIRE_UTM_ZONE_32_S = "Pointe_Noire_UTM_Zone_32S"
    PORTO_SANTO_1936_UTM_ZONE_28_N = "Porto_Santo_1936_UTM_Zone_28N"
    PSAD_1956_UTM_ZONE_17_S = "PSAD_1956_UTM_Zone_17S"
    PSAD_1956_UTM_ZONE_18_N = "PSAD_1956_UTM_Zone_18N"
    PSAD_1956_UTM_ZONE_18_S = "PSAD_1956_UTM_Zone_18S"
    PSAD_1956_UTM_ZONE_19_N = "PSAD_1956_UTM_Zone_19N"
    PSAD_1956_UTM_ZONE_19_S = "PSAD_1956_UTM_Zone_19S"
    PSAD_1956_UTM_ZONE_20_N = "PSAD_1956_UTM_Zone_20N"
    PSAD_1956_UTM_ZONE_20_S = "PSAD_1956_UTM_Zone_20S"
    PSAD_1956_UTM_ZONE_21_N = "PSAD_1956_UTM_Zone_21N"
    PSAD_1956_UTM_ZONE_22_S = "PSAD_1956_UTM_Zone_22S"
    PUERTO_RICO_UTM_ZONE_20_N = "Puerto_Rico_UTM_Zone_20N"
    SAMBOJA_UTM_ZONE_50_S = "Samboja_UTM_Zone_50S"
    SAO_BRAZ_UTM_ZONE_26_N = "Sao_Braz_UTM_Zone_26N"
    SAPPER_HILL_1943_UTM_ZONE_20_S = "Sapper_Hill_1943_UTM_Zone_20S"
    SAPPER_HILL_1943_UTM_ZONE_21_S = "Sapper_Hill_1943_UTM_Zone_21S"
    SCHWARZECK_UTM_ZONE_33_S = "Schwarzeck_UTM_Zone_33S"
    SELVAGEM_GRANDE_1938_UTM_ZONE_28_N = "Selvagem_Grande_1938_UTM_Zone_28N"
    SIERRA_LEONE_1968_UTM_ZONE_28_N = "Sierra_Leone_1968_UTM_Zone_28N"
    SIERRA_LEONE_1968_UTM_ZONE_29_N = "Sierra_Leone_1968_UTM_Zone_29N"
    SIRGAS_UTM_ZONE_17_N = "SIRGAS_UTM_Zone_17N"
    SIRGAS_UTM_ZONE_17_S = "SIRGAS_UTM_Zone_17S"
    SIRGAS_UTM_ZONE_18_N = "SIRGAS_UTM_Zone_18N"
    SIRGAS_UTM_ZONE_18_S = "SIRGAS_UTM_Zone_18S"
    SIRGAS_UTM_ZONE_19_N = "SIRGAS_UTM_Zone_19N"
    SIRGAS_UTM_ZONE_19_S = "SIRGAS_UTM_Zone_19S"
    SIRGAS_UTM_ZONE_20_N = "SIRGAS_UTM_Zone_20N"
    SIRGAS_UTM_ZONE_20_S = "SIRGAS_UTM_Zone_20S"
    SIRGAS_UTM_ZONE_21_N = "SIRGAS_UTM_Zone_21N"
    SIRGAS_UTM_ZONE_21_S = "SIRGAS_UTM_Zone_21S"
    SIRGAS_UTM_ZONE_22_N = "SIRGAS_UTM_Zone_22N"
    SIRGAS_UTM_ZONE_22_S = "SIRGAS_UTM_Zone_22S"
    SIRGAS_UTM_ZONE_23_S = "SIRGAS_UTM_Zone_23S"
    SIRGAS_UTM_ZONE_24_S = "SIRGAS_UTM_Zone_24S"
    SIRGAS_UTM_ZONE_25_S = "SIRGAS_UTM_Zone_25S"
    SAD_1969_UTM_ZONE_17_S = "SAD_1969_UTM_Zone_17S"
    SAD_1969_UTM_ZONE_18_N = "SAD_1969_UTM_Zone_18N"
    SAD_1969_UTM_ZONE_18_S = "SAD_1969_UTM_Zone_18S"
    SAD_1969_UTM_ZONE_19_N = "SAD_1969_UTM_Zone_19N"
    SAD_1969_UTM_ZONE_19_S = "SAD_1969_UTM_Zone_19S"
    SAD_1969_UTM_ZONE_20_N = "SAD_1969_UTM_Zone_20N"
    SAD_1969_UTM_ZONE_20_S = "SAD_1969_UTM_Zone_20S"
    SAD_1969_UTM_ZONE_21_N = "SAD_1969_UTM_Zone_21N"
    SAD_1969_UTM_ZONE_21_S = "SAD_1969_UTM_Zone_21S"
    SAD_1969_UTM_ZONE_22_N = "SAD_1969_UTM_Zone_22N"
    SAD_1969_UTM_ZONE_22_S = "SAD_1969_UTM_Zone_22S"
    SAD_1969_UTM_ZONE_23_S = "SAD_1969_UTM_Zone_23S"
    SAD_1969_UTM_ZONE_24_S = "SAD_1969_UTM_Zone_24S"
    SAD_1969_UTM_ZONE_25_S = "SAD_1969_UTM_Zone_25S"
    SUDAN_UTM_ZONE_35_N = "Sudan_UTM_Zone_35N"
    SUDAN_UTM_ZONE_36_N = "Sudan_UTM_Zone_36N"
    TANANARIVE_1925_UTM_ZONE_38_S = "Tananarive_1925_UTM_Zone_38S"
    TANANARIVE_1925_UTM_ZONE_39_S = "Tananarive_1925_UTM_Zone_39S"
    TETE_UTM_ZONE_36_S = "Tete_UTM_Zone_36S"
    TETE_UTM_ZONE_37_S = "Tete_UTM_Zone_37S"
    TIMBALAI_1948_UTM_ZONE_49_N = "Timbalai_1948_UTM_Zone_49N"
    TIMBALAI_1948_UTM_ZONE_50_N = "Timbalai_1948_UTM_Zone_50N"
    TOKYO_UTM_ZONE_51_N = "Tokyo_UTM_Zone_51N"
    TOKYO_UTM_ZONE_52_N = "Tokyo_UTM_Zone_52N"
    TOKYO_UTM_ZONE_53_N = "Tokyo_UTM_Zone_53N"
    TOKYO_UTM_ZONE_54_N = "Tokyo_UTM_Zone_54N"
    TOKYO_UTM_ZONE_55_N = "Tokyo_UTM_Zone_55N"
    TOKYO_UTM_ZONE_56_N = "Tokyo_UTM_Zone_56N"
    TC_1948_UTM_ZONE_39_N = "TC_1948_UTM_Zone_39N"
    TC_1948_UTM_ZONE_40_N = "TC_1948_UTM_Zone_40N"
    YEMEN_NGN_1996_UTM_ZONE_38_N = "Yemen_NGN_1996_UTM_Zone_38N"
    YEMEN_NGN_1996_UTM_ZONE_39_N = "Yemen_NGN_1996_UTM_Zone_39N"
    YOFF_1972_UTM_ZONE_28_N = "Yoff_1972_UTM_Zone_28N"
    ZANDERIJ_1972_UTM_ZONE_21_N = "Zanderij_1972_UTM_Zone_21N"
    WGS_1972_UTM_ZONE_10_N = "WGS_1972_UTM_Zone_10N"
    WGS_1972_UTM_ZONE_10_S = "WGS_1972_UTM_Zone_10S"
    WGS_1972_UTM_ZONE_11_N = "WGS_1972_UTM_Zone_11N"
    WGS_1972_UTM_ZONE_11_S = "WGS_1972_UTM_Zone_11S"
    WGS_1972_UTM_ZONE_12_N = "WGS_1972_UTM_Zone_12N"
    WGS_1972_UTM_ZONE_12_S = "WGS_1972_UTM_Zone_12S"
    WGS_1972_UTM_ZONE_13_N = "WGS_1972_UTM_Zone_13N"
    WGS_1972_UTM_ZONE_13_S = "WGS_1972_UTM_Zone_13S"
    WGS_1972_UTM_ZONE_14_N = "WGS_1972_UTM_Zone_14N"
    WGS_1972_UTM_ZONE_14_S = "WGS_1972_UTM_Zone_14S"
    WGS_1972_UTM_ZONE_15_N = "WGS_1972_UTM_Zone_15N"
    WGS_1972_UTM_ZONE_15_S = "WGS_1972_UTM_Zone_15S"
    WGS_1972_UTM_ZONE_16_N = "WGS_1972_UTM_Zone_16N"
    WGS_1972_UTM_ZONE_16_S = "WGS_1972_UTM_Zone_16S"
    WGS_1972_UTM_ZONE_17_N = "WGS_1972_UTM_Zone_17N"
    WGS_1972_UTM_ZONE_17_S = "WGS_1972_UTM_Zone_17S"
    WGS_1972_UTM_ZONE_18_N = "WGS_1972_UTM_Zone_18N"
    WGS_1972_UTM_ZONE_18_S = "WGS_1972_UTM_Zone_18S"
    WGS_1972_UTM_ZONE_19_N = "WGS_1972_UTM_Zone_19N"
    WGS_1972_UTM_ZONE_19_S = "WGS_1972_UTM_Zone_19S"
    WGS_1972_UTM_ZONE_1_N = "WGS_1972_UTM_Zone_1N"
    WGS_1972_UTM_ZONE_1_S = "WGS_1972_UTM_Zone_1S"
    WGS_1972_UTM_ZONE_20_N = "WGS_1972_UTM_Zone_20N"
    WGS_1972_UTM_ZONE_20_S = "WGS_1972_UTM_Zone_20S"
    WGS_1972_UTM_ZONE_21_N = "WGS_1972_UTM_Zone_21N"
    WGS_1972_UTM_ZONE_21_S = "WGS_1972_UTM_Zone_21S"
    WGS_1972_UTM_ZONE_22_N = "WGS_1972_UTM_Zone_22N"
    WGS_1972_UTM_ZONE_22_S = "WGS_1972_UTM_Zone_22S"
    WGS_1972_UTM_ZONE_23_N = "WGS_1972_UTM_Zone_23N"
    WGS_1972_UTM_ZONE_23_S = "WGS_1972_UTM_Zone_23S"
    WGS_1972_UTM_ZONE_24_N = "WGS_1972_UTM_Zone_24N"
    WGS_1972_UTM_ZONE_24_S = "WGS_1972_UTM_Zone_24S"
    WGS_1972_UTM_ZONE_25_N = "WGS_1972_UTM_Zone_25N"
    WGS_1972_UTM_ZONE_25_S = "WGS_1972_UTM_Zone_25S"
    WGS_1972_UTM_ZONE_26_N = "WGS_1972_UTM_Zone_26N"
    WGS_1972_UTM_ZONE_26_S = "WGS_1972_UTM_Zone_26S"
    WGS_1972_UTM_ZONE_27_N = "WGS_1972_UTM_Zone_27N"
    WGS_1972_UTM_ZONE_27_S = "WGS_1972_UTM_Zone_27S"
    WGS_1972_UTM_ZONE_28_N = "WGS_1972_UTM_Zone_28N"
    WGS_1972_UTM_ZONE_28_S = "WGS_1972_UTM_Zone_28S"
    WGS_1972_UTM_ZONE_29_N = "WGS_1972_UTM_Zone_29N"
    WGS_1972_UTM_ZONE_29_S = "WGS_1972_UTM_Zone_29S"
    WGS_1972_UTM_ZONE_2_N = "WGS_1972_UTM_Zone_2N"
    WGS_1972_UTM_ZONE_2_S = "WGS_1972_UTM_Zone_2S"
    WGS_1972_UTM_ZONE_30_N = "WGS_1972_UTM_Zone_30N"
    WGS_1972_UTM_ZONE_30_S = "WGS_1972_UTM_Zone_30S"
    WGS_1972_UTM_ZONE_31_N = "WGS_1972_UTM_Zone_31N"
    WGS_1972_UTM_ZONE_31_S = "WGS_1972_UTM_Zone_31S"
    WGS_1972_UTM_ZONE_32_N = "WGS_1972_UTM_Zone_32N"
    WGS_1972_UTM_ZONE_32_S = "WGS_1972_UTM_Zone_32S"
    WGS_1972_UTM_ZONE_33_N = "WGS_1972_UTM_Zone_33N"
    WGS_1972_UTM_ZONE_33_S = "WGS_1972_UTM_Zone_33S"
    WGS_1972_UTM_ZONE_34_N = "WGS_1972_UTM_Zone_34N"
    WGS_1972_UTM_ZONE_34_S = "WGS_1972_UTM_Zone_34S"
    WGS_1972_UTM_ZONE_35_N = "WGS_1972_UTM_Zone_35N"
    WGS_1972_UTM_ZONE_35_S = "WGS_1972_UTM_Zone_35S"
    WGS_1972_UTM_ZONE_36_N = "WGS_1972_UTM_Zone_36N"
    WGS_1972_UTM_ZONE_36_S = "WGS_1972_UTM_Zone_36S"
    WGS_1972_UTM_ZONE_37_N = "WGS_1972_UTM_Zone_37N"
    WGS_1972_UTM_ZONE_37_S = "WGS_1972_UTM_Zone_37S"
    WGS_1972_UTM_ZONE_38_N = "WGS_1972_UTM_Zone_38N"
    WGS_1972_UTM_ZONE_38_S = "WGS_1972_UTM_Zone_38S"
    WGS_1972_UTM_ZONE_39_N = "WGS_1972_UTM_Zone_39N"
    WGS_1972_UTM_ZONE_39_S = "WGS_1972_UTM_Zone_39S"
    WGS_1972_UTM_ZONE_3_N = "WGS_1972_UTM_Zone_3N"
    WGS_1972_UTM_ZONE_3_S = "WGS_1972_UTM_Zone_3S"
    WGS_1972_UTM_ZONE_40_N = "WGS_1972_UTM_Zone_40N"
    WGS_1972_UTM_ZONE_40_S = "WGS_1972_UTM_Zone_40S"
    WGS_1972_UTM_ZONE_41_N = "WGS_1972_UTM_Zone_41N"
    WGS_1972_UTM_ZONE_41_S = "WGS_1972_UTM_Zone_41S"
    WGS_1972_UTM_ZONE_42_N = "WGS_1972_UTM_Zone_42N"
    WGS_1972_UTM_ZONE_42_S = "WGS_1972_UTM_Zone_42S"
    WGS_1972_UTM_ZONE_43_N = "WGS_1972_UTM_Zone_43N"
    WGS_1972_UTM_ZONE_43_S = "WGS_1972_UTM_Zone_43S"
    WGS_1972_UTM_ZONE_44_N = "WGS_1972_UTM_Zone_44N"
    WGS_1972_UTM_ZONE_44_S = "WGS_1972_UTM_Zone_44S"
    WGS_1972_UTM_ZONE_45_N = "WGS_1972_UTM_Zone_45N"
    WGS_1972_UTM_ZONE_45_S = "WGS_1972_UTM_Zone_45S"
    WGS_1972_UTM_ZONE_46_N = "WGS_1972_UTM_Zone_46N"
    WGS_1972_UTM_ZONE_46_S = "WGS_1972_UTM_Zone_46S"
    WGS_1972_UTM_ZONE_47_N = "WGS_1972_UTM_Zone_47N"
    WGS_1972_UTM_ZONE_47_S = "WGS_1972_UTM_Zone_47S"
    WGS_1972_UTM_ZONE_48_N = "WGS_1972_UTM_Zone_48N"
    WGS_1972_UTM_ZONE_48_S = "WGS_1972_UTM_Zone_48S"
    WGS_1972_UTM_ZONE_49_N = "WGS_1972_UTM_Zone_49N"
    WGS_1972_UTM_ZONE_49_S = "WGS_1972_UTM_Zone_49S"
    WGS_1972_UTM_ZONE_4_N = "WGS_1972_UTM_Zone_4N"
    WGS_1972_UTM_ZONE_4_S = "WGS_1972_UTM_Zone_4S"
    WGS_1972_UTM_ZONE_50_N = "WGS_1972_UTM_Zone_50N"
    WGS_1972_UTM_ZONE_50_S = "WGS_1972_UTM_Zone_50S"
    WGS_1972_UTM_ZONE_51_N = "WGS_1972_UTM_Zone_51N"
    WGS_1972_UTM_ZONE_51_S = "WGS_1972_UTM_Zone_51S"
    WGS_1972_UTM_ZONE_52_N = "WGS_1972_UTM_Zone_52N"
    WGS_1972_UTM_ZONE_52_S = "WGS_1972_UTM_Zone_52S"
    WGS_1972_UTM_ZONE_53_N = "WGS_1972_UTM_Zone_53N"
    WGS_1972_UTM_ZONE_53_S = "WGS_1972_UTM_Zone_53S"
    WGS_1972_UTM_ZONE_54_N = "WGS_1972_UTM_Zone_54N"
    WGS_1972_UTM_ZONE_54_S = "WGS_1972_UTM_Zone_54S"
    WGS_1972_UTM_ZONE_55_N = "WGS_1972_UTM_Zone_55N"
    WGS_1972_UTM_ZONE_55_S = "WGS_1972_UTM_Zone_55S"
    WGS_1972_UTM_ZONE_56_N = "WGS_1972_UTM_Zone_56N"
    WGS_1972_UTM_ZONE_56_S = "WGS_1972_UTM_Zone_56S"
    WGS_1972_UTM_ZONE_57_N = "WGS_1972_UTM_Zone_57N"
    WGS_1972_UTM_ZONE_57_S = "WGS_1972_UTM_Zone_57S"
    WGS_1972_UTM_ZONE_58_N = "WGS_1972_UTM_Zone_58N"
    WGS_1972_UTM_ZONE_58_S = "WGS_1972_UTM_Zone_58S"
    WGS_1972_UTM_ZONE_59_N = "WGS_1972_UTM_Zone_59N"
    WGS_1972_UTM_ZONE_59_S = "WGS_1972_UTM_Zone_59S"
    WGS_1972_UTM_ZONE_5_N = "WGS_1972_UTM_Zone_5N"
    WGS_1972_UTM_ZONE_5_S = "WGS_1972_UTM_Zone_5S"
    WGS_1972_UTM_ZONE_60_N = "WGS_1972_UTM_Zone_60N"
    WGS_1972_UTM_ZONE_60_S = "WGS_1972_UTM_Zone_60S"
    WGS_1972_UTM_ZONE_6_N = "WGS_1972_UTM_Zone_6N"
    WGS_1972_UTM_ZONE_6_S = "WGS_1972_UTM_Zone_6S"
    WGS_1972_UTM_ZONE_7_N = "WGS_1972_UTM_Zone_7N"
    WGS_1972_UTM_ZONE_7_S = "WGS_1972_UTM_Zone_7S"
    WGS_1972_UTM_ZONE_8_N = "WGS_1972_UTM_Zone_8N"
    WGS_1972_UTM_ZONE_8_S = "WGS_1972_UTM_Zone_8S"
    WGS_1972_UTM_ZONE_9_N = "WGS_1972_UTM_Zone_9N"
    WGS_1972_UTM_ZONE_9_S = "WGS_1972_UTM_Zone_9S"
    WGS_1984_UTM_ZONE_10_N = "WGS_1984_UTM_Zone_10N"
    WGS_1984_UTM_ZONE_10_S = "WGS_1984_UTM_Zone_10S"
    WGS_1984_UTM_ZONE_11_N = "WGS_1984_UTM_Zone_11N"
    WGS_1984_UTM_ZONE_11_S = "WGS_1984_UTM_Zone_11S"
    WGS_1984_UTM_ZONE_12_N = "WGS_1984_UTM_Zone_12N"
    WGS_1984_UTM_ZONE_12_S = "WGS_1984_UTM_Zone_12S"
    WGS_1984_UTM_ZONE_13_N = "WGS_1984_UTM_Zone_13N"
    WGS_1984_UTM_ZONE_13_S = "WGS_1984_UTM_Zone_13S"
    WGS_1984_UTM_ZONE_14_N = "WGS_1984_UTM_Zone_14N"
    WGS_1984_UTM_ZONE_14_S = "WGS_1984_UTM_Zone_14S"
    WGS_1984_UTM_ZONE_15_N = "WGS_1984_UTM_Zone_15N"
    WGS_1984_UTM_ZONE_15_S = "WGS_1984_UTM_Zone_15S"
    WGS_1984_UTM_ZONE_16_N = "WGS_1984_UTM_Zone_16N"
    WGS_1984_UTM_ZONE_16_S = "WGS_1984_UTM_Zone_16S"
    WGS_1984_UTM_ZONE_17_N = "WGS_1984_UTM_Zone_17N"
    WGS_1984_UTM_ZONE_17_S = "WGS_1984_UTM_Zone_17S"
    WGS_1984_UTM_ZONE_18_N = "WGS_1984_UTM_Zone_18N"
    WGS_1984_UTM_ZONE_18_S = "WGS_1984_UTM_Zone_18S"
    WGS_1984_UTM_ZONE_19_N = "WGS_1984_UTM_Zone_19N"
    WGS_1984_UTM_ZONE_19_S = "WGS_1984_UTM_Zone_19S"
    WGS_1984_UTM_ZONE_1_N = "WGS_1984_UTM_Zone_1N"
    WGS_1984_UTM_ZONE_1_S = "WGS_1984_UTM_Zone_1S"
    WGS_1984_UTM_ZONE_20_N = "WGS_1984_UTM_Zone_20N"
    WGS_1984_UTM_ZONE_20_S = "WGS_1984_UTM_Zone_20S"
    WGS_1984_UTM_ZONE_21_N = "WGS_1984_UTM_Zone_21N"
    WGS_1984_UTM_ZONE_21_S = "WGS_1984_UTM_Zone_21S"
    WGS_1984_UTM_ZONE_22_N = "WGS_1984_UTM_Zone_22N"
    WGS_1984_UTM_ZONE_22_S = "WGS_1984_UTM_Zone_22S"
    WGS_1984_UTM_ZONE_23_N = "WGS_1984_UTM_Zone_23N"
    WGS_1984_UTM_ZONE_23_S = "WGS_1984_UTM_Zone_23S"
    WGS_1984_UTM_ZONE_24_N = "WGS_1984_UTM_Zone_24N"
    WGS_1984_UTM_ZONE_24_S = "WGS_1984_UTM_Zone_24S"
    WGS_1984_UTM_ZONE_25_N = "WGS_1984_UTM_Zone_25N"
    WGS_1984_UTM_ZONE_25_S = "WGS_1984_UTM_Zone_25S"
    WGS_1984_UTM_ZONE_26_N = "WGS_1984_UTM_Zone_26N"
    WGS_1984_UTM_ZONE_26_S = "WGS_1984_UTM_Zone_26S"
    WGS_1984_UTM_ZONE_27_N = "WGS_1984_UTM_Zone_27N"
    WGS_1984_UTM_ZONE_27_S = "WGS_1984_UTM_Zone_27S"
    WGS_1984_UTM_ZONE_28_N = "WGS_1984_UTM_Zone_28N"
    WGS_1984_UTM_ZONE_28_S = "WGS_1984_UTM_Zone_28S"
    WGS_1984_UTM_ZONE_29_N = "WGS_1984_UTM_Zone_29N"
    WGS_1984_UTM_ZONE_29_S = "WGS_1984_UTM_Zone_29S"
    WGS_1984_UTM_ZONE_2_N = "WGS_1984_UTM_Zone_2N"
    WGS_1984_UTM_ZONE_2_S = "WGS_1984_UTM_Zone_2S"
    WGS_1984_UTM_ZONE_30_N = "WGS_1984_UTM_Zone_30N"
    WGS_1984_UTM_ZONE_30_S = "WGS_1984_UTM_Zone_30S"
    WGS_1984_UTM_ZONE_31_N = "WGS_1984_UTM_Zone_31N"
    WGS_1984_UTM_ZONE_31_S = "WGS_1984_UTM_Zone_31S"
    WGS_1984_UTM_ZONE_32_N = "WGS_1984_UTM_Zone_32N"
    WGS_1984_UTM_ZONE_32_S = "WGS_1984_UTM_Zone_32S"
    WGS_1984_UTM_ZONE_33_N = "WGS_1984_UTM_Zone_33N"
    WGS_1984_UTM_ZONE_33_S = "WGS_1984_UTM_Zone_33S"
    WGS_1984_UTM_ZONE_34_N = "WGS_1984_UTM_Zone_34N"
    WGS_1984_UTM_ZONE_34_S = "WGS_1984_UTM_Zone_34S"
    WGS_1984_UTM_ZONE_35_N = "WGS_1984_UTM_Zone_35N"
    WGS_1984_UTM_ZONE_35_S = "WGS_1984_UTM_Zone_35S"
    WGS_1984_UTM_ZONE_36_N = "WGS_1984_UTM_Zone_36N"
    WGS_1984_UTM_ZONE_36_S = "WGS_1984_UTM_Zone_36S"
    WGS_1984_UTM_ZONE_37_N = "WGS_1984_UTM_Zone_37N"
    WGS_1984_UTM_ZONE_37_S = "WGS_1984_UTM_Zone_37S"
    WGS_1984_UTM_ZONE_38_N = "WGS_1984_UTM_Zone_38N"
    WGS_1984_UTM_ZONE_38_S = "WGS_1984_UTM_Zone_38S"
    WGS_1984_UTM_ZONE_39_N = "WGS_1984_UTM_Zone_39N"
    WGS_1984_UTM_ZONE_39_S = "WGS_1984_UTM_Zone_39S"
    WGS_1984_UTM_ZONE_3_N = "WGS_1984_UTM_Zone_3N"
    WGS_1984_UTM_ZONE_3_S = "WGS_1984_UTM_Zone_3S"
    WGS_1984_UTM_ZONE_40_N = "WGS_1984_UTM_Zone_40N"
    WGS_1984_UTM_ZONE_40_S = "WGS_1984_UTM_Zone_40S"
    WGS_1984_UTM_ZONE_41_N = "WGS_1984_UTM_Zone_41N"
    WGS_1984_UTM_ZONE_41_S = "WGS_1984_UTM_Zone_41S"
    WGS_1984_UTM_ZONE_42_N = "WGS_1984_UTM_Zone_42N"
    WGS_1984_UTM_ZONE_42_S = "WGS_1984_UTM_Zone_42S"
    WGS_1984_UTM_ZONE_43_N = "WGS_1984_UTM_Zone_43N"
    WGS_1984_UTM_ZONE_43_S = "WGS_1984_UTM_Zone_43S"
    WGS_1984_UTM_ZONE_44_N = "WGS_1984_UTM_Zone_44N"
    WGS_1984_UTM_ZONE_44_S = "WGS_1984_UTM_Zone_44S"
    WGS_1984_UTM_ZONE_45_N = "WGS_1984_UTM_Zone_45N"
    WGS_1984_UTM_ZONE_45_S = "WGS_1984_UTM_Zone_45S"
    WGS_1984_UTM_ZONE_46_N = "WGS_1984_UTM_Zone_46N"
    WGS_1984_UTM_ZONE_46_S = "WGS_1984_UTM_Zone_46S"
    WGS_1984_UTM_ZONE_47_N = "WGS_1984_UTM_Zone_47N"
    WGS_1984_UTM_ZONE_47_S = "WGS_1984_UTM_Zone_47S"
    WGS_1984_UTM_ZONE_48_N = "WGS_1984_UTM_Zone_48N"
    WGS_1984_UTM_ZONE_48_S = "WGS_1984_UTM_Zone_48S"
    WGS_1984_UTM_ZONE_49_N = "WGS_1984_UTM_Zone_49N"
    WGS_1984_UTM_ZONE_49_S = "WGS_1984_UTM_Zone_49S"
    WGS_1984_UTM_ZONE_4_N = "WGS_1984_UTM_Zone_4N"
    WGS_1984_UTM_ZONE_4_S = "WGS_1984_UTM_Zone_4S"
    WGS_1984_UTM_ZONE_50_N = "WGS_1984_UTM_Zone_50N"
    WGS_1984_UTM_ZONE_50_S = "WGS_1984_UTM_Zone_50S"
    WGS_1984_UTM_ZONE_51_N = "WGS_1984_UTM_Zone_51N"
    WGS_1984_UTM_ZONE_51_S = "WGS_1984_UTM_Zone_51S"
    WGS_1984_UTM_ZONE_52_N = "WGS_1984_UTM_Zone_52N"
    WGS_1984_UTM_ZONE_52_S = "WGS_1984_UTM_Zone_52S"
    WGS_1984_UTM_ZONE_53_N = "WGS_1984_UTM_Zone_53N"
    WGS_1984_UTM_ZONE_53_S = "WGS_1984_UTM_Zone_53S"
    WGS_1984_UTM_ZONE_54_N = "WGS_1984_UTM_Zone_54N"
    WGS_1984_UTM_ZONE_54_S = "WGS_1984_UTM_Zone_54S"
    WGS_1984_UTM_ZONE_55_N = "WGS_1984_UTM_Zone_55N"
    WGS_1984_UTM_ZONE_55_S = "WGS_1984_UTM_Zone_55S"
    WGS_1984_UTM_ZONE_56_N = "WGS_1984_UTM_Zone_56N"
    WGS_1984_UTM_ZONE_56_S = "WGS_1984_UTM_Zone_56S"
    WGS_1984_UTM_ZONE_57_N = "WGS_1984_UTM_Zone_57N"
    WGS_1984_UTM_ZONE_57_S = "WGS_1984_UTM_Zone_57S"
    WGS_1984_UTM_ZONE_58_N = "WGS_1984_UTM_Zone_58N"
    WGS_1984_UTM_ZONE_58_S = "WGS_1984_UTM_Zone_58S"
    WGS_1984_UTM_ZONE_59_N = "WGS_1984_UTM_Zone_59N"
    WGS_1984_UTM_ZONE_59_S = "WGS_1984_UTM_Zone_59S"
    WGS_1984_UTM_ZONE_5_N = "WGS_1984_UTM_Zone_5N"
    WGS_1984_UTM_ZONE_5_S = "WGS_1984_UTM_Zone_5S"
    WGS_1984_UTM_ZONE_60_N = "WGS_1984_UTM_Zone_60N"
    WGS_1984_UTM_ZONE_60_S = "WGS_1984_UTM_Zone_60S"
    WGS_1984_UTM_ZONE_6_N = "WGS_1984_UTM_Zone_6N"
    WGS_1984_UTM_ZONE_6_S = "WGS_1984_UTM_Zone_6S"
    WGS_1984_UTM_ZONE_7_N = "WGS_1984_UTM_Zone_7N"
    WGS_1984_UTM_ZONE_7_S = "WGS_1984_UTM_Zone_7S"
    WGS_1984_UTM_ZONE_8_N = "WGS_1984_UTM_Zone_8N"
    WGS_1984_UTM_ZONE_8_S = "WGS_1984_UTM_Zone_8S"
    WGS_1984_UTM_ZONE_9_N = "WGS_1984_UTM_Zone_9N"
    WGS_1984_UTM_ZONE_9_S = "WGS_1984_UTM_Zone_9S"
    WORLD_AITOFF = "World_Aitoff"
    WORLD_BEHRMANN = "World_Behrmann"
    WORLD_BONNE = "World_Bonne"
    WORLD_CRASTER_PARABOLIC = "World_Craster_Parabolic"
    WORLD_CYLINDRICAL_EQUAL_AREA = "World_Cylindrical_Equal_Area"
    WORLD_ECKERT_I = "World_Eckert_I"
    WORLD_ECKERT_II = "World_Eckert_II"
    WORLD_ECKERT_III = "World_Eckert_III"
    WORLD_ECKERT_IV = "World_Eckert_IV"
    WORLD_ECKERT_V = "World_Eckert_V"
    WORLD_ECKERT_VI = "World_Eckert_VI"
    WORLD_EQUIDISTANT_CONIC = "World_Equidistant_Conic"
    WORLD_EQUIDISTANT_CYLINDRICAL = "World_Equidistant_Cylindrical"
    WORLD_FLAT_POLAR_QUARTIC = "World_Flat_Polar_Quartic"
    WORLD_GALL_STEREOGRAPHIC = "World_Gall_Stereographic"
    WORLD_HAMMER_AITOFF = "World_Hammer_Aitoff"
    WORLD_LOXIMUTHAL = "World_Loximuthal"
    WORLD_MERCATOR = "World_Mercator"
    WORLD_MILLER_CYLINDRICAL = "World_Miller_Cylindrical"
    WORLD_MOLLWEIDE = "World_Mollweide"
    WORLD_PLATE_CARREE = "World_Plate_Carree"
    WORLD_POLYCONIC = "World_Polyconic"
    WORLD_QUARTIC_AUTHALIC = "World_Quartic_Authalic"
    WORLD_ROBINSON = "World_Robinson"
    WORLD_SINUSOIDAL = "World_Sinusoidal"
    SPHERE_AITOFF = "Sphere_Aitoff"
    SPHERE_BEHRMANN = "Sphere_Behrmann"
    SPHERE_BONNE = "Sphere_Bonne"
    SPHERE_CRASTER_PARABOLIC = "Sphere_Craster_Parabolic"
    SPHERE_CYLINDRICAL_EQUAL_AREA = "Sphere_Cylindrical_Equal_Area"
    SPHERE_ECKERT_I = "Sphere_Eckert_I"
    SPHERE_ECKERT_II = "Sphere_Eckert_II"
    SPHERE_ECKERT_III = "Sphere_Eckert_III"
    SPHERE_ECKERT_IV = "Sphere_Eckert_IV"
    SPHERE_ECKERT_V = "Sphere_Eckert_V"
    SPHERE_ECKERT_VI = "Sphere_Eckert_VI"
    SPHERE_EQUIDISTANT_CONIC = "Sphere_Equidistant_Conic"
    SPHERE_EQUIDISTANT_CYLINDRICAL = "Sphere_Equidistant_Cylindrical"
    SPHERE_FLAT_POLAR_QUARTIC = "Sphere_Flat_Polar_Quartic"
    SPHERE_GALL_STEREOGRAPHIC = "Sphere_Gall_Stereographic"
    SPHERE_HAMMER_AITOFF = "Sphere_Hammer_Aitoff"
    SPHERE_LOXIMUTHAL = "Sphere_Loximuthal"
    SPHERE_MERCATOR = "Sphere_Mercator"
    SPHERE_MILLER_CYLINDRICAL = "Sphere_Miller_Cylindrical"
    SPHERE_MOLLWEIDE = "Sphere_Mollweide"
    SPHERE_PLATE_CARREE = "Sphere_Plate_Carree"
    SPHERE_POLYCONIC = "Sphere_Polyconic"
    SPHERE_QUARTIC_AUTHALIC = "Sphere_Quartic_Authalic"
    SPHERE_ROBINSON = "Sphere_Robinson"
    SPHERE_SINUSOIDAL = "Sphere_Sinusoidal"
    SPHERE_TIMES = "Sphere_Times"
    SPHERE_VAN_DER_GRINTEN_I = "Sphere_Van_der_Grinten_I"
    SPHERE_VERTICAL_PERSPECTIVE = "Sphere_Vertical_Perspective"
    SPHERE_WINKEL_I = "Sphere_Winkel_I"
    SPHERE_WINKEL_II = "Sphere_Winkel_II"
    SPHERE_WINKEL_TRIPEL_NGS = "Sphere_Winkel_Tripel_NGS"
    THE_WORLD_FROM_SPACE = "The_World_From_Space"
    WORLD_TIMES = "World_Times"
    WORLD_VAN_DER_GRINTEN_I = "World_Van_der_Grinten_I"
    WORLD_VERTICAL_PERSPECTIVE = "World_Vertical_Perspective"
    WORLD_WINKEL_I = "World_Winkel_I"
    WORLD_WINKEL_II = "World_Winkel_II"
    WORLD_WINKEL_TRIPEL_NGS = "World_Winkel_Tripel_NGS"


@dataclass
class SpatialReferenceTypeVertCoordSysAltitudeSysDef:
    class Meta:
        global_type = False

    altitude_datum_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "altitudeDatumName",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    altitude_resolution: List[str] = field(
        default_factory=list,
        metadata={
            "name": "altitudeResolution",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    altitude_distance_units: Optional[str] = field(
        default=None,
        metadata={
            "name": "altitudeDistanceUnits",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    altitude_encoding_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "altitudeEncodingMethod",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class SpatialReferenceTypeVertCoordSysDepthSysDef:
    class Meta:
        global_type = False

    depth_datum_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "depthDatumName",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    depth_resolution: List[str] = field(
        default_factory=list,
        metadata={
            "name": "depthResolution",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    depth_distance_units: Optional[str] = field(
        default=None,
        metadata={
            "name": "depthDistanceUnits",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    depth_encoding_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "depthEncodingMethod",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


class AngleUnits(Enum):
    RADIAN = "radian"
    DEGREE = "degree"
    GRAD = "grad"


@dataclass
class GeogCoordSysTypeDatum:
    class Meta:
        global_type = False

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class GeogCoordSysTypePrimeMeridian:
    class Meta:
        global_type = False

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    longitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -180.0,
            "max_inclusive": 180.0,
        }
    )


@dataclass
class GeogCoordSysTypeSpheroid:
    class Meta:
        global_type = False

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    semi_axis_major: Optional[float] = field(
        default=None,
        metadata={
            "name": "semiAxisMajor",
            "type": "Attribute",
        }
    )
    denom_flat_ratio: Optional[float] = field(
        default=None,
        metadata={
            "name": "denomFlatRatio",
            "type": "Attribute",
        }
    )


@dataclass
class HorizCoordSysTypeProjCoordSysProjectionParameter:
    class Meta:
        global_type = False

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    value: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


class LengthUnits(Enum):
    METER = "meter"
    NANOMETER = "nanometer"
    MICROMETER = "micrometer"
    MICRON = "micron"
    MILLIMETER = "millimeter"
    CENTIMETER = "centimeter"
    DECIMETER = "decimeter"
    DEKAMETER = "dekameter"
    HECTOMETER = "hectometer"
    KILOMETER = "kilometer"
    MEGAMETER = "megameter"
    ANGSTROM = "angstrom"
    INCH = "inch"
    FOOT_US = "Foot_US"
    FOOT = "foot"
    FOOT_GOLD_COAST = "Foot_Gold_Coast"
    FATHOM = "fathom"
    NAUTICAL_MILE = "nauticalMile"
    YARD = "yard"
    YARD_INDIAN = "Yard_Indian"
    LINK_CLARKE = "Link_Clarke"
    YARD_SEARS = "Yard_Sears"
    MILE = "mile"


@dataclass
class DataQualityQuantitativeAccuracyReport2:
    class Meta:
        global_type = False

    quantitative_accuracy_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "quantitativeAccuracyValue",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    quantitative_accuracy_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "quantitativeAccuracyMethod",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


class GeometryType(Enum):
    POINT = "Point"
    LINE_STRING = "LineString"
    LINEAR_RING = "LinearRing"
    POLYGON = "Polygon"
    MULTI_POINT = "MultiPoint"
    MULTI_LINE_STRING = "MultiLineString"
    MULTI_POLYGON = "MultiPolygon"
    MULTI_GEOMETRY = "MultiGeometry"


class TopologyLevel(Enum):
    GEOMETRY_ONLY = "geometryOnly"
    NON_PLANAR_GRAPH = "nonPlanarGraph"
    PLANAR_LINE_GRAPH = "planarLineGraph"
    FULL_PLANAR_GRAPH = "fullPlanarGraph"
    SURFACE_GRAPH = "surfaceGraph"
    FULL_TOPOLOGY3_D = "fullTopology3D"


@dataclass
class ParameterType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/storedProcedure-2.1.1"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    domain_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "domainDescription",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    required: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    repeats: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class ListTypeListitem:
    class Meta:
        global_type = False

    para: List["ParagraphType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    itemizedlist: List["ListType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    orderedlist: List["ListType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class LengthUnitType(Enum):
    METER = "meter"
    NANOMETER = "nanometer"
    MICROMETER = "micrometer"
    MICRON = "micron"
    MILLIMETER = "millimeter"
    CENTIMETER = "centimeter"
    DECIMETER = "decimeter"
    DEKAMETER = "dekameter"
    HECTOMETER = "hectometer"
    KILOMETER = "kilometer"
    MEGAMETER = "megameter"
    ANGSTROM = "angstrom"
    INCH = "inch"
    FOOT_US = "Foot_US"
    FOOT = "foot"
    FOOT_GOLD_COAST = "Foot_Gold_Coast"
    FATHOM = "fathom"
    NAUTICAL_MILE = "nauticalMile"
    YARD = "yard"
    YARD_INDIAN = "Yard_Indian"
    LINK_CLARKE = "Link_Clarke"
    YARD_SEARS = "Yard_Sears"
    MILE = "mile"


class StandardUnitDictionary(Enum):
    METER = "meter"
    NANOMETER = "nanometer"
    MICROMETER = "micrometer"
    MICRON = "micron"
    MILLIMETER = "millimeter"
    CENTIMETER = "centimeter"
    DECIMETER = "decimeter"
    DEKAMETER = "dekameter"
    HECTOMETER = "hectometer"
    KILOMETER = "kilometer"
    MEGAMETER = "megameter"
    ANGSTROM = "angstrom"
    INCH = "inch"
    FOOT_US = "Foot_US"
    FOOT = "foot"
    FOOT_GOLD_COAST = "Foot_Gold_Coast"
    FATHOM = "fathom"
    NAUTICAL_MILE = "nauticalMile"
    YARD = "yard"
    YARD_INDIAN = "Yard_Indian"
    LINK_CLARKE = "Link_Clarke"
    YARD_SEARS = "Yard_Sears"
    MILE = "mile"
    KILOGRAM = "kilogram"
    NANOGRAM = "nanogram"
    MICROGRAM = "microgram"
    MILLIGRAM = "milligram"
    CENTIGRAM = "centigram"
    DECIGRAM = "decigram"
    GRAM = "gram"
    DEKAGRAM = "dekagram"
    HECTOGRAM = "hectogram"
    MEGAGRAM = "megagram"
    TONNE = "tonne"
    POUND = "pound"
    TON = "ton"
    DIMENSIONLESS = "dimensionless"
    SECOND = "second"
    KELVIN = "kelvin"
    COULOMB = "coulomb"
    AMPERE = "ampere"
    MOLE = "mole"
    CANDELA = "candela"
    NUMBER = "number"
    RADIAN = "radian"
    DEGREE = "degree"
    GRAD = "grad"
    CUBIC_METER = "cubicMeter"
    NOMINAL_MINUTE = "nominalMinute"
    NOMINAL_HOUR = "nominalHour"
    NOMINAL_DAY = "nominalDay"
    NOMINAL_WEEK = "nominalWeek"
    NOMINAL_YEAR = "nominalYear"
    NOMINAL_LEAP_YEAR = "nominalLeapYear"
    CELSIUS = "celsius"
    FAHRENHEIT = "fahrenheit"
    NANOSECOND = "nanosecond"
    MICROSECOND = "microsecond"
    MILLISECOND = "millisecond"
    CENTISECOND = "centisecond"
    DECISECOND = "decisecond"
    DEKASECOND = "dekasecond"
    HECTOSECOND = "hectosecond"
    KILOSECOND = "kilosecond"
    MEGASECOND = "megasecond"
    MINUTE = "minute"
    HOUR = "hour"
    KILOLITER = "kiloliter"
    MICROLITER = "microliter"
    MILLILITER = "milliliter"
    LITER = "liter"
    GALLON = "gallon"
    QUART = "quart"
    BUSHEL = "bushel"
    CUBIC_INCH = "cubicInch"
    PINT = "pint"
    MEGAHERTZ = "megahertz"
    KILOHERTZ = "kilohertz"
    HERTZ = "hertz"
    MILLIHERTZ = "millihertz"
    NEWTON = "newton"
    JOULE = "joule"
    CALORIE = "calorie"
    BRITISH_THERMAL_UNIT = "britishThermalUnit"
    FOOT_POUND = "footPound"
    LUMEN = "lumen"
    LUX = "lux"
    BECQUEREL = "becquerel"
    GRAY = "gray"
    SIEVERT = "sievert"
    KATAL = "katal"
    HENRY = "henry"
    MEGAWATT = "megawatt"
    KILOWATT = "kilowatt"
    WATT = "watt"
    MILLIWATT = "milliwatt"
    MEGAVOLT = "megavolt"
    KILOVOLT = "kilovolt"
    VOLT = "volt"
    MILLIVOLT = "millivolt"
    FARAD = "farad"
    OHM = "ohm"
    OHM_METER = "ohmMeter"
    SIEMEN = "siemen"
    WEBER = "weber"
    TESLA = "tesla"
    PASCAL = "pascal"
    MEGAPASCAL = "megapascal"
    KILOPASCAL = "kilopascal"
    ATMOSPHERE = "atmosphere"
    BAR = "bar"
    MILLIBAR = "millibar"
    KILOGRAMS_PER_SQUARE_METER = "kilogramsPerSquareMeter"
    GRAMS_PER_SQUARE_METER = "gramsPerSquareMeter"
    MILLIGRAMS_PER_SQUARE_METER = "milligramsPerSquareMeter"
    KILOGRAMS_PER_HECTARE = "kilogramsPerHectare"
    TONNE_PER_HECTARE = "tonnePerHectare"
    POUNDS_PER_SQUARE_INCH = "poundsPerSquareInch"
    KILOGRAM_PER_CUBIC_METER = "kilogramPerCubicMeter"
    MILLI_GRAMS_PER_MILLI_LITER = "milliGramsPerMilliLiter"
    GRAMS_PER_LITER = "gramsPerLiter"
    MILLIGRAMS_PER_CUBIC_METER = "milligramsPerCubicMeter"
    MICROGRAMS_PER_LITER = "microgramsPerLiter"
    MILLIGRAMS_PER_LITER = "milligramsPerLiter"
    GRAMS_PER_CUBIC_CENTIMETER = "gramsPerCubicCentimeter"
    GRAMS_PER_MILLILITER = "gramsPerMilliliter"
    GRAMS_PER_LITER_PER_DAY = "gramsPerLiterPerDay"
    LITERS_PER_SECOND = "litersPerSecond"
    CUBIC_METERS_PER_SECOND = "cubicMetersPerSecond"
    CUBIC_FEET_PER_SECOND = "cubicFeetPerSecond"
    SQUARE_METER = "squareMeter"
    ARE = "are"
    HECTARE = "hectare"
    SQUARE_KILOMETERS = "squareKilometers"
    SQUARE_MILLIMETERS = "squareMillimeters"
    SQUARE_CENTIMETERS = "squareCentimeters"
    ACRE = "acre"
    SQUARE_FOOT = "squareFoot"
    SQUARE_YARD = "squareYard"
    SQUARE_MILE = "squareMile"
    LITERS_PER_SQUARE_METER = "litersPerSquareMeter"
    BUSHELS_PER_ACRE = "bushelsPerAcre"
    LITERS_PER_HECTARE = "litersPerHectare"
    SQUARE_METER_PER_KILOGRAM = "squareMeterPerKilogram"
    METERS_PER_SECOND = "metersPerSecond"
    METERS_PER_DAY = "metersPerDay"
    FEET_PER_DAY = "feetPerDay"
    FEET_PER_SECOND = "feetPerSecond"
    FEET_PER_HOUR = "feetPerHour"
    YARDS_PER_SECOND = "yardsPerSecond"
    MILES_PER_HOUR = "milesPerHour"
    MILES_PER_SECOND = "milesPerSecond"
    MILES_PER_MINUTE = "milesPerMinute"
    CENTIMETERS_PER_SECOND = "centimetersPerSecond"
    MILLIMETERS_PER_SECOND = "millimetersPerSecond"
    CENTIMETER_PER_YEAR = "centimeterPerYear"
    KNOTS = "knots"
    KILOMETERS_PER_HOUR = "kilometersPerHour"
    METERS_PER_SECOND_SQUARED = "metersPerSecondSquared"
    WAVE_NUMBER = "waveNumber"
    CUBIC_METER_PER_KILOGRAM = "cubicMeterPerKilogram"
    CUBIC_MICROMETERS_PER_GRAM = "cubicMicrometersPerGram"
    AMPERE_PER_SQUARE_METER = "amperePerSquareMeter"
    AMPERE_PER_METER = "amperePerMeter"
    MOLE_PER_CUBIC_METER = "molePerCubicMeter"
    MOLARITY = "molarity"
    MOLALITY = "molality"
    CANDELA_PER_SQUARE_METER = "candelaPerSquareMeter"
    METERS_SQUARED_PER_SECOND = "metersSquaredPerSecond"
    METERS_SQUARED_PER_DAY = "metersSquaredPerDay"
    FEET_SQUARED_PER_DAY = "feetSquaredPerDay"
    KILOGRAMS_PER_METER_SQUARED_PER_SECOND = "kilogramsPerMeterSquaredPerSecond"
    GRAMS_PER_CENTIMETER_SQUARED_PER_SECOND = "gramsPerCentimeterSquaredPerSecond"
    GRAMS_PER_METER_SQUARED_PER_YEAR = "gramsPerMeterSquaredPerYear"
    GRAMS_PER_HECTARE_PER_DAY = "gramsPerHectarePerDay"
    KILOGRAMS_PER_HECTARE_PER_YEAR = "kilogramsPerHectarePerYear"
    KILOGRAMS_PER_METER_SQUARED_PER_YEAR = "kilogramsPerMeterSquaredPerYear"
    MOLES_PER_KILOGRAM = "molesPerKilogram"
    MOLES_PER_GRAM = "molesPerGram"
    MILLIMOLES_PER_GRAM = "millimolesPerGram"
    MOLES_PER_KILOGRAM_PER_SECOND = "molesPerKilogramPerSecond"
    NANOMOLES_PER_GRAM_PER_SECOND = "nanomolesPerGramPerSecond"
    KILOGRAMS_PER_SECOND = "kilogramsPerSecond"
    TONNES_PER_YEAR = "tonnesPerYear"
    GRAMS_PER_YEAR = "gramsPerYear"
    NUMBER_PER_METER_SQUARED = "numberPerMeterSquared"
    NUMBER_PER_KILOMETER_SQUARED = "numberPerKilometerSquared"
    NUMBER_PER_METER_CUBED = "numberPerMeterCubed"
    NUMBER_PER_LITER = "numberPerLiter"
    NUMBER_PER_MILLILITER = "numberPerMilliliter"
    METERS_PER_GRAM = "metersPerGram"
    NUMBER_PER_GRAM = "numberPerGram"
    GRAMS_PER_GRAM = "gramsPerGram"
    MICROGRAMS_PER_GRAM = "microgramsPerGram"
    CUBIC_CENTIMETERS_PER_CUBIC_CENTIMETERS = "cubicCentimetersPerCubicCentimeters"


class LangValue(Enum):
    VALUE = ""


@dataclass
class AccessRule:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/access-2.1.1"

    principal: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    permission: List[AccessRuleValue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class Accuracy:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/attribute-2.1.1"

    attribute_accuracy_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "attributeAccuracyReport",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    quantitative_attribute_accuracy_assessment: List[AccuracyQuantitativeAttributeAccuracyAssessment] = field(
        default_factory=list,
        metadata={
            "name": "quantitativeAttributeAccuracyAssessment",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class BoundsDateGroupBounds:
    class Meta:
        global_type = False

    minimum: Optional[BoundsDateGroupBoundsMinimum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    maximum: Optional[BoundsDateGroupBoundsMaximum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class BoundsGroupBounds:
    class Meta:
        global_type = False

    minimum: Optional[BoundsGroupBoundsMinimum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    maximum: Optional[BoundsGroupBoundsMaximum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class UnitType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/attribute-2.1.1"

    standard_unit: Optional[StandardUnitDictionary] = field(
        default=None,
        metadata={
            "name": "standardUnit",
            "type": "Element",
            "namespace": "",
        }
    )
    custom_unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "customUnit",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class ConstraintTypeNotNullConstraint:
    class Meta:
        global_type = False

    constraint_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "constraintName",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    constraint_description: Optional[object] = field(
        default=None,
        metadata={
            "name": "constraintDescription",
            "type": "Element",
            "namespace": "",
        }
    )
    key: Optional[ConstraintTypeNotNullConstraintKey] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class ConstraintTypePrimaryKey:
    class Meta:
        global_type = False

    constraint_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "constraintName",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    constraint_description: Optional[object] = field(
        default=None,
        metadata={
            "name": "constraintDescription",
            "type": "Element",
            "namespace": "",
        }
    )
    key: Optional[ConstraintTypePrimaryKeyKey] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class ConstraintTypeUniqueKey:
    class Meta:
        global_type = False

    constraint_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "constraintName",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    constraint_description: Optional[object] = field(
        default=None,
        metadata={
            "name": "constraintDescription",
            "type": "Element",
            "namespace": "",
        }
    )
    key: Optional[ConstraintTypeUniqueKeyKey] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class ForeignKeyGroupCardinality:
    class Meta:
        global_type = False

    parent_occurences: Optional[ForeignKeyGroupCardinalityParentOccurences] = field(
        default=None,
        metadata={
            "name": "parentOccurences",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    child_occurences: Optional[Union[int, CardinalityChildOccurancesTypeValue]] = field(
        default=None,
        metadata={
            "name": "childOccurences",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class GeographicCoverageBoundingCoordinatesBoundingAltitudes:
    class Meta:
        global_type = False

    altitude_minimum: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "altitudeMinimum",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    altitude_maximum: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "altitudeMaximum",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    altitude_units: Optional[LengthUnitType] = field(
        default=None,
        metadata={
            "name": "altitudeUnits",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class GeographicCoverageDatasetGpolygonDatasetGpolygonExclusionGring:
    class Meta:
        global_type = False

    g_ring_point: List[GringPointType] = field(
        default_factory=list,
        metadata={
            "name": "gRingPoint",
            "type": "Element",
            "namespace": "",
        }
    )
    g_ring: Optional[str] = field(
        default=None,
        metadata={
            "name": "gRing",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class GeographicCoverageDatasetGpolygonDatasetGpolygonOuterGring:
    class Meta:
        global_type = False

    g_ring_point: List[GringPointType] = field(
        default_factory=list,
        metadata={
            "name": "gRingPoint",
            "type": "Element",
            "namespace": "",
        }
    )
    g_ring: Optional[str] = field(
        default=None,
        metadata={
            "name": "gRing",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class SingleDateTimeType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/coverage-2.1.1"

    calendar_date: Optional[Union[XmlPeriod, XmlDate]] = field(
        default=None,
        metadata={
            "name": "calendarDate",
            "type": "Element",
            "namespace": "",
        }
    )
    time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    alternative_time_scale: Optional[SingleDateTimeTypeAlternativeTimeScale] = field(
        default=None,
        metadata={
            "name": "alternativeTimeScale",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class EmlAdditionalMetadata:
    class Meta:
        global_type = False

    describes: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    metadata: Optional[EmlAdditionalMetadataMetadata] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class PhysicalTypeDataFormatBinaryRasterFormat:
    class Meta:
        global_type = False

    row_column_orientation: Optional[PhysicalTypeDataFormatBinaryRasterFormatRowColumnOrientation] = field(
        default=None,
        metadata={
            "name": "rowColumnOrientation",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    multi_band: Optional[PhysicalTypeDataFormatBinaryRasterFormatMultiBand] = field(
        default=None,
        metadata={
            "name": "multiBand",
            "type": "Element",
            "namespace": "",
        }
    )
    nbits: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    byteorder: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    skipbytes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    bandrowbytes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    totalrowbytes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    bandgapbytes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class PhysicalTypeDataFormatTextFormatComplexTextDelimited:
    class Meta:
        global_type = False

    field_delimiter: Optional[str] = field(
        default=None,
        metadata={
            "name": "fieldDelimiter",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    collapse_delimiters: Optional[PhysicalTypeDataFormatTextFormatComplexTextDelimitedCollapseDelimiters] = field(
        default=None,
        metadata={
            "name": "collapseDelimiters",
            "type": "Element",
            "namespace": "",
        }
    )
    line_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "lineNumber",
            "type": "Element",
            "namespace": "",
        }
    )
    quote_character: List[str] = field(
        default_factory=list,
        metadata={
            "name": "quoteCharacter",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    literal_character: List[str] = field(
        default_factory=list,
        metadata={
            "name": "literalCharacter",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class PhysicalTypeDataFormatTextFormatSimpleDelimited:
    class Meta:
        global_type = False

    field_delimiter: List[str] = field(
        default_factory=list,
        metadata={
            "name": "fieldDelimiter",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    collapse_delimiters: Optional[PhysicalTypeDataFormatTextFormatSimpleDelimitedCollapseDelimiters] = field(
        default=None,
        metadata={
            "name": "collapseDelimiters",
            "type": "Element",
            "namespace": "",
        }
    )
    quote_character: List[str] = field(
        default_factory=list,
        metadata={
            "name": "quoteCharacter",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    literal_character: List[str] = field(
        default_factory=list,
        metadata={
            "name": "literalCharacter",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class UrlType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/resource-2.1.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    function: FunctionType = field(
        default=FunctionType.DOWNLOAD,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class I18NNonEmptyStringTypeValue:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Dependency:
    class Meta:
        name = "dependency"
        namespace = "eml://ecoinformatics.org/software-2.1.1"

    action: Optional[Action] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    software: Optional["Software"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class BandType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/spatialRaster-2.1.1"

    sequence_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "sequenceIdentifier",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    high_wavelength: Optional[float] = field(
        default=None,
        metadata={
            "name": "highWavelength",
            "type": "Element",
            "namespace": "",
        }
    )
    low_wave_length: Optional[float] = field(
        default=None,
        metadata={
            "name": "lowWaveLength",
            "type": "Element",
            "namespace": "",
        }
    )
    wave_length_units: Optional[LengthUnits] = field(
        default=None,
        metadata={
            "name": "waveLengthUnits",
            "type": "Element",
            "namespace": "",
        }
    )
    peak_response: Optional[object] = field(
        default=None,
        metadata={
            "name": "peakResponse",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class DataQuality1:
    class Meta:
        name = "DataQuality"
        target_namespace = "eml://ecoinformatics.org/spatialRaster-2.1.1"

    accuracy_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "accuracyReport",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    quantitative_accuracy_report: List[DataQualityQuantitativeAccuracyReport1] = field(
        default_factory=list,
        metadata={
            "name": "quantitativeAccuracyReport",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class SpatialRasterTypeGeoreferenceInfoControlPoint:
    class Meta:
        global_type = False

    column: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    row: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    x_coordinate: Optional[float] = field(
        default=None,
        metadata={
            "name": "xCoordinate",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    y_coordinate: Optional[float] = field(
        default=None,
        metadata={
            "name": "yCoordinate",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    point_in_pixel: Optional[SpatialRasterTypeGeoreferenceInfoControlPointPointInPixel] = field(
        default=None,
        metadata={
            "name": "pointInPixel",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class SpatialRasterTypeGeoreferenceInfoCornerPoint:
    class Meta:
        global_type = False

    x_coordinate: Optional[float] = field(
        default=None,
        metadata={
            "name": "xCoordinate",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    y_coordinate: Optional[float] = field(
        default=None,
        metadata={
            "name": "yCoordinate",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    point_in_pixel: Optional[SpatialRasterTypeGeoreferenceInfoCornerPointPointInPixel] = field(
        default=None,
        metadata={
            "name": "pointInPixel",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    corner: Optional[RasterOriginType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class SpatialReferenceTypeVertCoordSys:
    class Meta:
        global_type = False

    altitude_sys_def: Optional[SpatialReferenceTypeVertCoordSysAltitudeSysDef] = field(
        default=None,
        metadata={
            "name": "altitudeSysDef",
            "type": "Element",
            "namespace": "",
        }
    )
    depth_sys_def: Optional[SpatialReferenceTypeVertCoordSysDepthSysDef] = field(
        default=None,
        metadata={
            "name": "depthSysDef",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class GeogCoordSysTypeUnit:
    class Meta:
        global_type = False

    name: Optional[AngleUnits] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class HorizCoordSysTypeProjCoordSysProjectionUnit:
    class Meta:
        global_type = False

    name: Optional[LengthUnits] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class DataQuality2:
    class Meta:
        name = "DataQuality"
        target_namespace = "eml://ecoinformatics.org/spatialVector-2.1.1"

    accuracy_report: Optional[str] = field(
        default=None,
        metadata={
            "name": "accuracyReport",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    quantitative_accuracy_report: List[DataQualityQuantitativeAccuracyReport2] = field(
        default_factory=list,
        metadata={
            "name": "quantitativeAccuracyReport",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ListType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/text-2.1.1"

    listitem: List[ListTypeListitem] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class I18NString:
    class Meta:
        name = "i18nString"
        target_namespace = "eml://ecoinformatics.org/text-2.1.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class AccessType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/access-2.1.1"

    allow: List[AccessRule] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    deny: List[AccessRule] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    references: Optional[ReferencesGroupReferences] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    system: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    scope: ScopeType = field(
        default=ScopeType.DOCUMENT,
        metadata={
            "type": "Attribute",
        }
    )
    order: AccessTypeOrder = field(
        default=AccessTypeOrder.ALLOW_FIRST,
        metadata={
            "type": "Attribute",
        }
    )
    auth_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "authSystem",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class DateTimeDomainType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/attribute-2.1.1"

    bounds: List[BoundsDateGroupBounds] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    references: Optional[ReferencesGroupReferences] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class NumericDomainType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/attribute-2.1.1"

    number_type: Optional[NumberType] = field(
        default=None,
        metadata={
            "name": "numberType",
            "type": "Element",
            "namespace": "",
        }
    )
    bounds: List[BoundsGroupBounds] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    references: Optional[ReferencesGroupReferences] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class ConstraintTypeForeignKey:
    class Meta:
        global_type = False

    constraint_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "constraintName",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    constraint_description: Optional[object] = field(
        default=None,
        metadata={
            "name": "constraintDescription",
            "type": "Element",
            "namespace": "",
        }
    )
    key: Optional[ForeignKeyGroupKey] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    entity_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityReference",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    relationship_type: Optional[ForeignKeyGroupRelationshipType] = field(
        default=None,
        metadata={
            "name": "relationshipType",
            "type": "Element",
            "namespace": "",
        }
    )
    cardinality: Optional[ForeignKeyGroupCardinality] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ConstraintTypeJoinCondition:
    class Meta:
        global_type = False

    constraint_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "constraintName",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    constraint_description: Optional[object] = field(
        default=None,
        metadata={
            "name": "constraintDescription",
            "type": "Element",
            "namespace": "",
        }
    )
    key: Optional[ForeignKeyGroupKey] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    entity_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityReference",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    relationship_type: Optional[ForeignKeyGroupRelationshipType] = field(
        default=None,
        metadata={
            "name": "relationshipType",
            "type": "Element",
            "namespace": "",
        }
    )
    cardinality: Optional[ForeignKeyGroupCardinality] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    referenced_key: Optional[ConstraintTypeJoinConditionReferencedKey] = field(
        default=None,
        metadata={
            "name": "referencedKey",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class GeographicCoverageBoundingCoordinates:
    class Meta:
        global_type = False

    west_bounding_coordinate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "westBoundingCoordinate",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("-180.0"),
            "max_inclusive": Decimal("180.0"),
        }
    )
    east_bounding_coordinate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "eastBoundingCoordinate",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("-180.0"),
            "max_inclusive": Decimal("180.0"),
        }
    )
    north_bounding_coordinate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "northBoundingCoordinate",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("-90.0"),
            "max_inclusive": Decimal("90.0"),
        }
    )
    south_bounding_coordinate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "southBoundingCoordinate",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("-90.0"),
            "max_inclusive": Decimal("90.0"),
        }
    )
    bounding_altitudes: Optional[GeographicCoverageBoundingCoordinatesBoundingAltitudes] = field(
        default=None,
        metadata={
            "name": "boundingAltitudes",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class GeographicCoverageDatasetGpolygon:
    class Meta:
        global_type = False

    dataset_gpolygon_outer_gring: Optional[GeographicCoverageDatasetGpolygonDatasetGpolygonOuterGring] = field(
        default=None,
        metadata={
            "name": "datasetGPolygonOuterGRing",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    dataset_gpolygon_exclusion_gring: List[GeographicCoverageDatasetGpolygonDatasetGpolygonExclusionGring] = field(
        default_factory=list,
        metadata={
            "name": "datasetGPolygonExclusionGRing",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TemporalCoverageRangeOfDates:
    class Meta:
        global_type = False

    begin_date: Optional[SingleDateTimeType] = field(
        default=None,
        metadata={
            "name": "beginDate",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    end_date: Optional[SingleDateTimeType] = field(
        default=None,
        metadata={
            "name": "endDate",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class PhysicalTypeDataFormatTextFormatComplex:
    class Meta:
        global_type = False

    text_fixed: List[PhysicalTypeDataFormatTextFormatComplexTextFixed] = field(
        default_factory=list,
        metadata={
            "name": "textFixed",
            "type": "Element",
            "namespace": "",
        }
    )
    text_delimited: List[PhysicalTypeDataFormatTextFormatComplexTextDelimited] = field(
        default_factory=list,
        metadata={
            "name": "textDelimited",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class I18NNonEmptyStringType:
    class Meta:
        name = "i18nNonEmptyStringType"
        target_namespace = "eml://ecoinformatics.org/resource-2.1.1"

    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "value",
                    "type": I18NNonEmptyStringTypeValue,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class SpatialRasterTypeGeoreferenceInfo:
    class Meta:
        global_type = False

    corner_point: List[SpatialRasterTypeGeoreferenceInfoCornerPoint] = field(
        default_factory=list,
        metadata={
            "name": "cornerPoint",
            "type": "Element",
            "namespace": "",
            "max_occurs": 4,
        }
    )
    control_point: List[SpatialRasterTypeGeoreferenceInfoControlPoint] = field(
        default_factory=list,
        metadata={
            "name": "controlPoint",
            "type": "Element",
            "namespace": "",
        }
    )
    bilinear_fit: Optional[SpatialRasterTypeGeoreferenceInfoBilinearFit] = field(
        default=None,
        metadata={
            "name": "bilinearFit",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class SpatialRasterTypeImageDescription:
    class Meta:
        global_type = False

    illumination_elevation_angle: Optional[float] = field(
        default=None,
        metadata={
            "name": "illuminationElevationAngle",
            "type": "Element",
            "namespace": "",
        }
    )
    illumination_azimuth_angle: Optional[float] = field(
        default=None,
        metadata={
            "name": "illuminationAzimuthAngle",
            "type": "Element",
            "namespace": "",
        }
    )
    image_orientation_angle: Optional[float] = field(
        default=None,
        metadata={
            "name": "imageOrientationAngle",
            "type": "Element",
            "namespace": "",
        }
    )
    imaging_condition: Optional[ImagingConditionCode] = field(
        default=None,
        metadata={
            "name": "imagingCondition",
            "type": "Element",
            "namespace": "",
        }
    )
    image_quality_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "imageQualityCode",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    cloud_cover_percentage: Optional[float] = field(
        default=None,
        metadata={
            "name": "cloudCoverPercentage",
            "type": "Element",
            "namespace": "",
        }
    )
    pre_processing_type_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "preProcessingTypeCode",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    compression_generation_quality: Optional[int] = field(
        default=None,
        metadata={
            "name": "compressionGenerationQuality",
            "type": "Element",
            "namespace": "",
        }
    )
    triangulation_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "triangulationIndicator",
            "type": "Element",
            "namespace": "",
        }
    )
    radiometric_data_availability: Optional[bool] = field(
        default=None,
        metadata={
            "name": "radiometricDataAvailability",
            "type": "Element",
            "namespace": "",
        }
    )
    camera_calibration_information_availability: Optional[bool] = field(
        default=None,
        metadata={
            "name": "cameraCalibrationInformationAvailability",
            "type": "Element",
            "namespace": "",
        }
    )
    film_distortion_information_availability: Optional[bool] = field(
        default=None,
        metadata={
            "name": "filmDistortionInformationAvailability",
            "type": "Element",
            "namespace": "",
        }
    )
    lens_distortion_information_availability: Optional[bool] = field(
        default=None,
        metadata={
            "name": "lensDistortionInformationAvailability",
            "type": "Element",
            "namespace": "",
        }
    )
    band_description: List[BandType] = field(
        default_factory=list,
        metadata={
            "name": "bandDescription",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class GeogCoordSysType:
    class Meta:
        name = "geogCoordSysType"
        target_namespace = "eml://ecoinformatics.org/spatialReference-2.1.1"

    datum: Optional[GeogCoordSysTypeDatum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    spheroid: Optional[GeogCoordSysTypeSpheroid] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    prime_meridian: Optional[GeogCoordSysTypePrimeMeridian] = field(
        default=None,
        metadata={
            "name": "primeMeridian",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    unit: Optional[GeogCoordSysTypeUnit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class HorizCoordSysTypeProjCoordSysProjection:
    class Meta:
        global_type = False

    parameter: List[HorizCoordSysTypeProjCoordSysProjectionParameter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    unit: Optional[HorizCoordSysTypeProjCoordSysProjectionUnit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ParagraphTypeEmphasis:
    class Meta:
        global_type = False

    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "value",
                    "type": I18NString,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class ParagraphTypeLiteralLayout:
    class Meta:
        global_type = False

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "value",
                    "type": I18NString,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class ParagraphTypeUlink:
    class Meta:
        global_type = False

    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "citetitle",
                    "type": I18NString,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class SubSuperScriptType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/text-2.1.1"

    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "value",
                    "type": I18NString,
                    "namespace": "",
                },
                {
                    "name": "subscript",
                    "type": Type["SubSuperScriptType"],
                    "namespace": "",
                },
                {
                    "name": "superscript",
                    "type": Type["SubSuperScriptType"],
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class Access(AccessType):
    class Meta:
        name = "access"
        namespace = "eml://ecoinformatics.org/access-2.1.1"


@dataclass
class AttributeTypeMeasurementScaleDateTime:
    class Meta:
        global_type = False

    format_string: Optional[str] = field(
        default=None,
        metadata={
            "name": "formatString",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    date_time_precision: Optional[str] = field(
        default=None,
        metadata={
            "name": "dateTimePrecision",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    date_time_domain: Optional[DateTimeDomainType] = field(
        default=None,
        metadata={
            "name": "dateTimeDomain",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class AttributeTypeMeasurementScaleInterval:
    class Meta:
        global_type = False

    unit: Optional[UnitType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    precision: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    numeric_domain: Optional[NumericDomainType] = field(
        default=None,
        metadata={
            "name": "numericDomain",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class AttributeTypeMeasurementScaleRatio:
    class Meta:
        global_type = False

    unit: Optional[UnitType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    precision: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    numeric_domain: Optional[NumericDomainType] = field(
        default=None,
        metadata={
            "name": "numericDomain",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class ConstraintType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/constraint-2.1.1"

    primary_key: Optional[ConstraintTypePrimaryKey] = field(
        default=None,
        metadata={
            "name": "primaryKey",
            "type": "Element",
            "namespace": "",
        }
    )
    unique_key: Optional[ConstraintTypeUniqueKey] = field(
        default=None,
        metadata={
            "name": "uniqueKey",
            "type": "Element",
            "namespace": "",
        }
    )
    check_constraint: Optional[ConstraintTypeCheckConstraint] = field(
        default=None,
        metadata={
            "name": "checkConstraint",
            "type": "Element",
            "namespace": "",
        }
    )
    foreign_key: Optional[ConstraintTypeForeignKey] = field(
        default=None,
        metadata={
            "name": "foreignKey",
            "type": "Element",
            "namespace": "",
        }
    )
    join_condition: Optional[ConstraintTypeJoinCondition] = field(
        default=None,
        metadata={
            "name": "joinCondition",
            "type": "Element",
            "namespace": "",
        }
    )
    not_null_constraint: Optional[ConstraintTypeNotNullConstraint] = field(
        default=None,
        metadata={
            "name": "notNullConstraint",
            "type": "Element",
            "namespace": "",
        }
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    system: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    scope: ScopeType = field(
        default=ScopeType.DOCUMENT,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class GeographicCoverage:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/coverage-2.1.1"

    geographic_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "geographicDescription",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    bounding_coordinates: Optional[GeographicCoverageBoundingCoordinates] = field(
        default=None,
        metadata={
            "name": "boundingCoordinates",
            "type": "Element",
            "namespace": "",
        }
    )
    dataset_gpolygon: List[GeographicCoverageDatasetGpolygon] = field(
        default_factory=list,
        metadata={
            "name": "datasetGPolygon",
            "type": "Element",
            "namespace": "",
        }
    )
    references: Optional[ReferencesGroupReferences] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    system: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    scope: ScopeType = field(
        default=ScopeType.DOCUMENT,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TemporalCoverage:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/coverage-2.1.1"

    single_date_time: List[SingleDateTimeType] = field(
        default_factory=list,
        metadata={
            "name": "singleDateTime",
            "type": "Element",
            "namespace": "",
        }
    )
    range_of_dates: Optional[TemporalCoverageRangeOfDates] = field(
        default=None,
        metadata={
            "name": "rangeOfDates",
            "type": "Element",
            "namespace": "",
        }
    )
    references: Optional[ReferencesGroupReferences] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class Address:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/party-2.1.1"

    delivery_point: List[I18NNonEmptyStringType] = field(
        default_factory=list,
        metadata={
            "name": "deliveryPoint",
            "type": "Element",
            "namespace": "",
        }
    )
    city: Optional[I18NNonEmptyStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    administrative_area: Optional[I18NNonEmptyStringType] = field(
        default=None,
        metadata={
            "name": "administrativeArea",
            "type": "Element",
            "namespace": "",
        }
    )
    postal_code: Optional[I18NNonEmptyStringType] = field(
        default=None,
        metadata={
            "name": "postalCode",
            "type": "Element",
            "namespace": "",
        }
    )
    country: Optional[I18NNonEmptyStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    references: Optional[ReferencesGroupReferences] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    system: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    scope: ScopeType = field(
        default=ScopeType.DOCUMENT,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Person:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/party-2.1.1"

    salutation: List[I18NNonEmptyStringType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    given_name: List[I18NNonEmptyStringType] = field(
        default_factory=list,
        metadata={
            "name": "givenName",
            "type": "Element",
            "namespace": "",
        }
    )
    sur_name: Optional[I18NNonEmptyStringType] = field(
        default=None,
        metadata={
            "name": "surName",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class PhysicalTypeDataFormatTextFormat:
    class Meta:
        global_type = False

    num_header_lines: Optional[int] = field(
        default=None,
        metadata={
            "name": "numHeaderLines",
            "type": "Element",
            "namespace": "",
        }
    )
    num_footer_lines: Optional[int] = field(
        default=None,
        metadata={
            "name": "numFooterLines",
            "type": "Element",
            "namespace": "",
        }
    )
    record_delimiter: List[str] = field(
        default_factory=list,
        metadata={
            "name": "recordDelimiter",
            "type": "Element",
            "namespace": "",
        }
    )
    physical_line_delimiter: List[str] = field(
        default_factory=list,
        metadata={
            "name": "physicalLineDelimiter",
            "type": "Element",
            "namespace": "",
        }
    )
    num_physical_lines_per_record: Optional[int] = field(
        default=None,
        metadata={
            "name": "numPhysicalLinesPerRecord",
            "type": "Element",
            "namespace": "",
        }
    )
    max_record_length: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxRecordLength",
            "type": "Element",
            "namespace": "",
        }
    )
    attribute_orientation: Optional[PhysicalTypeDataFormatTextFormatAttributeOrientation] = field(
        default=None,
        metadata={
            "name": "attributeOrientation",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    simple_delimited: Optional[PhysicalTypeDataFormatTextFormatSimpleDelimited] = field(
        default=None,
        metadata={
            "name": "simpleDelimited",
            "type": "Element",
            "namespace": "",
        }
    )
    complex: Optional[PhysicalTypeDataFormatTextFormatComplex] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ResourceGroupKeywordSetKeyword(I18NNonEmptyStringType):
    class Meta:
        global_type = False

    keyword_type: Optional[KeyTypeCode] = field(
        default=None,
        metadata={
            "name": "keywordType",
            "type": "Attribute",
        }
    )


@dataclass
class HorizCoordSysTypeProjCoordSys:
    class Meta:
        global_type = False

    geog_coord_sys: Optional[GeogCoordSysType] = field(
        default=None,
        metadata={
            "name": "geogCoordSys",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    projection: Optional[HorizCoordSysTypeProjCoordSysProjection] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class ParagraphType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/text-2.1.1"

    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "value",
                    "type": I18NString,
                    "namespace": "",
                },
                {
                    "name": "itemizedlist",
                    "type": ListType,
                    "namespace": "",
                },
                {
                    "name": "orderedlist",
                    "type": ListType,
                    "namespace": "",
                },
                {
                    "name": "emphasis",
                    "type": ParagraphTypeEmphasis,
                    "namespace": "",
                },
                {
                    "name": "subscript",
                    "type": SubSuperScriptType,
                    "namespace": "",
                },
                {
                    "name": "superscript",
                    "type": SubSuperScriptType,
                    "namespace": "",
                },
                {
                    "name": "literalLayout",
                    "type": ParagraphTypeLiteralLayout,
                    "namespace": "",
                },
                {
                    "name": "ulink",
                    "type": ParagraphTypeUlink,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class CoverageTemporalCoverage(TemporalCoverage):
    class Meta:
        global_type = False

    system: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    scope: ScopeType = field(
        default=ScopeType.DOCUMENT,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Presentation:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/literature-2.1.1"

    conference_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "conferenceName",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    conference_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "conferenceDate",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    conference_location: Optional[Address] = field(
        default=None,
        metadata={
            "name": "conferenceLocation",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class MethodsTypeSamplingSpatialSamplingUnits:
    class Meta:
        global_type = False

    referenced_entity_id: List[object] = field(
        default_factory=list,
        metadata={
            "name": "referencedEntityId",
            "type": "Element",
            "namespace": "",
        }
    )
    coverage: List[GeographicCoverage] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ResponsibleParty:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/party-2.1.1"

    individual_name: List[Person] = field(
        default_factory=list,
        metadata={
            "name": "individualName",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    organization_name: List[I18NNonEmptyStringType] = field(
        default_factory=list,
        metadata={
            "name": "organizationName",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    position_name: List[I18NNonEmptyStringType] = field(
        default_factory=list,
        metadata={
            "name": "positionName",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    address: List[Address] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    phone: List[ResponsiblePartyPhone] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    electronic_mail_address: List[I18NNonEmptyStringType] = field(
        default_factory=list,
        metadata={
            "name": "electronicMailAddress",
            "type": "Element",
            "namespace": "",
        }
    )
    online_url: List[str] = field(
        default_factory=list,
        metadata={
            "name": "onlineUrl",
            "type": "Element",
            "namespace": "",
        }
    )
    user_id: List[ResponsiblePartyUserId] = field(
        default_factory=list,
        metadata={
            "name": "userId",
            "type": "Element",
            "namespace": "",
        }
    )
    references: Optional[ReferencesGroupReferences] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    system: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    scope: ScopeType = field(
        default=ScopeType.DOCUMENT,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ResourceGroupKeywordSet:
    class Meta:
        global_type = False

    keyword: List[ResourceGroupKeywordSetKeyword] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    keyword_thesaurus: Optional[str] = field(
        default=None,
        metadata={
            "name": "keywordThesaurus",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class HorizCoordSysType:
    class Meta:
        name = "horizCoordSysType"
        target_namespace = "eml://ecoinformatics.org/spatialReference-2.1.1"

    geog_coord_sys: Optional[GeogCoordSysType] = field(
        default=None,
        metadata={
            "name": "geogCoordSys",
            "type": "Element",
            "namespace": "",
        }
    )
    proj_coord_sys: Optional[HorizCoordSysTypeProjCoordSys] = field(
        default=None,
        metadata={
            "name": "projCoordSys",
            "type": "Element",
            "namespace": "",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class SectionType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/text-2.1.1"

    title: Optional[I18NString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    para: List[ParagraphType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    section: List["SectionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class TaxonomicCoverageTaxonomicSystemVouchersRepository:
    class Meta:
        global_type = False

    originator: List[ResponsibleParty] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class Article:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/literature-2.1.1"

    journal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    volume: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    issue: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    page_range: Optional[str] = field(
        default=None,
        metadata={
            "name": "pageRange",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    publisher: Optional[ResponsibleParty] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    publication_place: Optional[str] = field(
        default=None,
        metadata={
            "name": "publicationPlace",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    issn: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISSN",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class AudioVisual:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/literature-2.1.1"

    publisher: Optional[ResponsibleParty] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    publication_place: List[str] = field(
        default_factory=list,
        metadata={
            "name": "publicationPlace",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    performer: List[ResponsibleParty] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    isbn: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISBN",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class Book:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/literature-2.1.1"

    publisher: Optional[ResponsibleParty] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    publication_place: Optional[str] = field(
        default=None,
        metadata={
            "name": "publicationPlace",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    edition: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    volume: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    number_of_volumes: Optional[str] = field(
        default=None,
        metadata={
            "name": "numberOfVolumes",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    total_pages: Optional[str] = field(
        default=None,
        metadata={
            "name": "totalPages",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    total_figures: Optional[str] = field(
        default=None,
        metadata={
            "name": "totalFigures",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    total_tables: Optional[str] = field(
        default=None,
        metadata={
            "name": "totalTables",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    isbn: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISBN",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class Generic:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/literature-2.1.1"

    publisher: Optional[ResponsibleParty] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    publication_place: Optional[str] = field(
        default=None,
        metadata={
            "name": "publicationPlace",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    reference_type: Optional[object] = field(
        default=None,
        metadata={
            "name": "referenceType",
            "type": "Element",
            "namespace": "",
        }
    )
    volume: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    number_of_volumes: Optional[str] = field(
        default=None,
        metadata={
            "name": "numberOfVolumes",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    total_pages: Optional[str] = field(
        default=None,
        metadata={
            "name": "totalPages",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    total_figures: Optional[str] = field(
        default=None,
        metadata={
            "name": "totalFigures",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    total_tables: Optional[str] = field(
        default=None,
        metadata={
            "name": "totalTables",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    edition: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    original_publication: Optional[str] = field(
        default=None,
        metadata={
            "name": "originalPublication",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    reprint_edition: Optional[str] = field(
        default=None,
        metadata={
            "name": "reprintEdition",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    reviewed_item: Optional[str] = field(
        default=None,
        metadata={
            "name": "reviewedItem",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    isbn: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISBN",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    issn: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISSN",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class Manuscript:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/literature-2.1.1"

    institution: List[ResponsibleParty] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    total_pages: Optional[str] = field(
        default=None,
        metadata={
            "name": "totalPages",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class Map:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/literature-2.1.1"

    publisher: Optional[ResponsibleParty] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    edition: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    geographic_coverage: List[GeographicCoverage] = field(
        default_factory=list,
        metadata={
            "name": "geographicCoverage",
            "type": "Element",
            "namespace": "",
        }
    )
    scale: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class PersonalCommunication:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/literature-2.1.1"

    publisher: Optional[ResponsibleParty] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    publication_place: Optional[str] = field(
        default=None,
        metadata={
            "name": "publicationPlace",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    communication_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "communicationType",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    recipient: List[ResponsibleParty] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Report:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/literature-2.1.1"

    report_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "reportNumber",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    publisher: Optional[ResponsibleParty] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    publication_place: Optional[str] = field(
        default=None,
        metadata={
            "name": "publicationPlace",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    total_pages: Optional[str] = field(
        default=None,
        metadata={
            "name": "totalPages",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class Thesis:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/literature-2.1.1"

    degree: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    institution: Optional[ResponsibleParty] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    total_pages: Optional[str] = field(
        default=None,
        metadata={
            "name": "totalPages",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class Party(ResponsibleParty):
    class Meta:
        name = "party"
        namespace = "eml://ecoinformatics.org/party-2.1.1"


@dataclass
class ResearchProjectTypePersonnel(ResponsibleParty):
    class Meta:
        global_type = False

    role: List[Union[str, RoleTypeValue]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class ResourceGroupAssociatedParty(ResponsibleParty):
    class Meta:
        global_type = False

    role: Optional[Union[str, RoleTypeValue]] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class SpatialReferenceType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/spatialReference-2.1.1"

    horiz_coord_sys_name: Optional[SpatialReferenceTypeHorizCoordSysName] = field(
        default=None,
        metadata={
            "name": "horizCoordSysName",
            "type": "Element",
            "namespace": "",
        }
    )
    horiz_coord_sys_def: Optional[HorizCoordSysType] = field(
        default=None,
        metadata={
            "name": "horizCoordSysDef",
            "type": "Element",
            "namespace": "",
        }
    )
    vert_coord_sys: Optional[SpatialReferenceTypeVertCoordSys] = field(
        default=None,
        metadata={
            "name": "vertCoordSys",
            "type": "Element",
            "namespace": "",
        }
    )
    references: Optional[ReferencesGroupReferences] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    system: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    scope: ScopeType = field(
        default=ScopeType.DOCUMENT,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ProjectionList:
    class Meta:
        name = "projectionList"
        namespace = "eml://ecoinformatics.org/spatialReference-2.1.1"

    horiz_coord_sys_def: List[HorizCoordSysType] = field(
        default_factory=list,
        metadata={
            "name": "horizCoordSysDef",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class TextType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/text-2.1.1"

    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "section",
                    "type": SectionType,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": ParagraphType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class TaxonomicCoverageTaxonomicSystemVouchers:
    class Meta:
        global_type = False

    specimen: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    repository: Optional[TaxonomicCoverageTaxonomicSystemVouchersRepository] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class MaintenanceType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/dataset-2.1.1"

    description: Optional[TextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    maintenance_update_frequency: Optional[MaintUpFreqType] = field(
        default=None,
        metadata={
            "name": "maintenanceUpdateFrequency",
            "type": "Element",
            "namespace": "",
        }
    )
    change_history: List[MaintenanceTypeChangeHistory] = field(
        default_factory=list,
        metadata={
            "name": "changeHistory",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Description(TextType):
    class Meta:
        name = "description"
        namespace = "eml://ecoinformatics.org/documentation-2.1.1"


@dataclass
class Example(TextType):
    class Meta:
        name = "example"
        namespace = "eml://ecoinformatics.org/documentation-2.1.1"


@dataclass
class ModuleDocs:
    class Meta:
        name = "moduleDocs"
        namespace = "eml://ecoinformatics.org/documentation-2.1.1"

    module_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "moduleName",
            "type": "Element",
            "required": True,
        }
    )
    module_description: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "moduleDescription",
            "type": "Element",
            "required": True,
        }
    )
    recommended_usage: Optional[str] = field(
        default=None,
        metadata={
            "name": "recommendedUsage",
            "type": "Element",
            "required": True,
        }
    )
    stand_alone: Optional[str] = field(
        default=None,
        metadata={
            "name": "standAlone",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Chapter(Book):
    class Meta:
        target_namespace = "eml://ecoinformatics.org/literature-2.1.1"

    chapter_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "chapterNumber",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    editor: List[ResponsibleParty] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    book_title: Optional[str] = field(
        default=None,
        metadata={
            "name": "bookTitle",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    page_range: Optional[str] = field(
        default=None,
        metadata={
            "name": "pageRange",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class ConnectionDefinitionType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/resource-2.1.1"

    scheme_name: Optional[ConnectionDefinitionTypeSchemeName] = field(
        default=None,
        metadata={
            "name": "schemeName",
            "type": "Element",
            "namespace": "",
        }
    )
    description: Optional[TextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    parameter_definition: List[ConnectionDefinitionTypeParameterDefinition] = field(
        default_factory=list,
        metadata={
            "name": "parameterDefinition",
            "type": "Element",
            "namespace": "",
        }
    )
    references: Optional[ReferencesGroupReferences] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    system: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    scope: ScopeType = field(
        default=ScopeType.DOCUMENT,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class SpatialReference(SpatialReferenceType):
    class Meta:
        name = "spatialReference"
        namespace = "eml://ecoinformatics.org/spatialReference-2.1.1"


@dataclass
class Text(TextType):
    class Meta:
        name = "text"
        namespace = "eml://ecoinformatics.org/text-2.1.1"


@dataclass
class TaxonomicCoverageTaxonomicSystem:
    class Meta:
        global_type = False

    classification_system: List[TaxonomicCoverageTaxonomicSystemClassificationSystem] = field(
        default_factory=list,
        metadata={
            "name": "classificationSystem",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    identification_reference: List["CitationType"] = field(
        default_factory=list,
        metadata={
            "name": "identificationReference",
            "type": "Element",
            "namespace": "",
        }
    )
    identifier_name: List[ResponsibleParty] = field(
        default_factory=list,
        metadata={
            "name": "identifierName",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    taxonomic_procedures: Optional[str] = field(
        default=None,
        metadata={
            "name": "taxonomicProcedures",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    taxonomic_completeness: Optional[str] = field(
        default=None,
        metadata={
            "name": "taxonomicCompleteness",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    vouchers: List[TaxonomicCoverageTaxonomicSystemVouchers] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ConferenceProceedings(Chapter):
    class Meta:
        target_namespace = "eml://ecoinformatics.org/literature-2.1.1"

    conference_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "conferenceName",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    conference_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "conferenceDate",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    conference_location: Optional[Address] = field(
        default=None,
        metadata={
            "name": "conferenceLocation",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ConnectionType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/resource-2.1.1"

    connection_definition: Optional[ConnectionDefinitionType] = field(
        default=None,
        metadata={
            "name": "connectionDefinition",
            "type": "Element",
            "namespace": "",
        }
    )
    parameter: List[ConnectionTypeParameter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    references: Optional[ReferencesGroupReferences] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    system: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    scope: ScopeType = field(
        default=ScopeType.DOCUMENT,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TaxonomicCoverage:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/coverage-2.1.1"

    taxonomic_system: Optional[TaxonomicCoverageTaxonomicSystem] = field(
        default=None,
        metadata={
            "name": "taxonomicSystem",
            "type": "Element",
            "namespace": "",
        }
    )
    general_taxonomic_coverage: Optional[str] = field(
        default=None,
        metadata={
            "name": "generalTaxonomicCoverage",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    taxonomic_classification: List[TaxonomicClassificationType] = field(
        default_factory=list,
        metadata={
            "name": "taxonomicClassification",
            "type": "Element",
            "namespace": "",
        }
    )
    references: Optional[ReferencesGroupReferences] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class PhysicalOnlineType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/physical-2.1.1"

    online_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "onlineDescription",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    url: Optional[UrlType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    connection: Optional[ConnectionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class OnlineType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/resource-2.1.1"

    online_description: Optional[I18NNonEmptyStringType] = field(
        default=None,
        metadata={
            "name": "onlineDescription",
            "type": "Element",
            "namespace": "",
        }
    )
    url: Optional[UrlType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    connection: Optional[ConnectionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    connection_definition: Optional[ConnectionDefinitionType] = field(
        default=None,
        metadata={
            "name": "connectionDefinition",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class CoverageTaxonomicCoverage(TaxonomicCoverage):
    class Meta:
        global_type = False

    system: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    scope: ScopeType = field(
        default=ScopeType.DOCUMENT,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class PhysicalDistributionType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/physical-2.1.1"

    online: Optional[PhysicalOnlineType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    offline: Optional[OfflineType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    inline: Optional[InlineType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    access: Optional[AccessType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    references: Optional[ReferencesGroupReferences] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    system: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    scope: ScopeType = field(
        default=ScopeType.DOCUMENT,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DistributionType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/resource-2.1.1"

    online: Optional[OnlineType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    offline: Optional[OfflineType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    inline: Optional[InlineType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    references: Optional[ReferencesGroupReferences] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    system: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    scope: ScopeType = field(
        default=ScopeType.DOCUMENT,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Coverage:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/coverage-2.1.1"

    geographic_coverage: List[GeographicCoverage] = field(
        default_factory=list,
        metadata={
            "name": "geographicCoverage",
            "type": "Element",
            "namespace": "",
        }
    )
    temporal_coverage: List[CoverageTemporalCoverage] = field(
        default_factory=list,
        metadata={
            "name": "temporalCoverage",
            "type": "Element",
            "namespace": "",
        }
    )
    taxonomic_coverage: List[CoverageTaxonomicCoverage] = field(
        default_factory=list,
        metadata={
            "name": "taxonomicCoverage",
            "type": "Element",
            "namespace": "",
        }
    )
    references: Optional[ReferencesGroupReferences] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    system: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    scope: ScopeType = field(
        default=ScopeType.DOCUMENT,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class SoftwareTypeImplementation:
    class Meta:
        global_type = False

    distribution: List[PhysicalDistributionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    size: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    language: List[SoftwareTypeImplementationLanguage] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    operating_system: List[str] = field(
        default_factory=list,
        metadata={
            "name": "operatingSystem",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    machine_processor: List[str] = field(
        default_factory=list,
        metadata={
            "name": "machineProcessor",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    virtual_machine: Optional[str] = field(
        default=None,
        metadata={
            "name": "virtualMachine",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    disk_usage: Optional[str] = field(
        default=None,
        metadata={
            "name": "diskUsage",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    runtime_memory_usage: Optional[str] = field(
        default=None,
        metadata={
            "name": "runtimeMemoryUsage",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    programming_language: List[str] = field(
        default_factory=list,
        metadata={
            "name": "programmingLanguage",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    checksum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    dependency: List[Dependency] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/software-2.1.1",
        }
    )


@dataclass
class CitationType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/literature-2.1.1"

    alternate_identifier: List[ResourceGroupAlternateIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "alternateIdentifier",
            "type": "Element",
            "namespace": "",
        }
    )
    short_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "shortName",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    title: List[I18NNonEmptyStringType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    creator: List[ResponsibleParty] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    metadata_provider: List[ResponsibleParty] = field(
        default_factory=list,
        metadata={
            "name": "metadataProvider",
            "type": "Element",
            "namespace": "",
        }
    )
    associated_party: List[ResourceGroupAssociatedParty] = field(
        default_factory=list,
        metadata={
            "name": "associatedParty",
            "type": "Element",
            "namespace": "",
        }
    )
    pub_date: Optional[Union[XmlPeriod, XmlDate]] = field(
        default=None,
        metadata={
            "name": "pubDate",
            "type": "Element",
            "namespace": "",
        }
    )
    language: Optional[I18NNonEmptyStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    series: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    abstract: Optional[TextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    keyword_set: List[ResourceGroupKeywordSet] = field(
        default_factory=list,
        metadata={
            "name": "keywordSet",
            "type": "Element",
            "namespace": "",
        }
    )
    additional_info: List[TextType] = field(
        default_factory=list,
        metadata={
            "name": "additionalInfo",
            "type": "Element",
            "namespace": "",
        }
    )
    intellectual_rights: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "intellectualRights",
            "type": "Element",
            "namespace": "",
        }
    )
    distribution: List[DistributionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    coverage: Optional[Coverage] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    contact: List[ResponsibleParty] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    article: Optional[Article] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    book: Optional[Book] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    chapter: Optional[Chapter] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    edited_book: Optional[Book] = field(
        default=None,
        metadata={
            "name": "editedBook",
            "type": "Element",
            "namespace": "",
        }
    )
    manuscript: Optional[Manuscript] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    report: Optional[Report] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    thesis: Optional[Thesis] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    conference_proceedings: Optional[ConferenceProceedings] = field(
        default=None,
        metadata={
            "name": "conferenceProceedings",
            "type": "Element",
            "namespace": "",
        }
    )
    personal_communication: Optional[PersonalCommunication] = field(
        default=None,
        metadata={
            "name": "personalCommunication",
            "type": "Element",
            "namespace": "",
        }
    )
    map: Optional[Map] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    generic: Optional[Generic] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    audio_visual: Optional[AudioVisual] = field(
        default=None,
        metadata={
            "name": "audioVisual",
            "type": "Element",
            "namespace": "",
        }
    )
    presentation: Optional[Presentation] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    references: Optional[ReferencesGroupReferences] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    system: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    scope: ScopeType = field(
        default=ScopeType.DOCUMENT,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class MethodsTypeSamplingStudyExtent:
    class Meta:
        global_type = False

    coverage: List[Coverage] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    description: List[TextType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class NonNumericDomainTypeEnumeratedDomainExternalCodeSet:
    class Meta:
        global_type = False

    codeset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "codesetName",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    citation: List[CitationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    codeset_url: List[str] = field(
        default_factory=list,
        metadata={
            "name": "codesetURL",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )


@dataclass
class Citation(CitationType):
    class Meta:
        name = "citation"
        namespace = "eml://ecoinformatics.org/literature-2.1.1"


@dataclass
class MethodsTypeSampling:
    class Meta:
        global_type = False

    study_extent: Optional[MethodsTypeSamplingStudyExtent] = field(
        default=None,
        metadata={
            "name": "studyExtent",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    sampling_description: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "samplingDescription",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    spatial_sampling_units: Optional[MethodsTypeSamplingSpatialSamplingUnits] = field(
        default=None,
        metadata={
            "name": "spatialSamplingUnits",
            "type": "Element",
            "namespace": "",
        }
    )
    citation: List[CitationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class PhysicalTypeDataFormatExternallyDefinedFormat:
    class Meta:
        global_type = False

    format_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "formatName",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    format_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "formatVersion",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    citation: Optional[CitationType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ResearchProjectTypeDesignDescription:
    class Meta:
        global_type = False

    description: List[TextType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    citation: List[CitationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ResearchProjectTypeStudyAreaDescriptionDescriptor:
    class Meta:
        global_type = False

    descriptor_value: List[ResearchProjectTypeStudyAreaDescriptionDescriptorDescriptorValue] = field(
        default_factory=list,
        metadata={
            "name": "descriptorValue",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "sequential": True,
        }
    )
    citation: List[CitationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    name: Optional[Union[str, DescriptorTypeValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    citable_classification_system: Optional[bool] = field(
        default=None,
        metadata={
            "name": "citableClassificationSystem",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class NonNumericDomainTypeEnumeratedDomain:
    class Meta:
        global_type = False

    code_definition: List[NonNumericDomainTypeEnumeratedDomainCodeDefinition] = field(
        default_factory=list,
        metadata={
            "name": "codeDefinition",
            "type": "Element",
            "namespace": "",
        }
    )
    external_code_set: Optional[NonNumericDomainTypeEnumeratedDomainExternalCodeSet] = field(
        default=None,
        metadata={
            "name": "externalCodeSet",
            "type": "Element",
            "namespace": "",
        }
    )
    entity_code_list: Optional[NonNumericDomainTypeEnumeratedDomainEntityCodeList] = field(
        default=None,
        metadata={
            "name": "entityCodeList",
            "type": "Element",
            "namespace": "",
        }
    )
    enforced: NonNumericDomainTypeEnumeratedDomainEnforced = field(
        default=NonNumericDomainTypeEnumeratedDomainEnforced.YES,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class PhysicalTypeDataFormat:
    class Meta:
        global_type = False

    text_format: Optional[PhysicalTypeDataFormatTextFormat] = field(
        default=None,
        metadata={
            "name": "textFormat",
            "type": "Element",
            "namespace": "",
        }
    )
    externally_defined_format: Optional[PhysicalTypeDataFormatExternallyDefinedFormat] = field(
        default=None,
        metadata={
            "name": "externallyDefinedFormat",
            "type": "Element",
            "namespace": "",
        }
    )
    binary_raster_format: Optional[PhysicalTypeDataFormatBinaryRasterFormat] = field(
        default=None,
        metadata={
            "name": "binaryRasterFormat",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ResearchProjectTypeStudyAreaDescription:
    class Meta:
        global_type = False

    descriptor: List[ResearchProjectTypeStudyAreaDescriptionDescriptor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    citation: List[CitationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    coverage: List[Coverage] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class NonNumericDomainType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/attribute-2.1.1"

    enumerated_domain: List[NonNumericDomainTypeEnumeratedDomain] = field(
        default_factory=list,
        metadata={
            "name": "enumeratedDomain",
            "type": "Element",
            "namespace": "",
        }
    )
    text_domain: List[NonNumericDomainTypeTextDomain] = field(
        default_factory=list,
        metadata={
            "name": "textDomain",
            "type": "Element",
            "namespace": "",
        }
    )
    references: Optional[ReferencesGroupReferences] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class PhysicalType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/physical-2.1.1"

    object_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "objectName",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    size: Optional[PhysicalTypeSize] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    authentication: List[PhysicalTypeAuthentication] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    compression_method: List[str] = field(
        default_factory=list,
        metadata={
            "name": "compressionMethod",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
            "sequential": True,
        }
    )
    encoding_method: List[str] = field(
        default_factory=list,
        metadata={
            "name": "encodingMethod",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
            "sequential": True,
        }
    )
    character_encoding: Optional[str] = field(
        default=None,
        metadata={
            "name": "characterEncoding",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    data_format: Optional[PhysicalTypeDataFormat] = field(
        default=None,
        metadata={
            "name": "dataFormat",
            "type": "Element",
            "namespace": "",
        }
    )
    distribution: List[PhysicalDistributionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    references: Optional[ReferencesGroupReferences] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    system: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    scope: ScopeType = field(
        default=ScopeType.DOCUMENT,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ResearchProjectType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/project-2.1.1"

    title: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    personnel: List[ResearchProjectTypePersonnel] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    abstract: Optional[TextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    funding: Optional[TextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    study_area_description: Optional[ResearchProjectTypeStudyAreaDescription] = field(
        default=None,
        metadata={
            "name": "studyAreaDescription",
            "type": "Element",
            "namespace": "",
        }
    )
    design_description: Optional[ResearchProjectTypeDesignDescription] = field(
        default=None,
        metadata={
            "name": "designDescription",
            "type": "Element",
            "namespace": "",
        }
    )
    related_project: List["ResearchProjectType"] = field(
        default_factory=list,
        metadata={
            "name": "relatedProject",
            "type": "Element",
            "namespace": "",
        }
    )
    references: Optional[ReferencesGroupReferences] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    system: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    scope: ScopeType = field(
        default=ScopeType.DOCUMENT,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class AttributeTypeMeasurementScaleNominal:
    class Meta:
        global_type = False

    non_numeric_domain: Optional[NonNumericDomainType] = field(
        default=None,
        metadata={
            "name": "nonNumericDomain",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class AttributeTypeMeasurementScaleOrdinal:
    class Meta:
        global_type = False

    non_numeric_domain: Optional[NonNumericDomainType] = field(
        default=None,
        metadata={
            "name": "nonNumericDomain",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Physical(PhysicalType):
    class Meta:
        name = "physical"
        namespace = "eml://ecoinformatics.org/physical-2.1.1"


@dataclass
class ResearchProject(ResearchProjectType):
    class Meta:
        name = "researchProject"
        namespace = "eml://ecoinformatics.org/project-2.1.1"


@dataclass
class SoftwareType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/software-2.1.1"

    alternate_identifier: List[ResourceGroupAlternateIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "alternateIdentifier",
            "type": "Element",
            "namespace": "",
        }
    )
    short_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "shortName",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    title: List[I18NNonEmptyStringType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    creator: List[ResponsibleParty] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    metadata_provider: List[ResponsibleParty] = field(
        default_factory=list,
        metadata={
            "name": "metadataProvider",
            "type": "Element",
            "namespace": "",
        }
    )
    associated_party: List[ResourceGroupAssociatedParty] = field(
        default_factory=list,
        metadata={
            "name": "associatedParty",
            "type": "Element",
            "namespace": "",
        }
    )
    pub_date: Optional[Union[XmlPeriod, XmlDate]] = field(
        default=None,
        metadata={
            "name": "pubDate",
            "type": "Element",
            "namespace": "",
        }
    )
    language: Optional[I18NNonEmptyStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    series: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    abstract: Optional[TextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    keyword_set: List[ResourceGroupKeywordSet] = field(
        default_factory=list,
        metadata={
            "name": "keywordSet",
            "type": "Element",
            "namespace": "",
        }
    )
    additional_info: List[TextType] = field(
        default_factory=list,
        metadata={
            "name": "additionalInfo",
            "type": "Element",
            "namespace": "",
        }
    )
    intellectual_rights: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "intellectualRights",
            "type": "Element",
            "namespace": "",
        }
    )
    distribution: List[DistributionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    coverage: Optional[Coverage] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    implementation: List[SoftwareTypeImplementation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    dependency: List[Dependency] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/software-2.1.1",
        }
    )
    license_url: List[str] = field(
        default_factory=list,
        metadata={
            "name": "licenseURL",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
            "sequential": True,
        }
    )
    license: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
            "sequential": True,
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    project: Optional[ResearchProjectType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    references: Optional[ReferencesGroupReferences] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    system: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    scope: ScopeType = field(
        default=ScopeType.DOCUMENT,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class AttributeTypeMeasurementScale:
    class Meta:
        global_type = False

    nominal: Optional[AttributeTypeMeasurementScaleNominal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    ordinal: Optional[AttributeTypeMeasurementScaleOrdinal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    interval: Optional[AttributeTypeMeasurementScaleInterval] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    ratio: Optional[AttributeTypeMeasurementScaleRatio] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    date_time: Optional[AttributeTypeMeasurementScaleDateTime] = field(
        default=None,
        metadata={
            "name": "dateTime",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ProcedureStepType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/methods-2.1.1"

    description: Optional[TextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    citation: List[CitationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    protocol: List["ProtocolType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    instrumentation: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    software: List[SoftwareType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    sub_step: List["ProcedureStepType"] = field(
        default_factory=list,
        metadata={
            "name": "subStep",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Software(SoftwareType):
    class Meta:
        name = "software"
        namespace = "eml://ecoinformatics.org/software-2.1.1"


@dataclass
class AttributeType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/attribute-2.1.1"

    attribute_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "attributeName",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    attribute_label: List[str] = field(
        default_factory=list,
        metadata={
            "name": "attributeLabel",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    attribute_definition: Optional[str] = field(
        default=None,
        metadata={
            "name": "attributeDefinition",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    storage_type: List[AttributeTypeStorageType] = field(
        default_factory=list,
        metadata={
            "name": "storageType",
            "type": "Element",
            "namespace": "",
        }
    )
    measurement_scale: Optional[AttributeTypeMeasurementScale] = field(
        default=None,
        metadata={
            "name": "measurementScale",
            "type": "Element",
            "namespace": "",
        }
    )
    missing_value_code: List[AttributeTypeMissingValueCode] = field(
        default_factory=list,
        metadata={
            "name": "missingValueCode",
            "type": "Element",
            "namespace": "",
        }
    )
    accuracy: Optional[Accuracy] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    coverage: Optional[Coverage] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    methods: Optional["MethodsType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    references: Optional[ReferencesGroupReferences] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    system: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    scope: ScopeType = field(
        default=ScopeType.DOCUMENT,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ProtocolType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/protocol-2.1.1"

    alternate_identifier: List[ResourceGroupAlternateIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "alternateIdentifier",
            "type": "Element",
            "namespace": "",
        }
    )
    short_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "shortName",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    title: List[I18NNonEmptyStringType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    creator: List[ResponsibleParty] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    metadata_provider: List[ResponsibleParty] = field(
        default_factory=list,
        metadata={
            "name": "metadataProvider",
            "type": "Element",
            "namespace": "",
        }
    )
    associated_party: List[ResourceGroupAssociatedParty] = field(
        default_factory=list,
        metadata={
            "name": "associatedParty",
            "type": "Element",
            "namespace": "",
        }
    )
    pub_date: Optional[Union[XmlPeriod, XmlDate]] = field(
        default=None,
        metadata={
            "name": "pubDate",
            "type": "Element",
            "namespace": "",
        }
    )
    language: Optional[I18NNonEmptyStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    series: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    abstract: Optional[TextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    keyword_set: List[ResourceGroupKeywordSet] = field(
        default_factory=list,
        metadata={
            "name": "keywordSet",
            "type": "Element",
            "namespace": "",
        }
    )
    additional_info: List[TextType] = field(
        default_factory=list,
        metadata={
            "name": "additionalInfo",
            "type": "Element",
            "namespace": "",
        }
    )
    intellectual_rights: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "intellectualRights",
            "type": "Element",
            "namespace": "",
        }
    )
    distribution: List[DistributionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    coverage: Optional[Coverage] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    procedural_step: List[ProcedureStepType] = field(
        default_factory=list,
        metadata={
            "name": "proceduralStep",
            "type": "Element",
            "namespace": "",
        }
    )
    references: Optional[ReferencesGroupReferences] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    system: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    scope: ScopeType = field(
        default=ScopeType.DOCUMENT,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class AttributeListType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/attribute-2.1.1"

    attribute: List[AttributeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    references: Optional[ReferencesGroupReferences] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class Attribute(AttributeType):
    class Meta:
        name = "attribute"
        namespace = "eml://ecoinformatics.org/attribute-2.1.1"


@dataclass
class Protocol(ProtocolType):
    class Meta:
        name = "protocol"
        namespace = "eml://ecoinformatics.org/protocol-2.1.1"


@dataclass
class AttributeList(AttributeListType):
    class Meta:
        name = "attributeList"
        namespace = "eml://ecoinformatics.org/attribute-2.1.1"


@dataclass
class DataTableType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/dataTable-2.1.1"

    alternate_identifier: List[EntityGroupAlternateIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "alternateIdentifier",
            "type": "Element",
            "namespace": "",
        }
    )
    entity_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityName",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    entity_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityDescription",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    physical: List[PhysicalType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    coverage: Optional[Coverage] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    methods: Optional["MethodsType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    additional_info: List[TextType] = field(
        default_factory=list,
        metadata={
            "name": "additionalInfo",
            "type": "Element",
            "namespace": "",
        }
    )
    attribute_list: Optional[AttributeListType] = field(
        default=None,
        metadata={
            "name": "attributeList",
            "type": "Element",
            "namespace": "",
        }
    )
    constraint: List[ConstraintType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    case_sensitive: Optional[DataTableTypeCaseSensitive] = field(
        default=None,
        metadata={
            "name": "caseSensitive",
            "type": "Element",
            "namespace": "",
        }
    )
    number_of_records: Optional[str] = field(
        default=None,
        metadata={
            "name": "numberOfRecords",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    references: Optional[ReferencesGroupReferences] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    system: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    scope: ScopeType = field(
        default=ScopeType.DOCUMENT,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class OtherEntityType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/entity-2.1.1"

    alternate_identifier: List[EntityGroupAlternateIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "alternateIdentifier",
            "type": "Element",
            "namespace": "",
        }
    )
    entity_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityName",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    entity_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityDescription",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    physical: List[PhysicalType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    coverage: Optional[Coverage] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    methods: Optional["MethodsType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    additional_info: List[TextType] = field(
        default_factory=list,
        metadata={
            "name": "additionalInfo",
            "type": "Element",
            "namespace": "",
        }
    )
    attribute_list: Optional[AttributeListType] = field(
        default=None,
        metadata={
            "name": "attributeList",
            "type": "Element",
            "namespace": "",
        }
    )
    constraint: List[ConstraintType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    entity_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityType",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    references: Optional[ReferencesGroupReferences] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    system: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    scope: ScopeType = field(
        default=ScopeType.DOCUMENT,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class SpatialRasterType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/spatialRaster-2.1.1"

    alternate_identifier: List[EntityGroupAlternateIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "alternateIdentifier",
            "type": "Element",
            "namespace": "",
        }
    )
    entity_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityName",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    entity_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityDescription",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    physical: List[PhysicalType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    coverage: Optional[Coverage] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    methods: Optional["MethodsType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    additional_info: List[TextType] = field(
        default_factory=list,
        metadata={
            "name": "additionalInfo",
            "type": "Element",
            "namespace": "",
        }
    )
    attribute_list: Optional[AttributeListType] = field(
        default=None,
        metadata={
            "name": "attributeList",
            "type": "Element",
            "namespace": "",
        }
    )
    constraint: List[ConstraintType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    spatial_reference: Optional[SpatialReferenceType] = field(
        default=None,
        metadata={
            "name": "spatialReference",
            "type": "Element",
            "namespace": "",
        }
    )
    georeference_info: Optional[SpatialRasterTypeGeoreferenceInfo] = field(
        default=None,
        metadata={
            "name": "georeferenceInfo",
            "type": "Element",
            "namespace": "",
        }
    )
    horizontal_accuracy: Optional[DataQuality1] = field(
        default=None,
        metadata={
            "name": "horizontalAccuracy",
            "type": "Element",
            "namespace": "",
        }
    )
    vertical_accuracy: Optional[DataQuality1] = field(
        default=None,
        metadata={
            "name": "verticalAccuracy",
            "type": "Element",
            "namespace": "",
        }
    )
    cell_size_xdirection: Optional[object] = field(
        default=None,
        metadata={
            "name": "cellSizeXDirection",
            "type": "Element",
            "namespace": "",
        }
    )
    cell_size_ydirection: Optional[object] = field(
        default=None,
        metadata={
            "name": "cellSizeYDirection",
            "type": "Element",
            "namespace": "",
        }
    )
    number_of_bands: Optional[object] = field(
        default=None,
        metadata={
            "name": "numberOfBands",
            "type": "Element",
            "namespace": "",
        }
    )
    raster_origin: Optional[RasterOriginType] = field(
        default=None,
        metadata={
            "name": "rasterOrigin",
            "type": "Element",
            "namespace": "",
        }
    )
    rows: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    columns: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    verticals: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    cell_geometry: Optional[CellGeometryType] = field(
        default=None,
        metadata={
            "name": "cellGeometry",
            "type": "Element",
            "namespace": "",
        }
    )
    tone_gradation: Optional[int] = field(
        default=None,
        metadata={
            "name": "toneGradation",
            "type": "Element",
            "namespace": "",
        }
    )
    scale_factor: Optional[str] = field(
        default=None,
        metadata={
            "name": "scaleFactor",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    offset: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    image_description: Optional[SpatialRasterTypeImageDescription] = field(
        default=None,
        metadata={
            "name": "imageDescription",
            "type": "Element",
            "namespace": "",
        }
    )
    references: Optional[ReferencesGroupReferences] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    system: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    scope: ScopeType = field(
        default=ScopeType.DOCUMENT,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class SpatialVectorType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/spatialVector-2.1.1"

    alternate_identifier: List[EntityGroupAlternateIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "alternateIdentifier",
            "type": "Element",
            "namespace": "",
        }
    )
    entity_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityName",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    entity_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityDescription",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    physical: List[PhysicalType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    coverage: Optional[Coverage] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    methods: Optional["MethodsType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    additional_info: List[TextType] = field(
        default_factory=list,
        metadata={
            "name": "additionalInfo",
            "type": "Element",
            "namespace": "",
        }
    )
    attribute_list: Optional[AttributeListType] = field(
        default=None,
        metadata={
            "name": "attributeList",
            "type": "Element",
            "namespace": "",
        }
    )
    constraint: List[ConstraintType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    geometry: List[GeometryType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    geometric_object_count: Optional[str] = field(
        default=None,
        metadata={
            "name": "geometricObjectCount",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    topology_level: Optional[TopologyLevel] = field(
        default=None,
        metadata={
            "name": "topologyLevel",
            "type": "Element",
            "namespace": "",
        }
    )
    spatial_reference: Optional[SpatialReferenceType] = field(
        default=None,
        metadata={
            "name": "spatialReference",
            "type": "Element",
            "namespace": "",
        }
    )
    horizontal_accuracy: Optional[DataQuality2] = field(
        default=None,
        metadata={
            "name": "horizontalAccuracy",
            "type": "Element",
            "namespace": "",
        }
    )
    vertical_accuracy: Optional[DataQuality2] = field(
        default=None,
        metadata={
            "name": "verticalAccuracy",
            "type": "Element",
            "namespace": "",
        }
    )
    references: Optional[ReferencesGroupReferences] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    system: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    scope: ScopeType = field(
        default=ScopeType.DOCUMENT,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class StoredProcedureType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/storedProcedure-2.1.1"

    alternate_identifier: List[EntityGroupAlternateIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "alternateIdentifier",
            "type": "Element",
            "namespace": "",
        }
    )
    entity_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityName",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    entity_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityDescription",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    physical: List[PhysicalType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    coverage: Optional[Coverage] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    methods: Optional["MethodsType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    additional_info: List[TextType] = field(
        default_factory=list,
        metadata={
            "name": "additionalInfo",
            "type": "Element",
            "namespace": "",
        }
    )
    attribute_list: Optional[AttributeListType] = field(
        default=None,
        metadata={
            "name": "attributeList",
            "type": "Element",
            "namespace": "",
        }
    )
    constraint: List[ConstraintType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    parameter: List[ParameterType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    references: Optional[ReferencesGroupReferences] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    system: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    scope: ScopeType = field(
        default=ScopeType.DOCUMENT,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ViewType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/view-2.1.1"

    alternate_identifier: List[EntityGroupAlternateIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "alternateIdentifier",
            "type": "Element",
            "namespace": "",
        }
    )
    entity_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityName",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    entity_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityDescription",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    physical: List[PhysicalType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    coverage: Optional[Coverage] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    methods: Optional["MethodsType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    additional_info: List[TextType] = field(
        default_factory=list,
        metadata={
            "name": "additionalInfo",
            "type": "Element",
            "namespace": "",
        }
    )
    attribute_list: Optional[AttributeListType] = field(
        default=None,
        metadata={
            "name": "attributeList",
            "type": "Element",
            "namespace": "",
        }
    )
    constraint: List[ConstraintType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    query_statement: Optional[str] = field(
        default=None,
        metadata={
            "name": "queryStatement",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    references: Optional[ReferencesGroupReferences] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    system: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    scope: ScopeType = field(
        default=ScopeType.DOCUMENT,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DataTable(DataTableType):
    class Meta:
        name = "dataTable"
        namespace = "eml://ecoinformatics.org/dataTable-2.1.1"


@dataclass
class DatasetType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/dataset-2.1.1"

    alternate_identifier: List[ResourceGroupAlternateIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "alternateIdentifier",
            "type": "Element",
            "namespace": "",
        }
    )
    short_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "shortName",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    title: List[I18NNonEmptyStringType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    creator: List[ResponsibleParty] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    metadata_provider: List[ResponsibleParty] = field(
        default_factory=list,
        metadata={
            "name": "metadataProvider",
            "type": "Element",
            "namespace": "",
        }
    )
    associated_party: List[ResourceGroupAssociatedParty] = field(
        default_factory=list,
        metadata={
            "name": "associatedParty",
            "type": "Element",
            "namespace": "",
        }
    )
    pub_date: Optional[Union[XmlPeriod, XmlDate]] = field(
        default=None,
        metadata={
            "name": "pubDate",
            "type": "Element",
            "namespace": "",
        }
    )
    language: Optional[I18NNonEmptyStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    series: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    abstract: Optional[TextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    keyword_set: List[ResourceGroupKeywordSet] = field(
        default_factory=list,
        metadata={
            "name": "keywordSet",
            "type": "Element",
            "namespace": "",
        }
    )
    additional_info: List[TextType] = field(
        default_factory=list,
        metadata={
            "name": "additionalInfo",
            "type": "Element",
            "namespace": "",
        }
    )
    intellectual_rights: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "intellectualRights",
            "type": "Element",
            "namespace": "",
        }
    )
    distribution: List[DistributionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    coverage: Optional[Coverage] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    purpose: Optional[TextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    maintenance: Optional[MaintenanceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    contact: List[ResponsibleParty] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    publisher: Optional[ResponsibleParty] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    pub_place: Optional[str] = field(
        default=None,
        metadata={
            "name": "pubPlace",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    methods: Optional["MethodsType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    project: Optional[ResearchProjectType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    data_table: List[DataTableType] = field(
        default_factory=list,
        metadata={
            "name": "dataTable",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    spatial_raster: List[SpatialRasterType] = field(
        default_factory=list,
        metadata={
            "name": "spatialRaster",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    spatial_vector: List[SpatialVectorType] = field(
        default_factory=list,
        metadata={
            "name": "spatialVector",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    stored_procedure: List[StoredProcedureType] = field(
        default_factory=list,
        metadata={
            "name": "storedProcedure",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    view: List[ViewType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    other_entity: List[OtherEntityType] = field(
        default_factory=list,
        metadata={
            "name": "otherEntity",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    references: Optional[ReferencesGroupReferences] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    system: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    scope: ScopeType = field(
        default=ScopeType.DOCUMENT,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class OtherEntity(OtherEntityType):
    class Meta:
        name = "otherEntity"
        namespace = "eml://ecoinformatics.org/entity-2.1.1"


@dataclass
class SpatialRaster(SpatialRasterType):
    class Meta:
        name = "spatialRaster"
        namespace = "eml://ecoinformatics.org/spatialRaster-2.1.1"


@dataclass
class SpatialVector(SpatialVectorType):
    class Meta:
        name = "spatialVector"
        namespace = "eml://ecoinformatics.org/spatialVector-2.1.1"


@dataclass
class StoredProcedure(StoredProcedureType):
    class Meta:
        name = "storedProcedure"
        namespace = "eml://ecoinformatics.org/storedProcedure-2.1.1"


@dataclass
class View(ViewType):
    class Meta:
        name = "view"
        namespace = "eml://ecoinformatics.org/view-2.1.1"


@dataclass
class Dataset(DatasetType):
    class Meta:
        name = "dataset"
        namespace = "eml://ecoinformatics.org/dataset-2.1.1"


@dataclass
class Eml:
    class Meta:
        name = "eml"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    access: Optional[AccessType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    dataset: Optional[DatasetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    citation: Optional[CitationType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    software: Optional[SoftwareType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    protocol: Optional[ProtocolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    additional_metadata: List[EmlAdditionalMetadata] = field(
        default_factory=list,
        metadata={
            "name": "additionalMetadata",
            "type": "Element",
            "namespace": "",
        }
    )
    package_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "packageId",
            "type": "Attribute",
            "required": True,
        }
    )
    system: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "required": True,
            "tokens": True,
        }
    )
    scope: ScopeType = field(
        init=False,
        default=ScopeType.SYSTEM,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class MethodsTypeMethodStep(ProcedureStepType):
    class Meta:
        global_type = False

    data_source: List[DatasetType] = field(
        default_factory=list,
        metadata={
            "name": "dataSource",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class MethodsType:
    class Meta:
        target_namespace = "eml://ecoinformatics.org/methods-2.1.1"

    method_step: List[MethodsTypeMethodStep] = field(
        default_factory=list,
        metadata={
            "name": "methodStep",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "sequential": True,
        }
    )
    sampling: List[MethodsTypeSampling] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    quality_control: List[ProcedureStepType] = field(
        default_factory=list,
        metadata={
            "name": "qualityControl",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )


@dataclass
class Methods(MethodsType):
    """
    Comment describing your root element.
    """
    class Meta:
        name = "methods"
        namespace = "eml://ecoinformatics.org/methods-2.1.1"
