import unittest

from block_markdown import BlockType, block_to_block_type, markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """This is **bolded** paragraph

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

    def test_markdown_to_blocks_with_extra_newlines(self):
        md = """This is **bolded** paragraph




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

    # Test block_to_block_type with heading block
    def test_block_to_block_type_heading(self):
        block = "###### This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADER)

    # Test block_to_block_type with code block
    def test_block_to_block_type_code(self):
        block = "```\nThis is a code block\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    # Test block_to_block_type with quote block
    def test_block_to_block_type_quote(self):
        block = "> This is a quote block"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    # Test block_to_block_type with unordered list block
    def test_block_to_block_type_unordered_list(self):
        block = "- This is an unordered list block"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    # Test block_to_block_type with ordered list block
    def test_block_to_block_type_ordered_list(self):
        block = "1. This is an ordered list block"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    # Test block_to_block_type with paragraph block
    def test_block_to_block_type_paragraph(self):
        block = "This is a paragraph block"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
