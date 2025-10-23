from lib.text import top_n
from lib.text_stats import tokenize
import argparse
parser = argparse.ArgumentParser(description="Лабораторная №6")
subparsers = parser.add_subparsers(dest="comnds")
cat_parser = subparsers.add_parser("cat", help)
