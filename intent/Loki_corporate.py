#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for corporate

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
import json
import os

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
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), os.path.join("reply", "reply_corporate.json")), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[corporate] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern=""):
    debugInfo(inputSTR, utterance)
    
    # 前處理，把argument變小寫並去頭尾空格
    for i in range(len(args)):
        args[i] = args[i].lower().strip(' ')   
    
    # 初始化 resultDICT['response']
    if 'response' not in resultDICT.keys():
        resultDICT['response'] = []
            
    if utterance == "[可以]透過哪些[方式]開發信用狀":
        if CHATBOT_MODE:
            resultDICT["response"].append(getResponse(utterance, args))
        else:
            pass

    if utterance == "[可以]透過哪些[方式]辦理匯出匯款":
        if CHATBOT_MODE:
            resultDICT["response"].append(getResponse(utterance, args))
        else:
            pass

    if utterance == "[外幣][定存]利率是多少":
        if CHATBOT_MODE:
            if args[0] not in ['台幣','新台幣','臺幣','新臺幣'] and args[1] in ['定期存款', '定存']:
                resultDICT["response"].append(getResponse(utterance, args))
        else:
            pass

    if utterance == "[外幣][定存][期間]有哪些選擇":
        if CHATBOT_MODE:
            if args[0] not in ['台幣','新台幣','臺幣','新臺幣'] and args[1] in ['定期存款', '定存'] and args[2] == '期間':
                resultDICT["response"].append(getResponse(utterance, args))
        else:
            pass

    if utterance == "[外幣][活期存款]起存額是多少":
        if CHATBOT_MODE:
            if args[0] not in ['台幣','新台幣','臺幣','新臺幣']:
                if args[1] in ['活期存款', '活存']:
                    resultDICT["response"] = getResponse("[外幣][活期存款]起存額是多少", args)
                elif args[1] in ['定期存款', '定存']:
                    resultDICT["response"] = getResponse("[外幣][定期存款]起存額是多少", args)
        else:
            pass

    if utterance == "[外幣][活期存款]與[定期存款]起存額是多少":
        if CHATBOT_MODE:
            if args[0] not in ['台幣','新台幣','臺幣','新臺幣']:
                if args[1] in ['活期存款', '活存', '定期存款', '定存'] and args[2] in ['活期存款', '活存', '定期存款', '定存']:
                    resultDICT["response"].append(getResponse(utterance, args))
        else:
            pass

    if utterance == "[外幣][票據]託收、買入如何收費":
        if CHATBOT_MODE:
            if args[0] not in ['台幣','新台幣','臺幣','新臺幣'] and args[1] == '票據':
                resultDICT["response"].append(getResponse(utterance, args))
        else:
            pass

    if utterance == "[外幣][票據]託收多[久][會]入帳":
        if CHATBOT_MODE:
            if args[0] not in ['台幣','新台幣','臺幣','新臺幣'] and args[1] == '票據':
                resultDICT["response"].append(getResponse(utterance, args))
        else:
            pass

    if utterance == "[外幣][票據]託收如何收費":
        if CHATBOT_MODE:
            if args[0] not in ['台幣','新台幣','臺幣','新臺幣'] and args[1] == '票據':
                resultDICT["response"].append(getResponse(utterance, args))
        else:
            pass

    if utterance == "[外幣][票據]買入如何收費":
        if CHATBOT_MODE:
            if '幣' or '元' in args[0]:
                if args[0] not in ['台幣','新台幣','臺幣','新臺幣'] and args[1] == '票據':
                    resultDICT["response"].append(getResponse(utterance, args))
            else:
                pass
        else:
            pass

    if utterance == "[外幣]收款如何自動化銷帳":
        if CHATBOT_MODE:
            if args[0] not in ['台幣','新台幣','臺幣','新臺幣']:
                resultDICT["response"].append(getResponse(utterance, args))
        else:
            pass

    if utterance == "[是]否有承作[遠期信用狀賣斷]":
        if CHATBOT_MODE:
            if args[1].lower().strip(' ') in ['遠期信用狀賣斷', 'forfaiting']:
                resultDICT["response"].append(getResponse(utterance, args))
        else:
            pass

    if utterance == "全方位代收網停止支援TLS":
        if CHATBOT_MODE:
            resultDICT["response"].append(getResponse(utterance, args))
        else:
            pass

    if utterance == "匯出匯款如何收費":
        if CHATBOT_MODE:
            resultDICT["response"].append(getResponse(utterance, args))
        else:
            pass

    if utterance == "匯到[大陸]的[時間]需要多[久]":
        if CHATBOT_MODE:
            if args[0] in ['大陸', '中國'] and args[1] == '時間':
                resultDICT["response"].append(getResponse(utterance, args))
        else:
            pass

    if utterance == "匯款至[國][外][一般]需要多[久][才能]入帳":
        if CHATBOT_MODE:
            if args[0] in ['國', '境'] and args[1] == '外' and args[3] in ['久', '快', '慢']:
                resultDICT["response"].append(getResponse(utterance, args))
        else:
            pass

    if utterance == "[國外][票據]託收有受理的限制嗎":
        if CHATBOT_MODE:
            if args[0] == '國外' and args[1] == '票據':
                resultDICT["response"].append(getResponse(utterance, args))
        else:
            pass

    if utterance == "如何匯款至[玉山銀行][帳戶]":
        if CHATBOT_MODE:
            if args[0] in ['玉山', '玉山銀行'] and args[1] in ['帳戶', '戶頭', '帳號']:
                resultDICT["response"].append(getResponse(utterance, args))
        else:
            pass

    if utterance == "如何申請辦理[外幣票據]託收":
        if CHATBOT_MODE:
            if args[0] == '外幣票據':
                resultDICT["response"].append(getResponse(utterance, args))
        else:
            pass

    if utterance == "如何知道已收到信用狀":
        if CHATBOT_MODE:
            resultDICT["response"].append(getResponse(utterance, args))
        else:
            pass

    if utterance == "如何辦理[公司][代表人]變更":
        if CHATBOT_MODE:
            if args[0] in ['公司', '法人', '團體', '管委會'] and args[1] in ['代表人', '戶名']:
                resultDICT["response"] = getResponse("如何辦理[{}][{}]變更".format(args[0], args[1]), args)
        else:
            pass

    if utterance == "如何辦理公司、法人、團體（含管委會）[代表人]變更":
        if CHATBOT_MODE:
            if args[0] in ['代表人', '戶名']:
                resultDICT["response"] = getResponse("如何辦理公司、法人、團體（含管委會）[{}]變更".format(args[0]), args)
        else:
            pass

    if utterance == "如有未掛牌的[特殊][外幣]匯款[需求]如何辦理":
        if CHATBOT_MODE:
            if args[1] in ['外幣', '貨幣']:
                resultDICT["response"].append(getResponse(utterance, args))
        else:
            pass

    if utterance == "如果沒有[玉山銀行]的授信額度[可以]辦理開立信用狀[業務]嗎":
        if CHATBOT_MODE:
            if args[0] in ['玉山', '玉山銀行']:
                resultDICT["response"].append(getResponse(utterance, args))
        else:
            pass

    if utterance == "提供哪些[種類]的[外幣][現鈔]":
        if CHATBOT_MODE:
            if args[0] in ['種類', '國家']:
                if args[1] in ['外幣', '貨幣'] and ('鈔' or '金' in args[2]):
                    resultDICT["response"].append(getResponse(utterance, args))
        else:
            pass

    if utterance == "[法人]外幣帳戶開戶需要準備什麼[文件]":
        if CHATBOT_MODE:
            if args[0] == '法人' and args[1] in ['資料', '文件', '檔案']:
                resultDICT["response"].append(getResponse(utterance, args))
        else:
            pass

    if utterance == "買賣[外幣][現鈔]需要收多少[手續費]":
        if CHATBOT_MODE:
            if args[0] not in ['台幣','新台幣','臺幣','新臺幣'] and ('鈔' or '金' in args[1]) and args[2] in ['費用', '手續費']:
                resultDICT["response"].append(getResponse(utterance, args))
        else:
            pass

    if utterance == "辦理出口信用狀押匯與出口託收[都]需要申請授信額度嗎":
        if CHATBOT_MODE:
            resultDICT["response"].append(getResponse(utterance, args))
        else:
            pass
        
    if utterance == "查詢匯入匯款進度":
        if CHATBOT_MODE:
            resultDICT["response"].append(getResponse(utterance, args))
        else:
            pass
        
    return resultDICT