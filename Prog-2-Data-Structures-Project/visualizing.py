from manim import *
import json
import csv

PROJECT_PATH = ".\Prog-2-Data-Structures-Project"


class Main(Scene):
    def construct(self):
        circle = Circle()
        formating()
        self.play(Create(circle))
        

def formating():
    with open(fr'{PROJECT_PATH}\20191226-items.csv', 'r') as item_csv:
        item_csv_reader = csv.reader(item_csv)
    with open(fr'{PROJECT_PATH}\20191226-reviews.csv', 'r') as review_csv:
            review_csv_reader = csv.reader(review_csv)
    with open(fr'{PROJECT_PATH}\formatted.json', 'w') as formmated_json:
        
