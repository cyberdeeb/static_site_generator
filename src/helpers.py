from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    
    new_nodes = []

    for node in old_nodes:
        
        if node.text.count(delimiter) % 2 != 0:
            raise Exception(f"Unbalanced delimiter: '{delimiter}' in text: {node.text}")

        if node.text_type.value == 'text':
            split_text = node.text.split(delimiter)
            for i, text in enumerate(split_text):

                if i == 1:
                    new_nodes.append(TextNode(text, text_type))
                else:
                    new_nodes.append(TextNode(text, TextType.TEXT))

        else:
            new_nodes.append(node)

    return new_nodes

node = TextNode("This is text with a `code block` word", TextType.TEXT)
new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

print(new_nodes)