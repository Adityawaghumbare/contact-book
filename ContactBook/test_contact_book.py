import unittest
from contact_book import add_contact, delete_contact

class TestContactBook(unittest.TestCase):
    def test_add_contact(self):
        add_contact("Test User", "9999999999", "test@example.com")
        with open("contact_file.txt", "r") as f:
            content = f.read()
        self.assertIn("Test User", content)

    def test_delete_contact(self):
        add_contact("Delete Me", "1111111111", "del@example.com")
        delete_contact("Delete Me")
        with open("contact_file.txt", "r") as f:
            content = f.read()
        self.assertNotIn("Delete Me", content)

if __name__ == "__main__":
    unittest.main()