from model import transcript
from os.path import join, dirname
from unittest import TestCase


class TestSentiment(TestCase):
    def test_1(self):
        wav = join(dirname(__file__), "test", "CAFPHEE001.wav")
        actual = transcript(wav)
        expected = "cà phê"
        self.assertEqual(actual, expected)

    def test_2(self):
        wav = join(dirname(__file__), "test", "KHASCHSAJN003.wav")
        actual = transcript(wav)
        expected = "khách sạn"
        self.assertEqual(actual, expected)
