#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 15:58:54 2018

@author: descentis
"""

import xml.etree.cElementTree as ET

file = ET.parse('IIT/wiki_data/IIT.kml')
root = file.getroot()