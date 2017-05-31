# -*- coding: utf-8 -*-
"""
Created on Wed May 31 23:01:49 2017

@author: Fantasia
"""
import re
def kong(exp):
    for cha in exp:
        if(cha=='(' or cha==')' or cha=='[' or cha==']'):
            exp=exp.replace(cha," "+cha+" ")
    return exp
def token(exp):
    exp=kong(exp).split()
    return exp
def findp(lis,i):#支持两种括号
    i+=1
    a=0
    while i<=len(lis)-1:
        if lis[i]=="(" or lis[i]=='[':
            a+=1
            i+=1
        elif lis[i]==")" or lis[i]==']':
            if a==0:
                break
            elif a!=0:
                a-=1
                i+=1
        else:
            i+=1
    return i
def parse(exp):
    def atom(exp):
        if len(exp)==1:
            return True
    if atom(exp):
        return exp
    elif(exp==[]):
        return []
    elif(exp[0]=="(" or exp[0]=="["):
        sexp=exp[1:findp(exp,0)]
        return [parse(sexp)]+parse(exp[findp(exp,0)+1:])
    elif(exp[0]!="(" or exp[0]!="["):
        return [exp[0]]+parse(exp[1:])
def parser(exp):
        return parse(exp)[0]
def is_num(str):
    p="(\\-)?[0-9]+(//.)?[0-9]*"#支持小数和负数
    if re.search(p,str):
        return True
    elif str.isdigit():
        return True
    else:
        return False
def is_self_eval(ir):#还只有数字和布尔值
    return (type(ir)==str and (is_num(ir) or ir=="True" or ir=="False" or ir[0]==ir[-1]=="'"))
def is_application(ir):#这种粗糙的判法必须要放到evall的最后，不然误判
    return (len(ir)!=1)
def is_definition(ir):
    return (ir[0]=="define")
def is_variable(ir):
    return (type(ir)==str and (not is_self_eval(ir)))
def is_lambda(ir):
    return (ir[0]=="lambda")
def is_pri_pro(procedure):
    return (not is_com_pro(procedure))
def is_com_pro(procedure):
    return (type(procedure)==list)
def is_if(ir):
    return (ir[0]=='if')
def is_cond(ir):
    return (ir[0]=="cond")
def is_quote(ir):
    return (ir[0]=="quote")
def is_setq(ir):
    return (ir[0]=="set!")
def is_eval(ir):
    return (ir[0]=="eval")
def is_apply(ir):
    return (ir[0]=="apply")
def is_begin(ir):
    return ir[0]=='begin'
def comp_self(ir):
    return ir
def comp_variable(ir):
    return ir[0]
def lis_to_args(lis):
    if lis==[]:
        return ""
    elif len(lis)==1:
        return lis[0]
    else:
        return lis[0]+","+lis_to_args(lis[1:])

def comp_lambda(ir):
    return "function"+"("+lis_to_args(ir[1])+")"+"{return "+compilee(ir[2])+";}"
def comp_application(ir):
    return ir[0]+"("+lis_to_args(map(compilee,ir[1:]))+")"
def comp_definition(ir):
    def make_lambda(s,body):
        return ['lambda',s[1:],body]
    if(type(ir[1])==str):
        return "var "+ir[1]+"="+compilee(ir[2])+";"
    elif(type(ir[1])==list):
        return "var "+ir[1][0]+"="+compilee(make_lambda(ir[1],ir[2]))+";"
def compilee(ir):
    if(is_self_eval(ir)):
        return comp_self(ir)
    elif(is_definition(ir)):
        return comp_definition(ir)
    elif(is_lambda(ir)):
        return comp_lambda(ir)
    elif(is_variable(ir)):
        return comp_variable(ir)
    elif(is_begin(ir)):
        return eval_begin(ir)
    elif(is_if(ir)):
        return comp_if(ir)
    elif(is_cond(ir)):
        return comp_cond(ir)
    elif(is_quote(ir)):
        return comp_tuple(ir)
    elif(is_setq(ir)):
        return comp_setq(ir)
    elif(is_eval(ir)):
        return comp_eval(ir)
    elif(is_apply(ir)):
        return comp_apply(ir)
    elif(is_application(ir)):
        return comp_application(ir)
def compiler(exp):
    return compilee(parser(token(exp)))

    
