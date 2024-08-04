
#_*_coding:utf-8_*_
# This is a DEMO!

import sys
import os
from lxml import html

TAGET_URL = r"https://de.products.erstegroup.com/Retail/en/MarketsAndTrends/Overview/index.phtml"
global_contemporary_page = ""
INTERNATIONAL_INDICES_CEE_XPATH_BUTTON_CLICK_DEFAULT = r'//*[@id="elem900131"]/div/ul[1]/li[2]/a'
INTERNATIONAL_CURRENCIES_CEE_XPATH_BUTTON_CLICK_DEFAULT = r'//*[@id="elem900128"]/div/ul[1]/li[2]/a'
INTERNATIONAL_INTEREST_RATES_CEE_XPATH_BUTTON_CLICK_DEFAULT = r'//*[@id="elem900130"]/div/ul[1]/li[2]/a'

def switch_to_International_Indices_Cee_Page(xpath_reg_click_to_jump_to_page: str = INTERNATIONAL_INDICES_CEE_XPATH_BUTTON_CLICK_DEFAULT) -> bool:
    try:
        from PageImporter.scrap_raw_page import getWebSource
        global global_contemporary_page
        global_contemporary_page = getWebSource(TAGET_URL).decode("utf-8")

        htmlroot = html.fromstring(global_contemporary_page)
        click_button_elem = htmlroot.xpath(xpath_reg_click_to_jump_to_page)

        target_page_url = r'%s%s' %(TAGET_URL, click_button_elem[0].text)  # Bug
        target_page_url = r'%s%s' %(TAGET_URL, click_button_elem[0].attrib['href'])
        global_contemporary_page = getWebSource(target_page_url).decode("utf-8")
        with open(os.path.join(os.path.dirname(__file__), '../Download_More_Pages/indices_cee_html.page.html'), mode='w', encoding='utf-8') as page:
            page.write(global_contemporary_page)
        return True

    except BaseException as p_to_Indices_Cee_PageT:
        pass

def switch_to_International_Currencies_Cee_Page(xpath_reg_click_to_jump_to_page: str = INTERNATIONAL_CURRENCIES_CEE_XPATH_BUTTON_CLICK_DEFAULT) -> bool:
    try:
        from PageImporter.scrap_raw_page import getWebSource
        global global_contemporary_page
        global_contemporary_page = getWebSource(TAGET_URL).decode("utf-8")

        htmlroot = html.fromstring(global_contemporary_page)
        click_button_elem = htmlroot.xpath(xpath_reg_click_to_jump_to_page)

        target_page_url = r'%s%s' % (TAGET_URL, click_button_elem[0].text)  # Bug
        target_page_url = r'%s%s' % (TAGET_URL, click_button_elem[0].attrib['href'])
        global_contemporary_page = getWebSource(target_page_url).decode("utf-8")
        with open(os.path.join(os.path.dirname(__file__), '../Download_More_Pages/currencies_cee_html.page.html'), mode='w', encoding='utf-8') as page:
            page.write(global_contemporary_page)
        return True

    except BaseException as p_to_International_Curencies_Cee_Page:
        pass

def switch_to_International_Interest_Rates_Cee_Page(xpath_reg_click_to_jump_to_page: str = INTERNATIONAL_INTEREST_RATES_CEE_XPATH_BUTTON_CLICK_DEFAULT) -> bool:
    try:
        from PageImporter.scrap_raw_page import getWebSource
        global global_contemporary_page
        global_contemporary_page = getWebSource(TAGET_URL).decode("utf-8")

        htmlroot = html.fromstring(global_contemporary_page)
        click_button_elem = htmlroot.xpath(xpath_reg_click_to_jump_to_page)

        target_page_url = r'%s%s' % (TAGET_URL, click_button_elem[0].text)  # Bug
        target_page_url = r'%s%s' % (TAGET_URL, click_button_elem[0].attrib['href'])
        global_contemporary_page = getWebSource(target_page_url).decode("utf-8")
        with open(os.path.join(os.path.dirname(__file__), '../Download_More_Pages/interest_rates_cee_html.page.html'),mode='w', encoding='utf-8') as page:
            page.write(global_contemporary_page)
        return True

    except BaseException as p:
        pass


TAGET_URL = r"https://de.products.erstegroup.com/Retail/en/MarketsAndTrends/Overview/index.phtml"
LOCAL_SAVED_PAGE_OF_HTML = None #### ""


MARKET_INTERNATIONAL_INDICES_EUROPE_INTRA_DAY_DATA_TABLE_web_elem_REGEX_XPATH_expr_BY_DEFAULT = \
    r'//*[@id="elem900131"]/div/div/table/tbody/tr[%d]/td[%d]'

MARKET_INTERNATIONAL_CURRENCY_EUROPE_INTRA_DAY_DATA_TABLE_web_elem_REGEX_XPATH_expr_BY_DEFAULT = \
    r'//*[@id="elem900128"]/div/div/table/tbody/tr[%d]/td[%d]' # //*[@id="elem900128"]/

"""
MARKET_INTERNATIONAL_COMMODITIES_EUROPE_INTRA_DAY_DATA_TABLE_web_elem_REGEX_XPATH_expr_BY_DEFAULT = \
    r'//*[@id="elem900129"]/div/div/table/tbody/tr[%d]/td[%d]' # //*[@id="elem900129"]/
"""

