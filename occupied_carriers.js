#!/usr/bin/env node
'use strict';

function arr (len) {
    return Array.apply(null, Array(len));
}

// occupied_carriers

const half = 64;
const gap = 16;
const res = (
    arr(half)
    .map(function (e, i) { return i - half - gap; })
    .concat(
        arr(half)
        .map(function (e, i) { return i + 1 + gap; })
    )
);

console.log('(' + res.join(', ') + ')');
