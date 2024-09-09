#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for small_corp

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
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), os.path.join("reply", "reply_small_corp.json")), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[small_corp] {} ===> {}".format(inputSTR, utterance))

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
    
    if utterance == "[公司]貸款跟[個人]貸款有什麼不[一樣]":
        if CHATBOT_MODE:
            if (args[0] == '公司' and args[1] == '個人') or (args[0] == '個人' and args[1] == '公司'):
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[小型][企業]貸款適用申請[對][象]":
        if CHATBOT_MODE:
            if args[0] in ['小', '小型'] and args[1] == '企業':          
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何申請[小型][企業]貸款":
        if CHATBOT_MODE:
            if args[0] in ['小', '小型'] and args[1] == '企業':          
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何知道哪種貸款[模式]最適合[我]":
        if CHATBOT_MODE:
            if args[0] in ['模式', '方式', '方案']:          
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "申請[小型][企業]貸款需要準備哪些[文件]呢":
        if CHATBOT_MODE:
            if args[0] in ['小', '小型'] and args[1] == '企業' and args[2] in ['文件', '資料']:          
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "貸款申請到撥款[會]經過哪些[流程]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    return resultDICT