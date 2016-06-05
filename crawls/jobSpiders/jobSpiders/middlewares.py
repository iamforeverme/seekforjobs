from selenium import webdriver
import logging
from scrapy.http import HtmlResponse
import time
import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger()


class PhantomJSMiddleware(object):
    # overwrite process request
    def process_request(self, request, spider):
        if True:#request.meta.has_key('PhantomJS'):
            logger.debug('PhantomJS Requesting: '+request.url)
            service_args = ['--load-images=false', '--disk-cache=true']
            if request.meta.has_key('proxy'):
                logger.warning('PhantomJS proxy:'+request.meta['proxy'][7:])
                service_args.append('--proxy='+request.meta['proxy'][7:])
            try:
                driver = webdriver.PhantomJS(service_args = service_args)
                driver.get(request.url)
                try:
                    # driver.set_page_load_timeout(20)
                    # driver.get(request.url)
                    element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "standout experimental-fade experimental-fade-completed"))
                    )
                except Exception:
                    logger.debug("Get Time out")
                finally:
                    logger.debug("Finally")
                    content = driver.page_source.encode('utf-8')
                    url = driver.current_url.encode('utf-8')
                    driver.quit()
                    if content == '<html><head></head><body></body></html>':
                        return HtmlResponse(request.url, encoding = 'utf-8', status = 503, body = '')
                    else:
                        return HtmlResponse(url, encoding = 'utf-8', status = 200, body = content)

            except Exception, e:
                logger.warning('PhantomJS Exception!')
                return HtmlResponse(request.url, encoding = 'utf-8', status = 503, body = '')
        else:
            logger.debug('Common Requesting: '+request.url)