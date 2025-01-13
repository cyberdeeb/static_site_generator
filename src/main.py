from textnode import TextNode,TextType
import os
import shutil

def clean_directory(directory):
    """
    Deletes all contents of the given directory.
    """
    if os.path.exists(directory):
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                os.remove(item_path)

def copy_directory(source, destination):

    # Check if source exists
    if not os.path.exists(source):
        raise Exception(f'{source} does not exist')
    
    # Check if destination exists
    if not os.path.exists(destination):
        os.makedirs(destination)

    # Loop through source directory
    for item in os.listdir(source):
        source_item = os.path.join(source, item)
        destination_item = os.path.join(destination, item)

        # Copy directory
        if os.path.isdir(source_item):
            print(f'Creating directory: {destination_item}')
            os.makedirs(destination_item, exist_ok=True)
            copy_directory(source_item, destination_item)
        else:
            # Copy file
            print(f'Copying file: {source_item} to {destination_item}')
            shutil.copy2(source_item, destination_item)
        
    print("Copy completed")

def main():
    source = 'static'
    destination = 'public'

    print(f'Cleaning destination directory: {destination}')
    clean_directory(destination)

    print(f'Copying contents from {source} to {destination}...')
    copy_directory(source, destination)


if __name__ == "__main__":
    main()