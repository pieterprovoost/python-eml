from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Union
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod


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
class AdditionalMetadataMetadataGbifCollection:
    """
    :ivar parent_collection_identifier: Identifier for the parent
        collection for this sub-collection. Enables a hierarchy of
        collections and sub collections to be built.
    :ivar collection_identifier: The URI (LSID or URL) of the
        collection. In RDF, used as URI of the collection resource.
    :ivar collection_name: Official name of the Collection in the local
        language
    """
    class Meta:
        global_type = False

    parent_collection_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "parentCollectionIdentifier",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    collection_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "collectionIdentifier",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    collection_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "collectionName",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class Address:
    """
    The address field is a container for multiple subfields that describe the
    physical or electronic address of the responsible party for a resource.

    :ivar delivery_point: The delivery point field is used for the
        physical address for postal communication, e.g., GBIF
        Secretariat, Universitetsparken 15
    :ivar city: The city field is used for the city name of the contact
        associated with a particular resource.
    :ivar administrative_area: The administrative area field is the
        equivalent of a 'state' in the U.S., or Province in Canada. This
        field is intended to accommodate the many types of international
        administrative areas.
    :ivar postal_code: The postal code is equivalent to a U.S. zip code,
        or the number used for routing to an international address.
    :ivar country: The country field is used for the name of the
        contact's country.
    """
    class Meta:
        name = "address"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    delivery_point: Optional[str] = field(
        default=None,
        metadata={
            "name": "deliveryPoint",
            "type": "Element",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    administrative_area: Optional[str] = field(
        default=None,
        metadata={
            "name": "administrativeArea",
            "type": "Element",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    postal_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "postalCode",
            "type": "Element",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class AlternateIdentifier:
    """
    This is the only identifier issued by the IPT for the metadata document; it
    is a UUID.
    """
    class Meta:
        name = "alternateIdentifier"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class CalendarDate:
    """The calendar date field is used to express a date, giving the year,
    month, and day.

    The format should be one that complies with the International Standards Organization's standard 8601. The recommended format for EML is YYYY-MM-DD, where Y is the four digit year, M is the two digit month code (01 - 12, where January = 01), and D is the two digit day of the month (01 - 31). This field can also be used to enter just the year portion of a date.
    """
    class Meta:
        name = "calendarDate"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    value: Optional[Union[XmlPeriod, XmlDate]] = field(
        default=None
    )


@dataclass
class CalendarDate1:
    class Meta:
        name = "calendarDate"
        target_namespace = "eml://ecoinformatics.org/eml-2.1.1"

    calendar_date: Optional[Union[XmlPeriod, XmlDate]] = field(
        default=None,
        metadata={
            "name": "calendarDate",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class CharacterEncoding:
    """This element contains the name of the character encoding.

    This is typically ASCII or UTF-8, or one of the other common
    encodings.
    """
    class Meta:
        name = "characterEncoding"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class CitationType:
    """
    A single literature citation with an optional identifier.

    :ivar value:
    :ivar identifier: A URI, DOI or other persistent identifier for the
        citation
    """
    class Meta:
        name = "citationType"
        target_namespace = "eml://ecoinformatics.org/eml-2.1.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DataFormatExternallyDefinedFormat:
    """
    :ivar format_name: Name of the format of the data object, e.g., ESRI
        Shapefile.
    :ivar format_version: Version of the format of the data object
    """
    class Meta:
        global_type = False

    format_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "formatName",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "required": True,
        }
    )
    format_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "formatVersion",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


class DataFormatTextFormatAttributeOrientation(Enum):
    COLUMN = "column"
    ROW = "row"


class DataFormatTextFormatComplexTextDelimitedCollapseDelimiters(Enum):
    YES = "yes"
    NO = "no"


@dataclass
class DataFormatTextFormatComplexTextFixed:
    """
    :ivar field_width: Fixed width fields have a set length, thus the
        end of the field can always be determined by adding the
        fieldWidth to the starting column number.
    :ivar line_number: The line on which the data field is found, when
        the data record is written over more than one physical line in
        the file. A single logical data record may be written over
        several physical lines in a file, with no special marker to
        indicate the end of a record. In such cases, the relative
        location of a data field must be indicated by both relative row
        and column number.  The lineNumber should never greater that the
        number of physical lines per record.
    :ivar field_start_column: The starting column number for a fixed
        format attribute. Fixed width fields have a set length, thus the
        end of the field can always be determined by adding the
        fieldWidth to the starting column number. If the starting column
        is not provided, processors should assume that the field starts
        in the column following the previous field if the previous field
        was fixed, or in the column following the delimiter from the
        previous field if the previous field was delimited.
    """
    class Meta:
        global_type = False

    field_width: Optional[int] = field(
        default=None,
        metadata={
            "name": "fieldWidth",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "required": True,
        }
    )
    line_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "lineNumber",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
        }
    )
    field_start_column: Optional[int] = field(
        default=None,
        metadata={
            "name": "fieldStartColumn",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
        }
    )


class DataFormatTextFormatSimpleDelimitedCollapseDelimiters(Enum):
    YES = "yes"
    NO = "no"


class DescriptorEnum(Enum):
    THEMATIC = "thematic"
    GEOGRAPHIC = "geographic"
    GENERIC = "generic"


@dataclass
class DescriptorValue:
    """
    The descriptorValue field contains a general description, either thematic
    or geographic, of the study area.
    """
    class Meta:
        name = "descriptorValue"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class ElectronicMailAddress:
    """The electronic mail address is the email address for the party.

    It is intended to be an Internet SMTP email address, which should consist of a username followed by the @ symbol, followed by the email server domain name address.
    """
    class Meta:
        name = "electronicMailAddress"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class GeographicCoverageBoundingCoordinates:
    """
    :ivar west_bounding_coordinate: The westBoundingCoordinate field
        defines the longitude of the western-most point of the bounding
        box that is being described.
    :ivar east_bounding_coordinate: The eastBoundingCoordinate field
        defines the longitude of the eastern-most point of the bounding
        box that is being described.
    :ivar north_bounding_coordinate: The northBoundingCoordinate field
        defines the latitude of the northern-most point of the bounding
        box that is being described.
    :ivar south_bounding_coordinate: The southBoundingCoordinate field
        defines the latitude of the southern-most point of the bounding
        box that is being described.
    """
    class Meta:
        global_type = False

    west_bounding_coordinate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "westBoundingCoordinate",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "required": True,
        }
    )
    east_bounding_coordinate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "eastBoundingCoordinate",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "required": True,
        }
    )
    north_bounding_coordinate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "northBoundingCoordinate",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "required": True,
        }
    )
    south_bounding_coordinate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "southBoundingCoordinate",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "required": True,
        }
    )


