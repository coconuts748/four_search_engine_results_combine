import requests
from selenium.webdriver import chrome
import textwrap
from 已完成.各搜索平台结果汇总.pool import versify_ip_pool
from bs4 import BeautifulSoup
from 已完成.各搜索平台结果汇总.parts import search_start_no_sand_box,search_start_head_less,search_start_contain_proxy
from selenium.webdriver.common.by import By
from urllib.parse import quote


search_results = []
search_results_relevant_href = []


def search_engine_baidu(search_thing,baidu_ip):
    search_thing_ = quote(search_thing)
    baidu_url = f'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd={search_thing_}'
    try:
        baidu_search_results_location = '/html/body/div[3]/div[4]/div[1]/div[3]'
        baidu_start = search_start_contain_proxy(baidu_ip)
        baidu_start.get(baidu_url)
        baidu_start.minimize_window()
        baidu_start.implicitly_wait(120)
        # outer_html = baidu_start.get_attribute('outerHTML')
        # print(outer_html)
        try:

            baidu_start.find_element(By.XPATH,baidu_search_results_location)
            baidu_result = baidu_start.get_attribute('outerHTML')
            test_soup = BeautifulSoup(str(baidu_result), 'html.parser')
            test_result_source = test_soup.find_all('div', class_='result')
            # print(len(test_result_source))

            for i in range(len(test_result_source)):
                for test_result in test_result_source:
                    try:
                        test_text = test_result.text
                        test_text_1 = textwrap.wrap(str(test_text))
                        print(test_text_1)
                        search_results.append(test_text_1)

                        test_soup = BeautifulSoup(str(test_result), 'html.parser')
                        # print(test_soup.prettify())
                        test_first_div = test_soup.find('div', class_='result')
                        # print(test_first_div)
                        test_href = test_first_div['mu']
                        search_results_relevant_href.append(test_href)
                        print(test_href)
                        print('&&&&' * 99)
                    except Exception as e:

                        print(f'各搜索结果处理失败:{e}')

                print('done')
                return search_results,search_results_relevant_href

        except Exception as e:
            print(f'网站内容寻找失败:{e}')

    except Exception as e:
        print(f'访问失败:{e}')

# search_engine_baidu('酒','59.42.100.159:50266')
###################baidu_net#####################################

def search_360_net(search_thing,each_360_ip):
    search_proxy={
        'https:': f'http://{each_360_ip}',
        'http:': f'http://{each_360_ip}'
    }

    test_content_ = quote(search_thing)
    print(f'搜索内容为: {test_content_}')
    test_url = f'https://www.so.com/s?ie=utf-8&shb=1&hsid=e6068993204486db&src=hao_360so_b_per_bdtest_sj&eci=&nlpv=&ssid=&cp=1c50000160&q={test_content_}'
    print(test_url)
    try:
        r = requests.get(test_url,proxies=search_proxy)
        if r.status_code == 200:
            test_soup = BeautifulSoup(r.content, 'html.parser')
            # print(test_soup)
            try:
                result_list_content = test_soup.find('ul',class_='result')
                # print(result_list_content)
                result_deal_list = BeautifulSoup(str(result_list_content), 'html.parser')
                each_list = result_deal_list.find_all('li',class_='res-list')
                for i in each_list:
                    i_wrap = textwrap.wrap(str(i.text))
                    i_wrap_text = i_wrap
                    print(i_wrap_text)
                    search_results.append(i_wrap_text)

                    i_soup = BeautifulSoup(str(i), 'html.parser')
                    i_a_href = i_soup.find('a')
                    i_href = i_a_href['href']
                    print(i_href)
                    search_results_relevant_href.append(i_href)
                    # print(i_a_href)
                    print('&^'*88)

                print('done')
                return search_results,search_results_relevant_href

            except Exception as e:
                print(f'未搜索到节点:{e}')

    except Exception as e:
        print(e)

# search_360_net('酒',each_360_ip='117.65.113.147:35986')

##################360_net###################


