import os, sys
import pytest
import logging
import subprocess
import xlrd
import math

sys.path.append("../findCPcore/")

from CobraMetabolicModel import CobraMetabolicModel

LOGGER     = logging.getLogger(__name__)
LOGGER_MSG = "Executing cli file: {} {}"

TEST_MODEL = "data/MODEL1108160000_url.xml"


"""
    Check that dead reactions have flux <closer> to zero.
"""
#@pytest.mark.skip(reason="")
def test_verbose_output_on_model():
    model = CobraMetabolicModel(TEST_MODEL)
    EPSILON = model.epsilon()

    model.fva(update_flux = True)
    
    for r in model.dead_reactions():
        assert(EPSILON > abs(r.upper_bound))
