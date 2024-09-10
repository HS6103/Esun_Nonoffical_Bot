#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for wealth

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
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), os.path.join("reply", "reply_wealth.json")), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[wealth] {} ===> {}".format(inputSTR, utterance))

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
    
    if utterance == "[何]謂[基金]之[轉換]":
        if CHATBOT_MODE:
            if args[1] == '基金' and args[2] == '轉換':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[信託][管理費]如何計收":
        if CHATBOT_MODE:
            if args[0] == '信託' and args[1] == '管理費':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[匯率]的[基準][點]如何決定":
        if CHATBOT_MODE:
            if args[0] == '匯率' and args[1] == '基準':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[基金]之[轉換]有何限制":
        if CHATBOT_MODE:
            if args[0] == '基金' and args[1] == '轉換':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[基金]之轉換[手續費]為何":
        if CHATBOT_MODE:
            if args[0] == '基金' and '費' in args[1]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[基金]的[交易]有何時[間]限制":
        if CHATBOT_MODE:
            if args[0] == '基金' and args[1] == '交易':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[基金]的[單位數]與[報酬率]如何計算":
        if CHATBOT_MODE:
            if args[0] == '基金' and (args[1] and args[2] in ['單位數', '報酬率']):
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[尊榮禮賓]服務是什麼":
        if CHATBOT_MODE:
            if '禮賓' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[海外][ETF]/[股票][交易][時間]為何":
        if CHATBOT_MODE:
            if args[0] == '海外' and (args[1] and args[2] in ['etf','股票']) and args[3] == '交易' and '時' in args[4]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[海外][ETF]/[股票]有哪些[投資市場][可]提供選擇":
        if CHATBOT_MODE:
            if args[0] == '海外' and (args[1] and args[2] in ['etf','股票']) and '市場' in args[3]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[海外][ETF][交易][時間]為何":
        if CHATBOT_MODE:
            if args[0] == '海外' and '時' in args[3]:
                if args[1] == 'etf':
                    resultDICT["response"] = getResponse(utterance, args)
                elif args[1] == '債券':
                    resultDICT["response"] = getResponse("[海外][債券][交易][時間]為何", args)
        else:
            pass

    if utterance == "[海外][ETF]有哪些[投資市場][可]提供選擇":
        if CHATBOT_MODE:
            if args[0] == '海外' and args[1] in ['etf','股票'] and '市場' in args[3]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[玉山][是]否有[親子帳戶]":
        if CHATBOT_MODE:
            if args[0] in ['玉山', '玉山銀行'] and '親子' in args[2]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[玉山][財富]管理[是]否有[會員][制度]":
        if CHATBOT_MODE:
            if args[0] in ['玉山', '玉山銀行'] and args[1] in ['財富', '資產'] and args[3] == '會員':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[財富]管理[會員][可]享何[種][優惠]":
        if CHATBOT_MODE:
            if args[0] in ['財富', '資產'] and args[1] == '會員':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[贖回款]之淨值如何決定":
        if CHATBOT_MODE:
            if '贖回' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[贖回款]何時入帳":
        if CHATBOT_MODE:
            if '贖回' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[部分]贖回有何[條件]":
        if CHATBOT_MODE:
            if args[0] == '部分' and args[1] in ['條件']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[部分]轉換有何[條件]":
        if CHATBOT_MODE:
            if args[0] == '部分' and args[1] in ['條件']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "「[部分]轉換」或「[部分]贖回」有何[條件]":
        if CHATBOT_MODE:
            if args[0] and args[1] == '部分':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "什麼是[海外債券]":
        if CHATBOT_MODE:
            if args[0] == '海外債券':
                resultDICT["response"] = getResponse(utterance, args)
            elif args[0] == '隨行理專':
                resultDICT["response"] = getResponse("什麼是[隨行理專]", args)
                resultDICT["imgURL"] = []
                resultDICT["imgURL"] += [
                    "https://www.esunbank.com/zh-tw/-/media/ESUNBANK/Images/Home/About/wealth/QR_code03_fund.png"
                ]

        else:
            pass

    if utterance == "什麼是[結構型][商品]":
        if CHATBOT_MODE:
            if args[0] == '結構型' and args[1] in ['商品', '產品']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何使用[財富]管理[專區]的[我]的觀察清單":
        if CHATBOT_MODE:
            if args[0] in ['財富', '資產']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何使用[隨行理專]":
        if CHATBOT_MODE:
            if args[0] == '隨行理專':
                resultDICT["response"] = getResponse(utterance, args)
                resultDICT["imgURL"] = []
                resultDICT["imgURL"] += [
                    "https://www.esunbank.com/zh-tw/-/media/ESUNBANK/Images/Home/About/wealth/QR_code03_fund.png"
                ]
                
        else:
            pass

    if utterance == "如何取消[海外債券][交易]":
        if CHATBOT_MODE:
            if args[0] == '海外債券' and args[1] == '交易':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何得知[基金]的最新[淨值]報價":
        if CHATBOT_MODE:
            if args[0] == '基金' and args[1] == '淨值':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何找到[財富]管理各項[商品]的最新公告":
        if CHATBOT_MODE:
            if args[0] == '財富' and args[1] in ['商品', '產品']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何於[網路]/[行動銀行]申請[基金][定期][定額]申購":
        if CHATBOT_MODE:
            if args[0] and args[1] in ['網路', '行動銀行', '網銀'] and args[3] == '定期' and args[4] == '定額':
                if args[2] == '基金':
                    resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何於[行動銀行]申請[基金][定期][定額]申購":
        if CHATBOT_MODE:
            if args[0] in ['網路', '行動銀行', '網銀'] and args[2] == '定期' and args[3] == '定額':
                if args[1] == '基金':
                    resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何查詢[海外債券][庫存]損益":
        if CHATBOT_MODE:
            if args[0] == '海外債券' and args[1] == '庫存':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何查詢[海外債券][產品條件]":
        if CHATBOT_MODE:
            if args[0] == '海外債券':
                if args[1] == '產品條件':
                    resultDICT["response"] = getResponse(utterance, args)
                elif '價' in args[1]:
                    resultDICT["response"] = getResponse("如何查詢海外債券產品價格", args)
        else:
            pass

    if utterance == "如何查詢海外債券產品價格":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何查詢[海外債券]成交[結果]":
        if CHATBOT_MODE:
            if args[0] == '海外債券':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何決定[海外][ETF]/[股票]的委託[價格]":
        if CHATBOT_MODE:
            if args[0] == '海外' and (args[1] and args[2] in ['etf','股票']) and '價' in args[3]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何決定[海外股票]的委託[價格]":
        if CHATBOT_MODE:
            if args[0] == '海外股票' and args[1] == '價格':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何訂閱[玉山]理財電子週報":
        if CHATBOT_MODE:
            if args[0] in ['玉山', '玉山銀行']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何買賣[海外][ETF]":
        if CHATBOT_MODE:
            if args[0] == '海外' and args[1] == 'etf':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass
        
    if utterance == "如何買賣海外股票":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何進行[海外債券][交易]":
        if CHATBOT_MODE:
            if args[0] == '海外債券' and args[1] == '交易':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何進行[金融][商品]比較":
        if CHATBOT_MODE:
            if args[0] == '金融' and args[1] in ['商品', '產品']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "常見的[債券類型]有哪些":
        if CHATBOT_MODE:
            if '債券' in args[0]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "投信基金及境[外]基金淨值適用說明":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "投資[海外][ETF]/[股票]所需負擔的稅負為何":
        if CHATBOT_MODE:
            if args[0] == '海外' and (args[1] and args[2] in ['etf','股票']):
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "投資[海外][ETF]所需負擔的稅負為何":
        if CHATBOT_MODE:
            if args[0] == '海外' and args[1] in ['etf','股票']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "投資[海外債券][適合][我]嗎":
        if CHATBOT_MODE:
            if args[0] == '海外債券' and args[1] == '適合':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "投資[海外債券]的[風險]是什麼":
        if CHATBOT_MODE:
            if args[0] == '海外債券' and '險' in args[1]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "投資[結構型][商品]的[風險]是什麼":
        if CHATBOT_MODE:
            if args[0] == '結構型' and '險' in args[2]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "有哪些[類型]的[結構型][商品]":
        if CHATBOT_MODE:
            if args[1] == '結構型' and args[2] in ['商品', '產品']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "為何[手續費]及配息要按[比例]攤提":
        if CHATBOT_MODE:
            if args[0] == '手續費' and args[1] == '比例':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "申購[基金][應]填寫哪些[資料]":
        if CHATBOT_MODE:
            if args[0] == '基金':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "申購[基金][應]注意哪些[事項]":
        if CHATBOT_MODE:
            if args[0] == '基金':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "要如何申請[網路基金][交易]":
        if CHATBOT_MODE:
            if args[0] == '網路基金' and args[1] == '交易':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass
        
    if utterance == "如何進行金融商品([基金]、[海外][ETF]、[港股]、[美股])比較":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    return resultDICT