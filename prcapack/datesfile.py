import datetime as dt
import pandas as pd


def date():
    a=pd.Timestamp("2022/05/09")
    b=a-pd.offsets.MonthBegin(1)
    c=a+pd.offsets.MonthBegin(1)
    d = a - pd.offsets.MonthEnd(1)
    e = a + pd.offsets.MonthEnd(1)
    f=pd.offsets.MonthEnd(1)
    g=pd.offsets.MonthBegin(1)

    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)


date()

