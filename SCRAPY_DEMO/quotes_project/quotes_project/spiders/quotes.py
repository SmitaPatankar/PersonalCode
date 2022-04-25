import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from ..items import QuotesProjectItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/page/login']
    page_number = "2"

    def parse(self, response):
        token = response.css("form input::attr(value)").extract()
        return FormRequest.from_response(response, formdata={
            "csrf_token": token,
            "username": "concealed",
            "password": "concealed"
            }, callback=self.start_scraping)

    def start_scraping(self, response):
        open_in_browser(response)
        item = QuotesProjectItem()
        all_quotes = response.css("div")  # .xpath
        for q in all_quotes:
            title = q.css("span.text::text").extract() # extract_first
            author = q.css(".author::text").extract()
            tag = q.css(".tag::text").extract()
            item["title"] = title
            item["author"] = author
            item["tag"] = tag
            yield item
        next_page = f"http://quotes.toscrape.com/page/{QuotesSpider.page_number}/"
        QuotesSpider.page_number += 1
        yield response.follow(next_page, callback=self.parse)
