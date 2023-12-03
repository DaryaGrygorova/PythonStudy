"""Task 2 - Requests using asyncio and aiohttp
Download all comments from a subreddit of your choice using
URL: https://api.pushshift.io/reddit/comment/search/ .

As a result, store all comments in chronological order in JSON
and dump them to a file. For this task use asyncio and aiohttp
libraries for making requests to Reddit API.

NOTE: For this task I am using the
URL: https://api.themoviedb.org/3
to download list of movies page by page.
"""


import asyncio
import json
import aiohttp


BASE_URL = "https://api.themoviedb.org/3"
API_KEY = "d2f58f193ec10f64760e31baa52fd192"


async def fetch_movies(session, url):
    """Fetch movies by URL"""
    async with session.get(url) as response:
        return await response.json()


async def get_movies(limit_results=None):
    """Returns all movies (count = total_results) or a limit of results from 'discover'. """
    page = 1
    all_movies = []
    async with aiohttp.ClientSession() as session:
        try:
            while True:
                url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&page{page}&include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"
                data = await fetch_movies(session, url)
                movies_by_page = data.get("results", [])

                if not movies_by_page:
                    break

                all_movies += movies_by_page

                if (
                    len(all_movies) >= limit_results
                    if limit_results
                    else data.get("total_results")
                ):
                    break
                page += 1

        except Exception as err:
            print(f"An error occurred: {err}")
    return all_movies


async def main():
    """Main function. Get list of movies and save it to file movies.json"""
    movies = await get_movies(50)
    with open("movies.json", "w", encoding='UTF-8') as file:
        json.dump(movies, file, indent=4)
        print("movies saved to file")


if __name__ == "__main__":
    asyncio.run(main())
