"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
import pmt
from pmt import pmt_to_python
import time
import os
from gnuradio import gr
from multiprocessing import Pool, TimeoutError
import time


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    # fcorr_last = None

    def __init__(self):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='convert to message',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
            # out_sig=[]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.message_port_register_out(pmt.to_pmt("out"))


    def work(self, input_items, output_items):

        fcorr_ma = np.abs(3906.25*input_items[0][0])
        # print '{}'.format(fcorr_ma)
        self.message_port_pub(pmt.to_pmt("out"), pmt.cons(pmt.intern("freq"), pmt.to_pmt(fcorr_ma)))

        output_items[0][:] = input_items[0][0]
        return len(output_items[0])
