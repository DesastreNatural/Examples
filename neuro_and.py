#! /usr/bin/python
##neuro_and.py##
#Released under GNU General Public License v2.0 or higher

import random

threshold=0.2
learning_rate=0.1

def chopfloat(x):
    return float((repr(x)[0:repr(x).find(".")])+(repr(x)[repr(x).find("."):repr(x).find(".")+3]))

def synaptic_act(x):
    return (x-threshold)

def create_data(x=100):
    a,b,res=[],[],[]
    for i in xrange(x):
        d=random.randint(0,1)
        e=random.randint(0,1)
        a.append(d)
        b.append(e)
        res.append(d and e)
    return a,b,res

def calculateout(wn,dn):
    res=0
    for i in xrange(len(wn)):
        res=res+(wn[i]*dn[i])
    return synaptic_act(res)

def train(wn,dn,exp_out):
    out=calculateout(wn,dn)
    res=[]
    #print "Error Value:[",(exp_out-out),"]"
    for i in xrange(len(wn)):
        res.append(wn[i]+(learning_rate*(chopfloat((exp_out-out)*dn[i]))))
    return res
def test(n=10):
    a,b,c=create_data(350)
    wn=[]
    #inizializzazione
    for i in xrange(2):
        wn.append(chopfloat(random.randint(-10,10)+random.random()))
    #addestramento
    print "Training..."
    for i in xrange(len(a)):
        wn=train(wn,[a[i],b[i]],c[i])
    #prova
    print "Test:"
    a,b,c=create_data(n)
    numerr=0
    for i in xrange(len(a)):
        if round(calculateout(wn,[a[i],b[i]]))!=c[i]:
            numerr=numerr+1
        print a[i],"&&",b[i],"=",c[i]," <==> ",abs(round(calculateout(wn,[a[i],b[i]]))),"[ True Value:", (calculateout(wn,[a[i],b[i]]))," ]"," [ Error Value: ",(c[i]-calculateout(wn,[a[i],b[i]]))," ]"
    return numerr

test()
