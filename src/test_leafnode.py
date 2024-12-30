import unittest
from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode(
            "a",
            "Click me!",
            {"href": "https://www.google.com"},
        )
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_to_html_props(self):
        node = LeafNode(
            "div",
            "Hello, world!",
            {"class": "greeting", "href": "https://google.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://google.dev"',
        )

    def test_values(self):
        node = LeafNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = LeafNode(
            "p",
            "What a strange world",
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "LeafNode(p, What a strange world, {'class': 'primary'})"
        )


if __name__ == "__main__":
    unittest.main()