@dataclass
class IndividualName:
    """
    The individualName field contains subfields so that a person's name can be
    broken down into parts.

    :ivar given_name: The given name field can be used for first name of
        the individual associated with the resource, or for any other
        names that are not intended to be alphabetized, (as
        appropriate).
    :ivar sur_name: The surname field is used for the last name of the
        individual associated with the resource. This is typically the
        family name of an individual, for example, the name by which
        s/he is referred to in citations.
    """
    class Meta:
        name = "individualName"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    given_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "givenName",
            "type": "Element",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    sur_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "surName",
            "type": "Element",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class JgtiCuratorialUnitJgtiUnitRange:
    """
    :ivar begin_range: The lower value in a range of numbers. Use to
        represent an exact number by omitting the "endRange" value.
    :ivar end_range: The upper value in a range of numbers.
    """
    class Meta:
        global_type = False

    begin_range: Optional[int] = field(
        default=None,
        metadata={
            "name": "beginRange",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "required": True,
        }
    )
    end_range: Optional[int] = field(
        default=None,
        metadata={
            "name": "endRange",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "required": True,
        }
    )


@dataclass
class JgtiCuratorialUnitJgtiUnits:
    """
    :ivar value:
    :ivar uncertainty_measure: A measure of the uncertainty (+ or -) x
        associated with the jgtiUnits value
    """
    class Meta:
        global_type = False

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uncertainty_measure: Optional[int] = field(
        default=None,
        metadata={
            "name": "uncertaintyMeasure",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class KeywordSet:
    """
    A wrapper element for the keyword and keywordThesaurus elements.

    :ivar keyword: This field names a keyword or key phrase that
        concisely describes the resource or is related to the resource.
        Each keyword field should contain one and only one keyword
    :ivar keyword_thesaurus: The name of the official keyword thesaurus
        from which keyword was derived
    """
    class Meta:
        name = "keywordSet"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    keyword: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    keyword_thesaurus: Optional[str] = field(
        default=None,
        metadata={
            "name": "keywordThesaurus",
            "type": "Element",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class Language:
    """
    The language in which the resource (not the metadata document) is written.
    """
    class Meta:
        name = "language"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class ObjectName:
    """The name of the data object.

    This  often is the filename of a file in a file system or that is
    accessible on the network.
    """
    class Meta:
        name = "objectName"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class OnlineUrl:
    """A link to associated online information, usually a web site.

    When the party represents an organization, this is the URL to a
    website or other online information about the organization. If the
    party is an individual, it might be their personal web site or other
    related online information about the party.
    """
    class Meta:
        name = "onlineUrl"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Phone:
    """
    The phone field describes information about the responsible party's
    telephone, be it a voice phone, fax.
    """
    class Meta:
        name = "phone"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class PubDate:
    """
    The date on which the resource was published.
    """
    class Meta:
        name = "pubDate"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    value: Optional[Union[XmlPeriod, XmlDate]] = field(
        default=None
    )


@dataclass
class Role:
    """Use this field to describe the role the party played with respect to the
    resource.

    Some potential roles include technician, reviewer, principal
    investigator, and many others.
    """
    class Meta:
        name = "role"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class TaxonomicCoverageTaxonomicClassification:
    """
    :ivar taxon_rank_name: The name of the taxonomic rank for which the
        Taxon rank value is provided, e.g., Phylum, Class, Genus,
        Species
    :ivar taxon_rank_value: The name representing the taxonomic rank of
        the taxon being described
    :ivar common_name: Applicable common names; these common names may
        be general descriptions of a group of organisms if appropriate,
        e.g., invertebrates, waterfowl
    """
    class Meta:
        global_type = False

    taxon_rank_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "taxonRankName",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    taxon_rank_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "taxonRankValue",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    common_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "commonName",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class TemporalCoverageRangeOfDates:
    """
    :ivar begin_date: A single time stamp signifying the beginning of
        some time period
    :ivar end_date: A single time stamp signifying the end of some time
        period
    """
    class Meta:
        global_type = False

    begin_date: Optional[Union[XmlPeriod, XmlDate]] = field(
        default=None,
        metadata={
            "name": "beginDate",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "required": True,
        }
    )
    end_date: Optional[Union[XmlPeriod, XmlDate]] = field(
        default=None,
        metadata={
            "name": "endDate",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "required": True,
        }
    )


@dataclass
class Ulink:
    """
    this element and its children allow paragraphs to contain urls and titles
    for anchor tags.

    :ivar url: the url attribute contains the location of the work for a
        link.
    :ivar content:
    """
    class Meta:
        name = "ulink"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
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
                    "type": str,
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
                },
            ),
        }
    )


