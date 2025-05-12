from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, str):
            new_nodes.append(node)
            continue

        if delimiter == "":
            values = node
            new_nodes.append(TextNode(values, TextType.NORMAL))
            continue

        values = node.split(delimiter)
        if len(values) % 2 == 0:
            raise Exception("Invalid markdown syntax")
        for i in range(len(values)):
            if i % 2 == 0:
                new_nodes.append(TextNode(values[i], TextType.NORMAL))
            else:
                new_nodes.append(TextNode(values[i], text_type))        
        
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"[^!]\[(.*?)\]\((.*?)\)", text)

