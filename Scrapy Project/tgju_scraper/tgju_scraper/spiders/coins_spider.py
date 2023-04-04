import scrapy
from time import sleep


class CoinSpider(scrapy.Spider):
    name = "coins"
    start_urls = ["https://www.tgju.org/"]

    def parse(self, response):
        coin_table = response.css("table#coin-table")

        # First Row
        # yield {"coin type": ["Live Price", "Lowest Price", "Highest Price", "Time", "Change Percentage Amount"]}

        # Next Rows
        for item in coin_table.css("tbody tr"):
            yield {item.css("th::text").get(): [*item.css("td::text").getall(), item.css("span.low::text").get()]}
