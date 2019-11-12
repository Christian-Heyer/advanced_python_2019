import pytest
import sys, os
# This block is not neccessary if you instaled your package
# using e.g. pip install -e
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), # location of this file
            os.pardir, # and one level up, in linux ../
        )
    )
)
# EOBlock

import playground

def test_find_peaks():
    peaks = playground.core.find_peaks([0, 2, 1])
    assert peaks == [2]  
    
def test_find_two_peaks():
    peaks = playground.core.find_peaks([0, 2, 1, 0, 2, 1])
    assert peaks == [2, 2] 

def test_find_peaks_max_edge():
    peaks = playground.core.find_peaks([2, 1, 1])
    assert peaks == [] 
    
def test_find_peaks_empty_list():
    peaks = playground.core.find_peaks([])
    assert peaks == [] 

def test_color_peak():
    peaks = playground.core.find_color_peaks([[0,20,0],[0,19,0],[0,20,0]], False)
    assert peaks == [19]
def test_color_max():
    peaks = playground.core.find_color_peaks([[10,10,10],[5,25,30],[16,0,3]])
    assert peaks == [60]
