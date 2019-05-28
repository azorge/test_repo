#!/usr/bin/python

import sys
from collections import Counter, defaultdict

import json
import os
import re

PASS_CODES = [200, 201, 202, 301, 302, 303, 304, 307]


def find_logs(fpath):
	find_files = []
	log_matcher = '.+log'
	for _, _, files in os.walk(fpath):
		for f in files:
			if re.compile(log_matcher).search(f):
				find_files.append(os.path.join(fpath, f))
	return find_files


def get_results(log):
	if 'access' not in log:
		return None
	results = lambda: defaultdict(results)
	res = results()
	req, ips, bad_requests = parse_access_log(log)
	res[log]['requests'] = req
	res[log]['top_ips'] = ips
	res[log]['bad_requests'] = bad_requests
	print('requests by type: {}'.format(req))
	print('number of all requests: {}'.format(sum(req.values())))
	for key, value in sorted(
			ips.items(), key=lambda item: item[1], reverse=True)[:10]:
		print('top 10 IP address of the client:')
		print("\t ip: {}, count: {}".format(key[:-2], value))
	for k, v in bad_requests.items():
		print(k, v[:10])

	return res


def parse_access_log(f_path):
	bad_requests = {}
	ip_addr = "[\d]{1,3}.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}"
	method = "[\S]{3,6}"
	return_code = "[\d]{3}"
	matcher = re.compile(
		r'(?P<ip>{} )- - \[*.+\] \"(?P<method>{}) '
		r'(?P<url>/.+) HTTP/1.1" (?P<code>{})'.format(
			ip_addr,
			method,
			return_code
		)
	)

	req_results = {}
	with open(f_path) as f:
		log_data = f.readlines()
	data = '\n'.join([x for x in log_data])
	rest = ['GET', 'PATCH', 'POST', 'PUT', 'DELETE']
	for i in rest:
		req_results[i] = len(re.findall(i, data))
	ips = re.findall(r'{} -'.format(ip_addr), data)
	for r in log_data:
		m = matcher.match(r)
		if m:
			if int(m.group('code')) not in PASS_CODES:
				rr = 'ip: {}, method: {}, url: {}, error_code: {}'.format(
					m.group('ip'), m.group('method'), m.group('url'),
					m.group('code'))
				if m.group('code') in bad_requests:
					bad_requests[m.group('code')].append(rr)
				else:
					bad_requests[m.group('code')] = [rr]

	return req_results, dict(Counter(ips)), bad_requests


def main(log_path):
	result_path = os.path.abspath('result.json')
	f_path = os.path.abspath(log_path)
	if os.path.exists(f_path):
		if os.path.isdir(f_path):
			logs = find_logs(f_path)
		else:
			logs = os.path.abspath(f_path)
		if isinstance(logs, list):
			for log in logs:
				res = get_results(log)
				if res:
					if not os.path.exists(result_path):
						with open(result_path, 'w+') as f:
							if res:
								f.write(json.dumps(res, indent=2))
					else:
						with open(result_path, 'r') as load_json:
							lj = json.load(load_json)
						lj.update(res)
						with open(result_path, 'w+') as ff:
							ff.write(json.dumps(lj, indent=2))

		else:
			with open(result_path, 'w+') as f:
				f.write(json.dumps(get_results(logs), indent=2))


if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('You must enter the path to the folder or access.log')
		sys.exit(1)
	path = sys.argv[1]
	main(path)
