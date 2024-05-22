from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
import os
import csv


class VkApp:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)
        self._url = None
        self._filename = None
        self._comments = []

    def validate(self) -> None:
        members = dir(self)
        for member in members:
            if member.startswith("validate_"):
                validate_function = getattr(self, member)
                validate_function()

    def validate_link(self) -> None:
        parsed_url = urlparse(self._url)

        domain = parsed_url.netloc

        if "vk.com" not in domain:
            raise ValueError("This link is incorrect. It should be for vk.com")

    def validate_filename(self):
        if not self._filename:
            self._filename = "dataset.csv"

        if not self._filename.endswith(".csv"):
            self._filename += ".csv"

    def get_comments(self) -> list:
        self.driver.get(self._url)
        comments = self.driver.find_elements(By.CLASS_NAME, "wall_reply_text")
        self.to_list(comments)
        self.close()
        return self._comments

    def close(self):
        self.driver.close()
        self.driver.quit()

    def to_list(self, comments) -> list:
        for comment in comments:
            self._comments.append(comment.text)
        return self._comments

    def save_list_to_csv(self, comments):
        _type = "w"
        if os.path.exists(self._filename):
            _type = "a"

        with open(self._filename, _type, newline="") as csvfile:
            writer = csv.writer(csvfile)
            if "w" in _type:
                writer.writerow(["comments"])
            for item in comments:
                writer.writerow([item])

    def get(self, url: str, csv: bool | None = False, filename: str | None = None):
        self._url = url
        self._filename = filename
        self.validate()
        if csv:
            self.save_list_to_csv(self.get_comments())
            return self._comments
        return self.get_comments()
