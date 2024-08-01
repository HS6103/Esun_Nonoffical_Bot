#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for web_bank

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
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply\\reply_web_bank.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[web_bank] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern=""):
    debugInfo(inputSTR, utterance)
    if utterance == "個網銀行動銀行暨[數位]身分核驗[安全]宣告注意事項":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[可以][自行]取消子帳戶嗎":
        if CHATBOT_MODE:
            if args[1] == '自行':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "子帳戶[可]使用[金融卡]服務嗎":
        if CHATBOT_MODE:
            if '金融卡' in args[1]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[代]扣繳服務如遇[帳戶][餘額][不足][是]否[會]動用定存質借":
        if CHATBOT_MODE:
            if '代' in args[0] and args[1] in ['帳戶', '帳號', '戶頭'] and args[3] == '不足':
                resultDICT["response"] = getResponse(utterance, args)   
        else:
            pass

    if utterance == "[晶片金融卡]被鎖住[該]怎麼辦":
        if CHATBOT_MODE:
            if '金融卡' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[玉山][個人][網路銀行][使用者名稱]與[密碼]的設定[規則]為何":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[2] in ['網路銀行', '網銀'] and (args[3] and args[4]) in ['使用者名稱', '密碼', '用戶名'] and '規'in args[5]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[玉山]的[網路銀行]何時[可以]開始使用":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[1] in  ['網路銀行', '網銀']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[證券櫃檯]有哪些服務":
        if CHATBOT_MODE:
            if '證券' in args[0] and '櫃' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[讀卡機]未符合[玉山銀行][晶片金融卡]元件([WebATM]元件)要求":
        if CHATBOT_MODE:
            if '玉山' in args[1] and (args[2] and args[3].lower().strip(' ') in ['晶片金融卡', 'webatm']):
                if args[0].lower().strip(' ') in  ['讀卡機', 'smart card service', '作業系統', '瀏覽器', 'os']:
                    resultDICT["response"] = getResponse("[{}]未符合[玉山銀行][晶片金融卡]元件([WebATM]元件)要求".format(args[0].lower().strip(' ')), args)
        else:
            pass

    if utterance == "[讀卡機]未符合[玉山銀行][晶片金融卡]元件要求":
        if CHATBOT_MODE:
            if args[1].lower().strip(' ') in ['晶片金融卡', 'webatm']:
                if args[0].lower().strip(' ') in  ['讀卡機', 'smart card service', '作業系統', '瀏覽器', 'os']:
                    resultDICT["response"] = getResponse("[{}]未符合[玉山銀行][晶片金融卡]元件要求".format(args[0].lower().strip(' ')), args)
        else:
            pass

    if utterance == "[電腦版][網路銀行]的[精簡模式]怎麼找更多服務":
        if CHATBOT_MODE:
            if '電腦' in args[0] or 'pc' in args[0].lower():
                if args[1] in ['網路銀行', '網銀'] and args[2] == '精簡模式':
                    resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[電腦版][網路銀行]要如何切換[模式]":
        if CHATBOT_MODE:
            if '電腦' in args[0] or 'pc' in args[0].lower():
                if args[1] in ['網路銀行', '網銀']:
                    if args[2] == '模式':
                        resultDICT["response"] = getResponse("[電腦版][網路銀行]要如何切換[{}]".format(args[2]), args)
                    elif args[2] in  ['完整模式', '精簡模式']:
                            resultDICT["response"] = getResponse("[電腦版][網路銀行]要如何切換回[{}]".format(args[2]), args)
        else:
            pass

    if utterance == "[電腦版][網路銀行]要如何切換回[完整模式]":
        if CHATBOT_MODE:
            if '電腦' in args[0] or 'pc' in args[0].lower():
                if args[1] in ['網路銀行', '網銀']:
                    if args[2] in  ['完整模式', '精簡模式']:
                        resultDICT["response"] = getResponse("[電腦版][網路銀行]要如何切換回[{}]".format(args[2]), args)
        else:
            pass

    if utterance == "在[網路銀行]進行外幣涉及結匯交易申報書的[電子簽章][可以]用那些[方式]進行[身分]驗證呢":
        if CHATBOT_MODE:
            if args[0] in ['網路銀行', '網銀'] and '簽章' in args[1] and args[4] in ['身分', '身份']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass
        
    if utterance == "在[網路銀行]進行外幣涉及結匯交易申報書的[電子簽章][可以]用哪些[方式]進行[身分]驗證呢":
        if CHATBOT_MODE:
            if args[0] in ['網路銀行', '網銀'] and '簽章' in args[1] and args[4] in ['身分', '身份']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass
        
    if utterance == "如何[才能]使用[玉山銀行]的[網路銀行]":
        if CHATBOT_MODE:
            if '玉山' in args[1]:
                if args[2] in  ['網路銀行', '網銀']:
                    resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何使用代繳[明細]查詢":
        if CHATBOT_MODE:
            if args[0] == '項目':
                resultDICT["response"] = getResponse("如何使用代繳[項目]查詢", args)
            elif args[0] == '明細':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何使用代繳[項目]查詢/變更/終止":
        if CHATBOT_MODE:
            if args[0] == '項目':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何使用代繳[項目]終止":
        if CHATBOT_MODE:
            if args[0] == '項目':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何使用代繳[項目]變更":
        if CHATBOT_MODE:
            if args[0] == '項目':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何使用[外匯][存款]結售":
        if CHATBOT_MODE:
            if args[0] == '外匯' and args[1] == '存款':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何使用[帳戶]代扣繳":
        if CHATBOT_MODE:
            if args[0] in ['帳戶', '帳號', '戶頭']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何使用[綜存]轉[定存]":
        if CHATBOT_MODE:
            if args[0] in ['綜存', '綜合存款'] and args[1] in ['定存', '定期存款']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何使用[網路銀行][外幣]匯出":
        if CHATBOT_MODE:
            if args[0] in ['網路銀行', '網銀']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何使用[網路銀行]之預約匯出":
        if CHATBOT_MODE:
            if args[0] in ['網路銀行', '網銀']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何使用[網路銀行]繳交[信用卡]":
        if CHATBOT_MODE:
            if args[0] in ['網路銀行', '網銀'] and args[1] in ['信用卡', '卡費']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何使用預約[交易]取消":
        if CHATBOT_MODE:
            if args[0] == '交易':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何使用預約[交易]查詢":
        if CHATBOT_MODE:
            if args[0] == '交易':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何使用預約[綜存]轉[定存]":
        if CHATBOT_MODE:
            if args[0] in ['綜存', '綜合存款'] and args[1] in ['定存', '定期存款']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何加開[子帳戶]":
        if CHATBOT_MODE:
            if args[0] == '子帳戶':
                resultDICT["response"] = getResponse(utterance, args)
            elif args[0] == '簡訊密碼':
                resultDICT["response"] = getResponse("如何開通[簡訊密碼]", args)
        else:
            pass

    if utterance == "如何取消[網路銀行]約定轉入[帳號]":
        if CHATBOT_MODE:
            if args[0] in ['網路銀行', '網銀'] and args[1] in ['帳戶', '帳號', '戶頭']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何提升[限額]":
        if CHATBOT_MODE:
            if args[0] == '限額':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass
        
    if utterance == "如何申請[基金][單筆]申購":
        if CHATBOT_MODE:
            if args[0] == '基金' and args[1] == '單筆':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何設定[分行]/[ATM][驗證碼]":
        if CHATBOT_MODE:
            if args[0].lower() and args[1].lower() in ['分行'] + userDefinedDICT['atm'] and args[2] == '驗證碼':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何設定約定轉入[帳號]":
        if CHATBOT_MODE:
            if args[0] in ['帳戶', '帳號', '戶頭']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何註銷約定轉入[帳號]":
        if CHATBOT_MODE:
            if args[0] in ['帳戶', '帳號', '戶頭']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何賣[外幣]":
        if CHATBOT_MODE:
            if args[0] == '外幣':
                resultDICT["response"] = getResponse("如何使用[外匯][存款]結售", args)
        else:
            pass

    if utterance == "如何進行[基金]贖回":
        if CHATBOT_MODE:
            if args[0] == '基金':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何進行[基金]轉換":
        if CHATBOT_MODE:
            if args[0] == '基金':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何進行[外幣]轉帳":
        if CHATBOT_MODE:
            if args[0] == '外幣':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何進行[臺幣]預約轉帳":
        if CHATBOT_MODE:
            if args[0] in ['台幣', '臺幣']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何預約繳[信用卡]":
        if CHATBOT_MODE:
            if args[0] in ['信用卡', '卡費']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "忘記[使用者名稱]或[密碼]":
        if CHATBOT_MODE:
            if args[0] in ['使用者名稱', '密碼', '用戶名']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "忘記[晶片金融卡][密碼][該]怎麼辦":
        if CHATBOT_MODE:
            if '金融卡' in args[0] and args[1] == '密碼':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "怎麼在[電腦版][網路銀行]更改[我]的最愛":
        if CHATBOT_MODE:
            if '電腦' in args[0] or 'pc' in args[0].lower():
                if args[1] in ['網路銀行', '網銀']:
                    resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "怎麼在[電腦版][網路銀行]更改[我]的最愛[裡面]的[功能]":
        if CHATBOT_MODE:
            if '電腦' in args[0] or 'pc' in args[0].lower():
                if args[1] in ['網路銀行', '網銀']:
                    resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "怎麼沒在[電腦版]看到[能夠]切換[模式]的[按鈕]":
        if CHATBOT_MODE:
            if '電腦' in args[0] or 'pc' in args[0].lower():
                if args[2] == '模式':
                    resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "提升非約定轉帳[限額][後]，有哪些[通路]適用":
        if CHATBOT_MODE:
            if args[0] == '限額':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "為什麼[我][會]收到玉山網路銀行暨行動銀行帳戶[安全]提醒通知":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "為什麼無法[成功]申請[帳戶]代扣繳":
        if CHATBOT_MODE:
            if args[0] in ['成功', '順利'] and args[1] in ['帳戶', '帳號', '戶頭']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "為什麼進行子帳戶[線上]銷戶時出現資料輸入[錯誤]":
        if CHATBOT_MODE:
            if args[0] == '線上' and args[1] == '錯誤':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "為何[我]的[臺幣]轉帳之預約[交易][失敗]":
        if CHATBOT_MODE:
            if args[1] in ['台幣', '臺幣'] and args[2] == '交易' and args[3] == '失敗':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "無法使用[WebATM]元件":
        if CHATBOT_MODE:
            if args[0].lower().strip(' ') in userDefinedDICT['webatm']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "請問[我]要如何使用[帳戶]代扣繳":
        if CHATBOT_MODE:
            if args[1] in ['帳戶', '帳號', '戶頭']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass
        
    if utterance == "[我]與[玉山銀行]往來的[許多]業務[均]有約定密碼":
        if CHATBOT_MODE:
            if '玉山' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass
    return resultDICT