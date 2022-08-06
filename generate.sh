xsdata generate --package eml --structure-style single-package --unnest-classes xsd/eml-2.1.1/eml.xsd
mv eml.py ./eml/eml_2_1_1/__init__.py
rm __init__.py

xsdata generate --package eml --structure-style single-package --unnest-classes xsd/eml-2.2.0/eml.xsd
mv eml.py ./eml/eml_2_2_0/__init__.py
rm __init__.py

xsdata generate --package eml --structure-style single-package --unnest-classes http://rs.gbif.org/schema/eml-gbif-profile/1.1/eml.xsd
mv eml.py ./eml/gbif_1_1/__init__.py
rm __init__.py
