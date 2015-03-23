try:
    import Log  # @UnresolvedImport # pylint: disable=F0401
except ImportError:
    # Skip dummy import
    pass
def get_xml_text_value(xml_node, xpath, default_value=None):
    '''
    Get the text value for an XML element, return a specified default value if that element is not found.
    :param xml_element: The XML element on which we will evaluate the XPATH expression.
    :type xml_element: xml.etree.Element
    :param xpath: The XPATH expression used to get the XML element value.
    :type xpath: str
    :param default_value: (Optional) The value to be returned if the XPATH expression is invalid.
    :return: Text value for the specified XPATH expression, or the specified default value if that XPATH expression does not contain a text value.
    '''
    if xml_node != None:
        try:
            return xml_node.xpath("./" + xpath)[0].text
        except IndexError:
#             Log.Debug("Could not find text value for XML element using XPath expression '%s' under XML node '%s', returning default value '%s'", "./" + xpath, repr(xml_node), default_value)
            return default_value
    else:
        raise ValueError("xml_element cannot be None.")

def get_xml_int_value(xml_node, xpath, default_value=None):
    text_value = get_xml_text_value(xml_node, xpath, default_value)
    if text_value != None:
        return int(text_value)
    else:
        return text_value

def get_xml_node(xml_node, xpath, optional=False):
    '''
    Get a specified XML node using XPATH.
    :param xml_element: The XML element on which we will evaluate the XPATH expression.
    :type xml_element: xml.etree.Element
    :param xpath: The XPATH expression used to get the XML node.
    :type xpath: str
    @raise ValueError: If the XPATH expression could not be resolved to an XML node. 
    '''
    Log.Debug("Getting XML node from XML element: '%s'", repr(xml_node))
    found_node = xml_node.find(xpath)
    if found_node == None and not optional:
        message = "Could not find XML element using XPath expression '%s' under XML node '%s'", xpath, repr(xml_node)
        Log.Error(message)
        raise ValueError(message)
    return found_node
