#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for crossboarding

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
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply\\reply_crossboarding.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[crossboarding] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern=""):
    debugInfo(inputSTR, utterance)
    if utterance == "[可]使用哪些[銀行][帳戶]做為[玉山][電子]支付提領[帳戶]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[可以]使用[信用卡]儲值[玉山][電子]支付[帳戶][餘額]嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[我][可以]註冊多少[組][玉山][電子]支付[帳戶]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[手續費][會]退嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[樂享優惠專區]是甚麼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[活動]結束時[會]如何告知":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[玉山Wallet][電子]支付[交易][資訊][會]保留多[久]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[玉山Wallet][電子]支付[交易][資訊]要怎麼查詢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[玉山Wallet][電子]支付[可]綁定哪些支付[工具]呢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[玉山Wallet][電子]支付[可以]綁定非[玉山銀行][信用卡]或[銀行][帳戶]作為支付[工具]嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[玉山Wallet][電子]支付[條碼]付的付款[方式]為何":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[玉山Wallet][電子]支付「[條碼]付」(由[店家]掃描[手機條碼]) 的付款[方式]為何":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[玉山Wallet][電子]支付支援哪些繳費[項目]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[玉山Wallet][電子]支付於日本[PayPay][掃碼]付服務的[匯率]怎麼換算":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[玉山Wallet][電子]支付於日本[PayPay][掃碼]付服務需要負擔[國外][交易][服務費]嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[玉山Wallet][電子]支付綁定[信用卡]儲值付款[可以]使用[信用卡][紅利點數]折抵嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[玉山Wallet][電子]支付綁定[信用卡]消費[可以]獲得[信用卡]回饋嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[玉山Wallet][電子]支付重複繳交[水]/[電費][可以]退款嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[玉山Wallet][電子]支付重複繳交[水費][可以]退款嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[玉山][電子]支付[Email]驗證信[是]否有[時間]限制":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[玉山][電子]支付[帳戶][可以]綁定幾[組]提領[帳號]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[玉山][電子]支付[帳戶]提領[是]否[會]被收取[手續費]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[玉山][電子]支付[帳戶]是什麼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[玉山][電子]支付[帳戶]的[交易限額]是多少":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[玉山][電子]支付[帳戶款項]轉出完成[後][銀行][帳號備註欄位]為何":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[玉山][電子]支付[簡訊]驗證[是]否有[次數][上][限]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[該]如何使用[玉山Wallet][電子]支付於日本[PayPay][掃碼]付服務呢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[身分證]認證[是]否有[次數]限制":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[身分證]認證若[多次]認證[失敗][該]怎麼辦":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[電子]支付儲值[是]否[會]被收取[手續費]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "使用[玉山Wallet][電子]支付[交易][失敗]怎麼辦":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "使用[玉山Wallet][電子]支付不[小心]重複繳費了怎麼辦":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "使用[玉山Wallet][電子]支付若發生退款[情形][我]要如何處理":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "使用[玉山Wallet][電子]支付若發生退款[情形][款項][會]退回至哪裡":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "儲值完成[後][銀行][帳號備註欄位]為何":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "出現「[信用卡]儲值付款[交易]已達[限額]，請選擇其他付款[方式]」怎麼辦":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "哪些[PayPay][通路][可以]使用":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "哪裡[可以]使用[玉山Wallet]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "多[久][才能]收到[玉山][電子]支付—跨境網購服務的[退款]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何了解[樂享優惠][活動]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何使用[獨樂樂]的[購物金]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何使用[玉山Wallet][電子]支付綁定[水]/[電號]並設定繳款提醒通知":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何使用[玉山Wallet][電子]支付綁定[水號]並設定繳款提醒通知":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何使用[玉山Wallet][電子]支付進行繳費":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何使用[玉山][電子]支付—跨境網購[超商]繳費(不取貨)":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何使用[玉山][電子]支付—跨境網購轉帳付款":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何提供[玉山][電子]支付補件[資料]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何提升[玉山][電子]支付的[交易限額]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何提領[玉山][電子]支付[帳戶][餘額]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何查詢[活動]已結束超過[六個月]的[活動]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何查詢[玉山Wallet][電子]支付繳費[紀錄]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何查詢[玉山][電子]支付—跨境網購[交易][紀錄]與[訂單][狀況]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何綁定[郵局帳戶]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何設定[玉山][電子]支付[帳戶]的常用提領[銀行][帳戶]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何註冊[玉山][電子]支付[帳戶]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何變更[玉山][電子]支付[帳戶][手機號碼]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何進行[外匯]申報":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何進行[玉山][電子]支付[帳戶]儲值":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何進行[玉山][電子]支付[行動][電話]驗證[人工]審核":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何驗證[玉山][電子]支付[帳戶][姓名]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "忘記[玉山][電子]支付[網站帳戶]登入的[會員][序號]怎麼辦":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "掃描[店家][QR] [Code]的付款[方式]為何":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "提領[玉山][電子]支付[帳戶][餘額]至[銀行][帳戶]需要多[久]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "支付日本[PayPay][掃碼]付服務[我]需要有[外幣][帳戶]嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "支付日本[PayPay][掃碼]付服務是[新][臺幣]扣款還是[日圓]扣款":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "於[玉山銀行]補件[平台]上傳完成[後]為何仍顯示[近][六個月][內]「查[無案件][資訊]」":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "未收到[玉山][電子]支付[Email]驗證信[該]怎麼辦":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "沒有收到[驗證碼][簡訊][該]怎麼辦":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "為什麼[我][會]收到[簡訊]通知「[玉山][電子]支付[身分]驗證尚未完成」":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "為什麼[我][會]收到[簡訊]通知辦理[玉山][電子]支付[帳戶][定期]審查":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "為什麼[我]沒收到[玉山][電子]支付[帳戶]推播[訊息]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "為什麼[玉山][電子]支付[身分][證]驗證[會][失敗]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "為什麼[玉山][電子]支付[身分]認證[結果]顯示「啟用審核[中]，請[稍後]再試」":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "為什麼[玉山][電子]支付[身分]認證[結果]顯示註冊[資料]審核[中]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "為什麼[眾樂樂]的[活動][會][突然][不見]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "為什麼使用[玉山Wallet][電子]支付查詢[電費][帳單]/[水費][帳單]繳費[會][失敗]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "為什麼使用[玉山Wallet][電子]支付查詢[電費][帳單]繳費[會][失敗]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "為什麼使用[玉山][電子]支付—跨境網購服務[身分]驗證的[行動][電話]驗證[會][失敗]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "為什麼使用[玉山][電子]支付—跨境網購服務需要進行[身分]認證":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "為何[會]收到[玉山][電子]支付[帳戶]通知儲值[餘額]已達[上][限]的[簡訊]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "為何在日本[PayPay][商店]使用[玉山Wallet][電子]支付綁定[該][信用卡]付款[會]付款[失敗]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "為何無法找到[樂享優惠專區]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "由[店家]掃描[手機條碼]的付款[方式]為何":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "誰[可以]使用[玉山Wallet][電子]支付":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "誰[可以]使用[玉山][電子]支付跨境網購服務":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "跨境網購[是]否有[額度]限制":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "跨境網購[限額]多少":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "跨境網購提供了什麼服務":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "跨境網購服務[身分]驗證[結果]顯示「[電支帳戶姓名]未通過驗證」怎麼辦":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "跨境網購服務[身分]驗證時出現[系統]維護[作業][畫面][我][該]如何處理":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "跨境網購服務如何發動退款":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "跨境網購服務為什麼需要[外匯]申報":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "跨境網購的[超商]繳費[是]否[會]收取[手續費]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "跨境網購的轉帳付款[是]否[會]收取[手續費]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "跨境網購的轉帳付款及[超商]繳費[是]否[會]收取[手續費]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "退款[匯率]如何計算":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "退款[會]退到哪裡":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "逾期[帳單][可以]用[玉山Wallet][電子]支付繳費嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "開通[電子]支付[帳戶]，[行動][電話]為何[會]被變更":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    return resultDICT