# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 12:32:07 2021

@author: kater
"""

os.chdir('C:\Users\kater\Dropbox\PhD\Frictionless Data Fellowship')
from frictionless import extract

! frictionless describe datapackage-subset/16-11-20_correlational_fordatapackage.csv

! frictionless extract datapackage-subset/16-11-20_correlational_fordatapackage.csv

! frictionless validate datapackage-subset/16-11-20_correlational_fordatapackage.csv