from manim import *
import json
import csv
import operator

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

        sorted_averaged_scores = dict(sorted(averaged_scores.items(), key=operator.itemgetter(1)))
        sorted_scores = sorted_averaged_scores.values()

            #sorting the brands and scores


        sorted_scores = list(sorted_scores)
        sorted_scores.sort()
        sorted_scores.reverse()

        sorted_brands = []
        reference_items = averaged_scores.items()
        for score in sorted_scores:
            for pair in reference_items:
                pair = list(pair)
                if score == pair[1]:
                    sorted_brands.append(pair[0])
        sorted_brands[4] = 'Unknown'


        # making the sorted bar graph

        sorted_score_chart = BarChart(values=sorted_scores, bar_names=sorted_brands, y_range=[0,5,1])
        sorted_score_chart_values = sorted_score_chart.get_bar_labels()
        
        mean_score_bracket = Brace(sorted_score_chart, UP)

        average_score = getPopulationMean(data)
        


        average_score_text = MathTex(r"\text{Average score of all phones: }" + str(average_score))
        average_score_text.to_edge(UP)
        
        

        self.play(Write(presentation_title))
        self.wait(2)
        self.play(Unwrite(presentation_title, reverse=False))
        self.play(Write(first_analysis_title))
        self.wait(1)
        self.play(Create(average_score_chart), Write(average_score_chart_values))
        self.wait(2)
        self.play(ReplacementTransform(average_score_chart, sorted_score_chart), ReplacementTransform(average_score_chart_values, sorted_score_chart_values))
        self.wait(2)
        self.play(FadeIn(mean_score_bracket))
        self.wait(2)
        self.play(ReplacementTransform(first_analysis_title, average_score_text))
        self.wait(2)

        
def getPopulationMean(data):
    mean = []
    for brand in data:
        if brand != 'brand':
            for product in data[brand]:
                for review in data[brand][product]:
                    score = review[0]
                    mean.append(int(score))
    mean = sum(mean) / len(mean)
    mean = round(mean, 3)
    return mean

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

    population_mean = getPopulationMean(data)