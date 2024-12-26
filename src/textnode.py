from enum import Enum

class TextType(Enum):
    NORMAL_TEXT = 'normal_text'
    BOLD_TEXT = 'bold_text'
    ITALIC_TEXT = 'italic_text'
    CODE_TEXT = 'code_text'
    LINKS = 'links'
    IMAGES = 'images'

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url


