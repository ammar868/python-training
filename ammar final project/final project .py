import requests

# from dotenv import load_dotenv, dotenv_values 

class NewsAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.top_stories_url = "https://api.nytimes.com/svc/topstories/v2/"
        self.book_reviews_url = "https://api.nytimes.com/svc/books/v3/reviews.json"
        self.article_search_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

    def get_top_stories(self, section):
        url = f"{self.top_stories_url}{section}.json"
        params = {"api-key": self.api_key}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print("Error getting data")
            return None

    def search_books(self, title=None, author=None):
        params = {"api-key": self.api_key}
        if title:
            params["title"] = title
        if author:
            params["author"] = author
        response = requests.get(self.book_reviews_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print("Error getting data")
            return None

    def search_articles_by_news_desk(self, news_desk):
        params = {
            "api-key": self.api_key,
            "fq": f"news_desk:(\"{news_desk}\")"
        }
        response = requests.get(self.article_search_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print("Error getting data")
            return None

class TopStories:
    def __init__(self, api):
        self.api = api

    def handle(self):
        section_name = input("Enter the name of the section (e.g., Food, Fashion, Science, Movies, Sports, etc.): ").strip().lower()
        try:
            top_stories = self.api.get_top_stories(section_name)
            if top_stories:
                print(f"\nTop stories in the '{section_name}' section:")
                for story in top_stories['results']:
                    print(story['title'])
        except requests.exceptions.HTTPError as e:
            print(f"Error fetching data: {e}")

class BookSearch:
    def __init__(self, api):
        self.api = api

    def handle(self):
        print("\nBook Search Options:")
        print("1. Search by Title")
        print("2. Search by Author")
        book_choice = input("Choose an option (1-2): ").strip()

        if book_choice == '1':
            book_title = input("Enter the title of the book 'EX: Becoming' :").strip()
            self.search(title=book_title)
        elif book_choice == '2':
            book_author = input("Enter the author of the book 'EX: Michelle Obama' : ").strip()
            self.search(author=book_author)
        else:
            print("Invalid option, please try again.")

    def search(self, title=None, author=None):
        try:
            book_results = self.api.search_books(title=title, author=author)
            if book_results:
                if title:
                    print(f"\nBook reviews for '{title}':")
                else:
                    print(f"\nBook reviews for books by '{author}':")
                for book in book_results['results']:
                    print(f"Title: {book['book_title']}")
                    print(f"Author: {book['book_author']}")
                    print(f"Summary: {book['summary']}")
                    print(f"URL: {book['url']}")
                    print("-----------")
        except requests.exceptions.HTTPError as e:
            print(f"Error fetching data: {e}")

class ArticleSearch:
    def __init__(self, api):
        self.api = api

    def handle(self):
        news_desk_options = ["Business", "Food", "Jobs", "Sports", "Energy"]
        print(f"Article fields: {', '.join(news_desk_options)}")
        news_desk = input("Enter the Article field (choose from above): ").strip()
        if news_desk not in news_desk_options:
            print("Invalid Article field, please try again.")
            return
        try:
            article_results = self.api.search_articles_by_news_desk(news_desk)
            if article_results:
                print(f"\nArticles in the '{news_desk}' news desk:")
                for article in article_results['response']['docs']:
                    print(f"Title: {article['headline']['main']}")
                    print(f"Snippet: {article['snippet']}")
                    print(f"URL: {article['web_url']}")
                    print("-----------")
        except requests.exceptions.HTTPError as e:
            print(f"Error fetching data: {e}")

class NewsApp:
    def __init__(self, api_key):
        self.api = NewsAPI(api_key)
        self.top_stories = TopStories(self.api)
        self.book_search = BookSearch(self.api)
        self.article_search = ArticleSearch(self.api)

    def display_menu(self):
        print("\nPlease select one of the options:")
        print("1. Top Stories")
        print("2. Books")
        print("3. Article Search")
        print("4. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Choose an option (1-4): ").strip()

            if choice == '1':
                self.top_stories.handle()
            elif choice == '2':
                self.book_search.handle()
            elif choice == '3':
                self.article_search.handle()
            elif choice == '4':
                print("Exiting the program.")
                break
            else:
                print("Invalid option, please try again.")

if __name__ == "__main__":
    api_key = "EuxxzBHXDxHxckDEKJhMAV3dw5QsA7Mj"
    app = NewsApp(api_key)
    app.run()
