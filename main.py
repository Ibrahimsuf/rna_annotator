from driver import Driver
from  annotations_parser import Annotations_parser
import pandas as pd
import sys


def main():
    driver = Driver(sys.argv[1])

    annotations_html = driver.get_all_annotations()

    parser = Annotations_parser(annotations_html)

    parser.get_annotations()
    parser.write_annotations_to_csv(sys.argv[2]) 


if __name__ == "__main__":
    if len(sys.argv) == 3:
        main()
    else:
        print("python main.py <pdb id> <output_file.csv>")