"""1. Product Review Analysis
Task 1: Keyword Highlighter

Write a program that searches through reviews list and looks for keywords such as "good", "excellent", "bad", "poor", and "average". We want you to capitalize those keywords then print out each review. Print out each review with the keywords in uppercase so they stand out.
"""


"""
keywords = 'good', 'excellent', 'bad', 'poor', 'average'

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

for review in reviews:
    for keyword in keywords:
        review = review.replace(keyword, keyword.upper())
        review = review.replace(keyword.capitalize(), keyword.upper())
    print(review)
"""

# Task 2: Sentiment Tally

import string

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

def tally(reviews, positive_words, negative_words):
    total_positive = 0
    total_negative = 0
    
    translator = str.maketrans('', '', string.punctuation + string.digits)

    for review in reviews:
        cleaned_review = review.lower().translate(translator)
        words = cleaned_review.split()
        for word in words:
            if word in positive_words:
                    total_positive += 1
            elif word in negative_words:
                    total_negative += 1    
                
    return total_positive, total_negative

positive_count, negative_count = tally(reviews, positive_words, negative_words)

print(f"Total positive words: {positive_count}")
print(f"Total negative words: {negative_count}")



"""
Task 3: Review Summary

Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.

Example: "This product is really good. I'm...",
"""

def summarize_review(review, length=30):
    if len(review) <= length:
        return review
    
    summary = review[:length]
    
    if summary[-1].isalpha() and review[length].isalpha():
        summary = summary.rsplit(' ', 1)[0]
    
    return summary + "…"

summaries = [summarize_review(review) for review in reviews]

for summary in summaries:
    print(summary)


