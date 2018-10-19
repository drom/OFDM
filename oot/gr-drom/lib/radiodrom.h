#ifndef INCLUDE_RADIODROM_H
#define INCLUDE_RADIODROM_H

#include <gnuradio/io_signature.h>

static gr_complex radiodrom_gain (gr_complex inp, float gain) {
    return gr_complex(
        gain * inp.real(),
        gain * inp.imag()
    );
}

static void radiodrom_chunk_gain (
    const gr_complex *in,
    gr_complex *out,
    int noutput_items,
    float gain,
    int d_symbol_length
) {
    for (int i = 0; i < noutput_items / d_symbol_length; i++) {
        for (int j = 0; j < d_symbol_length; j++) {
            const gr_complex tmp = in[i * d_symbol_length + j];
            out[i * d_symbol_length + j] = radiodrom_gain(tmp, gain);
        }
    }
}

static gr_complex cmul_conj (gr_complex ab, gr_complex cd) {
    return gr_complex(
        ab.real() * cd.real() + ab.imag() * cd.imag(),
        ab.imag() * cd.real() - ab.real() * cd.imag()
    );
}

static void radiodrom_chunk_cmul_conj (
    const gr_complex *in,
    gr_complex *out,
    gr_complex *prev,
    int full_len,
    int chunk_len
) {
    for (int j = 0; j < chunk_len; j++) {
        out[j] = cmul_conj(in[j], prev[j]);
    }

    for (int i = 1; i < full_len / chunk_len; i++) {
        const int offset = i * chunk_len;
        for (int j = 0; j < chunk_len; j++) {
            const int index = offset + j;
            out[index] = cmul_conj(in[index], prev[index]);
        }
    }

    for (int j = 0; j < chunk_len; j++) {
        prev[j] = in[full_len - chunk_len + j];
    }
}

#endif
