
import pytest
import datetime
import os
import sys
from pathlib import Path
from pytest_html import extras



@pytest.fixture
def fix1():
   input = 39
   return input


@pytest.fixture
def fix2():
   input = 40
   return input

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    #script_name = os.path.splitext(os.path.basename('C:/Users/922619/PycharmProjects/sqlconection/prcapack'.get_path_executed_script()))[0]
    #scpath=sys.executable
    rdate=str(datetime.datetime.now().strftime('%Y-%m-%d %Hh%Mm%Ss'))
    if not os.path.exists('reports'):
       os.makedirs('reports')
    config.option.htmlpath = 'reports/'+ 'report__' + ".html"

    #config.option.self_contained_html = True

@pytest.mark.optionalhook
def pytest_metadata(metadata):
   # metadata.pop("JAVA_HOME",None)
    metadata["env"]=os.getenv("env")
