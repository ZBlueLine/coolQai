# -*- coding:utf-8 -*-

import cqplus
import random

def strpp(len1,len2, s1, s2):
    flag = 0
    for i in range(len1):
        ti = i
        if flag == 1:
            break
        for j in range(len2):
            if s1[ti] != s2[j]:
                break
            else:
                ti += 1
            if j == len2-1:
                flag = 1
                break
            if i == len1:
                break
    if flag == 1:
        return True
    else:
        return False

def strdel(len1,len2, s1, s2):
    flag = 0
    ans = ''
    i = 0
    while i < len1:
        if flag == 1:
            i = ti
            flag = 0
        else:
            ti = i
        if i == len1:
            break
        for j in range(len2):
            if s1[ti] != s2[j]:
                break
            else:
                ti += 1
            if j == len2-1:
                flag = 1
                break
            if i == len1:
                break
        if flag == 0:
            ans += s1[i]
        i += 1
    return ans

class cntans:
    def Fdans(self, aimstr):
        Maxnum = 0.4
        ans = list()
        for line in open("ans.txt"):
            nownum = 0
            tstr = line.strip('\n')
            tstr = tstr.split('-')
            length = len(tstr[0])
            cnlength = (len(tstr[0].encode())-len(tstr[0]))//2
            cnlength2 = (len(aimstr.encode())-len(aimstr))//2
            j = 0
            for i in aimstr:
                if j >= length:
                    break
                while i != tstr[0][j]:
                    j += 1
                    if j >= length:
                        break
                if j < length and i == tstr[0][j]:
                    nownum += 1
            if cnlength == 0:
                value = -100
            else:
                value = nownum/cnlength
            if value >= Maxnum and abs(cnlength - cnlength2) < 4:
                ans.append(tstr[1])
        if len(ans):
            return random.choice(ans)
        else:
            return ''

    def judge(self):
         with open("ans.txt", 'rb') as f:  # 打开文件
            f.seek(-1, 2)  
            lines = f.readlines()
            flag = lines[-1].decode() 
            if flag == '-':
                return True
            else:
                return False
    def write(self, msg, v):
        if(v == 1):
            with open("ans.txt", 'a') as f:  # 打开文件
                f.write(msg + "\n")
        else:
            length = len(msg)
            if length == 0:
                return
            with open("ans.txt", 'a') as f:  # 打开文件
                msg+='-'
                f.write(msg)

class MainHandler(cqplus.CQPlusHandler):
    def handle_event(self, event, params):
        if event == "on_group_msg" and (params['from_group'] == 759632530 or params['from_group'] == 112731254): # and (params['from_group'] == 112731254 or params['from_group'] == 759632530): # 759632530
            a = "[CQ:at,qq=1026393085]"
            b = params['msg']
            len1 = len(a)
            len2 = len(b)
            if strpp(len2, len1, b, a):
                b = strdel(len2, len1, b, a)
            solve = cntans()
            ans = solve.Fdans(b)
            if solve.judge():
                image = "CQ:image"
                if not strpp(len(params['msg']), 8, params['msg'], image):
                    solve.write(b, 1)
                    solve.write(ans, 2)
            else:
                solve.write(ans, 2)
            self.api.send_group_msg(params['from_group'], ans)
        if event == "on_private_msg":
            self.api.send_private_msg(3246327557, "来自"+' '+str(params['from_qq'])+"的消息："+params['msg'])
            




            """
            length = len(params['msg'])
            # self.api.send_group_msg(params['from_group'], "收到了")  
            if strpp(length, length2, params['msg'], name): 
                # self.api.send_group_msg(params['from_group'], params['from_group']) 用于获取群号
                image = "CQ:image"
                if strpp(length, 8, params['msg'], image):
                    self.api.send_group_msg(params['from_group'], "发你妈的图，老子看不到")    
                else:
                    msg = strdel(length, length2, params['msg'], name)
                    self.api.send_group_msg(params['from_group'], msg)    
                # self.api.send_group_msg(params['from_group'], params['msg'][i])
                # msg = '[CQ:at,qq=' + str(params['from_qq']) + ']' + params['msg']
                # self.api.send_group_msg(params['from_group'], msg)
            """