import json

import requests


def push():
    """
    参考文档: https://grafana.com/docs/loki/latest/api/#post-lokiapiv1push
    :return:
    """
    request_url = ""
    request_data = {
        "streams": [
            {
                "stream": {
                    "label": "value"
                },
                "values": [
                    ["<unix epoch in nanoseconds>", "<log line>"],
                    ["<unix epoch in nanoseconds>", "<log line>"]
                ]
            }
        ]
    }

    # 1570818238000000000
    request_headers = {'content-type': 'application/json'}
    resp = requests.post(request_url, data=json.dumps(request_data), headers=request_headers)
    return resp.text


if __name__ == '__main__':
    push()
