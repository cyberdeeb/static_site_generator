import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"


def markdown_to_blocks(markdown):
    
    blocks = [line.strip() for line in re.split(r'\n\s*\n', markdown)]
    
    return blocks

def block_to_block_type(block):
    if re.match(r"^#{1,6} .+", block):
        return block_type_heading
    elif re.match(r'^```[\s\S]*```$', block):
        return block_type_code
    elif all(re.match(r"^>", line) for line in block.splitlines()):
        return block_type_quote
    elif all(re.match(r"^[*-]\s", line) for line in block.splitlines()):
        return block_type_ulist
    elif all(re.match(r"^(\d+)\. (.+)$", line) for line in block.splitlines()):

        last_number = 0

        for line in block.splitlines():
           current_number = int(re.match(r"^(\d+)\. (.+)$", line).group(1))
           if current_number != last_number + 1:
                raise ValueError(f"Error: Expected {last_number + 1}, but found {current_number}")
           else:
               last_number = current_number
        return block_type_olist
    else:
        return block_type_paragraph