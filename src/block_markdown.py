from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    # Split the markdown into lines
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(blocks):
    # blocks is a list, write an if statement if first element starts with 1-6 # characters and then a whitespace, it is a heading
    if re.findall(r"^#{1,6} \w+", blocks[0]):
        return BlockType.HEADING
    elif blocks[0] == "```" and blocks[-1] == "```":
        return BlockType.CODE
    elif all(block.startswith("> ") for block in blocks):
        return BlockType.QUOTE
    elif all(block.startswith("- ") for block in blocks):
        return BlockType.UNORDERED_LIST
    elif all(blocks[i].startswith(f"{i + 1}. ") for i in range(0, len(blocks))):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
