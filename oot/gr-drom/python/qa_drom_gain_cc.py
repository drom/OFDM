#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018 drom.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

from gnuradio import gr, gr_unittest
from gnuradio import blocks
import drom_swig as drom

class qa_drom_gain_cc (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_drom_gain_cc (self):
        src_data = (-2 + 1j, 1 + 3j, 7 - 2j, 0 - 3j, 1 + 1j, 1 + 3j)
        expected_result = (-4 + 2j, 2 + 6j, 14 - 4j, 0 - 6j)
        src = blocks.vector_source_c(src_data)
        dut = drom.drom_gain_cc(2, 2)
        dst = blocks.vector_sink_c()
        self.tb.connect(src, dut)
        self.tb.connect(dut, dst)
        self.tb.run()
        result_data = dst.data()
        self.assertComplexTuplesAlmostEqual(expected_result, result_data)


if __name__ == '__main__':
    gr_unittest.run(qa_drom_gain_cc, "qa_drom_gain_cc.xml")
