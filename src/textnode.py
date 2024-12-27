from enum import Enum

class TextType(Enum):
    NORMAL_TEXT = 'normal_text'
    BOLD_TEXT = 'bold_text'
    ITALIC_TEXT = 'italic_text'
    CODE_TEXT = 'code_text'
    LINKS = 'links'
    IMAGES = 'images'

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
        return f'TextNode({self.text!r}, {self.text_type.value!r}, {self.url!r})'

