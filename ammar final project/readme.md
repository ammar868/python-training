
# NewsApp

NewsApp is a Python application that interacts with the New York Times API to fetch top stories, book reviews, and articles . This application provides a command-line interface for users to search and view this information.

# Features
- Top Stories:  Fetch and display top stories from different sections.
- Book Reviews: Search for book reviews by title or author.
- Article Search: Search for articles by news desk.


## Installation

- URLs :

- top_stories_url = "https://api.nytimes.com/svc/topstories/v2/"
- book_reviews_url = "https://api.nytimes.com/svc/books/v3/reviews.json"
- article_search_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

- Install required dependencies:

Make sure you have requests library installed. You can install it using pip:

pip install requests

- Set up your API Key:

Obtain an API key from the New York Times Developer Network by signing up at NY Times Developer.

Replace the placeholder API key in the script with your actual API key:


## Classes and Functions

# NewsAPI Class
Handles interactions with the New York Times API.


# TopStories Class
Handles fetching and displaying top stories.

get_top_stories(self, section): Fetches top stories from the specified section.


# BookSearch Class
Handles searching and displaying book reviews.

search_books(self, title=None, author=None): Searches for book reviews by title or author.


# ArticleSearch Class
Handles searching and displaying articles by news desk.

search_articles_by_news_desk(self, news_desk): Searches for articles by news desk.



# NewsApp Class
Main application class that integrates all functionalities.

 Main loop to run the application.

