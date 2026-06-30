import unittest

from extract_markdown_images import extract_markdown_images, extract_markdown_links


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_with_link(self):
        matches = extract_markdown_images(
            "This is a link [image](https://www.google.com)"
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_images_mult_images(self):
        matches = extract_markdown_images(
            "This is an ![image](images_one.com) an here is another ![second image](here another)"
        )
        self.assertListEqual([("image", "images_one.com"), ("second image", "here another")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is an [link](www.markdown.example)"
        )
        self.assertListEqual([("link", "www.markdown.example")], matches)

    def test_extract_markdown_links_with_image(self):
        matches = extract_markdown_links(
            "This is not a ![link](this.com)"
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_links_with_mult_links(self):
        matches = extract_markdown_links(
            "This [text](hast.two) links [inside](example.com)"
        )
        self.assertListEqual([("text", "hast.two"), ("inside", "example.com")], matches)



if __name__ == "__main__":
    unittest.main()
