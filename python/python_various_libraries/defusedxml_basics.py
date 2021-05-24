from defusedxml import ElementTree as ETree

# xml = "xml file path"
# tree = ETree.parse(xml)

xml = """<?xml version="1.0" encoding="UTF-8"?>
<ServiceResponse xmlns:xsi="xxxx" xsi:noNamespaceSchemaLocation="yyyy">
  <responseCode>SUCCESS</responseCode>
  <data>
    <Element>
      <ID>1</ID>
      <NAME>Smita</NAME>
      <ADDITIONAL_DETAILS>
          <PHONE>12345</PHONE>
      </ADDITIONAL_DETAILS>
    </Element>
    <Element>
      <NAME>Neha</NAME>
      <ADDITIONAL_DETAILS>
          <PHONE>56789</PHONE>
      </ADDITIONAL_DETAILS>
    </Element>
  </data>
</ServiceResponse>"""
tree = ETree.fromstring(xml)

for element in tree.iter("Element"):
    values = [
        element.find(field).text if element.find(field) is not None else ""
        for field in ["ID", "NAME"]
    ]
    values.append(
        element.find("ADDITIONAL_DETAILS")
            .find("PHONE")
            .text
    )
    print(values)

# ['1', 'Smita', '12345']
# ['', 'Neha', '56789']
