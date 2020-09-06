from django.shortcuts import render
from django.http import HttpResponse
import sys
import requests
import json
# Create your views here.
def home(request):
    res = render(request,'Home/home.html')
    return res


# def runcode(request):
#     if request.method == 'POST':
#         code_part = request.POST['code_area']  
#         input_part = request.POST['input_area']  
#         y = input_part
#         input_part = input_part.replace("\n"," ").split(",") 

#         def input():
#             a = input_part[0]
#             del input_part[0]
#             return a

#         try:
#             orig_stdout = sys.stdout
#             sys.stdout = open('file.txt', 'w')
#             exec(code_part)
#             sys.stdout.close()
#             sys.stdout=orig_stdout
#             output = open('file.txt', 'r').read()
#         except Exception as e:
#             sys.stdout.close()
#             sys.stdout=orig_stdout
#             output = e
#         print(output)
#     res = render(request,'Home/home.html',{"code":code_part,"input":y,"output":output})
#     return res




def runcode(request):
    if request.method == 'POST':
        code_part = request.POST['code_area']  
        input_part = request.POST['input_area']
        lang = request.POST['lang']
        lang_dict = {   'python3':'3',
                        'java': '3',
                        'c99':'0',
                        'cpp':'0',
                        'ruby':'3',
                        'go':'3',
                        'bash':'3',
                        'csharp':'3',
                        'swift':'3',
                        'dart':'3',
                        
                        }
        # y = input_part
        # input_part = input_part.replace("\n"," ").split(",")  
        headers={'Content-type':'application/json', 'Accept':'application/json'}

        payload = {

            'script':code_part,
            'language': lang,
            'versionIndex': lang_dict[lang],
            'clientId': "enter your client id here",
            'stdin': input_part ,
            'clientSecret':"enter your client secret here"
        }

        r = requests.post('https://api.jdoodle.com/v1/execute',json=payload,headers=headers)
        r_dict = r.text
        data = json.loads(r_dict)
        output =data['output']

    res = render(request,'Home/home.html',{"code":code_part,"output":output,'input':input_part,'lang':lang})
    return res


