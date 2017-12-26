#coding:utf-8
#说明：    测试view类，用于测试后端方法
#作者：    万良卿
#时间：    20171122
from datetime import datetime

from django.http import HttpResponseRedirect, HttpResponse, StreamingHttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.shortcuts import render

from stationconfig import util

class IndexView(View):
    def get(self, request, *args, **kwargs):
        def file_iterator(file_name, chunk_size=512):
            with open(file_name) as f:
                while True:
                    c = f.read(chunk_size)
                    if c:
                        yield c
                    else:
                        break
                    

        file_name = util.creat_temp_file(datetime.now().strftime('%a, %b %d %H:%M'))
        
        response = StreamingHttpResponse(file_iterator(file_name))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_name)
     
        return response