import re

def markdown_to_blocks(markdown):
    
    block = [line.strip() for line in re.split(r'\n\s*\n', markdown)]
    
    return block

markdown = """"
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""

print(markdown_to_blocks(markdown))