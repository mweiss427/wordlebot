import unittest
import yaml
from analysis import Word
from bot import Bot

# This is for tests just to print things.
# "Its fun to print things"
# basiclly chop up the output of the bot for formats.
# Today we want a json or yaml output. lets start yaml. for fun


class TestPrintStuff(unittest.TestCase):
    def testPrintStuff(self):
        oaten = Word("oaten", "nnnnn")
        shiur = Word("shiur", "rnrnn")

        meep_morp = Bot()
        meep_morp.input(oaten)
        meep_morp.input(shiur)
        print("Morp")
        print("Meep! Morp!, hello world: your answer details look like...")
        print(meep_morp.answer.toYaml())
        self.assertEqual("meep", meep_morp.answer.toYaml())


if __name__ == '__main__':
    unittest.main()
