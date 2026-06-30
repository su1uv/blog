from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT :
            new_nodes.append(node)
            continue
        if delimiter not in node.text and node.text_type == TextType.PLAIN_TEXT:
            raise Exception("invalid markdown syntax")

        splitted_text = node.text.split(delimiter)
        for i, v in enumerate(splitted_text):
            if v == "":
                continue
            if i % 2 != 0 and i != 0:
                new_nodes.append(TextNode(v, text_type))
                continue

            new_nodes.append(TextNode(v, TextType.PLAIN_TEXT))

    return new_nodes
