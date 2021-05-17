""" mockup 1D example with a custom postprocessor """
from profit.run import Postprocessor

import numpy as np


@Postprocessor.register('mockup')
class MockupPostprocessor(Postprocessor):
    """ almost identical copy of NumpytxtPostprocessor """
    def post(self, data):
        raw = np.loadtxt('mockup.out')
        data['f'] = raw

    @classmethod
    def handle_config(cls, config, base_config):
        pass