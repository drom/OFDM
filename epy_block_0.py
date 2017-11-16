"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block


    def __init__(self, example_param=1.0):  # only default arguments here
        self.fixed_index = None
        self.last_index = None
        self.done = False

        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='keep m in n',   # will show up in GRC
            in_sig=[(np.complex64,320),np.float32],
            out_sig=[(np.complex64,256)]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.example_param = example_param

    def work(self, input_items, output_items):
        input_vector = input_items[0][0]
        index = np.int(input_items[1][0])
        if (self.done == False):
            output_vector = input_vector[0:256]
            if (self.last_index == None) :
                self.last_index = index
                print "1"
            elif (self.last_index == index) :
                self.fixed_index = index
                self.done = True
                print "2"
            elif (self.last_index != index):
                self.last_index = index
                print "3"

        print "index:{}".format(self.fixed_index)

        if (self.done == True) :
            if (self.fixed_index < 32) :
                # print "{}:{}".format(index+32,(index-32)+320)
                output_vector = input_vector[self.fixed_index+32:(self.fixed_index-32)+320]
                # print "length:{}".format(len(output_vector2))
            elif (self.fixed_index > 287) :
                # print "{}:{}".format(((index+32)-320),320-(32+(320-index)))
                output_vector = input_vector[((self.fixed_index+32)-320):320-(32+(320-self.fixed_index))]
                # print "length:{}".format(len(output_vector2))
            else :
                # print "{}:{}:{}:{}".format(0,index-32,index+32,320)
                output_vector = np.concatenate((input_vector[0:self.fixed_index-32], input_vector[self.fixed_index+32:320]))
                # print "length:{}".format(len(output_vector2))

        output_items[0][:] = output_vector
        return len(output_items[0])
