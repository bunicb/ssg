from textnode import TextNode
from helpers import copy_static_files

def main():
    copy_static_files("static", "public")

main()