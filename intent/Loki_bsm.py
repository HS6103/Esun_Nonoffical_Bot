#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for bsm

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
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply\\reply_bsm.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[bsm] {} ===> {}".format(inputSTR, utterance))

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
    
    if utterance == "[可以]不要收到[綜合對帳單]嗎":
        if CHATBOT_MODE:
            if args[1] == '綜合對帳單':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[帳款][疑義][該]怎麼處理":
        if CHATBOT_MODE:
            if args[0] in ['帳款', '款項'] and args[1] in ['疑義', '疑問', '問題']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[是]否還[會]收到[信用卡][帳單]":
        if CHATBOT_MODE:
            if args[3] in ['帳單', '對帳單']:
                if args[2] in ['信用卡']:
                    resultDICT["response"] = getResponse(utterance, args)
                elif args[2] in ["保險"]:
                    resultDICT["response"] = getResponse("[是]否還[會]收到理財或[保險][對帳單]", args)
        else:
            pass

    if utterance == "[是]否還[會]收到理財或[保險][對帳單]":
        if CHATBOT_MODE:
            if args[2] in ['保險'] and args[3] in ['對帳單']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass
        
    if utterance == "[是]否還[會]收到理財[對帳單]":
        if CHATBOT_MODE:
            if args[2] in ['對帳單']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[綜合對帳單][內容]包含哪些[項目]":
        if CHATBOT_MODE:
            if args[0] == '綜合對帳單' and args[1] in ['內容']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[綜合對帳單][是]否[可]申請補發":
        if CHATBOT_MODE:
            if args[0] == '綜合對帳單':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[綜合對帳單]有哪些寄送[方式]":
        if CHATBOT_MODE:
            if args[0] == '綜合對帳單' and args[1] in ['方式', '管道']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[電子][綜合對帳單][可以]不要加密嗎":
        if CHATBOT_MODE:
            if args[0] in ['電子', '數位'] and args[1] == '綜合對帳單':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "下載[綜合對帳單]卻顯示查無[資料]":
        if CHATBOT_MODE:
            if args[0] == '綜合對帳單' and args[1] in ['資料']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "什麼[時間點][會]收到[綜合對帳單]":
        if CHATBOT_MODE:
            if args[0] in ["時間點", "時間"] and args[2] == '綜合對帳單':   
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass
        
    if utterance == "什麼[時候][會]收到[綜合對帳單]":
        if CHATBOT_MODE:
            if args[0] in ["時候"] and args[2] == '綜合對帳單':   
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何變更[綜合對帳單]寄送[方式]":
        if CHATBOT_MODE:
            if args[0] == '綜合對帳單':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何變更綜合對帳單的收件[地址]":
        if CHATBOT_MODE:
            if args[0] in ['地址', '通訊地址', '簡訊','手機號碼','email', 'e-mail']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "收到退件通知[會]有什麼影響":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "每個月[都][會]收到[綜合對帳單]嗎":
        if CHATBOT_MODE:
            if args[2] == '綜合對帳單':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass
        
    if utterance == "[每星期][都][會]收到[綜合對帳單]嗎":
        if CHATBOT_MODE:
            if args[3] == '綜合對帳單':
                if args[0] == '每月':
                    resultDICT["response"] = "是的!" + getResponse(utterance, args)
                else:
                    resultDICT["response"] = "不是喔!" + getResponse(utterance, args)                    
        else:
            pass

    if utterance == "為什麼[會]收到退件通知":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "為什麼沒收到[綜合對帳單]":
        if CHATBOT_MODE:
            if args[0] == '綜合對帳單':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "為什麼無法開啟[對帳單][檔案]":
        if CHATBOT_MODE:
            if args[0] in ['對帳單', '綜合對帳單'] and args[1] == '檔案':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    return resultDICT