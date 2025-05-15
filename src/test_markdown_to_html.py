import unittest
from markdown_to_html import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_blockquote(self):
        md = """
> This is a quote
> with a new line
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote\nwith a new line</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """
- This is a list
- with items
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. This is a list
2. with items
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is a list</li><li>with items</li></ol></div>",
        )

    def test_heading(self):
        md = """
# This is a heading

## This is a subheading

### This is a sub-subheading

#### This is a sub-sub-subheading

##### This is a sub-sub-sub-subheading

###### This is a sub-sub-sub-sub-subheading
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is a heading</h1><h2>This is a subheading</h2><h3>This is a sub-subheading</h3><h4>This is a sub-sub-subheading</h4><h5>This is a sub-sub-sub-subheading</h5><h6>This is a sub-sub-sub-sub-subheading</h6></div>",
        )

if __name__ == "__main__":
    unittest.main()