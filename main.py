from driver import Driver
from  annotations_parser import Annotations_parser
import pandas as pd
def main():
    driver = Driver("5fj8")

    annotations_html = driver.get_all_annotations()

    parser = Annotations_parser(annotations_html)

    parser.get_annotations()
    parser.write_annotations_to_csv("test.csv") 
main()