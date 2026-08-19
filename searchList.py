#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2024/4/30 16:22
# @Author : Carey
# @File : searchList.py
# @Description
import re
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")

import time
import requests
import execjs
import urllib




cookies = {

}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en',
    'From-Domain': '51job_web',
    'Referer': 'https://we.51job.com/pc/search',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}


def openWithJs( jsFile = "sha256.js" ):
    """
    编译执行指定的js文件
    """
    with open( jsFile, "r", encoding='utf-8', errors='replace' ) as f:
        js_tamp = f.read()

    jsDrive = execjs.compile( js_tamp )
    return jsDrive


def getCookieAcwScV2():
    """
    获取参数：acw_sc__v2
    """
    response = requests.get('https://we.51job.com/api/job/search-pc', headers=headers )
    cookies[ 'acw_tc' ] = response.cookies.get( 'acw_tc' )

    args1 = re.findall( r"var(?:\s?)arg1(?:\s?)='(.*?)';" , response.text )[0]
    jsDrive = openWithJs('sha256.js')
    cookie = jsDrive.call( 'getAcwScV2', args1 )
    strCookie = cookie.split(';')[0]
    dicCook = strCookie.split('=')

    cookies[dicCook[0]] = dicCook[1]
    return True


def getSearchPosList():
    """
    请求接口获取数据列表
    """
    iTime = time.time() * 1000
    params = {
        'api_key': '51job',
        'timestamp': str( iTime ),
        'keyword': 'Python',
        'searchType': '2',
        'function': '',
        'industry': '',
        'jobArea': '000000',
        'jobArea2': '',
        'landmark': '',
        'metro': '',
        'salary': '',
        'workYear': '',
        'degree': '',
        'companyType': '',
        'companySize': '',
        'jobType': '',
        'issueDate': '',
        'sortType': '0',
        'pageNum': '1',
        'requestId': '',
        'pageSize': '20',
        'source': '1',
        'accountId': '',
        'pageCode': 'sou|sou|soulb',
    }

    jsDrive = openWithJs( 'sha256.js' )
    uuid = jsDrive.call( 'getUUid' )
    headers[ 'uuid' ] = uuid

    query = urllib.parse.urlencode( params )
    sign = jsDrive.call( 'getSign', f"/api/job/search-pc?{query}" )
    headers[ 'sign' ] = sign

    response = requests.get('https://we.51job.com/api/job/search-pc', params=params, cookies= cookies, headers=headers)
    print( response )
    print( response.text )


if __name__ == '__main__':
    getCookieAcwScV2()
    getSearchPosList()