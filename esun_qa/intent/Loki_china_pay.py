#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for china_pay

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
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply\\reply_china_pay.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[china_pay] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern=""):
    debugInfo(inputSTR, utterance)
    if utterance == "兩岸支付通收款需要有[支付寶][帳號]嗎":
        if CHATBOT_MODE:
            if args[0] == '支付寶' and args[1] in ['帳戶', '帳號']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "兩岸支付通服務[可以]收[人民幣][款項]嗎":
        if CHATBOT_MODE:
            if args[1] == '人民幣':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "兩岸支付通服務[是]否[會]開立[手續費]用的[收據]":
        if CHATBOT_MODE:
            if args[2] == '手續費':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[可以]透過兩岸支付通儲值[我]的[支付寶][帳戶]嗎":
        if CHATBOT_MODE:
            if args[2] == '支付寶'and args[3] in ['帳戶', '帳號', '戶頭', '錢包', '餘額']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[可以]透過兩岸支付通在[淘寶網]開店收款嗎":
        if CHATBOT_MODE:
            if '淘寶' in args[1]:
                resultDICT["response"] = getResponse(utterance, args)
            else:
                pass
        else:
            pass

    if utterance == "[可以]透過兩岸支付通提領回台灣的[存款][帳戶]嗎":
        if CHATBOT_MODE:
            if args[1] == '存款' and args[2] in ['帳戶', '帳號', '戶頭']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[可以]透過兩岸支付通讓大陸[消費者]在[門市]使用[支付寶]付款嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "特店的販售[商品]有哪些要求":
        if CHATBOT_MODE:
            if args[0] in ['商品', '物品']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "特店的販售[商品]有哪些限制":
        if CHATBOT_MODE:
            if args[0] in ['商品', '物品']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "特店[網站]有哪些要求":
        if CHATBOT_MODE:
            if args[0] in ['網站', '網頁', '頁面']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "特店[網站]有哪些限制":
        if CHATBOT_MODE:
            if args[0] in ['網站', '網頁', '頁面']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "什麼是兩岸支付通":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "大陸[消費者]付款[流程]為何":
        if CHATBOT_MODE:
            if args[0] in ['消費者', '買家', '客戶'] and args[1] in ['流程', '手續', '過程']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何退款":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "撥款[週期]及撥款[幣別]為何":
        if CHATBOT_MODE:
            if args[0] in ['時間', '週期', '頻率', '幣別', '貨幣'] and args[1] in ['時間', '週期', '頻率', '幣別', '貨幣']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass
        
    if utterance == "撥款[幣別]為何":
        if CHATBOT_MODE:
            if args[0] in ['時間', '週期', '頻率']:
                resultDICT["response"] = getResponse("撥款[週期]為何", args)
            elif args[0] in ['幣別', '貨幣']:
                resultDICT["response"] = getResponse("撥款[幣別]為何", args)
            else:
                pass
        else:
            pass

    if utterance == "申請兩岸支付通服務需要支付哪些[費用]":
        if CHATBOT_MODE:
            if args[0] in ['費用']:    
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "申請兩岸支付通服務需要開立[外幣][帳戶]嗎":
        if CHATBOT_MODE:
            if args[1] in ['帳戶', '帳號', '戶頭']:
                if args[0] not in ['台幣', '新台幣', '臺幣', '新臺幣']:
                    resultDICT["response"] = getResponse(utterance, args).format(args[0])
                else:
                    pass
        else:
            pass

    if utterance == "申請兩岸支付通需要準備哪些[資料]":
        if CHATBOT_MODE:
            if args[0] in ['資料', '文件']:    
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "需要標示[人民幣][價格]嗎":
        if CHATBOT_MODE:
            if args[0] == '人民幣' and '價' in args[1]:    
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    return resultDICT