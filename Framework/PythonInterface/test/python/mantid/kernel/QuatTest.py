# Mantid Repository : https://github.com/mantidproject/mantid
#
# Copyright &copy; 2018 ISIS Rutherford Appleton Laboratory UKRI,
#   NScD Oak Ridge National Laboratory, European Spallation Source,
#   Institut Laue - Langevin & CSNS, Institute of High Energy Physics, CAS
# SPDX - License - Identifier: GPL - 3.0 +
import unittest
import math

from mantid.kernel import Quat, V3D


class QuatTest(unittest.TestCase):

    def test_empty_constructor(self):
        q = Quat()
        self.assertEqual(q[0],1.0);
        self.assertEqual(q[1],0.0);
        self.assertEqual(q[2],0.0);
        self.assertEqual(q[3],0.0);

    def test_value_constructor(self):
        q = Quat(1,2,3,4)
        self.assertEqual(q[0],1.0)
        self.assertEqual(q[1],2.0)
        self.assertEqual(q[2],3.0)
        self.assertEqual(q[3],4.0)

    def test_angle_axis_constructor(self):
        v = V3D(1,1,1);
        # Construct quaternion to represent rotation
        # of 45 degrees around the 111 axis.
        q = Quat(90.0, v)
        c = 1.0/math.sqrt(2.0)
        s = c/math.sqrt(3.0)
        self.assertAlmostEqual(q[0],c,)
        self.assertAlmostEqual(q[1],s)
        self.assertAlmostEqual(q[2],s)
        self.assertAlmostEqual(q[3],s)

    def test_index_operator(self):
        q = Quat(2,3,4,5)
        self.assertEqual(q[0],2.0);
        self.assertEqual(q[1],3.0);
        self.assertEqual(q[2],4.0);
        self.assertEqual(q[3],5.0);

    def test_len(self):
        q = Quat(1,2,3,4);
        self.assertAlmostEqual(q.len(),math.sqrt(30.0))

    def test_len2(self):
        q = Quat(1,2,3,4);
        self.assertAlmostEqual(q.len2(),30.0)

    def test_rotate(self):
        a = math.sqrt(2.0)/2.0
        #Trivial
        p = Quat(1,0,0,0) #Identity quaternion
        v = V3D(1,0,0)
        orig_v = v;
        p.rotate(v);
        self.assertEqual(orig_v,v)
        # Now do more angles
        v = V3D(1,0,0);
        p = Quat(90., V3D(0,1,0)); #90 degrees, right-handed, around y
        p.rotate(v);
        self.assertEqual(v, V3D(0,0,-1))

        v = V3D(1,0,0);
        p = Quat(45., V3D(0,0,1))
        p.rotate(v);
        self.assertEqual(v, V3D(a, a, 0))

if __name__ == '__main__':
    unittest.main()
