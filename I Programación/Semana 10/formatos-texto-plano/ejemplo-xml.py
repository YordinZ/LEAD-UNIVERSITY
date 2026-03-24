import xml.etree.ElementTree as ET

tree = ET.parse("data/datos.xml")

root = tree.getroot()

for hijo in root:
    print(hijo.tag, hijo.text)