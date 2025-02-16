# Mantid Repository : https://github.com/mantidproject/mantid
#
# Copyright &copy; 2018 ISIS Rutherford Appleton Laboratory UKRI,
#   NScD Oak Ridge National Laboratory, European Spallation Source,
#   Institut Laue - Langevin & CSNS, Institute of High Energy Physics, CAS
# SPDX - License - Identifier: GPL - 3.0 +
import unittest
from mantid import simpleapi


class CheckForSampleLogsTest(unittest.TestCase):
    def test_simple(self):
        w = simpleapi.Load('CNCS_7860_event.nxs')
        result = simpleapi.CheckForSampleLogs(w)
        self.assertEqual(result, '')
        result = simpleapi.CheckForSampleLogs(w, 'Phase1')
        self.assertEqual(result, '')
        result = simpleapi.CheckForSampleLogs(w, 'Phrase1')
        self.assertNotEqual(result, '')


if __name__=="__main__":
    unittest.main()
