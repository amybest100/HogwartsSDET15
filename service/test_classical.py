"""
企业微信接口测试
"""
import json

import requests


def test_tag_list():
    corpid = 'wwfee8fa9a12b128af'
    corpsecret = 'R99I6GJ7ts2c4AqgziEab135vt0UWKazuKfCDhbexlY'

    r = requests.get(
        "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
        params={'corpid': corpid, 'corpsecret': corpsecret}
    )
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0

    token = r.json()['access_token']

    r = requests.post(
        "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
        params={"access_token": token},
        json={
            'tag_id': []
        }
    )

    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0
