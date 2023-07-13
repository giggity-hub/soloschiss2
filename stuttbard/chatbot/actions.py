from selection import Selection
import re
import webbrowser

class Actions:
    def __init__(self) -> None:
        pass

    def open_website(self, url):
        webbrowser.open(url)