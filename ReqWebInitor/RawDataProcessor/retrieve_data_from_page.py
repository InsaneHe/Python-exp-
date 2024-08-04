
#_*_coding:utf-8_*_
# This is a DEMO!

TAGET_URL = r"https://de.products.erstegroup.com/Retail/en/MarketsAndTrends/Overview/index.phtml"
LOCAL_SAVED_PAGE_OF_HTML = ""


MARKET_INTERNATIONAL_INDICES_EUROPE_INTRA_DAY_DATA_TABLE_web_elem_REGEX_XPATH_expr_BY_DEFAULT = \
    r'//*[@id="elem900131"]/div/div/table/tbody/tr[%d]/td[%d]'

MARKET_INTERNATIONAL_CURRENCY_EUROPE_INTRA_DAY_DATA_TABLE_web_elem_REGEX_XPATH_expr_BY_DEFAULT = \
    r'//*[@id="elem900128"]/div/div/table/tbody/tr[%d]/td[%d]' # //*[@id="elem900128"]/

MARKET_INTERNATIONAL_COMMODITIES_EUROPE_INTRA_DAY_DATA_TABLE_web_elem_REGEX_XPATH_expr_BY_DEFAULT = \
    r'//*[@id="elem900129"]/div/div/table/tbody/tr[%d]/td[%d]' # //*[@id="elem900129"]/

MARKET_INTERNATIONAL_INTEREST_RATES_EUROPE_INTRA_DAY_DATA_TABLE_web_elem_REGEX_XPATH_expr_BY_DEFAULT = \
    r'//*[@id="elem900130"]/div/div/table/tbody/tr[%d]/td[%d]' # //*[@id="elem900130"]/


class TextOfStructure(object):

    pass

from lxml import html
import cssselect
from lxml.cssselect import CSSSelector
##driver = None  ## thre is no need to use webDriver for this simple case
symbolOfHtmlTree = None


def main_entry():

    def run_internal():
        try:
            from ReqWebInitor.PageImporter.scrap_raw_page import getWebSource
            global symbolOfHtmlTree
            global TAGET_URL
            global LOCAL_SAVED_PAGE_OF_HTML
            LOCAL_SAVED_PAGE_OF_HTML = getWebSource(TAGET_URL).decode("utf-8")
            with open('../html.page.html', mode = 'w', encoding = 'utf-8') as page:
                page.write(LOCAL_SAVED_PAGE_OF_HTML)
            symbolOfHtmlTree = html.fromstring(LOCAL_SAVED_PAGE_OF_HTML)

            pass
        except BaseException as berror:
            raise berror

    run_internal()
    simple_get_Market_InternationalIndices_Europe_Intraday_DataTable_Textonly()
    print('--------------S-E-P-E-R-A-T-E-D---L-I-N-E-S------------------------', end = '\n\n')
    simple_get_Market_InternationalCurrency_Europe_Intraday_DataTable_Textonly()
    print('--------------S-E-P-E-R-A-T-E-D---L-I-N-E-S------------------------', end = '\n\n')
    simple_get_Market_InternationalCommodities_Europe_Intraday_DataTable_Textonly()
    print('--------------S-E-P-E-R-A-T-E-D---L-I-N-E-S------------------------', end = '\n\n')
    simple_get_Market_InternationalInterestRates_Europe_Intraday_DataTable_Textonly()
    print('--------------------------------------------------------------------', end='\n')


