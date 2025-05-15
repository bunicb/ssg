from block_markdown import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import ParentNode, HTMLNode, LeafNode
from textnode import TextNode, TextType, text_node_to_html_node
from inline_markdown import text_to_textnodes
import re

def markdown_to_html_node(text):
    blocks = markdown_to_blocks(text)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            block = re.sub(r'\s+', ' ', block).strip()
            children.append(ParentNode("p", text_to_children(block)))
        elif block_type == BlockType.HEADING:
            if block.startswith("# "):
                children.append(ParentNode("h1", text_to_children(re.sub('^#+ ', '', block))))
            elif block.startswith("## "):
                children.append(ParentNode("h2", text_to_children(re.sub('^#+ ', '', block))))
            elif block.startswith("### "):
                children.append(ParentNode("h3", text_to_children(re.sub('^#+ ', '', block))))
            elif block.startswith("#### "):
                children.append(ParentNode("h4", text_to_children(re.sub('^#+ ', '', block))))
            elif block.startswith("##### "):
                children.append(ParentNode("h5", text_to_children(re.sub('^#+ ', '', block))))
            elif block.startswith("###### "):
                children.append(ParentNode("h6", text_to_children(re.sub('^#+ ', '', block))))
        elif block_type == BlockType.CODE:
            block = block[3:-3].lstrip()
            children.append(ParentNode("pre", text_node_to_html_node(TextNode(block, TextType.CODE))))
        elif block_type == BlockType.QUOTE:
            block = block.replace("> ", "")
            children.append(ParentNode("blockquote",  text_to_children(block)))
        elif block_type == BlockType.UNORDERED_LIST:
            children.append(ParentNode("ul", handle_list_items(block)))
        elif block_type == BlockType.ORDERED_LIST:
            children.append(ParentNode("ol", handle_list_items(block)))
    
    return ParentNode("div", children)

def text_to_children(block):
    text_nodes = text_to_textnodes(block)
    html_nodes = []

    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))

    return html_nodes


def handle_list_items(text):
    lines = text.split("\n")
    li_nodes = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if line[0] in {'-', '+', '*'}:
            content = line[1:].strip()
        elif line[0].isdigit() and line[1] == '.':
            content = line[2:].strip()
        else:
            continue

        if content.strip():
            children = text_to_children(content)
            li_nodes.append(ParentNode(tag='li', children=children))

    return li_nodes