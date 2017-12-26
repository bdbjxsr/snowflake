from django.http import StreamingHttpResponse

from datetime import datetime
import time  
import random

def big_file_download(request):
    # do something...
 
    def file_iterator(file_name, chunk_size=512):
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
 
    the_file_name = "C:/big_file.txt"
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
 
    return response

def creat_temp_file(content):            
    temp_file_dir = "C:/tempdir/"
        
    filenname = ""
    for i in range(0,1):  
        nowTime = datetime.now().strftime("%Y%m%d%H%M%S")#生成当前的时间  
        randomNum = random.randint(0,100)#生成随机数n,其中0<=n<=100  
        if randomNum<=10:  
            randomNum = str(0) + str(randomNum)
        filenname = temp_file_dir + str(nowTime) + str(randomNum) + '.txt'
        print(filenname)
        
    fp = open(filenname, 'w')
    fp.write(content)
    fp.close()
    return filenname