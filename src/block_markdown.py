from enum import Enum


class BlockType(Enum):
    HEADER = "header"
    PARAGRAPH = "paragraph"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown: str) -> list[str]:
    blocks: list[str] = markdown.split("\n\n")
    blocks = list(map(lambda block: block.strip(), blocks))
    blocks = list(filter(lambda block: block != "", blocks))
    return blocks


def block_to_block_type(block: str) -> BlockType:
    match block:
        case _ if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
            return BlockType.HEADER
        case _ if block.startswith("```") and block.endswith("```"):
            return BlockType.CODE
        case _ if block.startswith(">"):
            return BlockType.QUOTE
        case _ if block.startswith("- "):
            return BlockType.UNORDERED_LIST
        case _ if block.startswith("1. "):
            return BlockType.ORDERED_LIST
        case _:
            return BlockType.PARAGRAPH
