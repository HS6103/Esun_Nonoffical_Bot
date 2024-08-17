#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for app

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
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply\\reply_app.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[app] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern=""):
    debugInfo(inputSTR, utterance)

    if utterance == "[Android]如何[將][玉山銀行]快捷[功能]加入小工具":
        if CHATBOT_MODE:
            if args[0].lower().strip(' ') in ['android', '安卓']:
                if '玉山' in args[2]:
                    resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[QR] [Code]轉帳收款[碼]拆帳收款的計算[方式]為何":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[TWQR][功能]若消費完成[後]需退款[該]如何進行":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[Touch ID]被[系統][鎖][定時][該]如何解除":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[iOS][使用者]如何設定[Touch ID]":
        if CHATBOT_MODE:
            if args[0].lower().strip(' ') in ['android', '安卓']:
                if args[2] in ['指紋', '人臉']:
                    resultDICT["response"] = getResponse("[Android][使用者]如何設定[指紋][人臉]辨識登入", args)
            elif args[0].lower().strip(' ') in ['ios', '蘋果', 'iphone']:
                if args[2].lower().strip(' ') in ['touch id', '指紋']:
                    resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[iOS]如何綁定[行動][裝置]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[只]想開[啟][指紋]或[人臉]辨識其中[一種]登入[方式][該]如何設定":
        if CHATBOT_MODE:
            if args[2] or args[3] in ['指紋', '人臉']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[可]查詢多[久][以前]的[訊息]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[可以]透過[行動銀行]查詢到的[信託][帳號]之[信託][種類]為何":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[台灣Pay][相關][功能][是]否有[額度]限制":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[台灣Pay][相關][功能][限額]多少":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "夜間[靜音]服務為何":
        if CHATBOT_MODE:
            if args[0] == '靜音':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[密碼]之使用[規則]為何":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[手機號碼]轉帳的[額度]是怎麼計算":
        if CHATBOT_MODE:
            if '手機' in args[0] and args[1] == '額度':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[是]否[可以][同時][將][同][一隻][手機號碼]在多[個][銀行]的[連結][不同]收款[帳號]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[玉山][行動銀行][相關]服務[條款]為何":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[玉山][行動銀行][自動]登出的[時間]限制為何":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[玉山][行動銀行]取用[我][行動][裝置]哪些授權[項目]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "什麼是[QR] [Code]轉帳":
        if CHATBOT_MODE:
            if 'qr' in args[1].lower().strip(' '): 
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "什麼是[手機號碼]收款轉帳":
        if CHATBOT_MODE:
            if '手機' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "什麼是[最近]轉帳":
        if CHATBOT_MODE:
            if args[0] == '最近':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "什麼是[玉山][行動銀行]":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[1] == '行動銀行':
                resultDICT["response"] = getResponse(utterance, args)
            elif args[0] == '行動銀行' and args[1] == '驗證碼':
                resultDICT["response"] = getResponse("什麼是[行動銀行][驗證碼]", args)
        else:
            pass

    if utterance == "什麼是[玉山][行動銀行]認證":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[1] == '行動銀行':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "什麼是[玉山銀行][人臉]辨識":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[1] == '人臉':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "什麼是加入[Siri]":
        if CHATBOT_MODE:
            if 'siri' in args[0].lower():
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "使用[TWQR][功能]若付款[金額][錯誤]怎麼辦":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "使用[行動銀行][應]注意之[安全][事項]為何":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "裝置驗證[失敗]請再試[一次]":
        if CHATBOT_MODE:
            if args[0] == '失敗':            
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "加入[Siri][功能][可]應用在[玉山][行動銀行]哪些服務":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "哪些[人][可以]使用[台灣Pay]":
        if CHATBOT_MODE:
            if args[2].lower() in '台灣pay':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "哪些[銀行][APP][可]掃描[玉山][行動銀行]之[QR] [Code]轉帳收款[碼]進行轉帳":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何[將][玉山][行動銀行][App]調整為深色[模式]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何不顯示[圖形密碼]":
        if CHATBOT_MODE:
            if args[0] == '圖形密碼':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何使用[付款碼]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何使用[手機號碼]收款":
        if CHATBOT_MODE:
            if '手機' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何使用[手機號碼]轉帳":
        if CHATBOT_MODE:
            if '手機' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何使用[無卡提款]服務":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何使用[玉山銀行][人臉]辨識":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何使用加入[Siri]":
        if CHATBOT_MODE:
            if 'siri' in args[0].lower():
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何修改[手機號碼]收款所連結之[帳號]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何取消[手機號碼]轉帳":
        if CHATBOT_MODE:
            if '手機' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何取消[行動]裝置綁定":
        if CHATBOT_MODE:
            if args[0] == '行動':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何取消加入[Siri][功能]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何在[付款碼(台灣Pay)/TWQR][功能][中]新增或刪除[電子][發票載具]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何在[行動銀行][上]查詢[每月]跨行提款及跨行轉帳[優惠次數]":
        if CHATBOT_MODE:
            if args[0] in ['行動銀行', 'app'] and '優惠' in args[3]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何在[行動銀行][中]刪除常用[帳號]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何在[行動銀行][中]編輯刪除常用[帳號]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何在[行動銀行][中]編輯常用[帳號]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何在[行動銀行]查詢安養[信託][帳號]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何在非約定轉帳使用[行動銀行][驗證碼]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何查詢[台灣Pay/TWQR][相關][交易][紀錄]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何獲得推播通知[訊息]服務":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何申請[玉山][行動銀行]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何設定[簡易][密碼]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何設定[行動銀行][驗證碼]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何設定非約定轉帳":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何變更[Siri]呼叫[語音]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何變更[圖形密碼]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何變更[我][手機號碼]收款[功能]的[手機號碼]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何變更[簡易][密碼]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何開通[簡訊密碼]服務":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何隱藏[圖形密碼][軌跡]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如果[我]註銷留存於本行之[簡訊密碼]([OTP])[手機號碼]原[手機號碼]還是[會]連結[我]的[帳戶]嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如果[我]變更留存於本行之[簡訊密碼]([OTP])[手機號碼]原[手機號碼]還是[會]連結[我]的[帳戶]嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如果[我]變更留存於本行之[簡訊密碼][手機號碼]原[手機號碼]還是[會]連結[我]的[帳戶]嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如果[我]變更註銷留存於本行之[簡訊密碼]([OTP])[手機號碼]原[手機號碼]還是[會]連結[我]的[帳戶]嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "忘記[使用者名稱]或[密碼]":
        if CHATBOT_MODE:
            if args[0] and args[1] in ['使用者名稱', '密碼']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "忘記[使用者名稱]":
        if CHATBOT_MODE:
            if args[0] in ['使用者名稱', '密碼']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "想分享[我]轉帳的[結果]要如何操作":
        if CHATBOT_MODE:
            if args[0] in ['結果']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "接不到[玉山][語音][OTP][電話]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "提升非約定轉帳[限額][後]有哪些[通路]適用":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "操作[行動銀行]出現[畫面][空][白]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "收不到[簡訊][驗證碼]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "收不到[簡訊][驗證碼]或接不到[玉山][語音][OTP][電話]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "有支援哪些[台灣Pay/TWQR][功能]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "為什麼[我]無法透過[手機號碼][成功]轉帳":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "為何[我][會]在[同]一裝置收到二則[以上][相同]的[通知]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "為何[我]的[信用卡]繳款[後][行動銀行]沒有收到通知":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "為何[我]的[信用卡]繳款[後]沒有[即時]更新待繳[金額]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "為何推播通知[訊息][鈴聲]消失了":
        if CHATBOT_MODE:
            if args[1] == '鈴聲':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "為何於[行動銀行]設定約定[他][行同][戶名帳號][失敗]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "無法下載[行動銀行]":
        if CHATBOT_MODE:
            if args[0] == '行動銀行':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "無法下載或更新[行動銀行]":
        if CHATBOT_MODE:
            if args[0] == '行動銀行':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "無法更新[行動銀行]":
        if CHATBOT_MODE:
            if args[0] == '行動銀行':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "無法登入[圖形密碼]":
        if CHATBOT_MODE:
            if args[0] == '圖形密碼':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "無法綁定[圖形密碼]":
        if CHATBOT_MODE:
            if args[0] == '圖形密碼':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "若重複繳費怎麼辦":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "轉帳[紀錄]沒有顯示在[最近]轉帳列表":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "為何[Android][使用者]無法進行螢幕截圖":
        if CHATBOT_MODE:
            if args[0].lower().strip(' ') in ['android', '安卓']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "通知[訊息][可]設定哪些[項目]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    return resultDICT