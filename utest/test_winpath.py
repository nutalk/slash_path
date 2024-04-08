import unittest
from slash_path import SlashPath
from pathlib import Path


class WinPathTestCase(unittest.TestCase):
    def test_win_path(self):
        path_str = 'D:\next_cloud\newfile.txt'
        sp = SlashPath(path_str)
        self.assertEqual(sp.parts, ('D:\\', 'next_cloud', 'newfile.txt'))

        path_r_str = r'D:\next_cloud\newfile.txt'
        sp = SlashPath(path_r_str)
        self.assertEqual(sp.parts, ('D:\\', 'next_cloud', 'newfile.txt'))

        double_slash = 'D:\\next_cloud\\newfile.txt'
        sp = SlashPath(double_slash)
        self.assertEqual(sp.parts, ('D:\\', 'next_cloud', 'newfile.txt'))


if __name__ == '__main__':
    unittest.main()
