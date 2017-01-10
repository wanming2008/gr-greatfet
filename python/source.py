#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2017 Dominic Spill <dominicgs@gmail.com>
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

import numpy
from gnuradio import gr
import greatfet
from greatfet import GreatFET
from greatfet.protocol import vendor_requests

class source(gr.sync_block):
    """
    docstring for block source
    """
    def __init__(self, serial=None):
        gr.sync_block.__init__(
            self,
            name="source",
            in_sig=None,
            out_sig=[numpy.byte])
        try:
            # self.device = GreatFET(serial_number=serial)
            self.device = GreatFET()
        except greatfet.errors.DeviceNotFoundError:
            raise
        self.device.vendor_request_out(vendor_requests.SDIR_START)

    def work(self, input_items, output_items):
        output_items[0] = self.device.device.read(0x81, 0x4000, 1000)
        return len(output_items[0])