def simple_get_Market_InternationalIndices_Europe_Intraday_DataTable_Textonly \
        (regex_xpath_inputOrByDefault = MARKET_INTERNATIONAL_INDICES_EUROPE_INTRA_DAY_DATA_TABLE_web_elem_REGEX_XPATH_expr_BY_DEFAULT):
    global symbolOfHtmlTree
    raw_content = ""

    ###testxpath = r'//*[@id="elem900131"]/div/div/table/tr[2]/td[1]'  # //*[@id="elem900131"]/div/div/table/tbody/tr[2]/td[1]/a
    ###print(symbolOfHtmlTree.xpath(testxpath + '/a')[0].attrib['title'])

    table_row_count = 5
    header_rows = [1]
    header_cols_max = 3

    for iRow in header_rows:
        for iCol in range(1, 1 + header_cols_max, 1):
            text = ""
            try:
                xpathr = ("" + regex_xpath_inputOrByDefault) % (iRow, iCol)
                ###print(xpathr)
                text = symbolOfHtmlTree.xpath(xpathr)   ## // some unknwon bug
                text = symbolOfHtmlTree.xpath(xpathr.replace('tbody', ''))

                try:
                    print(text[0].text, end = '\t\t\t')
                except:
                    print(text[0].text, end = '\t\t')

            except: pass
        print()
    print('@' * 55)

    body_colums_count = 3
    body_rows = [2, 3, 4, 5, 6]

    raw_content += '\n\t'
    for iRow in body_rows:
        for iCol in range(1, 1 + body_colums_count, 1):
            text = ""
            try:
                xpathr = ("" + regex_xpath_inputOrByDefault) % (iRow, iCol)
                ###print(xpathr)
                text = symbolOfHtmlTree.xpath(xpathr)   ## // some unknwon bug

                try:
                    text = symbolOfHtmlTree.xpath(xpathr.replace('tbody', '') + '/a')
                    print(text[0].attrib['title'], end = '\t\t\t\t')
                except BaseException as bs:
                    text = symbolOfHtmlTree.xpath(xpathr.replace('tbody', ''))
                    print(text[0].text, sep = bs.__repr__(), end = '\t\t\t')

                ##text = symbolOfHtmlTree.xpath(r'//*[@id="elem900131"]/div/div/table/')
                ###selector = CSSSelector(r'#elem900131 > div > div > table > tbody > tr:nth-child(2) > td.name.cellleft > a')
                ###textselector = selector(symbolOfHtmlTree)

            except BaseException as ns:
                raise ns

            ##//print(text[0])

        print()

    print('&' * 50)
    print('\n')
    pass



def simple_get_Market_International_Europe_Intraday_DataTable_TextOfStructure():

    pass #TODO : To be added someday in order to export structured-data to external file for storage



def simple_get_Market_InternationalCurrency_Europe_Intraday_DataTable_Textonly \
        (regex_xpath_inputOrByDefault = MARKET_INTERNATIONAL_CURRENCY_EUROPE_INTRA_DAY_DATA_TABLE_web_elem_REGEX_XPATH_expr_BY_DEFAULT):
    global symbolOfHtmlTree
    raw_content = ""

    table_row_count = 5
    header_rows = [1]
    header_cols_max = 3

    for iRow in header_rows:
        for iCol in range(1, 1 + header_cols_max, 1):
            text = ""
            try:
                xpathr = ("" + regex_xpath_inputOrByDefault) % (iRow, iCol)
                ###print(xpathr)
                text = symbolOfHtmlTree.xpath(xpathr)   ## // some unknwon bug
                text = symbolOfHtmlTree.xpath(xpathr.replace('tbody', ''))

                try:
                    print(text[0].text, end = '\t\t\t')
                except:
                    print(text[0].text, end = '\t\t')

            except: pass
        print()
    print('@' * 55)

    body_colums_count = 3
    body_rows = [2, 3, 4, 5, 6]

    raw_content += '\n\t'
    for iRow in body_rows:
        for iCol in range(1, 1 + body_colums_count, 1):
            text = ""
            try:
                xpathr = ("" + regex_xpath_inputOrByDefault) % (iRow, iCol)
                text = symbolOfHtmlTree.xpath(xpathr)   ## // some unknwon bug

                try:
                    text = symbolOfHtmlTree.xpath(xpathr.replace('tbody', '') + '/a')
                    print(text[0].attrib['title'], end = '\t\t\t\t')
                except BaseException as bs:
                    text = symbolOfHtmlTree.xpath(xpathr.replace('tbody', ''))
                    print(text[0].text, sep = bs.__repr__(), end = '\t\t\t')

            except BaseException as ns:
                raise ns

        print()

    print('&' * 50)
    print('\n')
    pass




def simple_get_Market_InternationalCurrency_Europe_Intraday_DataTable_TextOfStructure():

    pass #TODO : To be added someday in order to export structured-data to extern





