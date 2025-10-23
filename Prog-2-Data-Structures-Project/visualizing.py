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
            condenced_review_dict = {}

    

            for review in review_csv_reader:
                if review[0] not in condenced_review_dict.keys():
                    short_review = review.copy()
                    short_review.pop(0)
                    condenced_review_dict[review[0]] = [short_review]
                else:
                    short_review = review.copy()
                    short_review.pop(0)
                    condenced_review_dict[review[0]].append(short_review)  
            print(condenced_review_dict)

            with open(fr'{PROJECT_PATH}\formatted.json', 'w') as formmated_json:
                for line in item_csv_reader:
                    print(line)
        
        

if __name__ == '__main__':
    formating()