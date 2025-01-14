from textnode import TextNode,TextType
from copystatic import clean_directory, copy_directory
from markdown_blocks import generate_page

def main():
    source = 'static'
    destination = 'public'

    print(f'Cleaning destination directory: {destination}')
    clean_directory(destination)

    print(f'Copying contents from {source} to {destination}...')
    copy_directory(source, destination)

    generate_page("content/index.md", "template/template.html", "public/index.html")


if __name__ == "__main__":
    main()