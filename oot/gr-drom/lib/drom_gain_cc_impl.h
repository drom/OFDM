/* -*- c++ -*- */
/*
 * Copyright 2018 drom.
 *
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifndef INCLUDED_DROM_DROM_GAIN_CC_IMPL_H
#define INCLUDED_DROM_DROM_GAIN_CC_IMPL_H

#include <drom/drom_gain_cc.h>

namespace gr {
    namespace drom {

        class drom_gain_cc_impl : public drom_gain_cc
        {
            private:
                // Nothing to declare in this block.
                int d_symbol_length;
                float d_gain;

            public:
                drom_gain_cc_impl(
                    int symbol_length,
                    float gain
                );
                ~drom_gain_cc_impl();

      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      int general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
    };

  } // namespace drom
} // namespace gr

#endif /* INCLUDED_DROM_DROM_GAIN_CC_IMPL_H */
