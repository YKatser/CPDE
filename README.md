# Ensembles of offline changepoint detection methods [![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/unsupervised-offline-changepoint-detection/change-point-detection-on-skab)](https://paperswithcode.com/sota/change-point-detection-on-skab?p=unsupervised-offline-changepoint-detection)
In this repository we provide Jupyter Notebooks to reproduce the results from the paper.

Instructions and code for the extending search methods (CPD algorithms) from *ruptures* python library to the ensemble case can be found [here](ruptures_changing/).

# Leaderboard for TEP benchmark
*Sorted by NAB (standard); for all metrics bigger is better.*  
*The current leaderboard is obtained with the window size for the NAB detection algorithm equal to 10% of the dataset length*  
| Algorithm | NAB (standard) | NAB (lowFP) | NAB (LowFN) |
|---|---|---|---|
Perfect detector | 100 | 100 | 100 
Opt (Mahalanobis) | 36.88 | 35.82 | 37.29
Win (Mahalanobis) | 27.79 | 27 | 28.05
BinSeg (Mahalanobis) | 36.88 | 35.82 | 37.29
OptEnsemble (Min+MinMax/Rank) | 41.81 | 41 | 42.16
WinEnsemble (WeightedSum+MinAbs) | 25.14 | 24.33 | 26.29
BinSegEnsemble (Min+MinMax/Rank) | 41.81 | 41 | 42.16
Null detector | 0 | 0 | 0

# Leaderboard for SKAB
*Sorted by NAB (standard); for all metrics bigger is better.*  
*The current leaderboard is obtained with the window size for the NAB detection algorithm equal to 30 sec.*  
| Algorithm | NAB (standard) | NAB (lowFP) | NAB (LowFN) |
|---|---|---|---|
Perfect detector | 100 | 100 | 100 
Opt (Mahalanobis) | 22.37 | 19.9 | 23.37
Win (l1) | 18.4 | 16.22 | 19.19
BinSeg (Mahalanobis) | 24.1 | 21.69 | 25.04
OptEnsemble (WeightedSum+Rank) | 23.07 | 20.52 | 24.35
WinEnsemble (Sum+MinAbs) | 19.38 | 17.03 | 20.35
BinSegEnsemble (WeightedSum+Rank) | 18.1 | 15.36 | 19.51
Null detector | 0 | 0 | 0

# Citation
To cite this work in your publications:
```
@article{katser2021unsupervised,
  title={Unsupervised Offline Changepoint Detection Ensembles},
  author={Katser, Iurii and Kozitsin, Viacheslav and Lobachev, Victor and Maksimov, Ivan},
  journal={Applied Sciences},
  volume={11},
  number={9},
  pages={4280},
  year={2021},
  publisher={Multidisciplinary Digital Publishing Institute}
}
```

# Used materials and 3rd party code
The experiment is based on the [*ruptures*](http://ctruong.perso.math.cnrs.fr/ruptures-docs/build/html/index.html) library (Copyright (c) 2017, ENS Paris-Saclay, CNRS. All rights reserved.) and the paper "Selective review of offline change point detection methods. Signal Processing" by C. Truong, L. Oudre, N. Vayatis. [journal](https://www.sciencedirect.com/science/article/pii/S0165168419303494?via%3Dihub), [pdf](http://www.laurentoudre.fr/publis/TOG-SP-19.pdf).

The *ruptures* python package is distributed under the following conditions:
```
BSD 2-Clause License

Copyright (c) 2017, ENS Paris-Saclay, CNRS. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```
