import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_empty(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_markdown_to_blocks_no_newline(self):
        md = "This is a single paragraph without newlines"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is a single paragraph without newlines"])

    def test_markdown_to_blocks_multiple_newlines(self):
        md = "\n\n\nThis is a paragraph after multiple newlines"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is a paragraph after multiple newlines"])

    # test block_to_block_type
    def test_block_to_block_type_paragraph(self):
        blocks = ["This is a paragraph"]
        block_type = block_to_block_type(blocks)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_heading(self):
        blocks = ["# This is a heading"]
        block_type = block_to_block_type(blocks)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_block_to_block_type_code(self):
        blocks = ["```", "print('Hello, World!')", "```"]
        block_type = block_to_block_type(blocks)
        self.assertEqual(block_type, BlockType.CODE)

    def test_block_to_block_type_quote(self):
        blocks = ["> This is a quote", "> with multiple lines"]
        block_type = block_to_block_type(blocks)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_block_to_block_type_unordered_list(self):
        blocks = ["- This is an unordered list", "- with multiple items"]
        block_type = block_to_block_type(blocks)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_block_to_block_type_ordered_list(self):
        blocks = ["1. This is an ordered list", "2. with multiple items"]
        block_type = block_to_block_type(blocks)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

if __name__ == "__main__":
    unittest.main()
