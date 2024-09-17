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
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), os.path.join("reply", "reply_crossboarding.json")), encoding="utf-8"))
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
    for i in range(len(args)):
        args[i] = args[i].lower().strip(' ')   # 前處理，把argument變小寫並去頭尾空格
    
    if utterance == "[可]使用哪些[銀行][帳戶]做為[玉山][電子]支付提領[帳戶]":
        if CHATBOT_MODE:
            if args[1] == '銀行' and (args[1] and args[5] in ['帳戶', '帳號', '戶頭']) and '玉山' in args[2]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[可以]使用[信用卡]儲值[玉山][電子]支付[帳戶][餘額]嗎":
        if CHATBOT_MODE:
            if args[1] == '信用卡' and '玉山' in args[2] and args[3] == '電子' and args[4] in ['帳戶', '帳號', '戶頭']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[我][可以]註冊多少[組][玉山][電子]支付[帳戶]":
        if CHATBOT_MODE:
            if '玉山' in args[3] and args[4] == '電子' and args[5] in ['帳戶', '帳號', '戶頭']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "退款時[手續費][會]退嗎":
        if CHATBOT_MODE:
            if args[0] == '手續費':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[樂享優惠專區]是甚麼":
        if CHATBOT_MODE:
            if '樂享' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
            elif '跨境網購' in args[0]:
                resultDICT["response"] = getResponse("[跨境網購專區]是甚麼", args)
            elif args[0] == '訂單狀態':
                resultDICT["response"] = getResponse("跨境網購專區的訂單狀態分別是什麼", args)
        else:
            pass

    if utterance == "[活動]結束時[會]如何告知":
        if CHATBOT_MODE:
            if args[0] == '活動':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[玉山Wallet][電子]支付[交易][資訊][會]保留多[久]":
        if CHATBOT_MODE:
            if 'wallet' in args[0] and args[2] == '交易' and args[3] == '資訊':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[玉山Wallet][電子]支付[交易][資訊]要怎麼查詢":
        if CHATBOT_MODE:
            if 'wallet' in args[0] and args[2] == '交易' and args[3] == '資訊':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[玉山Wallet][電子]支付[可]綁定哪些支付[工具]呢":
        if CHATBOT_MODE:
            if 'wallet' in args[0] and args[3] in ['工具', '軟體', '程式', '管道']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[玉山Wallet]電子支付[可以]綁定非[玉山銀行][信用卡]":
        if CHATBOT_MODE:
            if 'wallet' in args[0] and '玉山' in args[3] and args[4] in ['信用卡','銀行','帳戶', '帳號', '戶頭']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[玉山Wallet][電子]支付[條碼]付的付款[方式]為何":
        if CHATBOT_MODE:
            if 'wallet' in args[0] and args[2] == '條碼' and args[3] in ['方式','方法','程序','步驟']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[玉山Wallet][電子]支付「[條碼]付」(由[店家]掃描[手機條碼]) 的付款[方式]為何":
        if CHATBOT_MODE:
            if 'wallet' in args[0] and args[2] == '條碼' and args[5] in ['方式','方法','程序','步驟']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[玉山Wallet][電子]支付支援哪些繳費[項目]":
        if CHATBOT_MODE:
            if 'wallet' in args[0] and args[2] == '項目':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[玉山Wallet][電子]支付於日本[PayPay]掃碼付服務的[匯率]怎麼換算":
        if CHATBOT_MODE:
            if 'wallet' in args[0] and args[2] == 'paypay' and args[3] == '匯率':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[玉山Wallet][電子]支付於日本[PayPay]掃碼付服務需要負擔[國外][交易][服務費]嗎":
        if CHATBOT_MODE:
            if 'wallet' in args[0] and args[2] == 'paypay' and args[5] == '服務費':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[玉山Wallet][電子]支付綁定[信用卡]儲值付款[可以]使用[信用卡][紅利點數]折抵嗎":
        if CHATBOT_MODE:
            if 'wallet' in args[0] and args[2] and args[4] == '信用卡' and '紅利' in args[5]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[玉山Wallet][電子]支付綁定[信用卡]消費[可以]獲得[信用卡]回饋嗎":
        if CHATBOT_MODE:
            if 'wallet' in args[0] and args[2] and args[4] == '信用卡':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[玉山Wallet][電子]支付重複繳交[水]/[電費][可以]退款嗎":
        if CHATBOT_MODE:
            if 'wallet' in args[0] and args[1] == '電子' and args[2] in ['水費', '電費', '水電費', '水', '電']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[玉山Wallet][電子]支付重複繳交[水費][可以]退款嗎":
        if CHATBOT_MODE:
            if 'wallet' in args[0] and args[1] == '電子' and args[2] in ['水費', '電費', '水電費']:
                resultDICT["response"] = getResponse(utterance, args).format(args[2])
        else:
            pass

    if utterance == "[玉山][電子]支付[Email]驗證信[是]否有[時間]限制":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[1] == '電子' and args[2] in ['email', 'e-mail'] and args[4] == '時間':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[玉山][電子]支付[帳戶][可以]綁定幾[組]提領[帳號]":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[1] == '電子' and args[2] and args[5] in ['帳戶', '帳號', '戶頭']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[玉山][電子]支付[帳戶]提領[是]否[會]被收取[手續費]":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[1] == '電子' and args[2] in ['帳戶', '帳號', '戶頭'] and args[5] == '手續費':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[玉山][電子]支付[帳戶]是什麼":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[1] == '電子' and args[2] in ['帳戶', '帳號', '戶頭']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[玉山][電子]支付[帳戶]的[交易限額]是多少":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[1] == '電子' and args[2] in ['帳戶', '帳號', '戶頭'] and '限額' in args[3]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[玉山][電子]支付[帳戶款項]轉出完成[後][銀行][帳號備註欄位]為何":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[1] == '電子' and args[2] in ['帳戶', '帳號', '戶頭'] and '備註' in args[5]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[玉山][電子]支付[簡訊]驗證[是]否有[次數][上][限]":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[1] == '電子' and args[2] == '簡訊' and args[3] == '次數':
                resultDICT["response"] = getResponse(utterance, args)                
        else:
            pass

    if utterance == "[該]如何使用[玉山Wallet][電子]支付於日本[PayPay]掃碼付服務呢":
        if CHATBOT_MODE:
            if 'wallet' in args[1] and args[3] == 'paypay' and args[4] == '掃碼':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[身分證]認證[是]否有[次數]限制":
        if CHATBOT_MODE:
            if args[0] == '身分證' and args[2] == '次數':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[身分證]認證若[多次]認證[失敗][該]怎麼辦":
        if CHATBOT_MODE:
            if args[0] == '身分證' and args[2] == '失敗':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[電子]支付儲值[是]否[會]被收取[手續費]":
        if CHATBOT_MODE:
            if args[0] == '電子' and args[3] == '手續費':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "使用[玉山Wallet][電子]支付[交易][失敗]怎麼辦":
        if CHATBOT_MODE:
            if 'wallet' in args[0] and args[3] == '失敗':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "使用[玉山Wallet][電子]支付不[小心]重複繳費了怎麼辦":
        if CHATBOT_MODE:
            if 'wallet' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[玉山Wallet]電子支付若發生退款":
        if CHATBOT_MODE:
            if 'wallet' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[玉山Wallet]電子支付若發生退款[情形][款項][會]退回至哪裡":
        if CHATBOT_MODE:
            if 'wallet' in args[0] and '款' in args[2]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "信用卡儲值付款交易已達限額請選擇其他付款方式":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "儲值完成[後][銀行][帳號備註欄位]為何":
        if CHATBOT_MODE:
            if '備註' in args[2]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "哪些[PayPay][通路][可以]使用":
        if CHATBOT_MODE:
            if args[0] == 'paypay' and args[1] == '通路':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "哪裡[可以]使用[玉山Wallet]":
        if CHATBOT_MODE:
            if 'wallet' in args[1]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "啟用審核[中]請[稍後]再試":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "多[久][才能]收到[玉山][電子]支付—跨境網購服務的[退款]":
        if CHATBOT_MODE:
            if '玉山' in args[2] and args[3] == '電子' and args[4] == '退款':
                resultDICT["response"] = getResponse(utterance, args)                
        else:
            pass

    if utterance == "如何了解[樂享優惠]":
        if CHATBOT_MODE:
            if '樂享' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何使用獨樂樂的[購物金]":
        if CHATBOT_MODE:
            if args[0] in ['購物金', '抵用金']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何使用[玉山Wallet][電子]支付綁定[水]/[電號]並設定繳款提醒通知":
        if CHATBOT_MODE:
            if 'wallet' in args[0] and args[1] == '電子' and args[2] and args[3] in ['水號', '電號', '水', '電']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何使用[玉山Wallet][電子]支付綁定[水號]並設定繳款提醒通知":
        if CHATBOT_MODE:
            if 'wallet' in args[0] and args[1] == '電子' and args[2] in ['水號', '電號']:
                resultDICT["response"] = getResponse("如何使用[玉山Wallet][電子]支付綁定[{}]並設定繳款提醒通知".format(args[2]), args)
        else:
            pass

    if utterance == "如何使用[玉山Wallet][電子]支付進行繳費":
        if CHATBOT_MODE:
            if 'wallet' in args[0] and args[1] == '電子':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何使用[玉山]電子支付—跨境網購[超商]繳費":
        if CHATBOT_MODE:
            if '玉山' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何使用[玉山][電子]支付—跨境網購轉帳付款":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[1] == '電子':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何提供[玉山][電子]支付補件[資料]":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[1] == '電子':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何提升[玉山][電子]支付的[交易限額]":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[1] == '電子' and '限' or '額' in args[2]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何提領[玉山][電子]支付[帳戶][餘額]":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[1] == '電子' and args[3] == '餘額':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何查詢[活動]已結束超過[六個月]的[活動]":
        if CHATBOT_MODE:
            if args[2] == '活動' and args[1] in ['六個月', '半年']:
                resultDICT["response"] = getResponse(utterance, args).format(args[1])   
        else:
            pass

    if utterance == "如何查詢[玉山Wallet][電子]支付繳費[紀錄]":
        if CHATBOT_MODE:
            if 'wallet' in args[0] and args[2] == '紀錄':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何查詢[玉山][電子]支付—跨境網購[交易]":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[2] in ['訂單', '交易']:
                resultDICT["response"] = getResponse("如何查詢[玉山][電子]支付—跨境網購[{}]".format(args[2]), args)
        else:
            pass

    if utterance == "如何綁定[郵局帳戶]":
        if CHATBOT_MODE:
            if '郵局' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何設定[玉山][電子]支付[帳戶]的常用提領[銀行][帳戶]":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[1] == '電子' and args[2] and args[4] in ['帳戶', '帳號', '戶頭']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何註冊[玉山][電子]支付[帳戶]":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[1] == '電子' and args[2] in ['帳戶', '帳號', '戶頭']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何變更[玉山][電子]支付[帳戶][手機號碼]":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[1] == '電子' and args[2] in ['帳戶', '帳號', '戶頭'] and '手機' or '電話' in args[3]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何進行[外匯]申報":
        if CHATBOT_MODE:
            if args[0] == '外匯':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何進行[玉山][電子]支付[帳戶]儲值":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[1] == '電子' and args[2] in ['帳戶', '帳號', '戶頭']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何進行[玉山][電子]支付[行動][電話]驗證[人工]審核":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[4] == '人工':
                if (args[2] == '行動' and args[3] == '電話') or args[3] in ['手機', '電話']:
                    resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何驗證[玉山][電子]支付[帳戶][姓名]":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[1] == '電子' and args[2] in ['帳戶', '帳號', '戶頭'] and args[3] in ['姓名', '名字', '姓氏']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "忘記[玉山][電子]支付[網站帳戶]登入的[會員][序號]怎麼辦":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[1] == '電子' and args[4] == '序號':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "掃描[店家][QR Code]的付款[方式]為何":
        if CHATBOT_MODE:
            if '店' in args[0] and 'qr' in args[1]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "提領[玉山][電子]支付[帳戶][餘額]至[銀行][帳戶]需要多[久]":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[2] and args[5] in ['帳戶', '帳號', '戶頭'] and args[6] == '久':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "支付日本[PayPay]掃碼付服務[我]需要有[外幣][帳戶]嗎":
        if CHATBOT_MODE:
            if args[0] == 'paypay' and args[2] == '外幣' and args[3] in ['帳戶', '帳號', '戶頭']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "支付日本[PayPay]掃碼付服務是[新][臺幣]扣款還是[日圓]扣款":
        if CHATBOT_MODE:
            if args[0] == 'paypay' and args[2] and args[3] in ['臺幣','台幣','日圓','日幣']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[近][六個月][內]查無案件資訊":
        if CHATBOT_MODE:
            if args[1] in ['六個月', '半年']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "未收到[玉山][電子]支付[Email]驗證信[該]怎麼辦":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[1] == '電子' and 'mail' in args[2]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "沒有收到[驗證碼][簡訊][該]怎麼辦":
        if CHATBOT_MODE:
            if args[0] == '驗證碼' and args[1] == '簡訊':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[玉山]電子支付[身分]驗證尚未完成":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[1] in ['身分', '身份']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "通知辦理[玉山]電子支付[帳戶][定期]審查":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[2] in ['帳戶', '帳號'] and args[3] == '定期': 
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "為什麼[我]沒收到[玉山][電子]支付[帳戶]推播":
        if CHATBOT_MODE:
            if '玉山' in args[1] and args[2] == '電子':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "為什麼[玉山][電子]支付身分證驗證[會][失敗]":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[1] == '電子' and args[3] == '失敗':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "為什麼[玉山][電子]支付[身分]認證[結果]顯示註冊資料審核[中]":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[1] == '電子' and args[2] in ['身分', '身份'] :
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "為什麼[眾樂樂]的[活動][會][突然][不見]":
        if CHATBOT_MODE:
            if '眾樂樂' in args[0] and args[4] == '不見':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "為什麼使用[玉山Wallet][電子]支付查詢[電費][帳單]/[水費][帳單]繳費[會][失敗]":
        if CHATBOT_MODE:
            if 'wallet' in args[0] and (args[2] and args[4] in ['電費', '水費']) and args[8] == '失敗':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "為什麼使用[玉山Wallet][電子]支付查詢[電費][帳單]繳費[會][失敗]":
        if CHATBOT_MODE:
            if 'wallet' in args[0] and args[2] in ['電費', '水費'] and args[6] == '失敗':
                resultDICT["response"] = getResponse("為什麼使用[玉山Wallet][電子]支付查詢[{}][帳單]繳費[會][失敗]".format(args[2]), args)
        else:
            pass

    if utterance == "為什麼使用[玉山][電子]支付—跨境網購服務[身分]驗證的[行動][電話]驗證[會][失敗]":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[2] in ['身分', '身份'] and args[6] == '失敗':
                if (args[3] == '行動' and args[4] == '電話') or args[4] in ['手機', '電話']:
                    resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "為什麼使用[玉山][電子]支付—跨境網購服務需要進行[身分]認證":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[2] in ['身分', '身份']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[玉山]電子支付[帳戶]通知儲值[餘額]已達[上]限":
        if CHATBOT_MODE:
            if '玉山' in args[0]and args[3] == '上':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "為何在日本[PayPay][商店]使用[玉山Wallet][電子]支付綁定[該][信用卡]付款[會]付款[失敗]":
        if CHATBOT_MODE:
            if args[0] in ['paypay','pay pay'] and 'wallet' in args[2] and '卡' in args[5] and args[7] == '失敗':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "為何無法找到[樂享優惠專區]":
        if CHATBOT_MODE:
            if '樂享' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "由[店家]掃描[手機條碼]的付款[方式]為何":
        if CHATBOT_MODE:
            if '手機' or '條碼' in args[1]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "誰[可以]使用[玉山Wallet][電子]支付":
        if CHATBOT_MODE:
            if 'wallet' in args[1] and args[2] == '電子':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "誰[可以]使用[玉山][電子]支付跨境網購服務":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[1] == '電子':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "跨境網購[是]否有[額度]限制":
        if CHATBOT_MODE:
            if '額' in args[1]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "跨境網購[限額]多少":
        if CHATBOT_MODE:
            if args[0] in ['限額', '額度']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "跨境網購提供了什麼服務":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "電支帳戶姓名未通過驗證":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "跨境網購服務[身分]驗證時出現[系統]維護":
        if CHATBOT_MODE:
            if args[0] in ['身分', '身份']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "跨境網購服務如何發動退款":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "跨境網購服務為什麼需要[外匯]申報":
        if CHATBOT_MODE:
            if args[0] == '外匯':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "跨境網購的[超商]繳費[是]否[會]收取[手續費]":
        if CHATBOT_MODE:
            if args[0] == '超商' and args[3] == '手續費':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "跨境網購的轉帳付款[是]否[會]收取[手續費]":
        if CHATBOT_MODE:
            if args[2] == '手續費':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "跨境網購的轉帳付款及[超商]繳費[是]否[會]收取[手續費]":
        if CHATBOT_MODE:
            if args[0] == '超商' and args[3] == '手續費':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "退款[匯率]如何計算":
        if CHATBOT_MODE:
            if args[0] == '匯率':
                if 'paypay' in inputSTR:
                    resultDICT["response"] = getResponse("玉山Wallet電子支付退款匯率如何換算", args)
                elif '跨境網購' in inputSTR:
                    resultDICT["response"] = getResponse("跨境網購服務(轉帳付款/超商繳費)的退款匯率如何計算", args)
                    
        else:
            pass

    if utterance == "退款[會]退到哪裡":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "逾期[帳單][可以]用[玉山Wallet][電子]支付繳費嗎":
        if CHATBOT_MODE:
            if args[0] == '帳單' and 'wallet' in args[2]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "開通[電子]支付[帳戶]，[行動][電話]為何[會]被變更":
        if CHATBOT_MODE:
            if args[0] == '電子' and args[1] in ['帳戶', '帳號', '戶頭']:
                if args[3] in ['手機', '電話']:
                    resultDICT["response"] = getResponse(utterance, args)
        else:
            pass
        
    if utterance == "PayPay掃碼付服務[該]如何退款":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass
        
    if utterance == "跨境網購專區的訂單[可]保留多[久]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass
        
    if utterance == "[玉山Wallet]沒有跨境網購專區":
        if CHATBOT_MODE:
            if 'wallet' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass
        
    if utterance == "[電子]支付[帳戶]是什麼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "如何使用[玉山]電子支付—跨境網購超商繳費":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "如何查詢[玉山][電子]支付—跨境網購[交易][紀錄]與[訂單][狀況]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "沒有跨境網購專區":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "跨境網購服務身分驗證時出現系統維護":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "電子支付Email驗證信[是]否有時間限制":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "電子支付[可]綁定哪些支付工具呢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "電子支付[可以]綁定非玉山銀行信用卡":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "電子支付「條碼付」(由店家掃描手機條碼) 的付款方式為何":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "電子支付不[小心]重複繳費了怎麼辦":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "電子支付交易[失敗]怎麼辦":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "電子支付交易資訊[會]保留多[久]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "電子支付交易資訊要怎麼查詢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "電子支付帳戶[可以]綁定幾[組]提領帳號":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "電子支付帳戶提領[是]否[會]被收取手續費":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "電子支付帳戶的交易限額是多少":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "電子支付帳戶通知儲值餘額已達[上]限":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "電子支付支援哪些繳費項目":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "電子支付於日本PayPay掃碼付服務的匯率怎麼換算":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "電子支付於日本PayPay掃碼付服務需要負擔[國外]交易服務費嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "電子支付條碼付的付款方式為何":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "電子支付綁定信用卡儲值付款[可以]使用信用卡紅利點數折抵嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "電子支付綁定信用卡消費[可以]獲得信用卡回饋嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "電子支付若發生退款":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "電子支付若發生退款情形款項[會]退回至哪裡":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "電子支付身分驗證尚未完成":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "電子支付重複繳交水/電費[可以]退款嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "電子支付重複繳交水費[可以]退款嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "約定連結[存款帳戶]付款服務的[交易限額]是多少":
        if CHATBOT_MODE:
            if '存款' in args[0] and '限額' in args[1]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    return resultDICT