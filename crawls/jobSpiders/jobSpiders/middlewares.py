from selenium import webdriver
from scrapy.http import HtmlResponse
import logging
selenium_logger = logging.getLogger('selenium.webdriver.remote.remote_connection')
selenium_logger.setLevel(logging.WARNING)
logger = logging.getLogger()


class PhantomJSMiddleware(object):

    # overwrite process request
    def process_request(self, request, spider):
        if 'PhantomJS' in request.meta.keys():
            logger.debug('PhantomJS Requesting: '+request.url)
            try:
                service_args = ['--load-images=false', '--disk-cache=true']
                # service_args.append('--proxy=' + request.meta['proxy'][7:])
                driver = webdriver.PhantomJS(service_args=service_args)
                try:
                    driver.set_page_load_timeout(50)
                    driver.get(request.url)
                except Exception:
                    logger.debug("Get Time out")
                finally:
                    logger.debug("Finally")
                    content = driver.page_source.encode('utf-8')
                    url = driver.current_url.encode('utf-8')
                    driver.quit()
                    keywords = request.meta['keywords']
                    if content.find(keywords) == -1:
                        return HtmlResponse(request.url, encoding = 'utf-8', status = 503, body = '')
                    else:
                        return HtmlResponse(url, encoding = 'utf-8', status = 200, body = content)
            except Exception as e:
                logger.warning('PhantomJS Exception!')
                return HtmlResponse(request.url, encoding = 'utf-8', status = 503, body = '')
        else:
            logger.debug('Common Requesting: '+request.url)