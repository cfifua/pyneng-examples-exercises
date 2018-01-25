# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
with open('ospf.txt') as f:
    lines = f.readlines()

for ospf_route in lines:
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
{:<23} {}\n'''

	print(template.format('Protocol:', protocol, 'Prefix:', prefix, 'AD/Metric:', ad_metrix, 'Next-Hop:', next_hop, 'Last update:', last_update, 'Outbound Interface:', outbound_interface))