def search_sou_guo_engine(search_thing,each_sou_gou_ip):
    test_content_ = quote(search_thing)
    test_url = f'https://www.sogou.com/sie?hdq=AQxRG-2100110000&query={test_content_}&ie=utf8'
    print(test_url)
    try:
        test_search_result_location ='/html/body/div[3]/div[2]/div[1]/div[2]/div'
        test_engine = search_start_contain_proxy(each_sou_gou_ip)
        test_engine.get(test_url)
        test_engine.implicitly_wait(60)

        source_page = test_engine.find_element(By.XPATH,test_search_result_location).get_attribute('outerHTML')
        # print(source_page)
        results_soup = BeautifulSoup(source_page, 'html.parser')
        # print(results_soup)
        results = results_soup.find_all('div',class_='vrwrap')
        for i in results:
            try:
                # print(i)
                i_text_wrap = textwrap.wrap(str(i.text))
                print(i_text_wrap)
                search_results.append(i_text_wrap)
                i_soup = BeautifulSoup(str(i), 'html.parser')
                i_soup_href_source = i_soup.find('div',class_='r-sech')
                # print(i_soup_href_source)
                i_soup_href = i_soup_href_source['data-url']
                print(i_soup_href)
                search_results_relevant_href.append(i_soup_href)

                print('&&&&' * 99)

            except Exception as e:
                pass
                print(f'{e}')

        print('done')
        test_engine.quit()


    except Exception as e:
        print(f'driver启动失败:{e}')


# search_sou_guo_engine('酒',each_sou_gou_ip='117.65.113.147:35986')

##################sou_guo_net###################

def bing_net_search_engine(search_thing,each_bing_net_ip):
    bing_prosy = {
        'https:': f'http://{each_bing_net_ip}',
        'http:': f'http://{each_bing_net_ip}'
    }

    test_content_ = quote(search_thing)
    print(test_content_)
    test_url = f'https://cn.bing.com/search?q={test_content_}'
    print(test_url)
    try:
        r = requests.get(test_url, proxies=bing_prosy)
        if r.status_code == 200:
            test_soup = BeautifulSoup(r.content, 'html.parser')
            # print(test_soup)
            test_soup_body = test_soup.find('body')
            test_soup_divs = test_soup_body.find_all('div')
            # for i in test_soup_divs:
            #     print(i)
            #     print('&&&&' * 99)
            test_soup_div = test_soup_divs[19]
            # print(test_soup_div)
            test_soup_main = test_soup_div.find('main')
            # print(test_soup_main)
            test_soup_ol = test_soup_main.find('ol')
            # print(test_soup_ol)
            try:
                all_search_results = test_soup_ol.find_all('li', )
                for y in all_search_results:
                    try:
                        # print(y)
                        y_text_wrap = textwrap.wrap(str(y.text))
                        print(y_text_wrap)
                        y_url_deal = BeautifulSoup(str(y), 'html.parser')
                        y_url_dot = y_url_deal.find('div')
                        # print(y_url_dot)
                        y_url_dot_1 = y_url_dot.find('a')
                        y_url = y_url_dot_1['href']
                        print(y_url)
                        print('&&&&' * 99)
                        if y_text_wrap is None or y_url is None:
                            print('1')
                        else:
                            search_results.append(y_text_wrap)
                            search_results_relevant_href.append(y_url)
                    except Exception as e:
                        pass
                        # print(f'该节点内容无效: {e}')

                print('done')

            except Exception as e:
                print(f'各栏目未找到:{e}')
    except Exception as e:
        print('代理出错:{}'.format(e))


bing_net_search_engine('电影排行',each_bing_net_ip='117.65.113.147:35986')

##################bing_net###################

def total_search_engine_running_frame(search_thing):
    for single_ip in versify_ip_pool:
        try:
            # search_engine_baidu(search_thing, single_ip)    如网速快可启用
            search_360_net(search_thing, single_ip)
            # search_sou_guo_engine(search_thing, single_ip)   如网速快可启用
            bing_net_search_engine(search_thing, single_ip)

            def creat_data_totally():
                try:
                    print()
                    for i in range(0, len(search_results) + 1):
                        with open('combine_search_result.txt', 'a', encoding='utf-8') as f:
                            f.write(f'{search_results[i]}\n{search_results_relevant_href[i]}\n')


                    # with open('combine_search_result.txt', 'a', encoding='utf-8') as f:
                    #     f.write(f'{search_thing}\n{search_results_relevant_href}')

                    print('done')

                except Exception as e:
                    print(f'数据处理失败:{e}')
            creat_data_totally()

        except Exception as e:
            pass

