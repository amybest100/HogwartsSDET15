# request方法名称不能修改
from mitmproxy import http


def request(flow: http.HTTPFlow):
    # 增加请求头信息中的字段
    flow.request.headers["myheader"] = "mimi"
    print(flow.request.headers)
