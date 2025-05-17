from textnode import TextNode
from helpers import copy_static_files, generate_pages_recursive

def main():
    copy_static_files("static", "public")
    generate_pages_recursive("content", "template.html", "public")

main()