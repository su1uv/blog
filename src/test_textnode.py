import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This text does not have a url", TextType.PLAIN_TEXT)
        self.assertEqual(node.url, None)

    def test_url_not_eq(self):
        node = TextNode("This text does not have a url", TextType.PLAIN_TEXT)
        node2 = TextNode(
            "This text does not have a url",
            TextType.PLAIN_TEXT,
            "https://www.mytesturl.com",
        )
        self.assertNotEqual(node, node2)

    def test_text_type_not_eq(self):
        node = TextNode("Test code", TextType.LINK)
        node2 = TextNode("Test code", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_bold(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()
