from multiprocessing import connection
from multiprocessing.sharedctypes import Value
import sys
sys.path.append('./')
import unittest
from Writer import Writer
from unittest.mock import Mock
import datetime

class TestWriter(unittest.TestCase):
    
    def testGetData(self):
        writer = Writer()
        self.assertAlmostEqual(TypeError,writer.uzmiPodatke,"CODE")
        self.assertAlmostEqual(TypeError,writer.uzmiPodatke,"sfghjdg")
        self.assertAlmostEqual(TypeError,writer.uzmiPodatke,"Poslato:CODE_ANALOG:adfhfa")
        self.assertAlmostEqual(TypeError,writer.uzmiPodatke,"Poslato:")
        self.assertAlmostEqual(TypeError,writer.uzmiPodatke,"Poslato:aqdawa:12313")



