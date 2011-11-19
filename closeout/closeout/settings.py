# Scrapy settings for closeout project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'closeout'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['closeout.spiders']
NEWSPIDER_MODULE = 'closeout.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

