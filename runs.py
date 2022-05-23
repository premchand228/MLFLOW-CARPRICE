import os
import numpy as np

alpha_s=np.linspace(0.1,1,5)
l1_ratios=np.linspace(0.1,1,5)

for alpha in alpha_s:
    for l1_ratio in l1_ratios:
        print(f"logging experiment for alpha:{alpha}, l1_ratio: {l1_ratio}")
        os.system(f"python demo.py -a {alpha} -l1 {l1_ratio}")