MARKET_INTERNATIONAL_INTEREST_RATES_EUROPE_INTRA_DAY_DATA_TABLE_web_elem_REGEX_XPATH_expr_BY_DEFAULT = \
    r'//*[@id="elem900130"]/div/div/table/tbody/tr[%d]/td[%d]' # //*[@id="elem900130"]/


class TextOfStructure(object):

    pass

########import cssselect
symbolOfHtmlTree = None


def main_entry_of_cee():


    get_simple_CEE_Market_InternationalIndices_Europe_Intraday_DataTable_Textonly()
    print('--◽◽◽◽◽◽◽◽--S-E-P-E-R-A-T-E-D---L-I-N-E-S--◽◽◽◽◽◽◽◽--', end = '\n\n')
    get_simple_CEE_Market_InternationalCurrency_Europe_Intraday_DataTable_Textonly()
    print('--◽◽◽◽◽◽◽◽--S-E-P-E-R-A-T-E-D---L-I-N-E-S--◽◽◽◽◽◽◽◽--', end = '\n\n')
    """simple_get_InternationalCommodities_Europe_Intraday_DataTable_Textonly()
    print('--------------S-E-P-E-R-A-T-E-D---L-I-N-E-S------------------------', end = '\n\n')"""
    """get_simple_CEE_InternationalCommodities_Europe_Intraday_DataTable_Textonly()
    print('--------------S-E-P-E-R-A-T-E-D---L-I-N-E-S------------------------', end = '\n\n')"""
    get_simple_CEE_Market_InternationalInterestRates_Europe_Intraday_DataTable_Textonly()
    print('-------------------------◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽-------------------------', end='\n')



def run_internal():
    try:
        from PageImporter.scrap_raw_page import getWebSource
        global symbolOfHtmlTree
        ##global TAGET_URL##
        global global_contemporary_page
        symbolOfHtmlTree = html.fromstring(global_contemporary_page)
        pass
    except BaseException as berror:
        raise berror


def get_simple_CEE_Market_InternationalIndices_Europe_Intraday_DataTable_Textonly \
        (regex_xpath_inputOrByDefault = MARKET_INTERNATIONAL_INDICES_EUROPE_INTRA_DAY_DATA_TABLE_web_elem_REGEX_XPATH_expr_BY_DEFAULT):
    # 调用页面跳转方法
    if None == switch_to_International_Indices_Cee_Page(): raise Exception("debugging _International_Indices_Cee_Page()_ Unknown Error");
    if not switch_to_International_Indices_Cee_Page(): raise Exception("Error for _International_Indices_Cee_Page()_");
    # 更新 symbolOfHtmlTree
    run_internal()
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



def get_simple_CEE_Market_International_Europe_Intraday_DataTable_TextOfStructure():

    pass #TODO : To be added someday in order to export structured-data to external file for storage



def get_simple_CEE_Market_InternationalCurrency_Europe_Intraday_DataTable_Textonly \
        (regex_xpath_inputOrByDefault = MARKET_INTERNATIONAL_CURRENCY_EUROPE_INTRA_DAY_DATA_TABLE_web_elem_REGEX_XPATH_expr_BY_DEFAULT):
    # 调用页面跳转方法
    if None == switch_to_International_Currencies_Cee_Page(): raise Exception("debugging _switch_to_International_Currencies_Cee_Page()_ Unknown Error");
    if not switch_to_International_Currencies_Cee_Page(): raise Exception("Error for _switch_to_International_Currencies_Cee_Page()_");
    # 更新 symbolOfHtmlTree
    run_internal()
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




def get_simple_CEE_Market_InternationalCurrency_Europe_Intraday_DataTable_TextOfStructure():

    pass #TODO : To be added someday in order to export structured-data to extern





def get_simple_CEE_Market_InternationalCommodities_Europe_Intraday_DataTable_Textonly \
        (regex_xpath_inputOrByDefault: str):
    pass


def get_simple_CEE_Market_InternationalCommodities_Europe_Intraday_DataTable_TextOfStructure():

    pass #TODO : To be added someday in order to export structured-data to extern





def get_simple_CEE_Market_InternationalInterestRates_Europe_Intraday_DataTable_Textonly \
        (regex_xpath_inputOrByDefault = MARKET_INTERNATIONAL_INTEREST_RATES_EUROPE_INTRA_DAY_DATA_TABLE_web_elem_REGEX_XPATH_expr_BY_DEFAULT):
    # 调用页面跳转方法
    if None == switch_to_International_Interest_Rates_Cee_Page(): raise Exception("debugging _switch_to_International_Interest_Rates_Cee_Page()_ Unknown Error");
    if not switch_to_International_Interest_Rates_Cee_Page(): raise Exception("Error for _switch_to_International_Interest_Rates_Cee_Page()_");
    # 更新 symbolOfHtmlTree
    run_internal()
    global symbolOfHtmlTree

    raw_content = ""
    table_row_count = 4  -  1  ## varied rows (debugged Aug4 pm)
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
    body_rows = [2, 3, 4] ## varied rows (debugged Aug4 pm)  [2, 3, 4, 5] - [5]

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




def get_simple_CEE_InternationalInterestRates_Europe_Intraday_DataTable_TextOfStructure():

    pass #TODO : To be added someday in order to export structured-data to extern


