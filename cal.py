# -*- coding: cp936 -*-

"""
@author Edwin
"""

#list_diff��list_intersect��һ���൱����ĺ�����ƣ��ҽ����������ϵ����ǵ�cal.py���档
#list_diff��ʾ�����б���
#list_intersect��ʾ�����б��󲢼�
#ע����ǣ�list��û��ȥ�أ��ٸ����ӣ�[1, 1, 1, 2] - [1, 1, 2] = [1]
#������ǲ�ȡȥ�صĴ�ʩ����ô������ԭ������Ʒ���:
# set(a).intersect(set(b)) �������� [1, 1, 1, 2] - [1, 1, 2] = [1, 2] - [1, 2] = []
# �������Ԫ�ؼ��ϵĲ ����palie_listc�ܹ������ظ�Ԫ�ص�ԭ��֮һ��
#��Ȼ�ˣ�����Ԫ�ؾ�û�в����������ˣ�
#��Ϊ�䲢����
#��Ϊֻ�� alist+blist����

# @note apply a functor on tupleA and tupleB
def tpFun(atuple, btuple, fun):
    return fun(atuple, btuple)

# @note Get the intersection of DictA and DictB
# @attention dtInt([1, 1, 1, 2], [1, 1, 2]) = [1]
def dtInt(adict, bdict, fun):
    cdict = {}
    for i, v in enumerate(adict):
        bv = bdict.get(i)
        if (bv != None):
            cdict[i] = fun(v, bv)
    return cdict

#def dict_combine(adict, bdict, fun):
def dtCom(adict, bdict, fun):
    for i, v in enumerate(adict):
        bv = bdict.get(i)
        if (bv != None):
            adict[i] = fun(v, bv)

#def dict_union(adict, bdict, fun):
def dtUnion(adict, bdict, fun):
    s = set(adict.keys()) | set(bdict.keys())
    cdict = dict()
    for i in s:
        a = adict.get(i)
        b = bdict.get(i)
        if (a == None): cdict[i] = b
        else:
            if (b == None): cdict[i] = a
            else: cdict[i] = fun(a, b)
    return cdict

def slMerge(alist, blist, cmpbool):
    ita = iter(alist)
    itb = iter(blist)
    an, bn = map(len, (alist, blist))
    ai, bi = 0, 0
    clist = []
    while (ai < an)and(bi < bn):
        if (cmpbool(alist[ai], blist[bi])):
            clist.append(alist[ai])
            ai += 1
        else:
            clist.append(blist[bi])
            bi += 1
    if (ai == 0):
        clist += blist[bi:]
    else: clist += alist[ai:]
    return clist

def lMerge(alist, blist, cmpbool):
    c = alist+blist
    print c
    #c.sort(cmpbool)
    c.sort()
    print c
    return c

#def sortedlist_intersect(alist, blist)
def slInt(alist, blist):
    j, n = 0, len(blist)
    ans = []
    try:
        for i, v in enumerate(alist):
            while blist[j] < v: j += 1
            if blist[j] == v:
               j += 1
               ans.append(v)
    except IndexError:
        pass
    finally:
        return ans

#def sortedlist_difference(alist, blist):
def slDiff(alist, blist): 
    j, n = 0, len(blist)
    ans = []
    for i, v in enumerate(alist):
        while (j<n)and(blist[j] < v): j += 1
        if (j<n) and (blist[j] == v):
            j += 1
        else:
            ans.append(v)
    return ans

# list��intersect
#def list_intersect(alist, blist):
def lInt(alist, blist):
    return slInt(sorted(alist), sorted(blist))

# list��diff
#def list_diff(alist, blist):
def lDiff(alist, blist):
    return slDiff(sorted(alist), sorted(blist))

# ��������Ҫ��alist+blist������ (alist+blist).sort()
#def list_union(alist, blist):

###################### Test Code ############################
import unittest, random, copy

class ListOperatorTestCase(unittest.TestCase):
    def setUp(self):
        self.lista = range(0, 100, 3)
        self.listb = range(0, 100, 7)
        import random
        return
    def tearDown(self):
        return
    def testListIntersection(self):
        map(random.shuffle, (self.lista, self.listb))
        self.listc = lInt(self.lista, self.listb)
        tmp = filter(lambda a:(a % 21 == 0), self.listc)
        self.assertEqual(self.listc, tmp)
        
    def testListDiff(self):
    #    print self.lista
        self.listc = lDiff(self.lista, self.listb)
        try:
            for i in self.listc:
                self.assertTrue((i % 3 == 0) and (i % 7 != 0))
        except AssertionError:
            print "Wrong", i  

########################################################
########################################################
########################################################

### ���������һ��ջ����ջ�ܹ���O(1)��ʱ�䷵��һ����ֵ��Ĭ�����ֵ��

import operator
class bestStack(): 
    def __init__(self, alist=[], op=operator.gt):
        self.data = list()
        self.max = list([None])
        self.op = op
        for i in alist:
            self.push(i)
    def pop(self):
        self.max.pop()
        return self.data.pop()
    def best(self):
        return self.max[-1]
    def push(self, elem):
        if (self.max[-1]!=None)and(self.op(self.max[-1], elem)):
            self.max.append(self.max[-1])
        else: self.max.append(elem)
        self.data.append(elem)
    def __str__(self):
        return self.data.__str__()

import unittest
class BestStackTest(unittest.TestCase):
    def setUp(self):
        return
    def tearDown(self):
        return
    def testFun(self):
        s = bestStack()
        for i in xrange(3, 11, 3):
            s.push(i)
        for i in xrange(9, 2, -3):
            self.assertEqual(s.best(), i)
            self.assertEqual(s.pop(), i)
    def testFun1(self):
        s = bestStack([3, 6, 9], operator.gt)
        for i in xrange(9, 2, -3):
            self.assertEqual(s.best(), i)
            self.assertEqual(s.pop(), i)
    def testFun2(self):
        s = bestStack([3, 6, 9, 6, 11], operator.gt)
        self.assertEqual(s.best(), 11)
        s.pop(), self.assertEqual(s.best(), 9)
        s.pop(), self.assertEqual(s.best(), 9)
        s.pop(), self.assertEqual(s.best(), 6)
        s.pop(), self.assertEqual(s.best(), 3)
    
########################################################
########################################################
########################################################

def A(n, r):
    ans = 1
    for i in range(n-r+1, n+1):
        ans *= i
    return ans

def C(n, r):
    ans = 1
    for i in xrange(n-r+1, n+1):
        ans *= i
    for i in xrange(1, r+1):
        ans /= i
    return ans

def fac(n):
    ans = n
    for i in xrange(1, n):
        ans *= i
    return ans

import math
def ln(n):    
    return math.log(n)

########################################################
########################################################
########################################################


def calFileHash(filepath, hash_object=hashlib.sha1()):
    with open(filepath, 'rb') as f:
        hash_object.update(f.read())
        hashcode = hash_object.hexdigest()
        return hashcode

class Acc():
    def __init__(self):
        self.alist = list()
    def add(self, num):
        self.alist.append(num)
    def dlt(self, num):
        self.alist.remove(num)
    def dlt(self):
        self.alist.pop()
    def gsum(self):
        return sum(self.alist)
    def gavg(self):
        return sum(self.alist)+0.0 / len(self.alist)

 
        

if __name__ == "__main__":

    
    l1 = """
    acc = Acc()
    for i in xrange(10):
        acc.add(i)
    print acc.gsum(), acc.gavg()
    """

    a = unittest.main(exit=False)
    #print a.result
    

