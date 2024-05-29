# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class AccuweatherPipeline:
    def process_item(self, item, spider):
        item['city'] = item['city'].split(',')[1].strip() if item['city'] else None
        if item['time'] is None:
            del item['time']
        return item


