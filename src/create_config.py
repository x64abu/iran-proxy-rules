import json
from typing import Iterable

import constants as consts
import utils


def shadowrocket(bypass_domains: Iterable[str], ads_domains: Iterable[str]):
    config = (
        "#Shadowrocket\n"
        "[General]\n"
        "private-ip-answer = true\n"
        "bypass-system = true\n"
        "skip-proxy = 192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12, localhost, *.local, captive.apple.com\n"
        "tun-excluded-routes = 10.0.0.0/8, 100.64.0.0/10, 127.0.0.0/8, 169.254.0.0/16, 172.16.0.0/12, 192.0.0.0/24, 192.0.2.0/24, 192.88.99.0/24, 192.168.0.0/16, 198.18.0.0/15, 198.51.100.0/24, 203.0.113.0/24, 224.0.0.0/4, 255.255.255.255/32\n"
        "always-ip-address = true\n"
        "dns-server = tls://1.1.1.1#proxy,https://1.1.1.1/dns-query#proxy\n"
        "fallback-dns-server = tls://1.0.0.1#proxy,https://1.0.0.1/dns-query#proxy\n"
        "dns-direct-system = true\n"
        "dns-direct-fallback-proxy = true\n"
        "ipv6 = true\n"
        "update-url = https://github.com/x64abu/iran-proxy-rules/releases/latest/download/shadowrocket-iran-rules.conf\n"
        "[Rule]\n"
        "IP-CIDR,192.168.0.0/16,DIRECT\n"
        "IP-CIDR,10.0.0.0/8,DIRECT\n"
        "IP-CIDR,172.16.0.0/12,DIRECT\n"
        "IP-CIDR,127.0.0.0/8,DIRECT\n"
        "GEOIP,IR,DIRECT\n"
    )
    config += "\n".join(f"DOMAIN-SUFFIX,{domain},REJECT" for domain in ads_domains) + "\n"
    config += "DOMAIN-SUFFIX,ir,DIRECT\n"
    config += "\n".join(f"DOMAIN-SUFFIX,{domain},DIRECT" for domain in bypass_domains) + "\n"
    config += (        

        "FINAL,PROXY\n"
        "[Host]\n"
        "localhost = 127.0.0.1\n"
    )
    
    utils.save_to_file(consts.shadowrocket_path, config)
