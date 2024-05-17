from datetime import datetime
from flask import render_template, request
from run import app

from wxcloudrun.response import make_succ_empty_response, make_succ_response, make_err_response



import ctranslate2


# 假设ctranslate2的模型已经正确加载
translator_zh = ctranslate2.Translator("en_zh_cmodel/",device="cpu")#中->英
translator_en = ctranslate2.Translator("zh_en_cmodel/",device="cpu")

@app.route('/api/translate', methods=['POST'])
def translate():
    """
    接收翻译请求，使用ctranslate2进行翻译，并直接返回结果。
    """
    # 获取请求体参数
    data = request.get_json()
    
    # 检查必要的参数是否存在
    if 'direction' not in data or 'sentences' not in data:
        return make_err_response('缺少参数')
    
    # 获取翻译方向和待翻译的句子列表
    direction = data['direction']
    sentences = data['sentences']
    
    
    result = []
    if direction == 'zh2en':
        result = translator_zh.translate_batch([sentences])[0].hypotheses[0]
    else:
        result = translator_en.translate_batch([sentences])[0].hypotheses[0]
    
    # 返回翻译结果
    return make_succ_response(result=result,direction=direction)



@app.route('/api/count', methods=['GET'])
def get_count():
    """
    :return: 计数的值
    """
    
    return make_succ_response('zh2en',["hello","","worl"])
