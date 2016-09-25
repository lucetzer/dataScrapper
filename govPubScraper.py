import scrapy

class GovPubSpider(scrapy.Spider):
    name = "Government Publications"
    allowed_domains = ['gov.uk']
    start_urls = [
        'https://www.gov.uk/government/publications?keywords=&publication_filter_option=transparency-data&topics%5B%5D=community-and-society&departments%5B%5D=department-for-education&official_document_status=all&world_locations%5B%5D=all&from_date=&to_date=',
        'https://www.gov.uk/government/publications?keywords=&publication_filter_option=all&topics%5B%5D=all&departments%5B%5D=department-for-international-development&official_document_status=command_papers_only&world_locations%5B%5D=all&from_date=&to_date='
    ]

    def parse(self, response):

        for result_titles in response.css('.document-row'):
            yield {'name': result_titles.css('h3 a ::text').extract_first()}
