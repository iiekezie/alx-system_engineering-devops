# 0x16. API Advanced

## Project Overview
This project focuses on mastering API queries, particularly using the Reddit API. It covers tasks such as querying subscriber counts, retrieving hot posts, and recursively handling API pagination.


## Table of Contents
1. [Project Overview](#project-overview)
2. [Technologies](#technologies)
3. [Requirements](#requirements)
4. [Directory Structure](#directory-structure)
5. [Tasks](#tasks)
6. [Author](#author)

## Technologies
- Python 3.4.3
- Requests library
- Ubuntu 20.04 LTS

## Requirements
- Code style: PEP 8
- All Python scripts must be executable
- Use the Requests module to send HTTP requests
- Scripts must start with `#!/usr/bin/python3`
- Libraries must be imported in alphabetical order
- Proper documentation for each module

## Directory Structure
```bash
0x16-api_advanced/
│
├── 0-subs.py
├── 1-top_ten.py
├── 2-recurse.py
└── 100-count.py
```

## Tasks

| Task Number | File Name        | Description                                                                                           | Prototype                                      |
|-------------|------------------|-------------------------------------------------------------------------------------------------------|------------------------------------------------|
| 0           | `0-subs.py`      | Queries the Reddit API to return the number of subscribers for a given subreddit.                      | `def number_of_subscribers(subreddit)`         |
| 1           | `1-top_ten.py`   | Prints the titles of the first 10 hot posts for a given subreddit.                                     | `def top_ten(subreddit)`                       |
| 2           | `2-recurse.py`   | Recursively returns a list of titles for all hot articles in a subreddit.                              | `def recurse(subreddit, hot_list=[])`          |
| 3           | `100-count.py`   | Recursively counts and prints sorted occurrences of specified keywords in the titles of hot articles. | `def count_words(subreddit, word_list)`        |

## Author :black_nib:
* **Ifeanyi I Ekezie** <[iiekezie](https://github.com/iiekezie)>
