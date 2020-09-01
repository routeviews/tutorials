#!/usr/bin/env python3

#import the low level _pybgpsteam library and other necessary libraries
from pybgpstream import BGPStream
from ipaddress import ip_network
import requests



if __name__ == '__main__':
    #Initialize BGPStream and set it's data interfaces options
    bs = BGPStream(
            project="routeviews-stream",
            filter="router amsix")
    print("starting stream...")
    while True:
        for rec in bs.records():
            for elem in rec:
                prefix = ip_network(elem.fields['prefix'])
                if elem.type == "A":
                    #lookup RPKI state based on announced route.
                    r = requests.get(f"https://api.routeviews.org/rpki?prefix={prefix}")
                    print(r.json())
