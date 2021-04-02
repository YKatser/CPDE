# Skoltech Anomaly Benchmark (SKAB)
SKAB is designed for evaluating algorithms for anomaly detection. The benchmark currently includes 30+ datasets plus Python modules for algorithms’ evaluation. Each dataset represents a multivariate time series collected from the sensors installed on the testbed. All instances are labeled for evaluating the results of solving outlier detection and changepoint detection problems.

The [link](https://github.com/waico/SKAB) to the repository with the benchmark and all related information.

# License
SKAB is being distributed under the GPL-3.0 License.

# Folder structure
```
  └── SKAB_data                   # Data files and processing Jupyter Notebook
      ├── Load data.ipynb         # Jupyter Notebook to load all data
      ├── evaluating.py           # File with evaluating (NAB scoring algorithm) functions
      ├── README.md           
      ├── anomaly-free         
      │   └── anomaly-free.csv    # Data obtained from the experiments with normal mode
      ├── valve1                  # Data obtained from the experiments with closing the valve at the outlet of the flow from the pump.
      │   ├── 1.csv            
      │   ├── 2.csv            
      │   ├── 3.csv            
      │   └── 4.csv            	
      ├── valve2                  # Data obtained from the experiments with closing the valve at the flow inlet to the pump.
      │   ├── 1.csv            
      │   ├── 2.csv            
      │   ├── 3.csv            
      │   ├── 4.csv            
      │   ├── 5.csv            
      │   ├── 6.csv            
      │   ├── 7.csv            
      │   ├── 8.csv            
      │   ├── 9.csv            
      │   ├── 10.csv           
      │   ├── 11.csv           
      │   ├── 12.csv           
      │   ├── 12.csv           
      │   ├── 13.csv           
      │   ├── 14.csv           
      │   ├── 15.csv           
      │   └── 16.csv           
      └── other                   # Data obtained from the other experiments          
          ├── 13.csv              # Sharply behavior of rotor imbalance
          ├── 14.csv              # Linear behavior of rotor imbalance
          ├── 15.csv              # Step behavior of rotor imbalance
          ├── 16.csv              # Dirac delta function behavior of rotor imbalance
          ├── 17.csv              # Exponential behavior of rotor imbalance
          ├── 18.csv              # The slow increase in the amount of water in the circuit
          ├── 19.csv              # The sudden increase in the amount of water in the circuit
          ├── 20.csv              # Draining water from the tank until cavitation
          ├── 21.csv              # Two-phase flow supply to the pump inlet (cavitation)
          └── 22.csv              # Water supply of increased temperature
```
