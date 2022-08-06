# eml

This Python package contains dataclasses generated using [xsdata](https://xsdata.readthedocs.io/) for the [Ecological Metadata Language (EML)](https://eml.ecoinformatics.org/) standard as well its GBIF profile.

## Quick start

```python
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from eml.gbif_1_1 import AgentType, Eml, Dataset, IndividualName, IntellectualRights, KeywordSet, Para, Ulink, Abstract

doc = Eml(
    package_id="http://ipt.vliz.be/kmfri/resource?id=vegetation_gazi_bay_kenya_1987/v1.0",
    system="http://gbif.org",
    lang="eng",
    dataset=Dataset(
        title="Test dataset",
        abstract=Abstract([Para(["Suspendisse imperdiet imperdiet leo, at eleifend nisi rutrum eget. Donec aliquam mollis risus, feugiat laoreet nulla facilisis vel. Fusce viverra magna ante, ut lobortis sapien convallis ut. Nulla facilisi. Cras at tellus leo. Suspendisse eget blandit tellus. Duis auctor turpis eros. Nullam convallis ligula eleifend volutpat aliquam. Donec cursus mattis viverra. Nunc ac lorem vel lectus malesuada bibendum. Vestibulum non dolor quis enim auctor consectetur in a augue. Maecenas sodales ullamcorper quam."])]),
        alternate_identifier="http://ipt.vliz.be/kmfri/resource?id=vegetation_gazi_bay_kenya_1987/v1.0",
        creator=AgentType(individual_name=[IndividualName("John", "Doe")]),
        keyword_set=KeywordSet(keyword=["test keyword"]),
        intellectual_rights=IntellectualRights(
            para=Para(
                [
                    "This work is licensed under a ",
                    Ulink(
                        url="http://creativecommons.org/licenses/by/4.0/legalcode",
                        content=["Creative Commons Attribution (CC-BY) 4.0 License"]
                    ),
                    "."
                ]
            )
        ),
    )
)

config = SerializerConfig(pretty_print=True)
serializer = XmlSerializer(config=config)
print(serializer.render(doc))
```
