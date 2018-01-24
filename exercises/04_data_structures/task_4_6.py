# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface     FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

splitted = ospf_route.replace(',','').replace('[','').replace(']','').replace('O','OSPF').replace('via','').split()

protocol = splitted[0]
prefix = splitted[1]
ad_metrix = splitted[2]
next_hop = splitted[3]
last_update = splitted[4]
outbound_interface = splitted[5]

template = '''{:<23} {}
{:<23} {}
{:<23} {}
{:<23} {}
{:<23} {}
{:<23} {}'''

print(template.format('Protocol:', protocol, 'Prefix:', prefix, 'AD/Metric:', ad_metrix, 'Next-Hop:', next_hop, 'Last update:', last_update, 'Outbound Interface:', outbound_interface))
