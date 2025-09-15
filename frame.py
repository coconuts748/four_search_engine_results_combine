
from 已完成.各搜索平台结果汇总.pool import ip_pool_frame
from 已完成.各搜索平台结果汇总.login import the_first_ui


def start_progress(source_ips_net):
    ip_pool_frame(source_ips_net)
    the_first_ui()


start_progress(source_ips_net='http://www.zdopen.com/ShortProxy/GetIP/?api=202509142200096711&akey=041047f5cdc2af81&count=2&fitter=1&timespan=5&type=3')