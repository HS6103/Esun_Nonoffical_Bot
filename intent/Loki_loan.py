#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for loan

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
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply\\reply_loan.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[loan] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern=""):
    debugInfo(inputSTR, utterance)
    if utterance == "[MyData]服務[會]取得哪些[資料]":
        if CHATBOT_MODE:
            if args[0].lower().strip(' ') in ['my data', 'mydata'] and '資' in args[2]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[MyData]服務[會]取得那些[資料]":
        if CHATBOT_MODE:
            if args[0].lower().strip(' ') in ['my data', 'mydata'] and '資' in args[2]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[他][國]所設之[分校][是]否[可]申貸[留學貸款]":
        if CHATBOT_MODE:
            if '國' in args[1] and args[2] in ['分校', '校區'] and '學貸' in args[5]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[住宅]補貼如果有其他[問題]要向哪裡詢問":
        if CHATBOT_MODE:
            if args[0] in ['住宅', '房屋'] and '問' in args[1]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "保證人[是]否有[年齡]限制":
        if CHATBOT_MODE:
            if args[1] in ['年齡', '年紀', '歲數']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[保證人][資格]為何":
        if CHATBOT_MODE:
            if args[0] == '保證人' and args[1] == '資格':
                resultDICT["response"] = getResponse(utterance, args)
            elif args[0] == '房貸' and args[1] == '流程':
                resultDICT["response"] = getResponse('[{}][{}]為何'.format(args[0], args[1]), args)
            elif args[0] == '留學貸款' and args[1] in ['額度', '利率']:
                resultDICT["response"] = getResponse('[{}][{}]為何'.format(args[0], args[1]), args)
        else:
            pass

    if utterance == "[信用貸款]在打擊資恐[相關][法規][會]有什麼[措施]呢":
        if CHATBOT_MODE:
            if args[0] in ['信用貸款', '信貸']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[信用貸款]在防制洗錢[相關][法規][會]有什麼[措施]呢":
        if CHATBOT_MODE:
            if args[0] in ['信用貸款', '信貸']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[信用貸款]在防制洗錢及打擊資恐[相關][法規][會]有什麼[措施]呢":
        if CHATBOT_MODE:
            if args[0] in ['信用貸款', '信貸']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[信用貸款]撥款[前][銀行][會][再次]查[我]的聯徵[資料]嗎":
        if CHATBOT_MODE:
            if args[0] in ['信用貸款', '信貸']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[信用貸款]繳款完畢[後][可以]申請結清證明嗎":
        if CHATBOT_MODE:
            if args[0] in ['信用貸款', '信貸']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[信用貸款契約][中]貸款[費用][會]收取幾[筆]":
        if CHATBOT_MODE:
            if '信貸' or '信用貸款' in args[0] and '費' in args[2] and args[4] in ['筆', '次']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[個人信貸]利率最低為多少":
        if CHATBOT_MODE:
            if args[0] in ['個人信貸', '信貸']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[個人信貸][期]限[最長]多[久]":
        if CHATBOT_MODE:
            if args[0] == '個人信貸' and args[2] in ['最長', '最久', '最晚']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[個人信貸]是什麼":
        if CHATBOT_MODE:
            if args[0] in userDefinedDICT['loan']:
                resultDICT["response"] = getResponse("什麼是[{}]".format(args[0]), args)
        else:
            pass

    if utterance == "[個人信貸][最高][可以]貸多少":
        if CHATBOT_MODE:
            if args[0] == '個人信貸' and args[1] in ['最多', '最高']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[個人信貸]需要[費用]嗎":
        if CHATBOT_MODE:
            if args[0] == '個人信貸' and '費' in args[1]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[僅]由非原就讀[學校]頒發[文憑][是]否[可]申貸[留學貸款]":
        if CHATBOT_MODE:
            if '學貸' in args[5]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[可][否]以[有條件式入學許可]([conditional offer])申請本貸款":
        if CHATBOT_MODE:
            if args[2].lower().strip(' ') and args[3].lower().strip(' ') in ['有條件式入學許可', 'conditional offer']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[可][否]以[有條件式入學許可]申請本貸款":
        if CHATBOT_MODE:
            if args[2].lower().strip(' ') in ['有條件式入學許可', 'conditional offer']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[可以]提[前]償還[個人信貸][全部]本金嗎":
        if CHATBOT_MODE:
            if args[2] in ['個人信貸', '個人信用貸款'] and args[3] == '全部':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[可以]提[前]償還[個人信貸][部分]本金嗎":
        if CHATBOT_MODE:
            if args[2] in ['個人信貸', '個人信用貸款'] and args[3] == '部分':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[可以]提[前]償還[個人信貸][部分]或[全部]本金嗎":
        if CHATBOT_MODE:
            if args[2] in ['個人信貸', '個人信用貸款']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[家屬][可][否]代為申請[所得清單]":
        if CHATBOT_MODE:
            if '家' in args[0] and '所得' or '紀錄' in args[3]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[家屬][可][否]代為申請[所得清單]及[留學生]入出國[紀錄文件]":
        if CHATBOT_MODE:
            if '家' in args[0] and ('所得' or '紀錄' in args[3]) and ('所得' or '紀錄' in args[5]):
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[家屬][可][否]代為申請入出國[紀錄文件]":
        if CHATBOT_MODE:
            if '家' in args[0] and args[3].startswith('紀錄'):
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[成績單]如何繳交":
        if CHATBOT_MODE:
            if args[0] == '成績單':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[成績單]需於[每年幾月]繳交":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[我][可以]指定[我]的繳款[日期]嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[我]符合申請[個人信貸][資格]嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[房屋]貸款[期間][是]否[可以][部分]還款":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[房貸]簽約時需要攜帶哪些[資料]":
        if CHATBOT_MODE:
            if args[0] in ['房貸']:
                resultDICT["response"] = getResponse(utterance, args)
            elif args[0] in ['信貸', '信用貸款']:
                resultDICT["response"] = getResponse("[信貸]簽約時需要攜帶哪些[資料]", args)
        else:
            pass

    if utterance == "[所得]不需報稅需檢附何[種][文件]認定[其][家庭][年]收入":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[所得清單][應]如何辦理":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[指數型房貸]有什麼[優點]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "教育部採認規定之[國][外][大學][校院]為何":
        if CHATBOT_MODE:
            if args[0] in ['國', '境'] and args[1] == '外' and args[2] == '大學':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "[月繳月省房貸]的[利率]減碼[優惠][是]否適用於[政策][性]貸款":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[理財型房貸]的[利息][費用]如何計算":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[理財型房貸]要如何動用[資金]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[留學貸款][分期]撥貸[方式]為何":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[留學貸款][應]於何時償還":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[留學貸款][期][限]為何":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[留學貸款][額度]及[分期]撥貸[方式]為何":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[留學貸款]之[利息][應該]如何繳交":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[留學貸款]之[利息][應該]如何還款":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[留學貸款]之[利息]及[本金][應該]如何繳交及還款":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[留學貸款]的[申請人][是]否需要[保證人]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[留學貸款]的[申請人]為何及[是]否需要[保證人]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[留學貸款]的[申請人]為何需要[保證人]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[薪水][多寡]跟[可以]核貸的[額度]有關嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "[遠距]教學之[學位][是]否[可]申貸[留學貸款]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "什麼是[提前清償違約金]":
        if CHATBOT_MODE:
            if args[0] in userDefinedDICT['loan']:
                resultDICT["response"] = getResponse("什麼是[{}]".format(args[0]), args)
        else:
            pass

    if utterance == "何處[可]查詢[國外][大專][院][校]參考[名冊]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "使用[MyData]服務取得[相關][財證]時若發生[系統][異常]導至無法授權或授權[失敗][該]怎麼辦":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "使用[MyData]服務提供[玉山銀行]取用[個人][資料][可]在哪裡查詢[相關][紀錄]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "依[信用貸款契約]在什麼[情形][下][會]縮短[我]的借款[期限]呢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "入出國[紀錄文件][應]如何辦理":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "在[薪]轉[銀行]申請貸款[個人信貸][會]比較容易過[件]嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "多[久][可以]收到貸款[契約]呢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何使用[玉山銀行][IXML]":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[1].lower().strip(' ') == 'ixml':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "如何申請[玉山銀行][IXML]":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[1].lower().strip(' ') == 'ixml':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass
        
    if utterance == "如何申請/使用[玉山銀行][IXML]":
        if CHATBOT_MODE:
            if '玉山' in args[0] and args[1].lower().strip(' ') == 'ixml':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass
        
    if utterance == "如何知道[我]的[個人信貸][每月][應該]繳款的[金額]是多少":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如何透過[MyData]服務[將][個人][資料]給[玉山銀行]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "如果提[前]清償貸款有無違約[金]":
        if CHATBOT_MODE:
            if args[0] == '前':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "工作建議[滿]多[久][後]再申請貸款對[我][會]比較有利":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "已[先]申請到[留學貸款][者][是]否[可以]報考或申請[我][國][政府]提供之各項[公費]或留學[獎助學金]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "所修讀之[學校][學位]需較長[時間][可][否]延長[寬限期]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "所修讀之[學校][學位]需較長[時間][可][否]延長還款[期限]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "找[代辦公司]協助辦理貸款[利率][會]比較好嗎":
        if CHATBOT_MODE:
            if args[0] == '代辦公司':
                if args[1] == '利率':
                    resultDICT["response"] = getResponse(utterance, args)
                elif args[1] == '額度':
                    resultDICT["response"] = getResponse("找[代辦公司]協助辦理貸款[額度][會][比較高]嗎", args)
        else:
            pass

    if utterance == "找[代辦公司]協助辦理貸款[額度][會][比較高]嗎":
        if CHATBOT_MODE:
            if args[0] == '代辦公司' and args[1] in ['額度', '利率']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "找[代辦公司]協助辦理貸款[額度][會][比較高]或[利率][會]比較好嗎":
        if CHATBOT_MODE:
            if args[0] == '代辦公司' and args[1] and args[4] in ['額度','利率']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "沒收到[MyData][平台]與[玉山]取檔[成功]的[簡訊]通知卻收到補件通知":
        if CHATBOT_MODE:
            if args[0].lower().strip(' ') in ['my data', 'mydata'] and '玉山' in args[2]:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "申請[個人信貸][後]需要多[久][能]知道貸款[結果]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "申請[房屋貸款]需要準備哪些[資料]":
        if CHATBOT_MODE:
            if args[0] in ['房屋貸款', '房貸']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "申請[留學貸款][應]檢附哪些[文件]":
        if CHATBOT_MODE:
            if args[0] in ['房屋貸款', '房貸']:
                resultDICT["response"] = getResponse("申請[房屋貸款][應]檢附哪些[資料]", args)
            elif args[0] in ['留學貸款']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "申請留學貸款之[資格]":
        if CHATBOT_MODE:
            if args[0] == '資格':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "申請[留學貸款]所訂之[家庭][年]收入[標準]如何認定":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "申請[留學貸款]所訂之[家庭][年]收入[標準]為何":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "若留學生在[國][外][可][否]委託[國內]之[人]代為申請":
        if CHATBOT_MODE:
            if args[0] in ['國', '境'] and args[1] == '外' and args[4] == '國內':
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "返國[後]無法[立即]償還貸款[是]否[可]申請[暫][緩]攤還[本息]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "退學[應]如何還款":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "逾期未還款[者][會]有什麼[不良][後果]":
        if CHATBOT_MODE:
            if args[3] in ['後果', '下場', '責任', '問題']:
                resultDICT["response"] = getResponse(utterance, args)
        else:
            pass

    if utterance == "降息對[我]的貸款有甚麼影響":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            pass
        
    return resultDICT