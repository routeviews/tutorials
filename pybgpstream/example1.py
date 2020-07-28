#!/usr/bin/env python3

#import pybgpsteam and other necessary libraries
from pybgpstream import BGPStream
import time

#Initialize BGPStream and set it's data interfaces options
bs = BGPStream()
bs.stream.set_data_interface('kafka')
bs.stream.set_data_interface_option('kafka', 'brokers', 'rvdb.routeviews.org:9092')
bs.stream.set_data_interface_option('kafka', 'topic', "^routeviews\.linx\..+\.bmp_raw")
bs.set_live_mode()

#Print records yielded from bs.records() in a bgpreader-like format
for rec in bs.records():
    #make our date human readable
    rec_time = time.strftime('%y-%m-%d %H:%M:%S', time.localtime(rec.time))
    for elem in rec:
        
        print(f"{elem.record_type}|{elem.type}|{rec_time}|{elem.router}|{elem.router_ip}"
              f"|{elem.peer_asn}|{elem.peer_address}|{elem._maybe_field('prefix')}"
              f"|{elem._maybe_field('next-hop')}|{elem._maybe_field('as-path')}")

