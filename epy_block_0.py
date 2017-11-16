"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, example_param=1.0):  # only default arguments here
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
        index = np.int(input_items[1][0])
        print "index:{}".format(index)
        input_vector = input_items[0][0]

        # print len(input_vector)

        if (index < 32) :
            # print "{}:{}".format(index+32,(index-32)+320)
            output_vector = input_vector[np.int(index+32):np.int((index-32+320))]
            # print "length:{}".format(len(output_vector2))
            # output_vector = input_vector[0:256]
        elif (index > 287) :
            print "{}:{}".format(((index+32)-320),320-(32+(320-index)))
            output_vector2 = input_vector[index+32,320-(32+(320-index))]
            print "length:{}".format(len(output_vector2))
            output_vector = input_vector[0:256]
        else :
            # print "{}:{}:{}:{}".format(0,index-32,index+32,320)
            output_vector = np.concatenate((input_vector[0:index-32], input_vector[index+32:320]))
            # print "length:{}".format(len(output_vector2))
            # output_vector = np.concatenate((input_vector[0:250], input_vector[250:256]))

        output_items[0][:] = output_vector
        return len(output_items[0])
