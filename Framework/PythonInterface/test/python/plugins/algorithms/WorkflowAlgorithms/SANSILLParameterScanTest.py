# Mantid Repository : https://github.com/mantidproject/mantid
#
# Copyright &copy; 2018 ISIS Rutherford Appleton Laboratory UKRI,
#     NScD Oak Ridge National Laboratory, European Spallation Source
#     & Institut Laue - Langevin
# SPDX - License - Identifier: GPL - 3.0 +
import unittest

from mantid.api import MatrixWorkspace, WorkspaceGroup
from mantid.simpleapi import SANSILLParameterScan, config, mtd


class SANSILLParameterScanTest(unittest.TestCase):

    _facility = None

    def setUp(self):
        self._facility = config['default.facility']
        self._data_search_dirs = config.getDataSearchDirs()
        config.appendDataSearchSubDir('ILL/D16/')
        config.setFacility("ILL")

    def tearDown(self):
        config.setFacility(self._facility)
        config.setDataSearchDirs(self._data_search_dirs)
        mtd.clear()

    def test_D16_omega(self):
        SANSILLParameterScan(SampleRun="066321.nxs",
                             OutputWorkspace="output2d",
                             OutputJoinedWorkspace="reduced",
                             Observable="Omega.value",
                             PixelYmin=3,
                             PixelYMax=189)
        self._check_output(mtd["output2d"], 6)
        self.assertTrue(mtd["reduced"])

    def _check_output(self, ws, spectra=1):
        self.assertTrue(ws)
        self.assertTrue(isinstance(ws, MatrixWorkspace))
        self.assertEqual(str(ws.getAxis(0).getUnit().symbol()), "degrees")
        self.assertEqual(ws.getAxis(0).getUnit().caption(), "Scattering angle")
        self.assertEqual(str(ws.getAxis(1).getUnit().symbol()), "degrees")
        self.assertEqual(ws.getAxis(1).getUnit().caption(), "Omega.value")
        self.assertAlmostEqual(ws.getAxis(1).getValue(0), 5.2, delta=3)
        self.assertAlmostEqual(ws.getAxis(1).getValue(1), 5.4, delta=3)
        self.assertEqual(ws.getNumberHistograms(), spectra)
        self.assertTrue(ws.getInstrument())
        self.assertTrue(ws.getRun())
        self.assertTrue(ws.getHistory())
        self.assertTrue(ws.blocksize(), 1152)
        self.assertTrue(not ws.isHistogramData())
        self.assertTrue(not ws.isDistribution())


if __name__ == '__main__':
    unittest.main()
