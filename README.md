# Python Analysis of Financial and Election Data

<img src="https://www.fortworthtexas.gov/files/assets/public/news/images/city-news-elections-graphic.jpg?dimension=pageimage&w=480">

## Overview

This simple project is to demonstrate how [Python](https://www.python.org/) can be used to load and analyze CSV data without the help of [Pandas](https://pandas.pydata.org/).

Two different sets of data were used:

- [budget_data.csv](https://github.com/ericyang91/Python_Analysis_of_Financial_and_Election_Data/blob/main/PyBank/Resources/budget_data.csv) 
- [election_data.csv](https://github.com/ericyang91/Python_Analysis_of_Financial_and_Election_Data/blob/main/PyPoll/Resources/election_data.csv)

## Functions Used

- `os.path.join` is used to concatenate multiple path components into a single path string. It intelligently handles the differences in path separators ('/' or '') based on the operating system.
- `with` Once the code within the with block is executed, the file will be automatically closed, regardless of whether an exception occurs or not. This ensures proper cleanup and prevents resource leaks.
- `next()` is used to retrieve the next item from an iterator. It allows you to iterate over the elements of an iterable one at a time. It cannot be used on lists.
- `zip()` is used to combine multiple iterables into a single iterable of tuples. It takes iterables as input and returns an iterator that generates tuples containing elements from each input iterable, grouped together based on their positions. It's worth noting that if the input iterables are of different lengths, zip() will stop generating tuples as soon as the shortest iterable is exhausted. Any remaining elements in the longer iterables will be ignored. You can also convert the zip() result to other data structures like lists or dictionaries, if needed.


## Languages and Libraries

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
