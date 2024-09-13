#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for customer_service

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
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), os.path.join("reply","reply_customer_service.json")), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[customer_service] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern=""):
    debugInfo(inputSTR, utterance)
    for i in range(len(args)):
        args[i] = args[i].lower().strip(' ')   # 前處理，把argument變小寫並去頭尾空格
    
    if utterance == "電話銀行[台幣][綜合]存款轉[定存]服務[相關]規定":
        if CHATBOT_MODE:
            if args[0] in ['台幣', '臺幣'] and args[2] in ['定存', '定期存款']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[行動][裝置]的[系統][需求]":
        if CHATBOT_MODE:
            if args[0] == '行動' and args[1] == '裝置' and args[2] == '系統' and args[3] == '需求':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[語音][密碼]忘記[該]怎麼辦":
        if CHATBOT_MODE:
            if args[0] == '語音' and args[1] == '密碼':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[語音][密碼]忘記或鎖住[該]怎麼辦":
        if CHATBOT_MODE:
            if args[0] == '語音' and args[1] == '密碼':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[語音][密碼]鎖住[該]怎麼辦":
        if CHATBOT_MODE:
            if args[0] == '語音' and args[1] == '密碼':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[電話][銀行]服務[內容]":
        if CHATBOT_MODE:
            if args[0] == '電話' and args[1] == '銀行':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[電話][銀行]轉帳服務有沒[有]什麼限制":
        if CHATBOT_MODE:
            if args[0] == '電話' and args[1] == '銀行':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "不[方便]講[電話]如何聯繫[客服中心]":
        if CHATBOT_MODE:
            if args[1] == '電話' and '客服' in args[2]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "使用[電話][銀行]時[應該]注意[些]什麼呢":
        if CHATBOT_MODE:
            if args[0] == '電話' and args[1] == '銀行':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何設定約定轉入[帳號]":
        if CHATBOT_MODE:
            if args[0] in ['帳號', '帳戶']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何請求停止[電話]行銷":
        if CHATBOT_MODE:
            if args[0] == '電話':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "申請[電話][銀行]時[應該]注意[些]什麼呢":
        if CHATBOT_MODE:
            if args[0] == '電話' and args[1] == '銀行':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    return resultDICT