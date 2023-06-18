import unittest
import pandas as pd


class TextConverter(unittest.TestCase):
    def test_converter(self):
        from csv2excel import convert
        input_file = "./tests/fixture.csv"
        output_file = "./tests/output.xlsx"
        convert(input_file=input_file, output_file=output_file)
        input_df = pd.read_csv(input_file)
        output_df = pd.read_excel(output_file)

        # 入力csvと書き出したexcelが一致することを確認 
        self.assertTrue(input_df.equals(output_df))

