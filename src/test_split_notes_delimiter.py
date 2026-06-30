import unittest

from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_one_code(self):
        nodes_to_split: list[TextNode] = [
            TextNode("This is a `code` text", TextType.PLAIN_TEXT),
        ]
        splitted_nodes: list[TextNode] = [
            TextNode("This is a ", TextType.PLAIN_TEXT),
            TextNode("code", TextType.CODE_TEXT),
            TextNode(" text", TextType.PLAIN_TEXT)
        ]
        self.assertEqual(split_nodes_delimiter(nodes_to_split, "`", TextType.CODE_TEXT), splitted_nodes)

    def test_one_italic(self):
        nodes_to_split: list[TextNode] = [
            TextNode("This is a _code_ text", TextType.PLAIN_TEXT),
        ]
        splitted_nodes: list[TextNode] = [
            TextNode("This is a ", TextType.PLAIN_TEXT),
            TextNode("code", TextType.ITALIC_TEXT),
            TextNode(" text", TextType.PLAIN_TEXT)
        ]
        self.assertEqual(split_nodes_delimiter(nodes_to_split, "_", TextType.ITALIC_TEXT), splitted_nodes)

    def test_no_plain(self):
        nodes_to_split: list[TextNode] = [
            TextNode("This is not plain", TextType.BOLD_TEXT)
        ]
        self.assertEqual(split_nodes_delimiter(nodes_to_split, "**", TextType.BOLD_TEXT), nodes_to_split)

    def test_mult_bold(self):
        nodes_to_split: list[TextNode] = [
            TextNode("This is **multi** bold letters **node**.", TextType.PLAIN_TEXT),
        ]
        splitted_nodes: list[TextNode] = [
            TextNode("This is ", TextType.PLAIN_TEXT),
            TextNode("multi", TextType.BOLD_TEXT),
            TextNode(" bold letters ", TextType.PLAIN_TEXT),
            TextNode("node", TextType.BOLD_TEXT),
            TextNode(".", TextType.PLAIN_TEXT)
        ]
        result_nodes = split_nodes_delimiter(nodes_to_split, "**", TextType.BOLD_TEXT)
        self.assertEqual(result_nodes, splitted_nodes)

    def test_with_start_delimiter(self):
        nodes_to_split: list[TextNode] = [
            TextNode("**this** is a delimiter in the start", TextType.PLAIN_TEXT),
        ]
        splitted_nodes: list[TextNode] = [
            TextNode("this", TextType.BOLD_TEXT),
            TextNode(" is a delimiter in the start", TextType.PLAIN_TEXT)
        ]
        result_nodes = split_nodes_delimiter(nodes_to_split, "**", TextType.BOLD_TEXT)
        self.assertEqual(result_nodes, splitted_nodes)

    def test_with_end_delimiter(self):
        nodes_to_split: list[TextNode] = [
            TextNode("this has a delimiter in the _end_", TextType.PLAIN_TEXT)
        ]
        splitted_nodes: list[TextNode] = [
            TextNode("this has a delimiter in the ", TextType.PLAIN_TEXT),
            TextNode("end", TextType.ITALIC_TEXT),
        ]
        result_nodes = split_nodes_delimiter(nodes_to_split, "_", TextType.ITALIC_TEXT)
        self.assertEqual(result_nodes, splitted_nodes)

    def test_with_start_end_delimiter(self):
        nodes_to_split: list[TextNode] = [
            TextNode("`this has` a start and `end delimiter`", TextType.PLAIN_TEXT)
        ]
        splitted_nodes: list[TextNode] = [
            TextNode("this has", TextType.CODE_TEXT),
            TextNode(" a start and ", TextType.PLAIN_TEXT),
            TextNode("end delimiter", TextType.CODE_TEXT)
        ]
        result_nodes = split_nodes_delimiter(nodes_to_split, "`", TextType.CODE_TEXT)
        self.assertEqual(result_nodes, splitted_nodes)

if __name__ == "__main__":
    unittest.main()
