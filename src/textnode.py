from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = 'text'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINK = 'link'
    IMAGE = 'image'

class TextNode():
    def __init__(self, text, text_type: TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other_textnode):
        if isinstance(other_textnode, TextNode):
            return (
                self.text == other_textnode.text and 
                self.text_type == other_textnode.text_type and 
                self.url == other_textnode.url
                )
        return False

    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type.value}, {self.url})'

    def text_node_to_html_node(self):
        match self.text_type:
            case TextType.TEXT:
                return LeafNode(None, self.text)
            case TextType.BOLD:
                return LeafNode('b', self.text)
            case TextType.ITALIC:
                return LeafNode('i', self.text)
            case TextType.CODE:
                return LeafNode('code', self.text)
            case TextType.LINK:
                return LeafNode('a', self.text, {'href':self.url})
            case TextType.IMAGE:
                return LeafNode('img', '', {'src': self.url, 'alt': self.text})
            
            case _:
                raise ValueError(f"Invalid text type: {self.text_type}")
            
    