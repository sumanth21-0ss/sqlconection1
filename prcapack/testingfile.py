import pytest
import pandas as pd
from pytest_html import extras
import MyConnector
import jinja2
import dataframe_image as dfi
from docx import Document


def test_1(fix1,extra):
    extra.append(extras.html("<img src='C:/Users/922619/PycharmProjects/sqlconection/prac/ab.png'/>"))
    assert fix1==39

def test_2(fix2):
    assert fix2==25

@pytest.mark.parametrize("a,b,c",[(1,2,3),(2,4,7)])
def test_3(a,b,c):
    assert a+b==c

def test_4(extra):
    finaldf=MyConnector.db_data()
    link=3
    dfi.export(finaldf,"C:/Users/922619/PycharmProjects/sqlconection/prcapack/reports/df.png")
    img="<a href=C:/Users/922619/PycharmProjects/sqlconection/prcapack/reports/df.png>"+ str(link) + "</a>"
    extra.append((extras.html(img)))
    doc=Document()
    doc.add_picture('C:/Users/922619/PycharmProjects/sqlconection/prcapack/reports/df.png')
    doc.save('images.docx')
    #extra.append((extras.
    #extra.append(extras.html())

    assert True











