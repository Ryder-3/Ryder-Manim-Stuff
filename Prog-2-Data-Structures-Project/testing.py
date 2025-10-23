import csv

PROJECT_PATH = ".\Prog-2-Data-Structures-Project"

        


with open(fr'{PROJECT_PATH}\20191226-items.csv', 'r') as item_csv:
        item_csv_reader = csv.reader(item_csv)

        with open(fr'{PROJECT_PATH}\20191226-reviews.csv', 'r') as review_csv:
            review_csv_reader = csv.reader(review_csv)
            condenced_review_dict = {}


            for i in range(0, len(review_csv_reader)):

                try: test = review_csv_reader[i]
                except UnicodeDecodeError:
                    print(repr(review_csv_reader[i]))
                    
                    



                



    
