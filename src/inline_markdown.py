from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue

        if delimiter == "":
            new_nodes.append(node)
            continue

        values = node.text.split(delimiter)
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


def split_nodes_image(old_nodes):
    new_nodes = []
    for one_node in old_nodes:
        if one_node.text_type != TextType.NORMAL:
            new_nodes.append(one_node)
            continue
        node = one_node.text
        images = extract_markdown_images(node)

        if len(images) == 0:
            new_nodes.append(one_node)
            continue

        for i in range(len(images)):
            alt_text, image_url = images[i]
            nodes = node.split(f"![{alt_text}]({image_url})", maxsplit=1)
            if len(nodes) != 2:
                raise ValueError("Invalid markdown syntax")
            if nodes[0] != "":
                new_nodes.append(TextNode(nodes[0], TextType.NORMAL))
                new_nodes.append(TextNode(alt_text, TextType.IMAGE, image_url))
                node = nodes[1]
        if node != "":
            new_nodes.append(TextNode(node, TextType.NORMAL))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for one_node in old_nodes:
        if one_node.text_type != TextType.NORMAL:
            new_nodes.append(one_node)
            continue
        node = one_node.text
        links = extract_markdown_links(node)

        if len(links) == 0:
            new_nodes.append(one_node)
            continue

        for i in range(len(links)):
            alt_text, link_url = links[i]
            nodes = node.split(f"[{alt_text}]({link_url})", maxsplit=1)
            if len(nodes) != 2:
                raise ValueError("Invalid markdown syntax")
            if nodes[0] != "":
                new_nodes.append(TextNode(nodes[0], TextType.NORMAL))
                new_nodes.append(TextNode(alt_text, TextType.LINK, link_url))
            node = nodes[1]
        if node != "":
            new_nodes.append(TextNode(node, TextType.NORMAL))

    return new_nodes

def text_to_textnodes(text):
    text_node = TextNode(text, TextType.NORMAL)
    nodes = split_nodes_delimiter([text_node], "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes
