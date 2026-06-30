from enum import Enum

from htmlnode import LeafNode


class TextType(Enum):
    PLAIN_TEXT = "plain"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str | None = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other) -> bool:
        are_equal: bool = (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

        return are_equal

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type not in TextType:
        raise Exception("text_type is not a valid TextType")

    match text_node.text_type:
        case TextType.PLAIN_TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD_TEXT:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC_TEXT:
            return LeafNode("i", text_node.text)
        case TextType.CODE_TEXT:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            if not text_node.url:
                raise Exception("url is missing")
            return LeafNode("a", text_node.text, props={"href": text_node.url})
        case TextType.IMAGE:
            if not text_node.url:
                raise Exception("url is missing")
            return LeafNode(
                "img", "", props={"src": text_node.url, "alt": text_node.text}
            )
