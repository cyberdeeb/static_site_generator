import os
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    
    raise ValueError("No h1 header found in the markdown content.")

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')

    with open(from_path, "r") as f:
        markdown_content = f.read()
    
    with open(template_path, "r") as f:
        template_content = f.read()

    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()

    title = extract_title(markdown_content)

    full_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(full_html)

    print(f"Page generated successfully at {dest_path}")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # Ensure the destination directory exists
    os.makedirs(dest_dir_path, exist_ok=True)

    # Iterate over all items in the source directory
    for item in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)

        if os.path.isdir(from_path):
            # If the item is a directory, recurse into it
            generate_pages_recursive(from_path, template_path, dest_path)
        elif from_path.endswith(".md"):
            # If the item is a Markdown file, process it
            with open(from_path, "r") as f:
                markdown_content = f.read()

            with open(template_path, "r") as f:
                template_content = f.read()

            html_node = markdown_to_html_node(markdown_content)
            html_content = html_node.to_html()

            title = extract_title(markdown_content)

            full_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

            # Replace the .md extension with .html for the destination file
            dest_path = os.path.splitext(dest_path)[0] + ".html"

            # Write the generated HTML to the destination file
            with open(dest_path, 'w', encoding='utf-8') as f:
                f.write(full_html)

            print(f"Page generated successfully at {dest_path}")
