from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from eml.eml_2_1_1 import Eml, Dataset, ParagraphType, ParagraphTypeUlink, Person, ResourceGroupKeywordSet, ResponsibleParty, TextType

doc = Eml(
    package_id="http://ipt.vliz.be/kmfri/resource?id=vegetation_gazi_bay_kenya_1987/v1.0",
    system="http://gbif.org",
    lang="eng",
    dataset=Dataset(
        title="Test dataset",
        abstract=TextType(content=[ParagraphType(content=["Suspendisse imperdiet imperdiet leo, at eleifend nisi rutrum eget. Donec aliquam mollis risus, feugiat laoreet nulla facilisis vel. Fusce viverra magna ante, ut lobortis sapien convallis ut. Nulla facilisi. Cras at tellus leo. Suspendisse eget blandit tellus. Duis auctor turpis eros. Nullam convallis ligula eleifend volutpat aliquam. Donec cursus mattis viverra. Nunc ac lorem vel lectus malesuada bibendum. Vestibulum non dolor quis enim auctor consectetur in a augue. Maecenas sodales ullamcorper quam."])]),
        alternate_identifier="http://ipt.vliz.be/kmfri/resource?id=vegetation_gazi_bay_kenya_1987/v1.0",
        creator=ResponsibleParty(individual_name=[Person(given_name="Pieter", sur_name="Provoost")]),
        keyword_set=[ResourceGroupKeywordSet(keyword="test")],
        intellectual_rights=TextType(content=[
            ParagraphType(content=[
                "This work is licensed under a ",
                ParagraphTypeUlink(
                    url="http://creativecommons.org/licenses/by/4.0/legalcode",
                    content=["Creative Commons Attribution (CC-BY) 4.0 License"]
                ),
                "."
            ])
        ])
    )
)

config = SerializerConfig(pretty_print=True)
serializer = XmlSerializer(config=config)
print(serializer.render(doc))
