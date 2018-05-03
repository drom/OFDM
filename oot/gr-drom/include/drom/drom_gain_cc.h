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


#ifndef INCLUDED_DROM_DROM_GAIN_CC_H
#define INCLUDED_DROM_DROM_GAIN_CC_H

#include <drom/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace drom {

    /*!
     * \brief <+description of block+>
     * \ingroup drom
     *
     */
    class DROM_API drom_gain_cc : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<drom_gain_cc> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of drom::drom_gain_cc.
       *
       * To avoid accidental use of raw pointers, drom::drom_gain_cc's
       * constructor is in a private implementation
       * class. drom::drom_gain_cc::make is the public interface for
       * creating new instances.
       */
      static sptr make(int symbol_length, float gain);
    };

  } // namespace drom
} // namespace gr

#endif /* INCLUDED_DROM_DROM_GAIN_CC_H */
