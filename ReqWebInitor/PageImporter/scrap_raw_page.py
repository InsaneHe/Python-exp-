
#_*_coding:utf-8_*_
# This is a sample Python script.


from urllib import request


'''
獲取 Html 源碼
'''
def getWebSource(webUrl: str) -> str:
    page_source = ""
    try:
        httpRes = request.urlopen(webUrl)
        page_source = httpRes.read()
    except BaseException as b:
        raise b
    return page_source



# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    # test-only
    page_source = ""
    httpRes = request.urlopen(r"https://de.products.erstegroup.com/Retail/en/MarketsAndTrends/Overview/index.phtml")
    page_source = httpRes.read()
    print(httpRes.read()[::50])
    print(page_source[::50])
