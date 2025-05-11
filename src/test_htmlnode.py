import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode("div", "This is a div", None, {"class": "test"})
        self.assertEqual(node.props_to_html(), ' class="test"')

    def test_default(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        node = HTMLNode("a", "This is a link", None, {"href": "http://example.org", "target": "_blank"})
        node2 = "HTMLNode(tag=a, value=This is a link, children=None, props={'href': 'http://example.org', 'target': '_blank'})"
        self.assertEqual(repr(node), node2)

    def test_children(self):
        node = HTMLNode("div", "This is a div", [HTMLNode("span", "This is a span")], {"class": "test"})
        self.assertEqual(node.children[0].tag, "span")

    def test_children_two_levels(self):
        node = HTMLNode("div", "This is a div", [HTMLNode("span", "This is a span", [HTMLNode("a", "This is a link")])], {"class": "test"})
        self.assertEqual(node.children[0].children[0].tag, "a")

if __name__ == "__main__":
    unittest.main()