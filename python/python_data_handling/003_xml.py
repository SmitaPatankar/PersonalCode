# read big
# https://stackoverflow.com/a/326541/10064174
from lxml import etree
context = etree.iterparse("C:/REPOSITORIES/MyRepo/python/python_big_files_handling_web_scraping/sample.xml")
for index, (event, elem) in enumerate(context):
    if index == 0:
        root = elem
    if elem.tag == "book":
        print(elem.find("author").text)
        root.clear()

# write big
# https://stackoverflow.com/a/42800982/10064174
from lxml.etree import Element, SubElement, ElementTree

def get_data():
    yield ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    yield ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']      
    yield ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2']      
    yield ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3']      
    yield ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4']      
    yield ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'] 

with open('C:/REPOSITORIES/MyRepo/.trash/output.xml', 'wb') as outxml:
    outxml.write(b"""<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>\n<root>\n""")
    for num, data in enumerate(get_data()):
        if num > 0:
            a, b, c, d, e, f, g, h = data
            outxml.write(b"\n")
            element = Element('element', {'a':a})
            sub_element = SubElement(element, 'sub_element')
            sub_sub_element_1 = SubElement(sub_element, 'sub_sub_element_1', {'b':b, 'c':c, 'd':d,})
            sub_sub_element_2 = SubElement(sub_element, 'sub_sub_element_2', {'e': e,})
            sub_sub_element_3 = SubElement(sub_element, 'sub_sub_element_3',{'f': f, 'g': g, 'h': h,})
            ElementTree(element).write(outxml, encoding='utf-8',  method='xml',  pretty_print=True)
    outxml.write(b"""\n</root>""")
