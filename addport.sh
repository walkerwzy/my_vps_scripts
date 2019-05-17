#!/bin/bash
iptables -I INPUT -p udp --dport 29900 -j ACCEPT
iptables -I INPUT -p udp --dport 29901 -j ACCEPT
iptables -I INPUT -p tcp --dport 8000 -j ACCEPT
iptables -I INPUT -p tcp --dport 53 -j ACCEPT
iptables -I INPUT -p udp --dport 53 -j ACCEPT
iptables -I INPUT -p tcp --dport 6000 -j ACCEPT
iptables -I INPUT -p tcp --dport 7000 -j ACCEPT
iptables -I INPUT -p tcp --dport 7080 -j ACCEPT
iptables -I INPUT -p tcp --dport 7500 -j ACCEPT
iptables -I INPUT -p udp --dport 7000 -j ACCEPT
iptables -I INPUT -p udp --dport 7001 -j ACCEPT
netfilter-persistent save
netfilter-persistent reload
