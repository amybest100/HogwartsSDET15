from mitmproxy import http


def request(flow: http.HTTPFlow):
    # 修改判断条件
    if "quote.json" in flow.request.pretty_url:
        # 打开在本地的数据文件
        with open("C:\\Users\\zhaox\\Desktop\\quote.json") as f:
            # 创造一个response
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                # 读取文件中的数据作为返回内容
                f.read(),  # (optional) content
                # 指定返回数据的类型
                {"Content-Type": "application/json", "charset": "utf8"}  # (optional) headers
            )
