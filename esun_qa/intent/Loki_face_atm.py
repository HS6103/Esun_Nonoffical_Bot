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
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[無卡交易][密碼][該]如何[重新]設定呢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[無卡交易][密碼][錯誤][上][限]是幾[次]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[無卡交易][密碼][錯誤]達到[上][限][後][應該]怎麼辦":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[行動][無卡提款]之[無卡交易][密碼]和刷臉提款之[無卡交易][密碼][一樣]嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[金融卡][不見]了還[可以]使用刷臉提款嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "刷臉提款時辨識[失敗]怎麼辦":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "刷臉提款的[限額]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "刷臉辨識時如何操作[可]提升辨識[成功率]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何使用刷臉來提款":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何申請刷臉提款":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何註銷刷臉提款":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "想更新刷臉[ID]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "掛失[金融卡]需要再[重新]開通刷臉提款服務嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "更換[金融卡]需要再[重新]開通刷臉提款服務嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "補發[金融卡]需要再[重新]開通刷臉提款服務嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "設定刷臉[ID]有無[特殊][注意事項]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "變更[無卡交易][密碼]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "重設[無卡交易][密碼]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "開通時使用的[金融卡][會]影響刷臉提款時[能]選擇的提領[帳戶]嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    return resultDICT