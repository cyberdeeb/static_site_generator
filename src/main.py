from textnode import TextNode,TextType
from copystatic import clean_directory, copy_directory

def main():
    source = 'static'
    destination = 'public'

    print(f'Cleaning destination directory: {destination}')
    clean_directory(destination)

    print(f'Copying contents from {source} to {destination}...')
    copy_directory(source, destination)


if __name__ == "__main__":
    main()