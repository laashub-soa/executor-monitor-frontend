import json

from flask import Blueprint, request

from component import loki
from config import app_conf

app = Blueprint('service_frontend', __name__,
                url_prefix='')

running_environment = app_conf["loki"]["indexes"]["environment"]
loki_base_url = app_conf["loki"]["base_url"]


def post_2_loki(device):
    request_data = json.loads(request.get_data())
    replicaset = request_data["replicaset"]
    event = request_data["event"]
    indexes = {
        "replicaset": replicaset,
        "environment": running_environment,
    }
    # auth_token = request_data.get("auth_token")
    if request_data.__contains__("code_version"):
        indexes["code_version"] = request_data["code_version"]
    if request_data.__contains__("store_id"):
        indexes["store_id"] = request_data["store_id"]
    if request_data.__contains__("user_id"):
        indexes["user_id"] = request_data["user_id"]

    if request_data.__contains__("log"):
        indexes["job"] = "service_frontend_log_" + device
        values = [str(event) + "\n" + str(request_data["log"])]
    elif request_data.__contains__("time"):
        indexes["job"] = "service_frontend_trace_" + device
        values = [str(event) + "\n" + str(request_data["time"])]
    elif request_data.__contains__("metric"):
        indexes["job"] = "service_frontend_metric_" + device
        values = [str(event) + "\n" + str(request_data["metric"])]
    else:
        return "500"
    return loki.push(indexes, values)


@app.route('/service_frontend_web', methods=['POST'])
def service_frontend_web():
    device = "web"
    return str(post_2_loki(device))


@app.route('/service_frontend_app', methods=['POST'])
def service_frontend_error_log_app():
    device = "app"
    return str(post_2_loki(device))
