import json
import time

import requests


def push(indexes, values):
    """
    参考文档: https://grafana.com/docs/loki/latest/api/#post-lokiapiv1push
    :return:
    """
    request_url = "http://loki.logging.local.wangjiahuan.com" + "/loki/api/v1/push"
    request_data_values = []
    for item in values:
        request_data_values.append([str(int(time.time_ns())), str(item)])
    request_data = {
        "streams": [{"stream": indexes, "values": request_data_values}]
    }
    request_headers = {'content-type': 'application/json', 'Content-Encoding': 'gzip'}
    resp = requests.post(request_url, data=json.dumps(request_data), headers=request_headers)
    return resp.status_code
