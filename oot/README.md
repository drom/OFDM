Simple out-of-tree (OOT) module

Used this tutorial: https://wiki.gnuradio.org/index.php/OutOfTreeModules

```
gr_modtool newmod drom
cd gr-drom/
gr_modtool add -t general -l cpp drom_gain_cc
# Python QA => Y
```

Write some code.

Compile, Test.

```
cd build
camke ..
make
make test
```

Install

```
gr_modtool makexml drom_gain_cc
sudo make install
```
