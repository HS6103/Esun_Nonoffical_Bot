#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for face_atm

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
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply\\reply_face_atm.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[face_atm] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern=""):
    debugInfo(inputSTR, utterance)
    if utterance == "[別人]拿[我]的[照片]來使用刷臉提款怎麼辦":
        if CHATBOT_MODE:
            if args[1] == '我' and args[2] in ['照片', '相片']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[行動]無卡提款之無卡交易密碼和刷臉提款之無卡交易密碼[一樣]嗎":
        if CHATBOT_MODE:
            if args[1] in ['一樣', '相同']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "金融卡[不見]了還[可以]使用刷臉提款嗎":
        if CHATBOT_MODE:
            if args[0] == '不見':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "刷臉提款時辨識[失敗]怎麼辦":
        if CHATBOT_MODE:
            if args[0] == '失敗':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "刷臉提款的[限額]":
        if CHATBOT_MODE:
            if args[0] == '限額':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "刷臉辨識時如何操作[可]提升辨識[成功率]":
        if CHATBOT_MODE:
            if args[1] == '成功率':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何使用刷臉來提款":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何申請刷臉提款":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何註銷刷臉提款":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "想更新刷臉[ID]":
        if CHATBOT_MODE:
            if args[0].lower() == 'id':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "掛失金融卡需要再[重新]開通刷臉提款服務嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "更換金融卡需要再[重新]開通刷臉提款服務嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "補發金融卡需要再[重新]開通刷臉提款服務嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "設定刷臉[ID]有無[特殊][注意事項]":
        if CHATBOT_MODE:
            if args[0].lower() == 'id' and args[2] in ['注意事項', '規定']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "開通時使用的金融卡[會]影響刷臉提款時[能]選擇的提領[帳戶]嗎":
        if CHATBOT_MODE:
            if args[2] in ['帳戶', '戶頭', '帳號']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    return resultDICT