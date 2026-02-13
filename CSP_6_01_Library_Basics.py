#Please modify the below functions so they fulfill the described process.
#You must use a function from analytics.py in each question to receive credit.
#There is no provided test file. You must make and submit one yourself. (check older test files for reference)


import analytics

# Modify the below function such that it takes in a list of prices
# and returns that list with 15% added value
def process_expenses(rawPrices):
    newPrices = []

    for price in rawPrices:
        updatedPrice = analytics.add_15_percent(price)
        newPrices.append(updatedPrice)

    return newPrices

import analytics

# Modify the below function such that it asks the user for n scores
# and then returns the highest score and the average score of the list.
def analyze_scores(n):
    scores = []

    for i in range(n):
        score = float(input("Enter a score: "))
        scores.append(score)

    highest = analytics.find_highest(scores)
    average = analytics.find_average(scores)

    return highest, average

import analytics

# Modify the below function such that it takes in a list of strings
# and returns that list with all spaces removed and all letters lower case.
def sanitize_usernames(usernames):
    cleaned_list = []

    for name in usernames:
        cleaned_name = analytics.clean_text(name)
        cleaned_list.append(cleaned_name)

    return cleaned_list

import analytics

# Modify the function such that it takes in a list as an argument
# and returns a version of the list with all values over 100.
def identify_outliers(numbers):
    result = analytics.over_100(numbers)
    return result

import analytics

# Modify the below function such that it takes in a list of items
# and asks the user for an item to search for.
# Sanitize the list to only be lower case words with no extra spaces
# Then return the location of the word using binary search if the list is in order
# and linear search if it is not.
def search_and_report(items):

    cleaned_list = []

    # Clean each item in the list
    for item in items:
        cleaned_item = analytics.clean_text(item)
        cleaned_list.append(cleaned_item)

    # Ask user what to search for
    search_item = input("Enter item to search for: ")
    search_item = analytics.clean_text(search_item)

    # Check if list is sorted
    if analytics.is_sorted_list(cleaned_list):
        position = analytics.binary_search(cleaned_list, search_item)
    else:
        position = analytics.linear_search(cleaned_list, search_item)

    return position