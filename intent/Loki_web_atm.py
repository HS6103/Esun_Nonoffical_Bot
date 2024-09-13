#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for web_atm

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
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), os.path.join("reply", "reply_web_atm.json")), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[web_atm] {} ===> {}".format(inputSTR, utterance))

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
    
    if utterance == "[Edge][瀏覽器]無法[正常]顯示[玉山][WebATM]":
        if CHATBOT_MODE:
            if args[0] == 'edge' and args[4] in userDefinedDICT['webatm']:
                resultDICT["response"] = getResponse(utterance, args)
                resultDICT["imgURL"] = []
                resultDICT["imgURL"] += [
                    "https://www.esunbank.com/zh-tw/-/media/ESUNBANK/Images/Home/About/FAQ/webATM/webatmqa17_1.png",
                    "https://www.esunbank.com/zh-tw/-/media/ESUNBANK/Images/Home/About/FAQ/webATM/webatmqa17_2.png"
                ]
                
        else:
            pass

    if utterance == "[Linux][上]使用[玉山][WebATM]服務的[基本][需求]":
        if CHATBOT_MODE:
            if args[3] in userDefinedDICT['webatm'] and args[5] in ['需求', '條件']:          
                if args[0] == 'linux':
                    resultDICT["response"] = getResponse(utterance, args)
                elif 'mac' or 'ios' in args[0]:
                    resultDICT["response"] = getResponse('[mac][上]使用[玉山][WebATM]服務的[基本][需求]', args)
        else:
            pass

    if utterance == "[TLS]加密通訊[協定]調整教學":
        if CHATBOT_MODE:
            if args[0] == 'tls':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[WebATM]轉帳[成功][對方]卻表示未入帳怎麼辦":
        if CHATBOT_MODE:
            if args[0] in userDefinedDICT['webatm'] and args[1] in ['成功', '完成']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[消費者]透過[金融卡][交易]的[流程]有哪些":
        if CHATBOT_MODE:
            if args[1] == '金融卡' and args[2] == '交易' and args[3] in ['流程', '程序', '步驟']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[系統][一直]提示[我]插入[晶片卡]":
        if CHATBOT_MODE:
            if args[3] == '晶片卡':
                resultDICT["response"] = getResponse(utterance, args)
                resultDICT["imgURL"] = []
                resultDICT["imgURL"] += [
                    "https://www.esunbank.com/zh-tw/-/media/ESUNBANK/Images/Home/About/FAQ/webATM/webatmfaq6.jpg",
                    "https://www.esunbank.com/zh-tw/-/media/ESUNBANK/Images/Home/About/FAQ/webATM/webatmfaq7.jpg",
                    "https://www.esunbank.com/zh-tw/-/media/ESUNBANK/Images/Home/About/FAQ/webATM/webatmfaq8.jpg"
                ]
                
        else:
            pass

    if utterance == "[金融卡][可以][一直]插在[讀卡機][上]嗎":
        if CHATBOT_MODE:
            if '金融卡' in args[0] and args[3] == '讀卡機' and args[4] in ['上', '裡']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[金融卡]在[國][外][可]使用嗎":
        if CHATBOT_MODE:
            if '金融卡' in args[0] and args[1] in ['國', '境', '海'] and args[2] == '外':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[金融卡]被鎖住[該]怎麼辦":
        if CHATBOT_MODE:
            if '金融卡' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[WebATM][可以]在[國][外]使用嗎":
        if CHATBOT_MODE:
            if args[0] in userDefinedDICT['webatm'] and args[2] in ['國', '境', '海'] and args[3] == '外':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[WebATM]有轉帳[金額]的[限制]嗎":
        if CHATBOT_MODE:
            if args[0] in userDefinedDICT['webatm'] and args[1] == '金額' and '限' in args[2]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "「[繳費交易]」和「[轉出交易]」有什麼[不同]":
        if CHATBOT_MODE:
            if args[0] in ['繳費交易', '轉出交易'] and args[1] in ['繳費交易', '轉出交易']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "下拉[選單][中]沒有看到所安裝的[讀卡機][型號]時[應]如何處理":
        if CHATBOT_MODE:
            if args[2] == '讀卡機' and args[3] == '型號':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "什麼是[玉山][WebATM]":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[1] in userDefinedDICT['webatm']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "什麼是「[勞動保障卡]開卡」":
        if CHATBOT_MODE:
            if args[0] == '勞動保障卡':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "使用[Internet Explorer 11]為何[WebATM][網頁]無法[正常]顯示[網頁]":
        if CHATBOT_MODE:
            if args[0] in userDefinedDICT['ie']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "使用[Windows 7]時[元件]出現[亂碼]要怎麼排除":
        if CHATBOT_MODE:
            if args[0] in userDefinedDICT['windows 7'] and args[1] == '元件' and args[2] == '亂碼':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "使用[玉山][WebATM]服務的[基本][條件]":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[1] in userDefinedDICT['webatm']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何安裝[pcscd]":
        if CHATBOT_MODE:
            if args[0] == 'pcscd':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何確定[WebATM][元件]已安裝[成功]":
        if CHATBOT_MODE:
            if args[0] in userDefinedDICT['webatm'] and args[1] == '元件' and args[2] == None or '成功':
                resultDICT["response"] = getResponse(utterance, args)
                resultDICT["imgURL"] = []
                resultDICT["imgURL"] += [
                    "https://www.esunbank.com/zh-tw/-/media/ESUNBANK/Images/Home/About/FAQ/webATM/WebATM_FAQ_Linux1.jpg",
                    "https://www.esunbank.com/zh-tw/-/media/ESUNBANK/Images/Home/About/FAQ/webATM/WebATM_FAQ_Linux2.jpg",
                    "https://www.esunbank.com/zh-tw/-/media/ESUNBANK/Images/Home/About/FAQ/webATM/webatmfaq3.png"
                    ]
        else:
            pass

    if utterance == "如何確定[WebATM][讀卡機][是]否安裝[成功]":
        if CHATBOT_MODE:
            if args[0] in userDefinedDICT['webatm'] and args[1] == '讀卡機' and args[3] == '成功':
                resultDICT["response"] = getResponse(utterance, args)
                resultDICT["imgURL"] = []
                resultDICT["imgURL"] += [
                    "https://www.esunbank.com/zh-tw/-/media/ESUNBANK/Images/Home/About/FAQ/webATM/webatmfaq1.png",
                    "https://www.esunbank.com/zh-tw/-/media/ESUNBANK/Images/Home/About/FAQ/webATM/webatmfaq2.png"                    
                ]
                
        else:
            pass

    if utterance == "如何確認[Smart Card Service]已[啓]動":
        if CHATBOT_MODE:
            if 'smart card' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何確認[讀卡機][是]否[可][正常]運作":
        if CHATBOT_MODE:
            if args[0] == '讀卡機':
                resultDICT["response"] = getResponse(utterance, args)
                resultDICT["imgURL"] = "https://www.esunbank.com/zh-tw/-/media/ESUNBANK/Images/Home/About/FAQ/webATM/webatmfaq10.png"
        else:
            pass

    if utterance == "忘記[金融卡][密碼][該]怎麼辦":
        if CHATBOT_MODE:
            if '金融卡' in args[0] and args[1] == '密碼':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "為什麼[我]不[能]進行非約定[帳戶]轉帳":
        if CHATBOT_MODE:
            if args[2] == '帳戶':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "登入[WebATM]時出現元件未更新":
        if CHATBOT_MODE:
            if args[0] == 'webatm':
                resultDICT["response"] = getResponse(utterance, args)
                resultDICT["imgURL"] = "https://www.esunbank.com/zh-tw/-/media/ESUNBANK/Images/Home/About/FAQ/webATM/webatmqa16.png"                
        else:
            pass

    if utterance == "透過[金融卡][交易]的[流程]有哪些":
        if CHATBOT_MODE:
            if args[0] == '金融卡' and args[1] == '交易' and args[2] == '流程':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    return resultDICT