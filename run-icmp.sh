sysctl -w net.ipv4.conf.all.rp_filter=2
sysctl -w net.ipv4.conf.s1.rp_filter=2
sysctl -w net.ipv4.conf.s3.rp_filter=2
sysctl -w net.ipv4.conf.s2.rp_filter=2

python icmp-spoofing.py