@dataclass
class Url:
    """
    The URL of the resource that is available online.
    """
    class Meta:
        name = "url"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    function: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class UserId:
    """An identifier that links this party to a directory of personnel.

    Although specific contact information for a party might change, the
    underlying correspondence to a real individual does not.  This
    identifier provides a pointer within a personnel directory that may
    contain further, and possibly more current, information about the
    party.

    :ivar value:
    :ivar directory: This attribute names the directory system to which
        this userId applies. This will generally be a URL that shows how
        to look up information, for example an LDAP url. However, it
        could also be a non-parsable description of the directory system
        if that is all that is available.
    """
    class Meta:
        name = "userId"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    directory: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class Uri:
    class Meta:
        name = "URI"
        namespace = "http://purl.org/dc/terms/"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Created:
    class Meta:
        name = "created"
        namespace = "http://purl.org/dc/terms/"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Description1:
    class Meta:
        name = "description"
        namespace = "http://purl.org/dc/terms/"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Issued:
    class Meta:
        name = "issued"
        namespace = "http://purl.org/dc/terms/"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Modified:
    class Meta:
        name = "modified"
        namespace = "http://purl.org/dc/terms/"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Relation:
    class Meta:
        name = "relation"
        namespace = "http://purl.org/dc/terms/"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Replaces:
    class Meta:
        name = "replaces"
        namespace = "http://purl.org/dc/terms/"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Source:
    class Meta:
        name = "source"
        namespace = "http://purl.org/dc/terms/"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Subject:
    class Meta:
        name = "subject"
        namespace = "http://purl.org/dc/terms/"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Title1:
    class Meta:
        name = "title"
        namespace = "http://purl.org/dc/terms/"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class TypeType:
    class Meta:
        name = "type"
        namespace = "http://purl.org/dc/terms/"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


class LangValue(Enum):
    VALUE = ""


@dataclass
class AdditionalMetadataMetadataGbifBibliography:
    class Meta:
        global_type = False

    citation: List[CitationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "min_occurs": 1,
        }
    )


