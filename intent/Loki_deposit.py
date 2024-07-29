#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for deposit

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict,
        refDICT       dict,
        pattern       str

    Output:
        resultDICT    dict
"""

from random import sample
from ArticutAPI import Articut
from datetime import datetime
import json
import os
import re

try:
    with open("account.info", encoding="utf-8") as f:
        accountDICT = json.load(f)
        username = accountDICT['username']
        api_key = accountDICT['api_key']        
except Exception:
    username = None
    api_key = None

DEBUG = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply\\reply_deposit.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[deposit] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getCorrectTime(inputSTR):
    try:
        with open("account.info", encoding="utf-8") as f:
            accountDICT = json.load(f)
            username = accountDICT['username']
            api_key = accountDICT['api_key']
            
    except Exception:
        username = os.environ.get('loki_username')
        api_key = os.environ.get('articut_key')
                
    articut = Articut(username=username, apikey=api_key)
    resultDICT = articut.parse(inputSTR, level='lv3', timeRef=str(datetime.now())[0:19])
    # ##### to be modified below #######
    timeDICT = {}
    if resultDICT["time"][0] != []:
        timeDICT = {
            #'delta_day': datetime.date(resultDICT),
            'hour': resultDICT["time"][0][0]["time_span"]["hour"][0],
            'minute': resultDICT["time"][0][0]["time_span"]["minute"][0]
        }
    else:
        pass
    
    return timeDICT
        
def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern=""):
    debugInfo(inputSTR, utterance)
    if utterance == "[下午6點]至[網路銀行]買/賣[外幣][交易額度]是算在[明天]嗎":
        if CHATBOT_MODE:
            if args[1] in ['網路銀行', '網銀'] and '額度' in args[3]:
                timeDICT = getCorrectTime(inputSTR)
                if timeDICT != {}:
                    if (timeDICT['hour'] < 23) or (timeDICT['hour'] == 23 and timeDICT['minute'] == 0):
                        if args[4] in ['今天', '今日', '當日']:
                            tmpResponse = getResponse(utterance, args).format(args[0], '今天')
                            resultDICT["response"] = "是的! " + tmpResponse
                        else:
                            tmpResponse = getResponse(utterance, args).format(args[0], '明日')
                            resultDICT["response"] = "不是喔! " + tmpResponse
                    else:
                        if args[4] in ['今天', '今日', '當日']:
                            resultDICT["response"] = "不是喔!" + getResponse(utterance, args).format(args[0], '明日')
                        else:
                            resultDICT["response"] = "是的!" + getResponse(utterance, args).format(args[0], '今天')
        else:
            pass

    if utterance == "[下午6點]至[網路銀行]買賣[外幣][交易額度]是算在[明天]嗎":
        if CHATBOT_MODE:
            if args[1] in ['網路銀行', '網銀'] and '額度' in args[3]:
                timeDICT = getCorrectTime(args[0])
                if timeDICT != {}:
                    if (timeDICT['hour'] < 23) or (timeDICT['hour'] == 23 and timeDICT['minute'] == 0):
                        if args[4] in ['今天', '今日', '當日']:
                            tmpResponse = getResponse(utterance, args).format(args[0], '今天')
                            resultDICT["response"] = "是的! " + tmpResponse
                        else:
                            tmpResponse = getResponse(utterance, args).format(args[0], '明日')
                            resultDICT["response"] = "不是喔! " + tmpResponse
                    else:
                        if args[4] in ['今天', '今日', '當日']:
                            resultDICT["response"] = "不是喔!" + getResponse(utterance, args).format(args[0], '明日')
                        else:
                            resultDICT["response"] = "是的!" + getResponse(utterance, args).format(args[0], '今天')
        else:
            pass

    if utterance == "[分公司]如何辦理開戶":
        if CHATBOT_MODE:
            if args[0] == '分公司':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[北海道][也][能]利用[金融卡]提款有什麼樣的[限制]嗎":
        if CHATBOT_MODE:
            if args[0] == '北海道' and args[1] == '金融卡' and ('規' or '限' in args[2]):
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "外來人口換發「新式統一證號」資料變更提醒事項":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[存款人]亡故[須]徵提何[種][文件]以辦理[相關]繼承[事宜]":
        if CHATBOT_MODE:
            if args[0] == '存款人' and args[3] == '文件':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[定期]儲蓄[存款][利息]多少":
        if CHATBOT_MODE:
            if args[0] == '定期' and args[1] == '存款' and args[2] == '利息':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[晚上8點]至[ATM]存款到[玉山][帳戶][會]從[當日]計算利息嗎":
        if CHATBOT_MODE:
            if args[1].lower() in userDefinedDICT['atm'] and args[2] in ['玉山', '玉山銀行']:
                timeDICT = getCorrectTime(args[0])
                if timeDICT != {}:
                    if args[5] in ['今天', '今日', '當日']:
                        resultDICT["response"] = "是的! " + getResponse(utterance, args)
                    else:
                        resultDICT["response"] = "不會，" + getResponse(utterance, args)
        else:
            pass

    if utterance == "[晚上8點]還[能]用[行動銀行]作[外幣][定存]嗎":
        if CHATBOT_MODE:
            if args[2] in ['行動銀行'] and args[3] == '外幣' and args[4] in ['定存', '定期存款']:
                timeDICT = getCorrectTime(args[0])
                if timeDICT != {}:
                    if (9 < timeDICT['hour'] < 23) or (timeDICT['hour'] in [23, 9] and timeDICT['minute'] == 0):
                        resultDICT["response"] = "可以!" + getResponse(utterance, args)
                    else:
                        resultDICT["response"] = "不行喔!"
        else:
            pass

    if utterance == "[下午6點]使用[PayPal]提領入[新][臺幣][帳戶]之交易額度是算於[明日]嗎":
        if CHATBOT_MODE:
            if args[1].lower().strip(' ') == 'paypal' and args[3] in ['台幣', '臺幣'] and args[4] in ['帳戶', '戶頭', '帳號']:
                timeDICT = getCorrectTime(args[0])
                if timeDICT != {}:
                    if (timeDICT['hour'] < 23) or (timeDICT['hour'] == 23 and timeDICT['minute'] == 0):
                        if args[5] in ['今天', '今日', '當日']:
                            tmpResponse = getResponse(utterance, args).format('明日', '今日')
                            resultDICT["response"] = "是的! " + tmpResponse
                        else:
                            tmpResponse = getResponse(utterance, args).format('今日', '明日')
                            resultDICT["response"] = "不是喔! " + tmpResponse
                    else:
                        if args[5] in ['今天', '今日', '當日']:
                            resultDICT["response"] = "不是喔!" + getResponse(utterance, args).format('今日', '明日')
                        else:
                            resultDICT["response"] = "是的!" + getResponse(utterance, args).format('明日', '今日')
        else:
            pass

    if utterance == "[玉山]有哪幾[種][定期]儲蓄[存款]":
        if CHATBOT_MODE:
            if args[0] in ['玉山', '玉山銀行'] and args[1] == '定期' and args[2] == '存款':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[證券][交易][明細]要怎麼查詢":
        if CHATBOT_MODE:
            if args[0] in ['證券', '股票'] and args[1] == '交易' and args[2] == '明細':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[金融卡][不慎]遺失時[該]怎麼辦":
        if CHATBOT_MODE:
            if args[0] == '金融卡':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[金融卡][每日][可以]提款多少[金額]呢":
        if CHATBOT_MODE:
            if args[0] == '金融卡' and args[1] in ['每天', '每日', '一天', '一日'] and args[3] in ['金額', '錢']:
                        resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[金融卡][每日][可以]轉帳及提款多少[金額]呢":
        if CHATBOT_MODE:
            if args[0] == '金融卡' and args[1] in ['每天', '每日', '一天', '一日'] and args[3] in ['金額', '錢']:
                        resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[金融卡][每日][可以]轉帳多少[金額]呢":
        if CHATBOT_MODE:
            if args[0] == '金融卡' and args[1] in ['每天', '每日', '一天', '一日'] and args[3] in ['金額', '錢']:
                        resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[金融卡]在[國][外]提款[手續費]為何":
        if CHATBOT_MODE:
            if args[0] == '金融卡' and args[1] in ['國'] and args[2] == '外':
                if args[3] == '手續費':
                    resultDICT["response"] = getResponse(utterance, args)
                elif args[3] == '限額':
                    resultDICT["response"] = getResponse("[金融卡]在[國][外]提款[限額]為何", args)
        else:
            pass

    if utterance == "[金融卡]在[國][外]]提款[每日][限額]及[手續費]為何":
        if CHATBOT_MODE:
            if args[0] == '金融卡' and args[1] in ['國'] and args[2] == '外':
                if args[3] in ['每天', '每日', '一天', '一日']:
                    if args[4] and args[5] in [ '限額', '手續費']:
                        resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[首次]使用[金融卡]時[應該]注意[些]什麼呢":
        if CHATBOT_MODE:
            if args[0] =='首次' and args[1] == '金融卡':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "借款[利息]為何[現在]變成是[下個月1號]扣呢":
        if CHATBOT_MODE:
            if args[0] == '利息' and args[2].replace('1', '一') in ['每月1號', '下個月1號']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何使用[金融卡]在[國][外]提款":
        if CHATBOT_MODE:
            if args[0] == '金融卡':
                if args[1] in ['國'] and args[2] == '外':
                    resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何保障[金融卡]的[使用][安全]":
        if CHATBOT_MODE:
            if args[0] == '金融卡':
                if args[1] == '使用' and args[2] == '安全':
                    resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何列印扣繳[憑單]":
        if CHATBOT_MODE:
            if args[0] == '憑單':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何辦理[臺幣][一般][存款帳戶]開戶":
        if CHATBOT_MODE:
            if args[0] in ['台幣','新台幣','臺幣','新臺幣'] and args[2] in ['存款帳戶', '存戶']:
                if args[1] in ['一般', '普通', None]:
                    resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何辦理籌備[處]開立[帳戶]":
        if CHATBOT_MODE:
            if args[0] == '處' and args[1] in ['帳戶', '戶頭', '帳號']: 
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何辦理非[個人戶]開立[帳戶]":
        if CHATBOT_MODE:
            if args[0] == '個人戶' and args[1] in ['帳戶', '戶頭', '帳號']: 
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "開戶[是]否[可]委託[他人]辦理":
        if CHATBOT_MODE:
            if args[2] == '他人':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "為什麼[我]領了[存摺][後][都]沒有[之前]的[明細]":
        if CHATBOT_MODE:
            if args[1] in ['存摺'] and args[4] == '明細': 
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "轉帳誤入[他人][帳戶][應]如何處理":
        if CHATBOT_MODE:
            if args[1] in ['帳戶', '戶頭', '帳號']: 
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    return resultDICT