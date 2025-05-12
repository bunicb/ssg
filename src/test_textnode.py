import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_non_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a link node", TextType.LINK, "http://example.org")
        self.assertNotEqual(node, node2)

    def test_type_non_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.NORMAL)
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node2)

    def test_string_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    # test inline markdown
    def test_split_nodes_delimiter(self):
        old_nodes = [ "This is text with a **bolded phrase** in the middle" ]
        delimiter = "**"
        text_type = TextType.BOLD
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("bolded phrase", TextType.BOLD),
                TextNode(" in the middle", TextType.NORMAL),
            ]
        )

    def test_split_nodes_markdown_invalid(self):
        old_nodes = [ "This is text with a **bolded phrase in the middle" ]
        delimiter = "**"
        text_type = TextType.BOLD
        with self.assertRaises(Exception):
            split_nodes_delimiter(old_nodes, delimiter, text_type)

    def test_split_nodes_markdown_empty(self):
        old_nodes = [ "" ]
        delimiter = "**"
        text_type = TextType.BOLD
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(
            new_nodes,
            [
                TextNode("", TextType.NORMAL),
            ]
        )

    def test_split_nodes_markdown_empty_delimiter(self):
        old_nodes = [ "This is text with a bolded phrase in the middle" ]
        delimiter = ""
        text_type = TextType.BOLD
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a bolded phrase in the middle", TextType.NORMAL),
            ]
        )

    def test_split_existing_nodes_delimiter(self):
        old_nodes = [ 
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.NORMAL)
         ]
        delimiter = "**"
        text_type = TextType.BOLD
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("bolded phrase", TextType.BOLD),
                TextNode(" in the middle", TextType.NORMAL),
            ]
        )

    # test markdown extraction
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://example.com)"
        )
        self.assertListEqual([("link", "https://example.com")], matches)

    def test_extract_markdown_links_no_link(self):
        matches = extract_markdown_links(
            "This is text with a ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_images_no_image(self):
        matches = extract_markdown_images(
            "This is text with a [link](https://example.com)"
        )
        self.assertListEqual([], matches)

    def test_extract_links_matches(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and ![image](https://i.imgur.com/zjjcJKZ.png)."
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_extract_images_matches(self):
        matches = extract_markdown_images(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and ![image](https://i.imgur.com/zjjcJKZ.png)."
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

if __name__ == "__main__":
    unittest.main()