import requests
import json


class Spider:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/84.0.4147.89 Safari/537.36'
        }
        # Enter your key that you got in https://dev.heweather.com/
        self.key = ''
        self.url = {
            'city': {'': r'https://geoapi.heweather.net/v2/city/lookup?location=%s&key=%s'},
            'weather': {'now': r'https://devapi.heweather.net/v7/weather/now?location=%s&key=%s',
                        'daily-3': r'https://devapi.heweather.net/v7/weather/3d?location=%s&key=%s',
                        'daily-7': r'https://devapi.heweather.net/v7/weather/7d?location=%s&key=%s',
                        'hourly': r'https://devapi.heweather.net/v7/weather/24h?location=%s&key=%s'},
            # 'rain': {'': r'https://devapi.heweather.net/v7/minutely/5m?location=%s&key=%s'},
            'air': {'': r'https://devapi.heweather.net/v7/air/now?location=%s&key=%s'},
            'warning': {'': r'https://devapi.heweather.net/v7/warning/now?location=%s&key=%s'},
            # 'indices': {'1d': r'https://devapi.heweather.net/v7/indices/1d?location=%s&key=%s&type=%s',
            #             '3d': r'https://devapi.heweather.net/v7/indices/3d?location=%s&key=%stype=%s'},
            # 'sun_moon': {'': r'https://devapi.heweather.net/v7/astronomy/sunmoon?location=%s&key=%s'},
        }
        self.status = {
            '200': True,   # '请求成功'
            '204': False,  # '请求成功，但查询的地区暂时没有需要的数据'
            '400': False,  # '请求错误，可能包含错误的请求参数或缺少必选的请求参数'
            '401': False,  # '认证失败，可能使用了错误的KEY、数字签名错误、KEY的类型错误'
            '402': False,  # '超过访问次数或余额不足以支持继续访问服务'
            '403': False,  # '无访问权限'
            '404': False,  # '查询的数据或地区不存在'
            '429': False,  # '超过限定的QPM（每分钟访问次数）'
            '500': False,  # '无响应或超时，接口服务异常'
        }

    def get_data(self, loc: str, _type: str, _mode='') -> dict:
        """
        :param loc: 城市代码
        :param _type:
        :param _mode:
        :return: 完整json数据
        """
        url = self.url[_type][_mode] % (loc, self.key)
        response = requests.get(url, headers=self.headers).text
        data_dic = json.loads(response)
        if self.check_status(data_dic['code']):
            return data_dic
        else:
            return {}

    def check_status(self, _status: str) -> bool:
        return self.status[_status]


if __name__ == '__main__':
    Test = Spider()
    data = Test.get_data('air', '101010100')
    print(data)
