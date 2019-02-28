# from signature_data import parse_data

import requests
import json
import re




#获取URL参数dytk,tac
def get_formdata():
    response=requests.get(url,headers=headers)
    dytk=re.findall(r"dytk: '(.*?)'",response.text,re.S)
    dytk=dytk[0]
    tac=re.findall(r"<script>tac=(.*?)</script>",response.text,re.S)
    tac = "var tac={};".format(tac[0])
    return dytk,tac

#写入html,生成signature
def write_html(tac,user_id):
    with open('head.txt','r') as f1:
        head_txt=f1.read()
    with open('foot.txt','r') as f2:
        foot_txt=f2.read().replace('&user_id&',user_id)
    with open('test.html','w') as fw:
        fw.write(head_txt+'\n'+tac+'\n'+foot_txt)


def get_movie(user_url):
    # movie_urls=[]
    response = requests.get(user_url, headers=headers)
    json_data = json.loads(response.text)
    if json_data['aweme_list']==[]:
        print("解析失败")
    else:
        for item in json_data['aweme_list']:
            movie_url=item['video']['play_addr']['url_list'][0]
            movie_response=requests.get(movie_url, headers=headers)
            movie_name=((movie_url.split('/')[-1]).split('=')[-2]).split('&')[0]+'.mp4'
            with open(movie_name,'wb') as f:
                print("{} 正在下载中.....".format(movie_url))
                f.write(movie_response.content)

    print("全部下载完成")

if __name__ == '__main__':
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    url = 'https://www.iesdouyin.com/share/user/102951265836'
    user_id=url.split('/')[-1]
    dytk,tac=get_formdata()
    write_html(tac,user_id)
    input_signature = input("输入秘钥：")
    user_url = 'https://www.iesdouyin.com/aweme/v1/aweme/post/?user_id={}&count=21&max_cursor=0&aid=1128&_signature={}&dytk={}'\
        .format(user_id,input_signature, dytk)
    get_movie(user_url)