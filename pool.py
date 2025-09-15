import requests

origin_ip_pool = []
versify_ip_pool = []



def get_origin_ips(source_url_1):

    print('get_origin_ips running...')
    get_ip_url = source_url_1
    r = requests.get(get_ip_url)
    if r.status_code == 200:
        try:
            origin_ip = r.json()
            # print(origin_ip)
            data = origin_ip['data']
            proxy_list = data['proxy_list']
            try:
                for i in proxy_list:
                    each_ip = i['ip']
                    each_port = i['port']
                    full_ip = f'{each_ip}:{each_port}'
                    origin_ip_pool.append(full_ip)
                    print(f'now add the ip: {full_ip}......')
                print('all ip has been added')
                return origin_ip_pool

            except Exception as e:
                print(f"can't get proxy ip from {get_ip_url} yet:{e} ")

        except Exception as e:
            print(f"the net can't response successfully :{e}")
# get_origin_ips('http://www.zdopen.com/ShortProxy/GetIP/?api=202509101945051507&akey=cb86cf19e6ee5249&count=10&fitter=2&timespan=5&type=3')

def get_versify_ips():
    test_url_is = 'https://www.baidu.com/'
    print('get_versify_ips running...')
    try:
        for full__ip in origin_ip_pool:
            ip_own_proxy = {
                'https:': f'http://{full__ip}',
                'http': f'http://{full__ip}',
            }
            try:
                r = requests.get(test_url_is, proxies=ip_own_proxy)
                if r.status_code == 200:
                    versify_ip_pool.append(full__ip)
                    print(f'full_ip:{full__ip} is available...')
                else:
                    print(f'full_ip:{full__ip} is NOT available...')
                    pass
            except Exception as e:
                print(f"the net can't response successfully :{e}")

        for u in versify_ip_pool:
            print(u)
            print('=='*34)

        return versify_ip_pool

    except Exception as e:
        print(f"the_list is None:error:{e}")


def ip_pool_frame(source_url):
    get_origin_ips(source_url_1=source_url)
    get_versify_ips()

# ip_pool_frame(source_url='http://www.zdopen.com/ShortProxy/GetIP/?api=202509101945051507&akey=cb86cf19e6ee5249&count=10&fitter=2&timespan=5&type=3')