def simple_get_Market_InternationalCommodities_Europe_Intraday_DataTable_Textonly \
        (regex_xpath_inputOrByDefault = MARKET_INTERNATIONAL_COMMODITIES_EUROPE_INTRA_DAY_DATA_TABLE_web_elem_REGEX_XPATH_expr_BY_DEFAULT):
    global symbolOfHtmlTree
    raw_content = ""

    table_row_count = 6
    header_rows = [1]
    header_cols_max = 3

    for iRow in header_rows:
        for iCol in range(1, 1 + header_cols_max, 1):
            text = ""
            try:
                xpathr = ("" + regex_xpath_inputOrByDefault) % (iRow, iCol)
                ###print(xpathr)
                text = symbolOfHtmlTree.xpath(xpathr)   ## // some unknwon bug
                text = symbolOfHtmlTree.xpath(xpathr.replace('tbody', ''))

                try:
                    print(text[0].text, end = '\t\t\t')
                except:
                    print(text[0].text, end = '\t\t')

            except: pass
        print()
    print('@' * 55)

    body_colums_count = 3
    body_rows = [2, 3, 4, 5, 6, 7]

    raw_content += '\n\t'
    for iRow in body_rows:
        for iCol in range(1, 1 + body_colums_count, 1):
            text = ""
            try:
                xpathr = ("" + regex_xpath_inputOrByDefault) % (iRow, iCol)
                text = symbolOfHtmlTree.xpath(xpathr)   ## // some unknwon bug

                try:
                    text = symbolOfHtmlTree.xpath(xpathr.replace('tbody', '') + '/a')
                    print(text[0].attrib['title'], end = '\t\t\t\t')
                except BaseException as bs:
                    text = symbolOfHtmlTree.xpath(xpathr.replace('tbody', ''))
                    print(text[0].text, sep = bs.__repr__(), end = '\t\t\t')

            except BaseException as ns:
                raise ns

        print()

    print('&' * 50)
    print('\n')
    pass




def simple_get_Market_InternationalCommodities_Europe_Intraday_DataTable_TextOfStructure():

    pass #TODO : To be added someday in order to export structured-data to extern





def simple_get_Market_InternationalInterestRates_Europe_Intraday_DataTable_Textonly \
        (regex_xpath_inputOrByDefault = MARKET_INTERNATIONAL_INTEREST_RATES_EUROPE_INTRA_DAY_DATA_TABLE_web_elem_REGEX_XPATH_expr_BY_DEFAULT):
    global symbolOfHtmlTree
    raw_content = ""

    table_row_count = 4
    header_rows = [1]
    header_cols_max = 3

    for iRow in header_rows:
        for iCol in range(1, 1 + header_cols_max, 1):
            text = ""
            try:
                xpathr = ("" + regex_xpath_inputOrByDefault) % (iRow, iCol)
                ###print(xpathr)
                text = symbolOfHtmlTree.xpath(xpathr)   ## // some unknwon bug
                text = symbolOfHtmlTree.xpath(xpathr.replace('tbody', ''))

                try:
                    print(text[0].text, end = '\t\t\t')
                except:
                    print(text[0].text, end = '\t\t')

            except: pass
        print()
    print('@' * 55)

    body_colums_count = 3
    body_rows = [2, 3, 4, 5]

    raw_content += '\n\t'
    for iRow in body_rows:
        for iCol in range(1, 1 + body_colums_count, 1):
            text = ""
            try:
                xpathr = ("" + regex_xpath_inputOrByDefault) % (iRow, iCol)
                text = symbolOfHtmlTree.xpath(xpathr)   ## // some unknwon bug

                try:
                    text = symbolOfHtmlTree.xpath(xpathr.replace('tbody', '') + '/a')
                    print(text[0].attrib['title'], end = '\t\t\t\t')
                except BaseException as bs:
                    text = symbolOfHtmlTree.xpath(xpathr.replace('tbody', ''))
                    print(text[0].text, sep = bs.__repr__(), end = '\t\t\t')

            except BaseException as ns:
                raise ns

        print()

    print('&' * 50)
    print('\n')
    pass




def simple_get_Market_InternationalInterestRates_Europe_Intraday_DataTable_TextOfStructure():

    pass #TODO : To be added someday in order to export structured-data to extern


