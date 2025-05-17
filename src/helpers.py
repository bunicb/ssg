import os
import shutil
from markdown_to_html import markdown_to_html_node

def copy_static_files(src, dst):
    # empty the public folder if it exists
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.makedirs(dst)

    contents = os.listdir(src)
    for file in contents:
        src_file = os.path.join(src, file)
        dst_file = os.path.join(dst, file)
        print(f"Copying {src_file} to {dst_file}")
        if os.path.isfile(src_file):
            shutil.copy2(src_file, dst_file)
        elif os.path.isdir(src_file):
            copy_static_files(src_file, dst_file)

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No title found in markdown")

def generate_page(from_path, template_path, dest_path):
    print (f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as f:
        template = f.read()

    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    modified_template = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
    # Ensure the destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(modified_template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    files = os.listdir(dir_path_content)
    print(files)
    for file in files:
        src_path = os.path.join(dir_path_content, file)
        dst_path = os.path.join(dest_dir_path, file)
        if file.endswith(".md"):
            generate_page(src_path, template_path, dst_path.replace(".md", ".html"))
        elif os.path.isdir(src_path):
            generate_pages_recursive(src_path, template_path, dst_path)
