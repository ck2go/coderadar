from __future__ import absolute_import

from ..pytest import CoverageReport

def test_tests():
    assert True

def test_CoverageReport():
    my_report = CoverageReport()
    assert isinstance(my_report, CoverageReport)