@dataclass
class AgentType:
    """
    :ivar organization_name: The full name of the organization that is
        associated with the resource. This field is intended to describe
        which institution or overall organization is associated with the
        resource being described.
    :ivar individual_name:
    :ivar position_name: This field is intended to be used instead of a
        particular person or full organization name. If the associated
        person who holds the role changes frequently, then Position Name
        would be used for consistency. E.g., GBIF Data Manager.
    :ivar address:
    :ivar phone:
    :ivar electronic_mail_address:
    :ivar online_url:
    :ivar user_id:
    """
    class Meta:
        name = "agentType"
        target_namespace = "eml://ecoinformatics.org/eml-2.1.1"

    organization_name: List[str] = field(
        default_factory=list,
        metadata={
            "name": "organizationName",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
            "sequential": True,
        }
    )
    individual_name: List[IndividualName] = field(
        default_factory=list,
        metadata={
            "name": "individualName",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    position_name: List[str] = field(
        default_factory=list,
        metadata={
            "name": "positionName",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
            "sequential": True,
        }
    )
    address: Optional[Address] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    phone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    electronic_mail_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "electronicMailAddress",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    online_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "onlineUrl",
            "type": "Element",
            "namespace": "",
        }
    )
    user_id: List[UserId] = field(
        default_factory=list,
        metadata={
            "name": "userId",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class DataFormatTextFormatComplexTextDelimited:
    """
    :ivar field_delimiter: This element specifies a character to be used
        in the object for indicating the ending column for an attribute.
        The delimiter character itself is not part of the attribute
        value, but rather is present in the column following the last
        character of the value. Typical delimiter characters include
        commas, tabs, spaces, and semicolons.  The only time the
        fieldDelimiter character is not interpreted as a delimiter is if
        it is contained in a quoted string (see quoteCharacter) or is
        immediately preceded by a literalCharacter. Non-printable quote
        characters can be provided as their hex values, and for tab
        characters by its ASCII string "\\t".  Processors should assume
        that the field starts in the column following the previous field
        if the previous field was fixed, or in the column following the
        delimiter from the previous field if the previous field was
        delimited.
    :ivar collapse_delimiters: The collapseDelimiters element specifies
        whether sequential delimiters should be treated as a single
        delimiter or multiple delimiters.    An example is when a space
        delimiter is used; often there may be several repeated spaces
        that should be treated as a single delimiter, but not always.
        The valid values are yes or no.  If it is set to yes, then
        consecutive delimiters will be collapsed to one.  If set to no
        or absent, then consecutive delimiters will be treated as
        separate delimiters. Default behaviour is no; hence, consecutive
        delimiters will be treated as separate delimiters, by default.
    :ivar line_number: A single logical data record may be written over
        several physical lines in a file, with no special marker to
        indicate the end of a record. In such cases, the relative
        location of a data field must be indicated by both relative row
        and column number. The lineNumber should never be greater that
        the number of physical lines per record.  When parsing the first
        field on a physical line as a delimited field, they should
        assume that the field data starts in the first column.
        Otherwise, follow the rules indicated under fieldDelimiter.
    :ivar quote_character: This element specifies a character to be used
        in the object for quoting values so that field delimiters can be
        used within the value. This basically allows delimiter
        "escaping". The quoteChacter is typically a " or '. When a
        processor encounters a quote character, it should not interpret
        any following characters as a delimiter until a matching quote
        character has been encountered (i.e., quotes come in pairs). It
        is an error to not provide a closing quote before the record
        ends. Non-printable quote characters can be provided as their
        hex values.
    :ivar literal_character: This element specifies a character to be
        used for escaping special character values so that they are
        treated as literal values.  This allows "escaping" for special
        characters like quotes, commas, and spaces when they are
        intended to be used in an attribute value rather than being
        intended as a delimiter. The literalCharacter is typically a \\.
    """
    class Meta:
        global_type = False

    field_delimiter: Optional[str] = field(
        default=None,
        metadata={
            "name": "fieldDelimiter",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "required": True,
        }
    )
    collapse_delimiters: Optional[DataFormatTextFormatComplexTextDelimitedCollapseDelimiters] = field(
        default=None,
        metadata={
            "name": "collapseDelimiters",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
        }
    )
    line_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "lineNumber",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
        }
    )
    quote_character: List[str] = field(
        default_factory=list,
        metadata={
            "name": "quoteCharacter",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    literal_character: List[str] = field(
        default_factory=list,
        metadata={
            "name": "literalCharacter",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class DataFormatTextFormatSimpleDelimited:
    """
    :ivar field_delimiter: This element specifies a character to be used
        in the object for indicating the ending column for an attribute.
        The delimiter character itself is not part of the attribute
        value, but rather is present in the column following the last
        character of the value. Typical delimiter characters include
        commas, tabs, spaces, and semicolons. The only time the
        fieldDelimiter character is not interpreted as a delimiter is if
        it is contained in a quoted string (see quoteCharacter) or is
        immediately preceded by a literalCharacter. Non-printable quote
        characters can be provided as their hex values, and for tab
        characters by its ASCII string "\\t". Processors should assume
        that the field starts in the column following the previous field
        if the previous field was fixed, or in the column following the
        delimiter from the previous field if the previous field was
        delimited.
    :ivar collapse_delimiters: The collapseDelimiters element specifies
        whether sequential delimiters should be treated as a single
        delimiter or multiple delimiters.    An example is when a space
        delimiter is used; often there may be several repeated spaces
        that should be treated as a single delimiter, but not always.
        The valid values are yes or no. If it is set to yes, then
        consecutive delimiters will be collapsed to one.  If set to no
        or absent, then consecutive delimiters will be treated as
        separate delimiters. Default behaviour is no; hence, consecutive
        delimiters will be treated as separate delimiters, by default.
    :ivar quote_character: This element specifies a character to be used
        in the object for quoting values so that field delimiters can be
        used within the value. This basically allows delimiter
        "escaping". The quoteChacter is typically a " or '. When a
        processor encounters a quote character, it should not interpret
        any following characters as a delimiter until a matching quote
        character has been encountered (i.e., quotes come in pairs). It
        is an error to not provide a closing quote before the record
        ends. Non-printable quote characters can be provided as their
        hex values.
    :ivar literal_character: This element specifies a character to be
        used for escaping special character values so that they are
        treated as literal values. This allows "escaping" for special
        characters like quotes, commas, and spaces when they are
        intended to be used in an attribute value rather than being
        intended as a delimiter.  The literalCharacter is typically a
        \\.
    """
    class Meta:
        global_type = False

    field_delimiter: List[str] = field(
        default_factory=list,
        metadata={
            "name": "fieldDelimiter",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "min_occurs": 1,
        }
    )
    collapse_delimiters: Optional[DataFormatTextFormatSimpleDelimitedCollapseDelimiters] = field(
        default=None,
        metadata={
            "name": "collapseDelimiters",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
        }
    )
    quote_character: List[str] = field(
        default_factory=list,
        metadata={
            "name": "quoteCharacter",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    literal_character: List[str] = field(
        default_factory=list,
        metadata={
            "name": "literalCharacter",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )


@dataclass
class Descriptor:
    """
    The descriptor field is used to document domains (themes) of interest such
    as climate, geology, soils or disturbances.
    """
    class Meta:
        name = "descriptor"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    descriptor_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "descriptorValue",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    citable_classification_system: Optional[bool] = field(
        default=None,
        metadata={
            "name": "citableClassificationSystem",
            "type": "Attribute",
        }
    )
    name: Optional[DescriptorEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class GeographicCoverage:
    """
    A container for spatial information about a resource; allows a bounding box
    for the overall coverage (in lat long), and also allows description of
    arbitrary polygons with exclusions.

    :ivar geographic_description: A short text description of a
        dataset's geographic areal domain. A text description is
        especially important to provide a geographic setting when the
        extent of the dataset cannot be well described by the
        "boundingCoordinates".
    :ivar bounding_coordinates: Bounding Coordinates are the four
        margins (N, S, E, W) of a bounding box, or when considered in
        lat-lon pairs, the corners of the box.
    """
    class Meta:
        name = "geographicCoverage"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    geographic_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "geographicDescription",
            "type": "Element",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    bounding_coordinates: Optional[GeographicCoverageBoundingCoordinates] = field(
        default=None,
        metadata={
            "name": "boundingCoordinates",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class I18NString:
    class Meta:
        name = "i18nString"
        target_namespace = "eml://ecoinformatics.org/eml-2.1.1"

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
class JgtiCuratorialUnit:
    """
    A quantitative descriptor (number of specimens, samples or batches).

    :ivar jgti_unit_type: A general description of the unit of curation,
        e.g., 'jar containing plankton sample';
    :ivar jgti_units: The exact number of units within the collection
    :ivar jgti_unit_range: A range of numbers (x to x), with the lower
        value representing an exact number, when the higher value is
        omitted.
    """
    class Meta:
        name = "jgtiCuratorialUnit"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    jgti_unit_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "jgtiUnitType",
            "type": "Element",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    jgti_units: Optional[JgtiCuratorialUnitJgtiUnits] = field(
        default=None,
        metadata={
            "name": "jgtiUnits",
            "type": "Element",
        }
    )
    jgti_unit_range: Optional[JgtiCuratorialUnitJgtiUnitRange] = field(
        default=None,
        metadata={
            "name": "jgtiUnitRange",
            "type": "Element",
        }
    )


@dataclass
class Online:
    """
    This element contains information for accessing the resource online
    represented as a URL connection.
    """
    class Meta:
        name = "online"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    url: Optional[Url] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Para:
    """
    The "paragraph" element allows for text blocks to be included in EML.
    """
    class Meta:
        name = "para"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ulink",
                    "type": Ulink,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class TaxonomicCoverage:
    """Taxonomic Coverage is a container for taxonomic information about a
    resource.

    It includes a list of species names (or higher level ranks) from one
    or more classification systems.

    :ivar general_taxonomic_coverage: A general description of the range
        of taxa addressed in the data set or collection
    :ivar taxonomic_classification: Information about the range of taxa
        addressed in the dataset or collection
    """
    class Meta:
        name = "taxonomicCoverage"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    general_taxonomic_coverage: Optional[str] = field(
        default=None,
        metadata={
            "name": "generalTaxonomicCoverage",
            "type": "Element",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    taxonomic_classification: List[TaxonomicCoverageTaxonomicClassification] = field(
        default_factory=list,
        metadata={
            "name": "taxonomicClassification",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class TemporalCoverage:
    """
    This field specifies temporal coverage, and allows coverages to be a single
    point in time, multiple points in time, or a range of dates.

    :ivar range_of_dates: The 'RangeOfDates' field is intended to be
        used for describing a range of dates and/or times. It may be
        used multiple times to document multiple date ranges. It allows
        for two 'singleDateTime' fields, the first to be used as the
        beginning dateTime, and the second to be used as the ending
        dateTime of the range.
    :ivar single_date_time: The SingleDateTime field is intended to
        describe a single date and time for an event
    """
    class Meta:
        name = "temporalCoverage"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    range_of_dates: Optional[TemporalCoverageRangeOfDates] = field(
        default=None,
        metadata={
            "name": "rangeOfDates",
            "type": "Element",
        }
    )
    single_date_time: Optional[Union[XmlPeriod, XmlDate]] = field(
        default=None,
        metadata={
            "name": "singleDateTime",
            "type": "Element",
        }
    )


@dataclass
class Abstract:
    """
    A brief overview describing the dataset.
    """
    class Meta:
        name = "abstract"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    para: List[Para] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class AdditionalInfo:
    """
    Any information that is not characterized by the other resource metadata
    fields.
    """
    class Meta:
        name = "additionalInfo"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    para: Optional[Para] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class AgentWithRoleType(AgentType):
    class Meta:
        name = "agentWithRoleType"
        target_namespace = "eml://ecoinformatics.org/eml-2.1.1"

    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Coverage:
    """
    Describes the extent of the coverage of the resource in terms of its
    spatial extent, temporal extent, and taxonomic extent.
    """
    class Meta:
        name = "coverage"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    geographic_coverage: List[GeographicCoverage] = field(
        default_factory=list,
        metadata={
            "name": "geographicCoverage",
            "type": "Element",
            "namespace": "",
        }
    )
    temporal_coverage: List[TemporalCoverage] = field(
        default_factory=list,
        metadata={
            "name": "temporalCoverage",
            "type": "Element",
            "namespace": "",
        }
    )
    taxonomic_coverage: List[TaxonomicCoverage] = field(
        default_factory=list,
        metadata={
            "name": "taxonomicCoverage",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class DataFormatTextFormatComplex:
    """
    :ivar text_fixed: Describes the physical format of data sequences
        that use a fixed number of characters in a specified position in
        the stream to locate attribute values. This method is common in
        sensor-derived data and in legacy database systems.  To parse
        it, one must know the number of characters for each attribute
        and the starting column and line to begin reading the value.
    :ivar text_delimited: Describes the physical format of data
        sequences that use delimiters in the stream to locate attribute
        values. This method is common in data exported from spreadsheets
        and database systems, To parse it, one must know the character
        that indicates the end of each attribute and the line to begin
        reading the value.
    """
    class Meta:
        global_type = False

    text_fixed: List[DataFormatTextFormatComplexTextFixed] = field(
        default_factory=list,
        metadata={
            "name": "textFixed",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
        }
    )
    text_delimited: List[DataFormatTextFormatComplexTextDelimited] = field(
        default_factory=list,
        metadata={
            "name": "textDelimited",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
        }
    )


@dataclass
class Description3:
    """
    The field Description contains general textual descriptions.
    """
    class Meta:
        name = "description"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "para",
                    "type": Para,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class Distribution:
    """This element provides information on how the resource is distributed.

    When used at the resource level, this element can provide only
    general information, but elements for describing connections to
    online systems are provided.
    """
    class Meta:
        name = "distribution"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    online: Optional[Online] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    scope: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class IntellectualRights:
    """
    Contain a rights management statement for the resource, or reference a
    service providing such information.
    """
    class Meta:
        name = "intellectualRights"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    para: Optional[Para] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class MethodsSamplingSamplingDescription:
    class Meta:
        global_type = False

    para: Optional[Para] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class ProjectFunding:
    class Meta:
        global_type = False

    para: Optional[Para] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class ProjectStudyAreaDescription:
    class Meta:
        global_type = False

    descriptor: Optional[Descriptor] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Purpose:
    """
    A description of the purpose of the resource/dataset.
    """
    class Meta:
        name = "purpose"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    para: Optional[Para] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Title2(I18NString):
    """The 'title' field provides a description of the resource that is being
    documented that is long enough to differentiate it from other similar
    resources.

    Multiple titles may be provided, particularly when trying to express
    the title in more than one language (use the "xml:lang" attribute to
    indicate the language if not English/en).
    """
    class Meta:
        name = "title"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"


@dataclass
class AssociatedParty(AgentWithRoleType):
    """A party associated with the resource.

    Parties have particular roles.
    """
    class Meta:
        name = "associatedParty"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"


@dataclass
class DataFormatTextFormat:
    """
    :ivar num_header_lines: Number of header lines preceding data.
        Lines are determined by the physicalLineDelimiter, or if it is
        absent, by the recordDelimiter.  This value indicated the number
        of header lines that should be skipped before starting to parse
        the data.
    :ivar num_footer_lines: Number of footer lines following data.
        Lines are determined by the physicalLineDelimiter, or if it is
        absent, by the recordDelimiter.  This value indicated the number
        of footer lines that should be skipped after parsing the data.
        If this value is omitted, parsers should assume the data
        continues to the end of the data stream.
    :ivar record_delimiter: This element specifies the record delimiter
        character when the format is text. The record delimiter is
        usually a linefeed (\\n) on UNIX, a carriage return (\\r) on
        MacOS, or both (\\r\\n) on Windows/DOS. Multiline records are
        usually delimited with two line ending characters, for example
        on UNIX it would be two linefeed characters (\\n\\n). As record
        delimiters are often non-printing characters, one can use either
        the special value "\\n" to represent a linefeed (ASCII 0x0a) and
        "\\r" to represent a carriage return (ASCII 0x0d).
        Alternatively, one can use the hex value to represent character
        values (e.g., 0x0a).
    :ivar physical_line_delimiter: This element specifies the physical
        line delimiter character when the format is text. The line
        delimiter is usually a linefeed (\\n) on UNIX, a carriage return
        (\\r) on MacOS, or both (\\r\\n) on Windows/DOS. Multiline
        records are usually delimited with two line ending characters,
        for example on UNIX it would be two linefeed characters
        (\\n\\n). As line delimiters are often non-printing characters,
        one can use either the special value "\\n" to represent a
        linefeed (ASCII 0x0a) and "\\r" to represent a carriage return
        (ASCII 0x0d).  Alternatively, one can use the hex value to
        represent character values (e.g., 0x0a). If this value is not
        provided, processors should assume that the physical line
        delimiter is the same as the record delimiter.
    :ivar num_physical_lines_per_record: A single logical data record
        may be written over several physical lines in a file, with no
        special marker to indicate the end of a record. In such cases,
        it is necessary to know the number of lines per record in order
        to correctly read them. If this value is not provided,
        processors should assume that records are wholly contained on
        one physical line.  If the value is greater than 1, then
        processors should examine the lineNumber field for each
        attribute to determine which line of the record contains the
        information.
    :ivar max_record_length: The maximum number of characters in any
        record in the physical file.  For delimited files, the record
        length varies and this is not particularly useful.  However, for
        fixed format files that do not contain record delimiters, this
        field is critical to tell processors when one record stops and
        another begins.
    :ivar attribute_orientation: Specifies whether the attributes
        described in the physical stream are found in columns or rows.
        The valid values are column or row. If set to 'column', then the
        attributes are in columns. If set to 'row', then the attributes
        are in rows.  Row orientation is rare,  but some systems such as
        SPlus and R utilize it. For example, some data with column
        orientation: DATE          PLOT           SPECIES 2002-01-15
        hfr5           acer rubrum 2002-01-15    hfr5           acer
        xxxx The same data in a rowMajor table: DATE   2002-01-15 PLOT
        hfr5 SPECIES acer rubrum  acer xxxx
    :ivar simple_delimited: A simple delimited format that uses one of a
        series of delimiters to indicate the ends of fields in the data
        stream. More complex formats such as fixed format or mixed
        delimited and fixed formats can be described using the "complex"
        element.
    :ivar complex: A complex text format that can describe delimited
        fields, fixed width fields, and mixtures of the two. This
        supports multiline records (where one record is distributed
        across multiple physical lines).  When using the complex format,
        the number of textFixed and textDelimited elements should
        exactly equal the number of attributes that have been described
        for the entity, and the order of the textFixed and textDelimited
        elements should correspond to the order of the attributes as
        described in the entity. Thus, for a delimited file with
        fourteen attributes, one should provide exactly fourteen
        textDelimited elements.
    """
    class Meta:
        global_type = False

    num_header_lines: Optional[int] = field(
        default=None,
        metadata={
            "name": "numHeaderLines",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
        }
    )
    num_footer_lines: Optional[int] = field(
        default=None,
        metadata={
            "name": "numFooterLines",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
        }
    )
    record_delimiter: List[str] = field(
        default_factory=list,
        metadata={
            "name": "recordDelimiter",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
        }
    )
    physical_line_delimiter: List[str] = field(
        default_factory=list,
        metadata={
            "name": "physicalLineDelimiter",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
        }
    )
    num_physical_lines_per_record: Optional[int] = field(
        default=None,
        metadata={
            "name": "numPhysicalLinesPerRecord",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
        }
    )
    max_record_length: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxRecordLength",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
        }
    )
    attribute_orientation: Optional[DataFormatTextFormatAttributeOrientation] = field(
        default=None,
        metadata={
            "name": "attributeOrientation",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "required": True,
        }
    )
    simple_delimited: Optional[DataFormatTextFormatSimpleDelimited] = field(
        default=None,
        metadata={
            "name": "simpleDelimited",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
        }
    )
    complex: Optional[DataFormatTextFormatComplex] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
        }
    )


@dataclass
class DatasetMaintenance:
    class Meta:
        global_type = False

    description: Optional[Description3] = field(
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
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "required": True,
        }
    )


@dataclass
class Description2:
    class Meta:
        name = "description"
        target_namespace = "eml://ecoinformatics.org/eml-2.1.1"

    description: Optional[Description3] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class MethodsSampling:
    """
    :ivar study_extent: The field studyExtent represents both a specific
        sampling area and the sampling frequency (temporal boundaries,
        frequency of occurrence). The geographic studyExtent is usually
        a surrogate (representative area of) for the larger area
        documented in the "studyAreaDescription".
    :ivar sampling_description: The samplingDescription field allows for
        a text-based/human readable description of the sampling
        procedures used in the research project. The content of this
        element would be similar to a description of sampling procedures
        found in the methods section of a journal article.
    """
    class Meta:
        global_type = False

    study_extent: Optional[Description3] = field(
        default=None,
        metadata={
            "name": "studyExtent",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "required": True,
        }
    )
    sampling_description: Optional[MethodsSamplingSamplingDescription] = field(
        default=None,
        metadata={
            "name": "samplingDescription",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "required": True,
        }
    )


@dataclass
class Project:
    """The project field contains information on the project in which this
    dataset was collected.

    It includes information such as project personnel, funding, study
    area, project design and related projects.

    :ivar title:
    :ivar personnel: The Personnel field extends ResponsibleParty with
        role information and is used to document people involved in a
        research project by providing contact information and their role
        in the project.
    :ivar abstract:
    :ivar funding: The funding field is used to provide information
        about funding sources for the project such as: grant and
        contract numbers; names and addresses of funding sources.
    :ivar study_area_description: The studyAreaDescription field
        documents the physical area associated with the research
        project. It can include descriptions of the geographic,
        temporal, and taxonomic coverage of the research location and
        descriptions of domains (themes) of interest such as climate,
        geology, soils or disturbances.
    :ivar design_description: The field designDescription contains
        general textual descriptions of research design. It can include
        detailed accounts of goals, motivations, theory, hypotheses,
        strategy, statistical design, and actual work.
    :ivar id: A unique identifier for the project. This can be used to
        link multiple datasets that are associated in some way with the
        same project.
    """
    class Meta:
        name = "project"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    title: Optional[Title2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    personnel: List[AgentWithRoleType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    abstract: Optional[Abstract] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    funding: Optional[ProjectFunding] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    study_area_description: Optional[ProjectStudyAreaDescription] = field(
        default=None,
        metadata={
            "name": "studyAreaDescription",
            "type": "Element",
        }
    )
    design_description: Optional[Description3] = field(
        default=None,
        metadata={
            "name": "designDescription",
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DataFormat:
    """
    This is a container element for other elements which describe the internal
    physical characteristics of the data object.

    :ivar text_format: Description of a text formatted object. The
        description includes detailed parsing instructions for
        extracting attributes from the bytestream for simple delimited
        file formats (e.g., CSV), fixed format files that use fixed
        columns for attribute locations, and mixtures of the two.  It
        also supports records that span multiple lines.
    :ivar externally_defined_format: Information about a non-text or
        proprietary formatted object.
    """
    class Meta:
        name = "dataFormat"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    text_format: Optional[DataFormatTextFormat] = field(
        default=None,
        metadata={
            "name": "textFormat",
            "type": "Element",
        }
    )
    externally_defined_format: Optional[DataFormatExternallyDefinedFormat] = field(
        default=None,
        metadata={
            "name": "externallyDefinedFormat",
            "type": "Element",
        }
    )


@dataclass
class Methods:
    """The methods field documents scientific methods used in the collection of
    this dataset.

    It includes information on items such as tools, instrument
    calibration and software.

    :ivar method_step: The methodStep field allows for repeated sets of
        elements that document a series of procedures followed to
        produce a data object. These include text descriptions of the
        procedures, relevant literature, software, instrumentation,
        source data and any quality control measures taken.
    :ivar sampling: Description of sampling procedures including the
        geographic, temporal and taxonomic coverage of the study.
    :ivar quality_control: The qualityControl field provides a location
        for the description of actions taken to either control or assess
        the quality of data resulting from the associated method step.
    """
    class Meta:
        name = "methods"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    method_step: List[Description3] = field(
        default_factory=list,
        metadata={
            "name": "methodStep",
            "type": "Element",
            "min_occurs": 1,
            "sequential": True,
        }
    )
    sampling: List[MethodsSampling] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    quality_control: List[Description3] = field(
        default_factory=list,
        metadata={
            "name": "qualityControl",
            "type": "Element",
            "sequential": True,
        }
    )


@dataclass
class AdditionalMetadataMetadataGbifPhysical:
    class Meta:
        global_type = False

    object_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "objectName",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
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
    data_format: Optional[DataFormat] = field(
        default=None,
        metadata={
            "name": "dataFormat",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    distribution: Optional[Distribution] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Dataset:
    """
    The dataset element is a wrapper for all other elements relating to a
    single dataset.

    :ivar alternate_identifier:
    :ivar title:
    :ivar creator: The creator is the person who created the resource
        (not necessarily the author of this metadata about the
        resource). This is the person or institution to contact with
        questions about the use, interpretation of a dataset.
    :ivar metadata_provider: The party responsible for the creation of
        the metadata document
    :ivar associated_party:
    :ivar pub_date:
    :ivar language:
    :ivar abstract:
    :ivar keyword_set:
    :ivar additional_info:
    :ivar intellectual_rights:
    :ivar distribution:
    :ivar coverage:
    :ivar purpose:
    :ivar maintenance:
    :ivar contact:
    :ivar methods:
    :ivar project:
    """
    class Meta:
        name = "dataset"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    alternate_identifier: List[str] = field(
        default_factory=list,
        metadata={
            "name": "alternateIdentifier",
            "type": "Element",
            "namespace": "",
        }
    )
    title: List[Title2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    creator: List[AgentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    metadata_provider: List[AgentType] = field(
        default_factory=list,
        metadata={
            "name": "metadataProvider",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    associated_party: List[AssociatedParty] = field(
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
            "required": True,
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    abstract: Optional[Abstract] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    keyword_set: List[KeywordSet] = field(
        default_factory=list,
        metadata={
            "name": "keywordSet",
            "type": "Element",
            "namespace": "",
        }
    )
    additional_info: Optional[AdditionalInfo] = field(
        default=None,
        metadata={
            "name": "additionalInfo",
            "type": "Element",
            "namespace": "",
        }
    )
    intellectual_rights: Optional[IntellectualRights] = field(
        default=None,
        metadata={
            "name": "intellectualRights",
            "type": "Element",
            "namespace": "",
        }
    )
    distribution: Optional[Distribution] = field(
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
    purpose: Optional[Purpose] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    maintenance: Optional[DatasetMaintenance] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    contact: List[AgentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    methods: Optional[Methods] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    project: Optional[Project] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class AdditionalMetadataMetadataGbif:
    """
    :ivar date_stamp: The date the metadata document was created or
        modified.
    :ivar hierarchy_level:
    :ivar citation: A single citation for use when citing the dataset
    :ivar bibliography: A list of citations that form a bibliography on
        literature related / used in the dataset
    :ivar physical: A container element for all of the elements that let
        you describe the internal/external characteristics and
        distribution of a data object (e.g., dataObject, dataFormat,
        distribution) .
    :ivar resource_logo_url: URL of the logo associated with a resource
    :ivar collection: A container element for other elements associated
        with collections (e.g., collectionIdentifier, collectionName).
    :ivar formation_period: Text description of the time period during
        which the collection was assembled e.g. "Victorian", or "1922 -
        1932", or "c. 1750".
    :ivar specimen_preservation_method: Picklist keyword indicating the
        process or technique used to prevent physical deterioration of
        non-living collections. Expected to contain a value from the
        GBIF Specimen Preservation Method vocabulary
    :ivar living_time_period: Time period during which biological
        material was alive. (for palaeontological collections)
    :ivar jgti_curatorial_unit:
    :ivar replaces: Pointer to previous version of the document
    """
    class Meta:
        global_type = False

    date_stamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "dateStamp",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "required": True,
        }
    )
    hierarchy_level: Optional[str] = field(
        default=None,
        metadata={
            "name": "hierarchyLevel",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    citation: Optional[CitationType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
        }
    )
    bibliography: Optional[AdditionalMetadataMetadataGbifBibliography] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
        }
    )
    physical: List[AdditionalMetadataMetadataGbifPhysical] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
        }
    )
    resource_logo_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "resourceLogoUrl",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
        }
    )
    collection: List[AdditionalMetadataMetadataGbifCollection] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
        }
    )
    formation_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "formationPeriod",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    specimen_preservation_method: List[str] = field(
        default_factory=list,
        metadata={
            "name": "specimenPreservationMethod",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    living_time_period: List[str] = field(
        default_factory=list,
        metadata={
            "name": "livingTimePeriod",
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        }
    )
    jgti_curatorial_unit: List[JgtiCuratorialUnit] = field(
        default_factory=list,
        metadata={
            "name": "jgtiCuratorialUnit",
            "type": "Element",
            "namespace": "",
        }
    )
    replaces: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
        }
    )


@dataclass
class AdditionalMetadataMetadata:
    """
    :ivar gbif: A block of additional metadata used for some special
        GBIF purposes and crossmapping to other schemas like the TDWG
        Natural Collection Data (NCD) schema
    """
    class Meta:
        global_type = False

    gbif: Optional[AdditionalMetadataMetadataGbif] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "eml://ecoinformatics.org/eml-2.1.1",
            "required": True,
        }
    )


@dataclass
class AdditionalMetadata:
    """A flexible field for including any other relevant metadata that pertains
    to the resource being described.

    This field allows EML to be extensible in that any XML-based
    metadata can be included in this element.

    :ivar metadata: This element contains the additional metadata to be
        included in the document. This element should be used for
        extending EML to include metadata that is not already available
        in another part of the EML specification.
    """
    class Meta:
        name = "additionalMetadata"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    metadata: Optional[AdditionalMetadataMetadata] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Eml:
    """
    :ivar dataset:
    :ivar additional_metadata:
    :ivar package_id: Unique global ID for this exact version of the EML
        document
    :ivar scope:
    :ivar system:
    :ivar lang: The language in which the metadata (as opposed to the
        resource being described by the metadata) is written
    """
    class Meta:
        name = "eml"
        namespace = "eml://ecoinformatics.org/eml-2.1.1"

    dataset: Optional[Dataset] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    additional_metadata: Optional[AdditionalMetadata] = field(
        default=None,
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
    scope: str = field(
        init=False,
        default="system",
        metadata={
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
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
