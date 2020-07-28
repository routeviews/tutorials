#!/usr/bin/env python3

#import the low level _pybgpsteam library and other necessary libraries
from pybgpstream import BGPStream
from ipaddress import ip_network
import time
import requests



if __name__ == '__main__':
    #Initialize BGPStream and set it's data interfaces options
    bs = BGPStream()
    bs.stream.set_data_interface('kafka')
    bs.stream.set_data_interface_option('kafka', 'brokers', 'rvdb.routeviews.org:9092')
    bs.stream.set_data_interface_option('kafka', 'topic', "^routeviews\.linx\..+\.bmp_raw")
    bs.set_live_mode()
    print("starting stream...")
    while True:
        for rec in bs.records():
            rec_time = time.strftime('%y-%m-%d %H:%M:%S', time.localtime(rec.time))
            for elem in rec:
                prefix = ip_network(elem.fields['prefix'])
                if elem.type == "A":
                    as_path = elem.fields['as-path'].split(" ")
                    #print all elements with 16509 in the path
                    if '16509' in as_path:
                        print(f"peer asn: {elem.peer_asn} as path: {as_path} communities: {elem.fields['communities']} timestamp: {rec_time}")
