# import requests
# from selenium.webdriver.common.by import By
# from 未完成.各搜索平台结果汇总.searching_parts import search_encrypted_something,search_start_contain_proxy,search_start_head_less,search_start_no_sand_box
# from urllib.parse import quote
# from bs4 import BeautifulSoup
# import textwrap
#
# test_results = []
# test_relevant_href = []
#
#
# def test_baidu(test_content):
#     test_content_ = quote(test_content)
#     test_url = f'https://www.baidu.com/s?ie=utf-8&wd={test_content_}'
#     test_search_result_location = '/html/body/div[3]/div[4]/div[1]/div[3]'
#
#
#     test_baidu__ = search_start_no_sand_box()
#     test_baidu__.get(test_url)
#     test_baidu__.implicitly_wait(60)
#     test_outer_html = test_baidu__.find_element(By.XPATH,test_search_result_location).get_attribute('outerHTML')  #可用
#     # print(test_outer_html)
#     test_soup = BeautifulSoup(test_outer_html, 'html.parser')
#     test_result_source = test_soup.find_all('div',class_='result')
#     # print(len(test_result_source))
#
#     for i in range(len(test_result_source)):
#         for test_result in test_result_source:
#             # print(test_result)
#             test_text = test_result.text
#             test_text_1 = textwrap.wrap(str(test_text))
#             print(test_text_1)
#             test_results.append(test_text_1)
#
#             test_soup = BeautifulSoup(str(test_result), 'html.parser')
#             # print(test_soup.prettify())
#             test_first_div = test_soup.find('div',class_='result')
#             # print(test_first_div)
#             test_href = test_first_div['mu']
#             test_relevant_href.append(test_href)
#             print(test_href)
#             print('&&&&' * 99)
#
#         print('done')
#         # test_baidu__.close()
#
# # test_baidu('789789789789')
#
# def test_360_net(test_content):
#     test_content_ = quote(test_content)
#     print(f'搜索内容为: {test_content_}')
#     test_url = f'https://www.so.com/s?ie=utf-8&shb=1&hsid=e6068993204486db&src=hao_360so_b_per_bdtest_sj&eci=&nlpv=&ssid=&cp=1c50000160&q={test_content}'
#     print(test_url)
#     try:
#         r = requests.get(test_url)
#         if r.status_code == 200:
#             test_soup = BeautifulSoup(r.content, 'html.parser')
#             # print(test_soup)
#             try:
#                 result_list_content = test_soup.find('ul',class_='result')
#                 # print(result_list_content)
#                 result_deal_list = BeautifulSoup(str(result_list_content), 'html.parser')
#                 each_list = result_deal_list.find_all('li',class_='res-list')
#                 for i in each_list:
#                     print(i.text)
#                     i_soup = BeautifulSoup(str(i), 'html.parser')
#                     i_a_href = i_soup.find('a')
#                     i_href = i_a_href['href']
#                     print(i_href)
#                     # print(i_a_href)
#                     print('&^'*88)
#
#                 # for t in result_list:
#                 #     print(t)
#                 #     print('___' * 77)
#             except Exception as e:
#                 print(f'未搜索到节点:{e}')
#
#
#     except Exception as e:
#         print(e)
#
# # test_360_net('321654987')
#
#
#
#
#
# def test_sou_guo_engine(test_content):
#     test_content_ = quote(test_content)
#     test_url = f'https://www.sogou.com/sie?hdq=AQxRG-2100110000&query={test_content_}&ie=utf8'
#     print(test_url)
#     try:
#         test_search_result_location ='/html/body/div[3]/div[2]/div[1]/div[2]/div'
#         test_engine = search_start_no_sand_box()
#         test_engine.get(test_url)
#         test_engine.implicitly_wait(60)
#
#         source_page = test_engine.find_element(By.XPATH,test_search_result_location).get_attribute('outerHTML')
#         # print(source_page)
#         results_soup = BeautifulSoup(source_page, 'html.parser')
#         # print(results_soup)
#         results = results_soup.find_all('div',class_='vrwrap')
#         for i in results:
#             try:
#                 # print(i)
#                 i_text_wrap = textwrap.wrap(str(i.text))
#                 print(i_text_wrap)
#                 test_results.append(i_text_wrap)
#                 i_soup = BeautifulSoup(str(i), 'html.parser')
#                 i_soup_href_source = i_soup.find('div',class_='r-sech')
#                 # print(i_soup_href_source)
#                 i_soup_href = i_soup_href_source['data-url']
#                 print(i_soup_href)
#                 test_relevant_href.append(i_soup_href)
#
#
#                 print('&&&&' * 99)
#
#             except Exception as e:
#                 pass
#                 print(f'{e}')
#
#         print('done')
#
#     except Exception as e:
#         print(f'driver启动失败:{e}')
#
#
# # test_sou_guo_engine('7878979879797897')
#
# def bing_net_search_engine(test_content):
#     test_content_ = quote(test_content)
#     print(test_content_)
#     test_url = f'https://cn.bing.com/search?q={test_content_}'
#     print(test_url)
#     r = requests.get(test_url)
#     if r.status_code == 200:
#         test_soup = BeautifulSoup(r.content, 'html.parser')
#         # print(test_soup)
#         test_soup_body = test_soup.find('body')
#         test_soup_divs = test_soup_body.find_all('div')
#         # for i in test_soup_divs:
#         #     print(i)
#         #     print('&&&&' * 99)
#         test_soup_div = test_soup_divs[19]
#         # print(test_soup_div)
#         test_soup_main = test_soup_div.find('main')
#         # print(test_soup_main)
#         test_soup_ol = test_soup_main.find('ol')
#         # print(test_soup_ol)
#         try:
#             all_search_results = test_soup_ol.find_all('li',)
#             for y in all_search_results:
#                 try:
#                     # print(y)
#                     y_text_wrap = textwrap.wrap(str(y.text))
#                     print(y_text_wrap)
#                     y_url_deal = BeautifulSoup(str(y), 'html.parser')
#                     y_url_dot = y_url_deal.find('div')
#                     # print(y_url_dot)
#                     y_url_dot_1 = y_url_dot.find('a')
#                     y_url = y_url_dot_1['href']
#                     print(y_url)
#                     print('&&&&' * 99)
#                     if y_text_wrap is None or y_url is None:
#                         print('1')
#                     else:
#                         test_results.append(y_text_wrap)
#                         test_relevant_href.append(y_url)
#                 except Exception as e:
#                     pass
#                     # print(f'该节点内容无效: {e}')
#
#             print('done')
#
#         except Exception as e:
#             print(f'各栏目未找到:{e}')
#
#
# # bing_net_search_engine('电影排行')