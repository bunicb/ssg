from textnode import TextNode
from helpers import copy_static_files, generate_pages_recursive
import sys

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    copy_static_files("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

main()