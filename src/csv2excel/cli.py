import argparse
from csv2excel import convert


def main():
    parser = argparse.ArgumentParser(description='入力されたcsvファイルをexcelに変換')
    parser.add_argument('input_file', help='対象のファイル')
    parser.add_argument('output_file', help='出力ファイル')
    args = parser.parse_args()

    convert(input_file=args.input_file, output_file=args.output_file)


if __name__ == "__main__":
    main()
