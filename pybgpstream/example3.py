#!/usr/bin/env python3

#import the low level _pybgpsteam library and other necessary libraries
from pybgpstream import BGPStream
from ipaddress import ip_network
import requests



if __name__ == '__main__':
    #Initialize BGPStream and set it's data interfaces options
    bs = BGPStream()
    bs.stream.set_data_interface('kafka')
    bs.stream.set_data_interface_option('kafka', 'brokers', 'rvdb.routeviews.org:9092')
    bs.stream.set_data_interface_option('kafka', 'topic', "^routeviews.linx.6939.bmp_raw")
    bs.set_live_mode()
    print("starting stream...")
    while True:
        for rec in bs.records():
            for elem in rec:
                prefix = ip_network(elem.fields['prefix'])
                if elem.type == "A":
                    #lookup RPKI state based on announced route.
                    r = requests.get(f"https://api.routeviews.org/rpki?prefix={prefix}")
                    print(r.json())
