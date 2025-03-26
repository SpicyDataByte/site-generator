import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a node", TextType.TEXT)
        self.assertNotEqual(node1, node2)

    def test_url_none(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        self.assertIsNone(node1.url)
        
if __name__ == "__main__":
    unittest.main()