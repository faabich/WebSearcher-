import reflex as rx
from ddgs import DDGS
from vue.states.home_state import HomeState

# class DDGS:
#     """Dux Distributed Global Search. A metasearch library that aggregates results from diverse web search services.
#
#     Args:
#         proxy (str, optional): proxy for the HTTP client, supports http/https/socks5 protocols.
#             example: "http://user:pass@example.com:3128". Defaults to None.
#         timeout (int, optional): Timeout value for the HTTP client. Defaults to 5.
#         verify: (bool | str):  True to verify, False to skip, or a str path to a PEM file. Defaults to True.
#     """
#
#     def text(
#             query: str,
#             region: str = "us-en",
#             safesearch: str = "moderate",
#             timelimit: str | None = None,
#             max_results: int | None = 10,
#             page: int = 1,
#             backend: str = "auto",
#     ) -> list[dict[str, str]]:
#         """DDGS text metasearch.
#
#         Args:
#             query: text search query.
#             region: us-en, uk-en, ru-ru, etc. Defaults to us-en.
#             safesearch: on, moderate, off. Defaults to "moderate".
#             timelimit: d, w, m, y. Defaults to None.
#             max_results: maximum number of results. Defaults to 10.
#             page: page of results. Defaults to 1.
#             backend: A single or comma-delimited backends. Defaults to "auto".
#
#         Returns:
#             List of dictionaries with search results.
#         """
#
#     def images(
#             query: str,
#             region: str = "us-en",
#             safesearch: str = "moderate",
#             timelimit: str | None = None,
#             max_results: int | None = 10,
#             page: int = 1,
#             backend: str = "auto",
#             size: str | None = None,
#             color: str | None = None,
#             type_image: str | None = None,
#             layout: str | None = None,
#             license_image: str | None = None,
#     ) -> list[dict[str, str]]:
#         """DDGS images metasearch.
#
#         Args:
#             query: images search query.
#             region: us-en, uk-en, ru-ru, etc. Defaults to us-en.
#             safesearch: on, moderate, off. Defaults to "moderate".
#             timelimit: d, w, m, y. Defaults to None.
#             max_results: maximum number of results. Defaults to 10.
#             page: page of results. Defaults to 1.
#             backend: A single or comma-delimited backends. Defaults to "auto".
#             size: Small, Medium, Large, Wallpaper. Defaults to None.
#             color: color, Monochrome, Red, Orange, Yellow, Green, Blue,
#                 Purple, Pink, Brown, Black, Gray, Teal, White. Defaults to None.
#             type_image: photo, clipart, gif, transparent, line.
#                 Defaults to None.
#             layout: Square, Tall, Wide. Defaults to None.
#             license_image: any (All Creative Commons), Public (PublicDomain),
#                 Share (Free to Share and Use), ShareCommercially (Free to Share and Use Commercially),
#                 Modify (Free to Modify, Share, and Use), ModifyCommercially (Free to Modify, Share, and
#                 Use Commercially). Defaults to None.
#
#         Returns:
#             List of dictionaries with images search results.
#         """
#
#     def news(
#             query: str,
#             region: str = "us-en",
#             safesearch: str = "moderate",
#             timelimit: str | None = None,
#             max_results: int | None = 10,
#             page: int = 1,
#             backend: str = "auto",
#     ) -> list[dict[str, str]]:
#         """DDGS news metasearch.
#
#         Args:
#             query: news search query.
#             region: us-en, uk-en, ru-ru, etc. Defaults to us-en.
#             safesearch: on, moderate, off. Defaults to "moderate".
#             timelimit: d, w, m. Defaults to None.
#             max_results: maximum number of results. Defaults to 10.
#             page: page of results. Defaults to 1.
#             backend: A single or comma-delimited backends. Defaults to "auto".
#
#         Returns:
#             List of dictionaries with news search results.
#         """
#
#     def books(
#             query: str,
#             max_results: int | None = 10,
#             page: int = 1,
#             backend: str = "auto",
#     ) -> list[dict[str, str]]:
#         """DDGS books metasearch.
#
#         Args:
#             query: news search query.
#             max_results: maximum number of results. Defaults to 10.
#             page: page of results. Defaults to 1.
#             backend: A single or comma-delimited backends. Defaults to "auto".
#
#         Returns:
#             List of dictionaries with news search results.
#         """

# class DDGSState(rx.State):
#     OS_def = ""
#     OS_weather = ""
#     OS_action = ""
#     OS_map = ""
#     OS_movie = ""



class DuckDuckGoSearch(rx.State):
    home_state: HomeState = HomeState()
    query: str = ""

    def construct_query(self):
        if self.home_state.OS_def != "":
            self.query += "define:" + self.home_state.OS_def
        if self.home_state.OS_weather != "":
            self.query += "weather:" + self.home_state.OS_weather
        if self.home_state.OS_action != "":
            self.query += "stocks:" + self.home_state.OS_action
        if self.home_state.OS_map != "":
            self.query += "map:" + self.home_state.OS_map
        if self.home_state.OS_movie != "":
            self.query += "movie:" + self.home_state.OS_movie

    @rx.event
    async def launch_web_search(self):
        # Construct query for search
        self.construct_query()
        print("QueryString:", self.query)

        results = DDGS().text(self.query, max_results=5, region='ch-fr', safesearch='off', timelimit='y', page=1, backend="google, duckduckgo, brave, yahoo")
        print(results)