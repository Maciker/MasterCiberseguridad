import xml.etree.ElementTree as ET

tree = ET.parse('scan.xml')
root = tree.getroot()

for child in root:
   for addr in child.findall('address'):
       print(addr.get('addr'))