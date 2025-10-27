from manim import *
import json
import csv
from collections import OrderedDict

PROJECT_PATH = ".\Prog-2-Data-Structures-Project"


class Main(Scene):
    def construct(self):
        #formating()
        with open(r".\formatted.json", 'r') as formatted_json:
            data = json.load(formatted_json)
        

        averaged_scores = {}
        for brand in data:
            if brand != 'brand':
                average_score = getAverageReviewScore(brand, data)
                averaged_scores[brand] = average_score

        presentation_title = Text("Comparing Phone Reveiws to Date and Brand")

        first_analysis_title = Text("Average Score of Different Brands")
        first_analysis_title.to_edge(UP)


        # getting the data for the bars in the unsorted graph
        brands = averaged_scores.keys()
        scores = averaged_scores.values()

        scores = list(scores)
        brands = list(brands)
        brands[0] = 'Unknown'

        # making the unsorted graph
        average_score_chart = BarChart(values=scores, bar_names=brands, y_range=[0,5,1])
        average_score_chart_values = average_score_chart.get_bar_labels()
        

        # getting the data for the sorted graph
        reversed_averaged_scores = {}
        for i in range(0, len(scores)):
            pass

        sorted_scores = scores.copy().sort()

        sorted_brands = []
        for score in sorted_scores:
            sorted_brands.append()
        

        self.play(Write(presentation_title))
        self.wait(2)
        self.play(Unwrite(presentation_title, reverse=False))
        self.play(Write(first_analysis_title))
        self.wait(1)
        self.play(Create(average_score_chart.axes))
        self.play(Create(average_score_chart.bars), Write(average_score_chart_values))
        self.wait(2)
        

def getAverageReviewScore(brand, data):
    temp_scores = []
    for product in data[brand]:
        for review in data[brand][product]:
            score = review[0]
            temp_scores.append(int(score))
    mean = sum(temp_scores) / len(temp_scores)
    mean = round(mean, 3)
    return mean

        


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
                    to_json[item[1]] = {item[0] : 'temp'}
                else:
                    to_json[item[1]][item[0]] = 'temp'
            
            items = condenced_review_dict.keys()
            for brand in to_json:
                for asin in to_json[brand]:
                    for item in items:
                        if asin == item:
                            to_json[brand][asin] = condenced_review_dict[item]
                       
            with open(fr'{PROJECT_PATH}\formatted.json', 'w') as formmated_json:
                json.dump(to_json, formmated_json, indent=4)
        
        

if __name__ == '__main__':
    with open(fr"{PROJECT_PATH}\formatted.json", 'r') as formatted_json:
        data = json.load(formatted_json)

    averaged_scores = {}
    for brand in data:
        if brand != 'brand':
            average_score = getAverageReviewScore(brand, data)
            averaged_scores[brand] = average_score