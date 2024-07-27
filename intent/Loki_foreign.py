#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for foreign

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
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply\\reply_foreign.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[foreign] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern=""):
    debugInfo(inputSTR, utterance)
    if utterance == "[e]化[通路]承作[外匯交易][是]否有[時間]限制":
        if CHATBOT_MODE:
            if args[0].lower() in ['e', '電子', '數位'] and '外匯' in args[2] and args[4] in ['時間', '時段']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[人民幣][外幣][現鈔]存入[外幣][帳戶]有無[金額]限制":
        if CHATBOT_MODE:
            if args[0].lower() in ['rmb','人民幣'] and args[2] in ['現鈔','現金','鈔票'] and '額' in args[5]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[光票]託收[是]否收取[費用]":
        if CHATBOT_MODE:
            if args[0] == '光票' and args[2] in ['費用', '手續費']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[光票]託收如何使用":
        if CHATBOT_MODE:
            if args[0] == '光票':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[光票]託收如何兌現":
        if CHATBOT_MODE:
            if args[0] == '光票':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[國外]的[支票][是]否收取[費用]":
        if CHATBOT_MODE:
            if args[0] in ['國外', '外國', '海外'] and args[1].lower() in ['支票', 'check'] and args[3] in ['費用', '手續費']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[國外]的[支票]如何使用":
        if CHATBOT_MODE:
            if args[0] in ['國外', '外國', '海外'] and args[1].lower() in ['支票', 'check']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[國外]的[支票]如何兌現":
        if CHATBOT_MODE:
            if args[0] in ['國外', '外國', '海外'] and args[1].lower() in ['支票', 'check']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[外幣][現鈔][可][否]存入[我]在[玉山銀行]的[外幣][帳戶]呢":
        if CHATBOT_MODE:
            if '玉山' in args[5]:
                if (args[1] and args[6] not in ['台幣','新台幣','臺幣','新臺幣']) and ('鈔' or '金' in args[2]):
                    resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[日期處]有[註記]「[*]」[符號]是代表什麼[意思]":
        if CHATBOT_MODE:
            if '日期' in args[0] and args[2] in ['*', '星星']:
                resultDICT["response"] = getResponse(utterance, args)
            elif '金額' in args[0] and args[2] in ['-', '減號']:
                resultDICT["response"] = getResponse("[金額][前]有標明「[-]」[符號]是代表什麼[意思]", args)
        else:
            pass

    if utterance == "[是]否有提供[ATM]提領[外幣][現鈔]服務":
        if CHATBOT_MODE:
            if args[1].lower() == 'atm' and args[2] not in ['台幣','新台幣','臺幣','新臺幣'] and ('鈔' or '金' in args[3]):
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[是]否有提供買賣[外幣][現鈔]服務呢":
        if CHATBOT_MODE:
            if args[1] not in ['台幣','新台幣','臺幣','新臺幣'] and ('鈔' or '金' in args[2]):
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[玉山銀行][外幣帳戶]提領[外幣][現鈔][是]否需支付[手續費]":
        if CHATBOT_MODE:
            if args[0] in ['玉山', '玉山銀行']:
                if args[1] not in ['台幣','新台幣','臺幣','新臺幣'] and ('鈔' or '金' in args[2]):
                    resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[網路銀行][外匯][交易]的[每日]承作[限額]為":
        if CHATBOT_MODE:
            if args[0] in ['網路銀行', '網銀'] and '外匯' in args[1]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[網路銀行][外匯][交易]的承作[匯率]規定為何":
        if CHATBOT_MODE:
            if args[0] in ['網路銀行', '網銀'] and '外匯' in args[1]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[網路銀行][外匯][交易]還需注意哪些[事項]":
        if CHATBOT_MODE:
            if args[0] in ['網路銀行', '網銀'] and '外匯' in args[1]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[金額][前]有標明「[-]」[符號]是代表什麼[意思]":
        if CHATBOT_MODE:
            if '日期' in args[0] and args[2] in ['*', '星星']:
                resultDICT["response"] = getResponse("[日期處]有[註記]「[*]」[符號]是代表什麼[意思]", args)
            elif '金額' in args[0] and args[2] in ['-', '減號']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "使用[網路銀行][外匯][交易]所需負擔的[費用]為何":
        if CHATBOT_MODE:
            if args[0] in ['網路銀行', '網銀'] and '外匯' in args[1] and args[3] in ['費用', '手續費']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何使用[網路銀行]的[外匯交易]":
        if CHATBOT_MODE:
            if args[0] in ['網路銀行', '網銀'] and '外匯' in args[1]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何收到[外幣]匯入匯款通知":
        if CHATBOT_MODE:
            if args[0] not in ['台幣','新台幣','臺幣','新臺幣']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何查詢匯入[款項][進度]":
        if CHATBOT_MODE:
            if args[0] == '款項' and '進' in args[1]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "從[國外]匯入[款項]至[我]的[玉山銀行][帳戶][我][該]提供什麼[資料]":
        if CHATBOT_MODE:
            if '外' in args[0] and '玉山' in args[3]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "怎樣[將][款項]匯給[國][外][親友]":
        if CHATBOT_MODE:
            if args[1] in ['款項','錢'] and args[1] in ['國', '海'] and args[2] == '外' and ('親' or '友' in args[3]):
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "購買[人民幣][現鈔][金額][是]否有[相關]限制":
        if CHATBOT_MODE:
            if args[0].lower() in ['rmb','人民幣'] and args[1] in ['現鈔','現金','鈔票'] and '額' in args[2]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    return resultDICT