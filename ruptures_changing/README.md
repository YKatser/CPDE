# Changes of the *ruptures* python library for the experiment running
We provide here the needed changes to extend classic *ruptures* library for the ensembling case.
We have extended 3 algorithms of the search methods to be used with the ensemble of cost functions:
- binseg
- dynp (opt)
- window (win)

Additionally, we have constructed a complex cost function that contains a combination of the cost functions and should be configured manually.

### How it works
All the .py files from the current folder should be transferred to the `.../ruptures/detection` folder manually.
To avoid overwriting `__init__.py` file, the following lines just can be added to the existing file `.../ruptures/detection/__init__.py`:
```
from .dynpensembling import DynpEnsembling
from .windowensembling import WindowEnsembling
from .binsegensembling import BinsegEnsembling
from .bottomupensembling import BottomUpEnsembling
```

Afterward, the ensembling part of the library works similarly to the classic part.
Moreover, the `custom_cost.py` file is an important part of the ensembling approach, and it can be found in the utils folder of the repository.

### Files
`__init__.py` - init package file
`dynpensembling.py` - file containing ensemble-extended Dynp algorithm
`windowensembling.py` - file containing ensemble-extended Window algorithm
`binsegensembling.py` - file containing ensemble-extended Binseg algorithm
`aggregations.py` - file containing various aggregation functions

### Used materials

The `dynpensembling.py`, `windowensembling.py`, `binsegensembling.py` files are based on the [*ruptures*](http://ctruong.perso.math.cnrs.fr/ruptures-docs/build/html/index.html) library (Copyright (c) 2017, ENS Paris-Saclay, CNRS. All rights reserved.).

The *ruptures* python package is distributed under the following conditions:
```
BSD 2-Clause License
Copyright (c) 2017, ENS Paris-Saclay, CNRS. All rights reserved.
Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
* Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```
