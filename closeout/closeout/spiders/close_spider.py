import re
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

class closeoutSpider(BaseSpider):
    name = "closeout"
    allowed_domains = ["www.realtor.ca"]
    start_urls = [
        'http://www.realtor.ca/propertyDetails.aspx?propertyId=11257989&PidKey=1527560019'
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        suggest_price = hxs.select('//td[@class="MainHeadingRight"]/div/span[1]/text()').extract()
        suggest = re.search('\$([0-9,]+)', suggest_price).groups()[0]

        building_type = hxs.select('//table[@class="PropDetailsTable"]/tr[2]/td[1]/table/tr[1]/td[1]/div[2]/text()')[1].extract()

        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)
