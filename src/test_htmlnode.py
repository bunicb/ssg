import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    # HTMLNode tests
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

    # LeafNode tests
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")  

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_no_tag_no_value(self):
        node = LeafNode(None, None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_leaf_to_html_with_props(self):
        node = LeafNode("a", "This is a link", {"href": "http://example.org"})
        self.assertEqual(node.to_html(), '<a href="http://example.org">This is a link</a>')

    # ParentNode tests
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"class": "test"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="test"><span>child</span></div>',
        )

    def test_to_html_many_children(self):
        child_node1 = LeafNode("b", "Bold text")
        child_node2 = LeafNode(None, "Normal text")
        child_node3 = LeafNode("i", "Italic text")
        child_node4 = LeafNode(None, "Normal text")
        parent_node = ParentNode("p", [child_node1, child_node2, child_node3, child_node4])
        self.assertEqual(
            parent_node.to_html(),
            "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>",
        )

    def test_to_html_no_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_no_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_to_html_no_tag_no_children(self):
        parent_node = ParentNode(None, None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_no_tag_no_children_props(self):
        parent_node = ParentNode(None, None, {"class": "test"})
        with self.assertRaises(ValueError):
            parent_node.to_html()

if __name__ == "__main__":
    unittest.main()