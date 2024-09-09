#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for credit_card

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
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), os.path.join("reply", "reply_credit_card.json")), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[credit_card] {} ===> {}".format(inputSTR, utterance))

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
    
    if utterance == "[TWQR跨機構購物交易][疑似]遭冒用[可以]怎麼處理":
        if CHATBOT_MODE:
            if 'twqr' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[TWQR跨機構購物交易][疑似]遭冒用或消費[爭議][可以]怎麼處理":
        if CHATBOT_MODE:
            if 'twqr' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[TWQR跨機構購物交易]是在哪[一家][商店]消費":
        if CHATBOT_MODE:
            if 'twqr' in args[0] and '店' in args[2]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass
        
    if utterance == "[TWQR跨機構購物交易]是[甚麼]的[消費]":
        if CHATBOT_MODE:
            if 'twqr' in args[0] and '消費' in args[2]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass
        
    if utterance == "[信用卡][利息]如何計算":
        if CHATBOT_MODE:
            if args[0] == '信用卡' and args[1] == '利息':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[信用卡][利息]／違約金如何計算":
        if CHATBOT_MODE:
            if args[0] == '信用卡' and args[1] == '利息':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[信用卡][道路]救援服務[項目]包含哪些":
        if CHATBOT_MODE:
            if args[0] == '信用卡' and args[1] == '道路':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[信用卡][額度][是]否[可以]調整":
        if CHATBOT_MODE:
            if args[0] == '信用卡' and args[1] == '額度':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[信用卡]不限[金額]消費通知如何設定":
        if CHATBOT_MODE:
            if args[0] == '信用卡' and args[1] in ['金額']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[信用卡]受損[感應][不良]如何申請補換發":
        if CHATBOT_MODE:
            if args[0] == '信用卡' and args[1] == '感應':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[信用卡]繳款[方式]包含哪些":
        if CHATBOT_MODE:
            if args[0] == '信用卡' and args[1] in ['方式', '管道', '途徑']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[信用卡]違約金如何計算":
        if CHATBOT_MODE:
            if args[0] == '信用卡':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[信用卡]遺失怎麼辦":
        if CHATBOT_MODE:
            if args[0] == '信用卡':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[個人信貸]撥款[時間]要多[久]":
        if CHATBOT_MODE:
            if args[0] == '個人信貸' and '時' in args[1]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[個人信貸]有哪些撥款[方式]":
        if CHATBOT_MODE:
            if args[0] == '個人信貸' and args[1] in ['方式', '管道', '途徑']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "帳單有[年費問題]如何爭取減免":
        if CHATBOT_MODE:
            if args[0] == '年費問題':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[結帳日][是]否[可以]更改":
        if CHATBOT_MODE:
            if args[0] == '結帳日':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[信貸]申訴陳情":
        if CHATBOT_MODE:
            if args[0] in ['信貸', '信用貸款', '信用卡']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[信貸]繳款有哪些[方式]":
        if CHATBOT_MODE:
            if args[0] in ['信貸', '信用貸款'] and args[1] in ['方式', '管道', '途徑']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "哪裡[可以]查詢[信用卡][優惠]":
        if CHATBOT_MODE:
            if args[0] == '信用卡' and args[2] in ['優惠']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何使用[信用卡]約定扣繳":
        if CHATBOT_MODE:
            if args[0] == '信用卡':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何使用[紅利][點數]":
        if CHATBOT_MODE:
            if args[0] == '紅利':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何使用預借[現金功能]":
        if CHATBOT_MODE:
            if '現金' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何修改[帳戶][自動]扣繳[卡費]":
        if CHATBOT_MODE:
            if args[0] in ['帳戶', '帳號', '戶頭'] and args[1] == '自動' and args[2] == '卡費':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何停用[信用卡]":
        if CHATBOT_MODE:
            if args[0] == '信用卡':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何更改[信用卡][帳單][地址]": # 電話 email
        if CHATBOT_MODE:
            if args[0] == '信用卡' and args[1] == '帳單':
                if args[0] in ['地址', '電話', 'email', 'e-mail', '信箱']:
                    resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何更改[戶籍][地址]":
        if CHATBOT_MODE:
            if args[0] == '戶籍' and args[1] == '地址':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何更改[銀行][基本][資料]":
        if CHATBOT_MODE:
            if args[0] == '銀行' and args[2] == '資料':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何查詢[信用卡][即時][交易]":
        if CHATBOT_MODE:
            if args[0] == '信用卡' and args[1] == '即時' and args[2] == '交易':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何查詢[信用卡][帳單][金額]":
        if CHATBOT_MODE:
            if args[0] == '信用卡' and args[1] == '帳單' and args[2] == '金額':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何查詢[信用卡]之持卡[狀況]":
        if CHATBOT_MODE:
            if args[0] == '信用卡' and args[1] == '狀況':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何查詢[信用卡]未入[帳單][交易]":
        if CHATBOT_MODE:
            if args[0] == '信用卡' and args[1] == '帳單' and args[2] == '交易':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何查詢[信用卡]未請款消費":
        if CHATBOT_MODE:
            if args[0] == '信用卡':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何查詢[信用卡]未請款消費或[即時][交易]":
        if CHATBOT_MODE:
            if args[0] == '信用卡' and args[2] == '交易':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何查詢[信用卡]繳款[紀錄]":
        if CHATBOT_MODE:
            if args[0] == '信用卡' and args[1] == '紀錄':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何查詢[信用卡]辦卡[進度]":
        if CHATBOT_MODE:
            if args[0] == '信用卡' and '進' in args[1]:
                resultDICT["response"] = getResponse(utterance, args)
            elif args[0] == '個人信貸' and '進' in args[1]:
                resultDICT["response"] = getResponse("如何查詢[個人信貸]申辦[進度]", args)
            
        else:
            pass

    if utterance == "如何查詢[歷史]的消費[明細]":
        if CHATBOT_MODE:
            if args[0] == '歷史' and args[1] == '明細':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何查詢[目前][可]用的[額度]":
        if CHATBOT_MODE:
            if args[2] == '額度':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何查詢[結帳日]":
        if CHATBOT_MODE:
            if args[0] == '結帳日':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何查詢推薦[好友]辦卡([MGM])[是]否符合[資格]":
        if CHATBOT_MODE:
            if '友' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何查詢繳款[截止日]":
        if CHATBOT_MODE:
            if args[0] == '截止日':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何查詢預借[現金]的[額度]":
        if CHATBOT_MODE:
            if args[0] in ['現金'] and args[1] == '額度':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何申請[信用卡]": # #個人信貸
        if CHATBOT_MODE:
            if args[0] == '信用卡':
                resultDICT["response"] = getResponse(utterance, args)
            elif args[0] == '個人信貸':
                resultDICT["response"] = getResponse("如何申請[個人信貸]", args)
        else:
            pass

    if utterance == "如何申請信用卡[帳單]使用[他][行][帳戶][自動]扣繳":
        if CHATBOT_MODE:
            if args[0] in ['帳單', '卡費']:
                if args[1] == '他' and args[2] == '行' and args[3] in ['帳戶', '帳號', '戶頭'] and args[4] == '自動':
                    resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何申請提[前]還款結清貸款":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args) 
        else:
            pass

    if utterance == "如何登錄[道路]救援服務":
        if CHATBOT_MODE:
            if args[0] == '道路':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何補寄[簡訊]":
        if CHATBOT_MODE:
            if args[0] == '簡訊':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何補寄[簡訊]/[電子][帳單]":
        if CHATBOT_MODE:
            if args[0] and args[1] in ['簡訊', '電子'] and args[2] == '帳單':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何補寄[電子][帳單]":
        if CHATBOT_MODE:
            if args[0] in ['簡訊', '電子'] and args[1] == '帳單':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何計算預借[現金][手續費]":
        if CHATBOT_MODE:
            if args[0] in ['現金'] and args[1] == '手續費':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何設定每筆刷卡消費[都]收到通知":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何設定預借[現金][密碼]":
        if CHATBOT_MODE:
            if args[0] in ['現金'] and args[1] == '密碼':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何變更[我]的[中文][姓名]":
        if CHATBOT_MODE:
            if args[1] in ['中文'] and args[2] in ['姓名', '名字']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何開卡":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[帳單]的消費[款項]有[疑問][該][怎麼]做":
        if CHATBOT_MODE:
            if args[0] in ['帳單','信用卡'] and '問' or '疑' in args[2]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "已經有向[銀行]貸款還[可以]再申請嗎":
        if CHATBOT_MODE:
            if '銀行' or '玉山' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "拾獲[玉山][信用卡][該][怎麼]做":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[1] == '信用卡':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "拾獲本行[信用卡][該][怎麼]做":
        if CHATBOT_MODE:
            if args[0] == '信用卡':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "持[信用卡]在[國][外]消費[會]收取什麼[費用]":
        if CHATBOT_MODE:
            if args[0] == '信用卡' and args[1] in ['國', '境'] and args[2] == '外':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "提[前]還款[是]否[須]負擔[提前清償違約金]":
        if CHATBOT_MODE:
            if '違約金' in args[3]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "收到逾期[簡訊]通知[是]否[會]有[利息]產生":
        if CHATBOT_MODE:
            if args[0] == '簡訊' and args[3] == '利息':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "有其他家銀行貸款[是]否[可]申請[玉山][信貸]債務整合":
        if CHATBOT_MODE:
            if '玉山' in args[2] and args[3] in ['信貸', '信用貸款']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "為什麼已經刷退卻還沒收到退款":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "申請[個人信貸]的[流程]為何":
        if CHATBOT_MODE:
            if args[0] in ['信貸', '信用貸款', '個人信貸'] and args[1] == '流程':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "申請[個人信貸]需要有[玉山][帳戶]嗎":
        if CHATBOT_MODE:
            if args[0] in ['信貸', '信用貸款', '個人信貸'] and '玉山' in args[1] and args[2] in ['帳戶', '戶頭', '帳號']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "申請[個人信貸]需要準備哪些[文件]":
        if CHATBOT_MODE:
            if args[0] in ['信貸', '信用貸款', '個人信貸'] and args[1] in ['文件', '資料']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "申辦[額度]調整[缺][資料]如何補件":
        if CHATBOT_MODE:
            if args[0] == '額度' and args[2] in ['文件', '資料']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "繳款[截止日][是]否[可以]更改":
        if CHATBOT_MODE:
            if args[0] == '截止日':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "辦卡有[缺][資料]如何補件":
        if CHATBOT_MODE:
            if args[1] in ['文件', '資料']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    return resultDICT