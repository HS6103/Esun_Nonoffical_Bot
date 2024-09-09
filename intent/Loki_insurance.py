#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for insurance

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
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), os.path.join("reply", "reply_insurance.json")), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[insurance] {} ===> {}".format(inputSTR, utterance))

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
    
    if utterance == "[一定]要完成「網路投保註冊」[才][可以]投保嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[一定]要完成「網路投保註冊暨[身分]驗證」[才][可以]投保嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[一次]繳跟[分期]繳[保費]的對[我]的[年金]給付有什麼影響":
        if CHATBOT_MODE:
            if args[0] and args[1] in ['一次', '分期']:
                if args[2] in ['保費', '保險費'] and args[4] == '年金':
                    resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[中國人壽]更名為[凱基人壽][保單][權益][會]受影響嗎":
        if CHATBOT_MODE:
            if args[0] and args[1] in ['中國人壽', '凱基人壽'] and '保' in args[2]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[剛剛]成家的[我][應該]規劃什麼樣的[保險]呢":
        if CHATBOT_MODE:
            if args[3] == '保險':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[可以]改[年金]開始給付[日]嗎":
        if CHATBOT_MODE:
            if args[1] == '年金' and '日' in args[2]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[可以]用[我]的[銀行][帳戶]幫[家人]投保及繳[首期][保險費]嗎":
        if CHATBOT_MODE:
            if args[1] in ['我', '自己'] and args[3] in ['帳戶', '帳號', '戶頭'] and args[5] == '首期' and args[6] in ['保費', '保險費']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[可以]用[我]的[銀行][帳戶]幫[家人]投保嗎":
        if CHATBOT_MODE:
            if args[1] in ['我', '自己'] and args[3] in ['帳戶', '帳號', '戶頭']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[可以]用[我]的[銀行][帳戶]幫[家人]繳[首期][保險費]嗎":
        if CHATBOT_MODE:
            if args[1] in ['我', '自己'] and args[3] in ['帳戶', '帳號', '戶頭'] and args[5] == '首期' and args[6] in ['保費', '保險費']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[名詞]解釋":
        if CHATBOT_MODE:
            if args[0] == '名詞':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[國內]旅行多[久][前][可以]來投保":
        if CHATBOT_MODE:
            if '前' in args[2]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[寶貝][剛]出生[應該]規劃什麼樣的[保險]呢":
        if CHATBOT_MODE:
            if '寶' or '孩' in args[0] and args[3] == '保險':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[年金][保險][是]否[可以]搭配附約":
        if CHATBOT_MODE:
            if args[0] == '年金' and args[1] == '保險':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[年金]給付的[方式]選擇要注意什麼限制":
        if CHATBOT_MODE:
            if args[0] == '年金':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[年金]給付選擇[一次]給付或是[分期]給付的[好處]為何":
        if CHATBOT_MODE:
            if args[0] == '年金' and args[1] and args[2] in ['一次', '分期'] and ('好' or '優' in args[3]):
                    resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[年金受益人]要如何變更":
        if CHATBOT_MODE:
            if args[0] in ['年金受益人', '身故受益人']:
                resultDICT["response"] = getResponse("[{}]要如何變更".format(args[0]), args)
        else:
            pass

    if utterance == "[強制汽/機車責任保險]到期[前]多[久][可以]來投保":
        if CHATBOT_MODE:
            if args[0] in userDefinedDICT['insurance'] and '汽' or '機' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[強制汽/機車責任保險]是哪家[保險][公司]呢":
        if CHATBOT_MODE:
            if args[0] in userDefinedDICT['insurance']:
                resultDICT["response"] = getResponse("[{}]是哪家[保險][公司]呢".format(args[0]), args)
        else:
            pass

    if utterance == "[後續]服務是找[保險][公司]嗎":
        if CHATBOT_MODE:
            if '後' in args[0] and args[1] == '保險' and args[2] == '公司':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[旅行平安保險][受益人][可以]指定誰":
        if CHATBOT_MODE:
            if args[0] in userDefinedDICT['insurance'] and '旅' in args[0] and '受益人' in args[1]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[旅行平安保險]的[商品]有那些":
        if CHATBOT_MODE:
            if args[0] in userDefinedDICT['insurance']:
                if '旅' in args[0]:
                    resultDICT["response"] = getResponse("[旅行平安保險]的[商品]有那些", args)
                elif '汽' or '機' in args[0]:
                    resultDICT["response"] = getResponse("[強制汽/機車責任保險]的[商品]有那些", args)
        else:
            pass

    if utterance == "[旅行平安保險]的「投保[流程]」為何":
        if CHATBOT_MODE:
            if args[0] in userDefinedDICT['insurance'] and '險' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[旅行平安保險]的生效從什麼[時間點]開始":
        if CHATBOT_MODE:
            if args[0] in userDefinedDICT['insurance'] and '時' in args[1]:
                if '平' in args[0]:
                    resultDICT["response"] = getResponse("[旅行平安保險]的生效從什麼[時間點]開始", args)
                elif '綜' in args[0]:
                    resultDICT["response"] = getResponse("[旅行綜合險]的生效從什麼[時間點]開始", args)
                elif '汽' or '機' in args[0]:
                    resultDICT["response"] = getResponse("[強制汽/機車責任保險]的生效從什麼[時間點]開始", args)
        else:
            pass

    if utterance == "[旅行平安險]之[保額]限制":
        if CHATBOT_MODE:
            if args[0] in userDefinedDICT['insurance']:
                if '綜' in args[0]:
                    resultDICT["response"] = getResponse("[旅行綜合險]之[保額]限制", args)
                elif '平' in args[0]:
                    resultDICT["response"] = getResponse("[旅行平安保險]之[保額]限制", args)
        else:
            pass

    if utterance == "[旅行綜合險]的繳費[方式]有什麼":
        if CHATBOT_MODE:
            if args[0] in userDefinedDICT['insurance']:
                if '綜' in args[0]:
                    resultDICT["response"] = getResponse("[旅行綜合險]的繳費[方式]有什麼", args)
                elif '平' in args[0]:
                    resultDICT["response"] = getResponse("[旅行平安保險]的繳費[方式]有什麼", args)
        else:
            pass

    if utterance == "[是]否[可以]透過網路投保[線上]執行提[前]解約":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[是]否有[終身醫療保險][可]供參考":
        if CHATBOT_MODE:
            if args[1] in userDefinedDICT['insurance'] and '醫療' in args[1]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[暫時]停止扣繳續期每月定額[保險費]要如何申辦":
        if CHATBOT_MODE:
            if args[1] in ['保險費', '保費']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "每月定額[保險費]的宣告利率與投保時的宣告利率是[一樣]嗎":
        if CHATBOT_MODE:
            if args[0] in ['保險費', '保費'] and '一樣' or '相同' in args[1]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "網路[上]找不到[廠牌]":
        if CHATBOT_MODE:
            if args[1] in ['廠牌', '車型', '車款']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "網路投保[可以]取消嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "網路投保[年金][保險][前][應]注意哪些[事項]":
        if CHATBOT_MODE:
            if args[0] == '年金' and args[1] == '保險':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "網路投保[過程][中]如何確認[個人]的[身分]驗證":
        if CHATBOT_MODE:
            if args[0] == '過程' and args[3] in ['身分', '身份']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "網路投保完成[後]何時[可]收到[保險單]":
        if CHATBOT_MODE:
            if args[2] in ['保險單', '保單']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "網路投保完成[後]如何確定投保[成功]":
        if CHATBOT_MODE:
            if args[1] == '成功':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "網路投保有什麼[應]注意呢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "網路投保的[交易][時間]為何":
        if CHATBOT_MODE:
            if args[0] == '交易' and '時' in args[1]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "網路投保需要具備哪些[資格]":
        if CHATBOT_MODE:
            if args[0] == '資格':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "續期每月定額[保險費][可][否]從[他][行][帳戶]扣款":
        if CHATBOT_MODE:
            if args[0] in ['保險費', '保費'] and args[3] == '他' and args[4] == '行':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "續期每月定額[保險費]未扣款[成功][會]通知[我]嗎":
        if CHATBOT_MODE:
            if args[0] in ['保險費', '保費']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[身故受益人]有什麼[身分]限制嗎":
        if CHATBOT_MODE:
            if args[0] in ['年金受益人', '身故受益人']:
                resultDICT["response"] = getResponse("[{}]要如何變更".format(args[0]), args)
        else:
            pass

    if utterance == "出國多[久][前][可以]來投保":
        if CHATBOT_MODE:
            if args[2] == '前':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "出發時還沒收到[保單][是]否[會]影響[保險]效力":
        if CHATBOT_MODE:
            if args[0] in ['保單','保險單'] and args[3] == '保險':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "在[國][外][是]否還[可]投保[旅行綜合險]":
        if CHATBOT_MODE:
            if args[0] in ['國', '境'] and args[1] == '外' and args[4]:
                resultDICT["response"] = getResponse(utterance, args)   
        else:
            pass

    if utterance == "在[玉山銀行]查詢或下載[任何]網路投保的[相關][資訊][是]否需要[另][外]付費":
        if CHATBOT_MODE:
            if args[0] in ['玉山', '玉山銀行']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何修改[保單]寄件[地址]":
        if CHATBOT_MODE:
            if args[0] in ['保單','保險單'] and args[1] == '地址':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何取得[詳細]的網路投保[商品]說明及[保險條款]":
        if CHATBOT_MODE:
            if '條款' in args[2]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何申請理賠":
        if CHATBOT_MODE:
            if '理賠' in inputSTR:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何申辦提早領回[年金]":
        if CHATBOT_MODE:
            if args[0] == '年金':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何申辦更改[年金]開始給付[日]":
        if CHATBOT_MODE:
            if args[0] == '年金':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何確認續期每月定額[保險費][是]否有扣款[成功]":
        if CHATBOT_MODE:
            if args[0] in ['保險費', '保費'] and args[2] == '成功':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何詢問[出][險]或申請理賠[問題]":
        if CHATBOT_MODE:
            if args[0] == '出' and args[1] == '險' and '問' or '事' in args[2]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何進行[玉山銀行]網路投保":
        if CHATBOT_MODE:
            if '玉山' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如果[帳戶][餘額][不足]導致扣款[失敗]續期每月定額[保險費][會]停扣嗎":
        if CHATBOT_MODE:
            if args[0] in ['帳戶', '帳號', '戶頭'] and args[2] in ['不足', '不夠'] and args[3] == '失敗' and args[4] in ['保費', '保險費']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "宣告[利率]要去哪裡查詢":
        if CHATBOT_MODE:
            if args[0] == '利率':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[壯年]的[我][應該]規劃什麼樣的[保險]":
        if CHATBOT_MODE:
            if args[0] == '壯年' and args[3] == '保險':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "恢復扣繳續期每月定額[保險費]要如何申辦":
        if CHATBOT_MODE:
            if args[0] in ['保費', '保險費']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass
        
    if utterance == "投保[過程][中]有[問題][能]詢問誰":
        if CHATBOT_MODE:
            if '問' in args[2]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[年金][一次]給付或[分期]給付[將]來[可以]改嗎":
        if CHATBOT_MODE:
            if args[0] == '年金' and args[1] and args[2] in ['一次', '分期']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "有沒[有][適合][小朋友]的[保險]規劃[產品]":
        if CHATBOT_MODE:
            if args[2] in ['小朋友', '小孩']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "未申請扣繳續期每月定額[保險費][將]來要如何申辦":
        if CHATBOT_MODE:
            if args[0] in ['保費', '保險費']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "沒有[玉山]的[帳戶]還是[可以]透過[玉山][臨櫃]或[網路]投保嗎":
        if CHATBOT_MODE:
            if args[0] and args[3] in ['玉山', '玉山銀行'] and args[1] in ['帳戶', '帳號', '戶頭'] and args[4] and args[5] in ['網路', '臨櫃']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "沒有[玉山]的[帳戶]還是[可以]透過[玉山][臨櫃]投保嗎":
        if CHATBOT_MODE:
            if args[0] and args[3] in ['玉山', '玉山銀行'] and args[1] in ['帳戶', '帳號', '戶頭'] and args[4] in ['網路', '臨櫃']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "沒有[玉山]的[帳戶]還是[可以]透過[網路]投保嗎":
        if CHATBOT_MODE:
            if args[0] in ['玉山', '玉山銀行'] and args[1] in ['帳戶', '帳號', '戶頭'] and args[3] in ['網路', '臨櫃']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "申請續期每月定額[保險費]繳費[成功][後]何時[會]開始扣款":
        if CHATBOT_MODE:
            if args[0] in ['保費', '保險費'] and args[1] == '成功':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "規劃退休有[適合]的[保險]嗎":
        if CHATBOT_MODE:
            if args[1] == '保險':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[網路]投保[一定]要填寫[email]嗎":
        if CHATBOT_MODE:
            if args[0] == '網路' and args[2] in ['email', 'e-mail']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "透過[玉山]投保[只][能]向原[服務人員]所屬[分行]諮詢[保險][相關][問題]嗎":
        if CHATBOT_MODE:
            if args[0] in ['玉山', '玉山銀行'] and '險' in args[5] and args[7] in ['問題', '事宜', '疑問']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "透過[玉山銀行]進行網路投保如何確保[我]的[交易][安全]":
        if CHATBOT_MODE:
            if args[0] in ['玉山', '玉山銀行'] and args[2] == '交易' and args[3] == '安全':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[英文]投保證明[應]如何辦理":
        if CHATBOT_MODE:
            if args[0] in ['英文']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "非本[國籍][可以]購買[保險]嗎":
        if CHATBOT_MODE:
            if '國' in args[0] and args[2] == '保險' or args[2] in userDefinedDICT['insurance']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    return resultDICT