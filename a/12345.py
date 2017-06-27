#-*- coding: utf-8 -*-
'''
Created on 2017/06/27

@author: kaneda-kazutomo
'''

if __name__ == '__main__':
    import sys
    import zenhan
    line = sys.stdin.readline()
    a = line.split("　")
    sa = a[0]
    sb = a[1]
    if isinstance(sa, str):
        sa = sa.decode('utf-8')
    if isinstance(sb, str):
        sb = sb.decode('utf-8')
    string1 = zenhan.z2h(sa)
    string2 = zenhan.z2h(sb)
    string2a = string2.rstrip("\r\n")
    n1 = len(a[0])/3
    n2 = len(a[1])/3
    s1 = str(n1)
    s2 = str(n2)
    total = "{\"" + string1 + "\":" + s1 + ",\"" + string2a + "\":" + s2 + "}"
    print total