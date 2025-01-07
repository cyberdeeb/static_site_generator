import re

def markdown_to_blocks(markdown):
    
    block = [line.strip() for line in re.split(r'\n\s*\n', markdown)]
    
    return block