#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for trust_fund

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
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply\\reply_trust_fund.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[trust_fund] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern=""):
    debugInfo(inputSTR, utterance)

    if utterance == "[公司][應]於何時辦理[其]發行股票之簽證":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass
        
    if utterance == "[有價]證券信託的[定義]":
        if CHATBOT_MODE:
            if args[0] == '有價':
                if args[1] in ['特色', '特點']:
                    resultDICT["response"] = getResponse('[有價]證券信託的[特色]', args)
                elif args[1] in ['定義']:
                    resultDICT["response"] = getResponse(utterance, args)
                else:
                    pass
        else:
            pass
        
    if utterance == "[財產]交付信託[業者]有什麼保障":
        if CHATBOT_MODE:
            if args[1] == '業者':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "何謂[信託]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "何謂信託借券":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "來臺從事[證券]投資或[期貨]交易之大陸地區投資人以何為限":
        if CHATBOT_MODE:
            if args[0] in ['證券', '期貨', '股票']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "儲蓄信託最大[特色]為何":
        if CHATBOT_MODE:
            if args[0] in ['特色', '特點']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "員工持股/儲蓄信託之[優點]為何":
        if CHATBOT_MODE:
            if args[0] in ['優點', '好處', '優勢', '利多']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "員工持股/儲蓄信託最大[特色]為何":
        if CHATBOT_MODE:
            if args[0] in ['特色', '特點']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "員工持股最大[特色]為何":
        if CHATBOT_MODE:
            if args[0] in ['特色', '特點']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如欲辦理股票簽證[業務][該]如何辦理":
        if CHATBOT_MODE:
            if args[0] == '業務':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "本行[目前][可]辦理哪些保管[業務]":
        if CHATBOT_MODE:
            if args[2] == '業務':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "本行信託[業務]包含哪些":
        if CHATBOT_MODE:
            if args[0] == '業務':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "為何[外資]或[陸資]欲進行[國內]投資需指定保管[機構]為代理人":
        if CHATBOT_MODE:
            if args[0] in ['外資', '陸資', '中資'] and args[1] in ['外資', '陸資', '中資'] and args[2] == '國內':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "為何[外資]欲進行[國內]投資需指定保管[機構]為代理人":
        if CHATBOT_MODE:
            if args[0] in ['外資', '陸資', '中資'] and args[1] == '國內':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "符合什麼[條件]之[公司]需辦理[其]股票簽證":
        if CHATBOT_MODE:
            if args[0] in ['條件', '標準'] and args[1] in ['公司', '企業']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    return resultDICT