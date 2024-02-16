import unittest
import os
from src.helpers import db_manager
from reportair import App

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
    

class TestMainGUI(unittest.TestCase):
    def setUp(self) -> None:
        self.app = App()
        return super().setUp()
    
    def test_main_exists(self):
        self.assertTrue(self.app.winfo_exists())

    def test_left_sidebar_exists(self):
        self.assertTrue(self.app.l_frame.winfo_exists())

    def test_right_sidebar_exists(self):
        self.assertTrue(self.app.r_frame.winfo_exists())



    

