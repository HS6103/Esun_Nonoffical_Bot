#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for paypal

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
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), os.path.join("reply", "reply_paypal.json")), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[paypal] {} ===> {}".format(inputSTR, utterance))

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
    
    if utterance == "PayPal[帳號]連結已失效":
        if CHATBOT_MODE:
            if args[0] in ['帳戶', '帳號']:
                resultDICT["response"].append(getResponse(utterance, args))
        else:
            pass

    if utterance == "PayPal[餘額][突然]不[能]提領":
        if CHATBOT_MODE:
            if args[0] in ['餘額']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "PayPal跨行提領[可]約定的[臺幣]入帳[銀行]有哪些":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[可以]至[玉山銀行][臨櫃][將]PayPal[款項]提領出來嗎":
        if CHATBOT_MODE:
            if args[1] in ['玉山', '玉山銀行'] and '櫃' in args[2]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[數位帳戶][可以]進行PayPal連結及提領服務嗎":
        if CHATBOT_MODE:
            if args[0] == '數位帳戶':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[甲]的PayPal[款項][可以]提領至[乙]的[銀行][帳戶]嗎":
        if CHATBOT_MODE:
            if args[0] != args[3] and args[4] == '銀行' and args[5] in ['帳戶', '帳號', '戶頭']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "什麼時候[會]使用[玉山全球通]":
        if CHATBOT_MODE:
            if '全球通' in args[1]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "什麼是[PayPal]":
        if CHATBOT_MODE:
            if args[0] in ['paypal', '玉山全球通'] or '全球通' in args[0]:
                resultDICT["response"] = getResponse("什麼是{}".format(args[0]), args)
        else:
            pass

    if utterance == "修改PayPal跨行[帳戶][基本][資料][成功][將][資料]送出[後][須]等待多[久][會]收到審核[結果]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "身分證註冊資料不[正確]請[重新]確認資料正確性":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何查詢PayPal提領[明細]":
        if CHATBOT_MODE:
            if args[0] in ['明細']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何申請[玉山全球通]":
        if CHATBOT_MODE:
            if '全球通' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何確認PayPal跨行[帳戶][基本]資料修改[失敗][原因]":
        if CHATBOT_MODE:
            if args[0] in ['帳戶', '帳號'] and args[2] == '失敗':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何確認PayPal跨行[帳戶][基本]資料註冊/修改[失敗][原因]":
        if CHATBOT_MODE:
            if args[0] in ['帳戶', '帳號'] and args[2] == '失敗':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何確認PayPal跨行[帳戶][基本]資料註冊[失敗][原因]":
        if CHATBOT_MODE:
            if args[0] in ['帳戶', '帳號'] and args[2] == '失敗':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "登打完PayPal[帳號][密碼]並點選授權[後]仍無反應":
        if CHATBOT_MODE:
            if args[0] in ['帳戶', '帳號'] and args[1] == '密碼':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "登打完PayPal[帳號][密碼]並點選授權[後]出現[轉圈圈]":
        if CHATBOT_MODE:
            if args[0] in ['帳戶', '帳號'] and args[1] == '密碼' and ['轉圈', 'loading'] in args[3]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "提領PayPal[款項][是]否有[時間]及[金額][上]限":
        if CHATBOT_MODE:
            if ('款' or '額' in args[0]) and (args[2] and args[3] in ['時間', '金額']) and args[4] == '上':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "提領PayPal[款項][是]否有最低提領[金額]":
        if CHATBOT_MODE:
            if ('款' or '額' in args[0]) and '額' in args[2]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "提領PayPal[款項]的[費用]如何計算":
        if CHATBOT_MODE:
            if ('款' or '額' in args[0]) and args[1] in ['費用', '']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "提領PayPal[款項]至[玉山銀行][帳戶]或其他[銀行][帳戶]需多[久][時間][才會]入帳":
        if CHATBOT_MODE:
            if ('款' or '額' in args[0]) and args[1] in ['玉山', '玉山銀行'] and args[2] and args[4] in ['帳戶', '帳號', '戶頭'] and args[6] == '時間':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "有PayPal[帳戶][相關][問題]怎麼辦":
        if CHATBOT_MODE:
            if args[0] in ['帳戶', '帳號'] and '問' in args[2]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "有[玉山銀行][帳戶][我]還[能]申請使用PayPal跨行提領服務嗎":
        if CHATBOT_MODE:
            if args[0] in ['玉山', '玉山銀行']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "查無PayPal[帳號權限]":
        if CHATBOT_MODE:
            if '權限' in args[0]:
                resultDICT["response"].append(getResponse(utterance, args))
        else:
            pass

    if utterance == "為什麼[我]不[能]提領入[他][行][外幣帳戶]":
        if CHATBOT_MODE:
            if args[2] == '他' and args[3] == '行' and '外幣' in args[4]: 
                resultDICT["response"] = getResponse(utterance, args)   
        else:
            pass

    if utterance == "為什麼[我]約定[他][行][臺幣][帳戶][會][失敗]":
        if CHATBOT_MODE:
            if args[1] == '他' and args[2] == '行' and args[3] in ['台幣','新台幣','臺幣','新臺幣'] and args[4] in ['帳戶', '帳號', '戶頭'] and args[6] == '失敗':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "為什麼操作PayPal連結[一直][失敗]":
        if CHATBOT_MODE:
            if args[1] == '失敗':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "為什麼約定[臺幣]轉入[帳號][後]還是不[能]提領":
        if CHATBOT_MODE:
            if args[0] in ['台幣','新台幣','臺幣','新臺幣'] and args[1] in ['帳戶', '帳號', '戶頭']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "為何還沒送出註冊[資料]卻收到審核[失敗]通知信":
        if CHATBOT_MODE:
            if args[1] == '失敗':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[玉山全球通]提供哪些PayPal提領[功能]":
        if CHATBOT_MODE:
            if '全球通' in args[0] and args[1] == '功能':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[玉山全球通]服務[安全]嗎":
        if CHATBOT_MODE:
            if '全球通' in args[0] and args[1] == '安全':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "申請[玉山全球通]服務[是]否有[資格]限制":
        if CHATBOT_MODE:
            if '全球通' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "註冊PayPal跨行[帳戶][基本][資料][成功][將][資料]送出[後][須]等待多[久][會]收到審核[結果]":
        if CHATBOT_MODE:
            if args[0] in ['帳戶', '帳號', '戶頭']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "跨行提領申請註冊提供的佐證[文件]為何":
        if CHATBOT_MODE:
            if args[0] in ['文件', '資料']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "跳出[您]尚未完成臺幣轉入帳號驗證敬請驗證的提醒[視窗]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "透過[玉山全球通]確認提領PayPal[款項][後][能]否取消[交易]呢":
        if CHATBOT_MODE:
            if '全球通' in args[0] and args[4] == '交易':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    return resultDICT