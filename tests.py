import unittest
import os
from src.helpers import db_manager

class TestDB(unittest.TestCase):
    def setUp(self) -> None:
        self.db = db_manager.DB("Test.db")
        return super().setUp()
    
    def test_db_init(self):
        print(self.db.name)
        self.db.close()

    def tearDown(self) -> None:
        os.remove("Test.db")
        return super().tearDown()
    

