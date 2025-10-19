from bs4 import BeautifulSoup
import requests
from collections import Counter
import string

import matplotlib.pyplot as plt
import numpy as np

# Setting up the project
url = "http://books.toscrape.com/"
text = requests.get(url).text
# print(text)

# parsing the html so they can be extracted
soup = BeautifulSoup(text, "html.parser")

# 2 Print the title of the page
print("\nPage Title:")
print(soup.title.string)

# 3A Finding an element - Sub Header
print("\nSub Header:")
sub_title = soup.find("small")
print(sub_title.text.strip())

# 3B Finding an element - Warning
print("\nWarning message:")
warning = soup.find("div", class_="alert-warning")
print(warning.text.strip())

# 3C Finding an element - Just warning
print("\nJust Warning:")
just_warning = soup.find("div", class_="alert-warning").strong
print(just_warning.text)

# 3D Finding multiple elements - Titles
print("\nTitles:")
titles = soup.findAll("h3")
for title in titles:
    print(title.text)

# -- Phase 3 --
def get_words_list(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    
    # Combine all titles into one big string
    text = ""
    titles = soup.findAll("h3")
    for title in titles:
        text += " " + title.text.lower()

    # Remove punctuation
    for char in string.punctuation:
        text = text.replace(char, "")

    # Split into words
    text_list = text.split()

    # Count most common words
    word_counts = Counter(text_list).most_common(50)

    return word_counts

# --- Phase 4 ---
def plot_words(words_list, fname):
    # separate word and the numbers
    words = []
    numbers = []
    for (w, n) in words_list:
        words.append(w)
        numbers.append(n)

    # index will be from 0 to number of words
    index = np.arange(len(words))

    fig = plt.figure()

    #-- Bar Chart
    plt.bar(index, numbers)

    #-- x line setting
    # index+.5 = adding 0.5 shifts all ticks by 0.5 units to the right
    # words = label underneath x line
    # rotation = vertical - make it to be vertical rotated
    # size=x-small = set font size
    plt.xticks(index + .5, words, rotation="vertical", size="x-small")
    
    # saving the figure based on the name
    plt.title(fname)
    fig.savefig(fname)

# --- Phase 3&4 ----

def main():
    words_list = get_words_list("http://books.toscrape.com/")
    print(words_list)
    plot_words(words_list, "Word counts")
main()