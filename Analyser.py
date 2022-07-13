import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns




def analyse_product_review():
    df = pd.read_excel('reviews.xlsx')
    #open reviews column
    reviews = df['Review']
    #open names column
    names = df['Name']
    #open stars column
    stars = df['Stars']

    star_det= [0,0]
    for i in range(stars.count()):


        if float(stars[i])>=4.0:
            star_det[0]+=1
        else:
            star_det[1]+=1

    return star_det


def give_overreview(details):
    if details[0]>details[1]:
        return "Positive Reviews"
    else:
        return "Negative Reviews"


def analyze():
    details = analyse_product_review()
    print("The product has", give_overreview(details))
    print("The product has", details[0], "positive reviews and", details[1], "negative reviews")


#here
analyze()
