#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for digital_account

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
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply\\reply_digital_account.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[digital_account] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern=""):
    debugInfo(inputSTR, utterance)

    if utterance == "[Email]驗證超過限制[次數]怎麼辦":
        if CHATBOT_MODE:
            if args[0] in ['手機', '電話', '簡訊']:
                resultDICT["response"] = getResponse("[手機]驗證超過限制[次數]怎麼辦", args)
            elif args[0].lower().strip(' ') in ['email', 'e-mail']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[一直]未收到簽帳[金融卡][該]如何處理":
        if CHATBOT_MODE:
            if args[1] == '金融卡':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[信用卡]未開卡[是]否[會]影響開戶申請":
        if CHATBOT_MODE:
            if args[0] == '信用卡':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[信用卡]被管制[是]否[會]影響開戶申請":
        if CHATBOT_MODE:
            if args[0] == '信用卡':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[信用卡]被管制或未開卡[是]否[會]影響開戶申請":
        if CHATBOT_MODE:
            if args[0] == '信用卡':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[可以]不申請[網路銀行]嗎":
        if CHATBOT_MODE:
            if args[1] in ['網路銀行', '網銀']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[悠遊簽帳金融卡]關閉簽帳[功能][後][可以]使用[悠遊卡][自動]加值服務嗎":
        if CHATBOT_MODE:
            if '悠遊' in args[0] and args[4] == '悠遊卡':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[所有]瀏覽[器][下][都][可以]進行驗證嗎":
        if CHATBOT_MODE:
            if args[1] == '器':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[自然人憑證]未通過驗證怎麼辦":
        if CHATBOT_MODE:
            if '自然人' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "各類數位帳戶的轉帳[限額]為何":
        if CHATBOT_MODE:
            if '限' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何上傳[照片]":
        if CHATBOT_MODE:
            if args[0] in ['照片', '相片']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何完成補件":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何申請[網路銀行]":
        if CHATBOT_MODE:
            if args[0] in ['網路銀行', '網銀']:
                resultDICT["response"] = getResponse(utterance, args)
            elif args[0] == '數位帳戶':
                resultDICT["response"] = getResponse("如何申請[數位帳戶]", args)
        else:
            pass

    if utterance == "如何知道[我]已經[成功]完成補件":
        if CHATBOT_MODE:
            if args[1] in ['成功', '順利', None]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何知道簽帳[金融卡][進度]":
        if CHATBOT_MODE:
            if args[0] == '金融卡' and '進' in args[1]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何確定[我]的[讀卡機][是]否安裝[成功]":
        if CHATBOT_MODE:
            if args[1] == '讀卡機' and args[2] == '成功':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何補換發數位帳戶的[金融卡]":
        if CHATBOT_MODE:
            if args[0] == '金融卡':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如果[身分][證件][資料]辨識[結果][錯誤]怎麼辦":
        if CHATBOT_MODE:
            if '身分' in args[0] and args[4] in ['錯誤', '失敗']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如果已經有[信用卡][版]的[網路銀行][是]否還需要[再次]申請":
        if CHATBOT_MODE:
            if args[0] == '信用卡' and args[2] in ['網路銀行', '網銀']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如果沒完成數位帳戶申請下[一次]申請需要[重新]填寫[資料]嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "完成補件請問需要多[久][才能]完成審核":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "審核[期間][可以]申請[信用卡][版]的[網路銀行]嗎":
        if CHATBOT_MODE:
            if args[2] == '信用卡' and args[4] in ['網路銀行', '網銀']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "審核[期間][密碼]輸入[錯誤][5次]被暫停[該]怎麼辦":
        if CHATBOT_MODE:
            if args[1] == '密碼':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "審核[期間]忘記[信用卡][版][網銀]的[使用者][密碼][該]怎麼辦":
        if CHATBOT_MODE:
            if args[1] == '信用卡' and args[3] in ['網路銀行', '網銀'] and args[5] == '密碼':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "審核[期間]忘記[信用卡][版][網銀]的[使用者][密碼]或輸入[錯誤][5次]被暫停[該]怎麼辦":
        if CHATBOT_MODE:
            if args[1] == '信用卡' and args[3] in ['網路銀行', '網銀'] and args[5] == '密碼':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "已安裝[元件]但[網頁]還是[一直]顯示需下載安裝[元件]怎麼辦":
        if CHATBOT_MODE:
            if '元件' in args[0] and args[3]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "已有本行[臨櫃][帳戶][是]否[可以]再申請數位帳戶":
        if CHATBOT_MODE:
            if args[0] in ['臨櫃', '銀行', '分行'] and args[1] in ['帳戶', '帳號', '戶頭']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "忘記[自然人憑證][密碼]如何處理":
        if CHATBOT_MODE:
            if '自然人' in args[0] and args[1] == '密碼':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "數位帳戶[可以]作為[期貨帳戶]的[出入]金約定[帳戶]嗎":
        if CHATBOT_MODE:
            if '期貨' in args[1] and args[2] == '出入':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "數位帳戶[可以]作為[薪]轉帳[戶]嗎":
        if CHATBOT_MODE:
            if '薪' in args[1]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "數位帳戶[可以]作為[證券]交割[戶]嗎":
        if CHATBOT_MODE:
            if args[1] in ['證券', '股票']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "數位帳戶[可以]作為撥貸[帳戶]嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "數位帳戶[可以]接受[國外]匯入[款]嗎":
        if CHATBOT_MODE:
            if '外' in args[1]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "數位帳戶[可以]約定[ACH]委託轉帳扣款嗎":
        if CHATBOT_MODE:
            if args[1].lower().strip(' ') == 'ach':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "數位帳戶[可以]約定為[代]扣繳[帳號]嗎":
        if CHATBOT_MODE:
            if args[1] == '代':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "數位帳戶[可以]繳[信用卡][款]嗎":
        if CHATBOT_MODE:
            if args[1] == '信用卡':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "數位帳戶[可以]連結[街口支付]":
        if CHATBOT_MODE:
            if args[3] in userDefinedDICT['as_payment']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "數位帳戶[可以]進行[PayPal]連結及提領服務嗎":
        if CHATBOT_MODE:
            if args[1].lower().strip(' ') == 'paypal':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "數位帳戶[可以]進行[國外]匯出匯款嗎":
        if CHATBOT_MODE:
            if '外' in args[1]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "數位帳戶[可以]進行哪些[交易]":
        if CHATBOT_MODE:
            if args[1] in ['交易', '業務']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "數位帳戶[可以]郵寄銷戶嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "數位帳戶[可以]開立子帳戶嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "數位帳戶[是]否享有[優惠][利率]":
        if CHATBOT_MODE:
            if args[1] == '優惠' and args[2] == '利率':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "數位帳戶[是]否有[存摺]":
        if CHATBOT_MODE:
            if '存摺' in args[1]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "數位帳戶[是]否有提供[金融卡]":
        if CHATBOT_MODE:
            if args[1] == '金融卡':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "數位帳戶[金融卡][可以][國外]提款嗎":
        if CHATBOT_MODE:
            if args[0] == '金融卡' and '外' in args[2]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "數位帳戶之[金融卡][可以]使用轉帳[功能]嗎":
        if CHATBOT_MODE:
            if args[0] == '金融卡':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "數位帳戶享有哪些[優惠]":
        if CHATBOT_MODE:
            if args[0] in ['優惠']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "數位帳戶作為[證券]交割[戶]時有什麼限制":
        if CHATBOT_MODE:
            if args[0] == '證券':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "數位帳戶有提供哪些臨櫃交易":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "數位帳戶申辦[流程]":
        if CHATBOT_MODE:
            if '程' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "數位帳戶的[金融卡]要開卡嗎":
        if CHATBOT_MODE:
            if args[0] == '金融卡':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "數位帳戶的申辦[資格]為何":
        if CHATBOT_MODE:
            if args[0] == '資格':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "數位帳戶簽帳金融卡[可以]連結[行動]支付":
        if CHATBOT_MODE:
            if args[1] == '行動':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "數位帳戶至[臨櫃]辦理[業務]需要支付[手續費]嗎":
        if CHATBOT_MODE:
            if args[0] in ['臨櫃', '銀行', '分行'] and args[2] == '手續費':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "數位帳戶金融卡[可以]變更寄送地址嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "有數位帳戶[可]在[臨櫃]開[一般]存款帳戶嗎":
        if CHATBOT_MODE:
            if args[0] in ['臨櫃', '銀行', '分行'] and args[2] in ['一般', '普通', None]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "每[人][能]申請幾[個][玉山]數位帳戶":
        if CHATBOT_MODE:
            if '玉山' in args[3]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "為什麼[一直]無法收到[簡訊][驗證碼]":
        if CHATBOT_MODE:
            if args[2] == '驗證碼':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "為什麼[具][他][國]或[地區][身分者]不[能]申請數位帳戶":
        if CHATBOT_MODE:
            if ('國' in args[2] or args[3]) and args[4] in ['身分', '戶籍', '國籍']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "為什麼[我]不[能]申請數位帳戶":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "為什麼[我]收到數位帳戶補件通知":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "為什麼[我]無法登入補件[網頁]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "為什麼美國納稅[義務人]不[能]申請數位帳戶":
        if CHATBOT_MODE:
            if '人' or '者' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "為什麼美國納稅[義務人]或[具][他][國]或[地區][身分者]不[能]申請數位帳戶":
        if CHATBOT_MODE:
            if ('人' or '者' in args[0]) and ('國' in args[3] or args[4]):
                if args[5] in ['身分', '戶籍', '國籍'] or ('人' or '者' in args[5]):
                    resultDICT["response"] = getResponse(utterance, args)       
        else:
            pass

    if utterance == "申請數位帳戶[後]如何拿到[金融卡]":
        if CHATBOT_MODE:
            if args[1] == '金融卡':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "申請數位帳戶上傳[資料]有什麼限制":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "申請數位帳戶時操作到[一半]斷線[該]怎麼辦":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "申請數位帳戶需準備哪些[資料]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "若領補換[資訊]超過限制查詢[次數]怎麼辦":
        if CHATBOT_MODE:
            if args[1] == '次數':            
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "補件[照片]需要注意什麼":
        if CHATBOT_MODE:
            if args[0] in ['照片', '相片']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "變更過[中文戶名]且未至[臨櫃]更新[資訊][是]否[可]申請數位帳戶":
        if CHATBOT_MODE:
            if '中文' in args[0] or args[0] == '戶名' and args[1] in ['臨櫃', '銀行', '分行']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "逾補[件][期]限未完成補件怎麼辦":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "驗證[之前]需要[先進]行[讀卡機]的[安裝]嗎":
        if CHATBOT_MODE:
            if args[2] == '讀卡機' and args[3] == '安裝':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "驗證有[版本]或[系統]的[限制]嗎":
        if CHATBOT_MODE:
            if args[0] and args[1] in ['版本','系統', '規格', '作業系統', 'os', '環境'] and '限' in args[2]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    return resultDICT