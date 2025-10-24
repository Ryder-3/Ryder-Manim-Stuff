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
    with open(fr'{PROJECT_PATH}\20191226-items.csv', 'r', encoding='utf-8') as item_csv:
        item_csv_reader = csv.reader(item_csv)

        with open(fr'{PROJECT_PATH}\20191226-reviews.csv', 'r', encoding='utf-8') as review_csv:
            review_csv_reader = csv.reader(review_csv)
            condenced_review_dict = {}

    

            for review in review_csv_reader:
                if review[0] not in condenced_review_dict.keys():
                    short_review = [review[2], review[3]]
                    condenced_review_dict[review[0]] = [short_review]
                else:
                    short_review = [review.copy()[2], review.copy()[3]]
                    condenced_review_dict[review[0]].append(short_review)

            to_json = {}
            for item in item_csv_reader:
                if item[1] not in to_json.keys():
                    to_json[item[1]] = [{item[0] : 'temp'}]
                else:
                    to_json[item[1]].append({item[0] : 'temp'})
            
            items = condenced_review_dict.keys()
            for brand in to_json:
                for product_num in range(0,len(to_json[brand])):
                    if to_json[brand][product_num]
                    
                    
                    
                    
                            
                    
            

            with open(fr'{PROJECT_PATH}\formatted.json', 'w') as formmated_json:
                pass
        
        

if __name__ == '__main__':
    formating()