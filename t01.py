import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn') # 이 두줄은 본 필자가 항상 쓰는 방법입니다. matplotlib 의 기본 
sns.set(font_scale=2.5) # scheme 말고 seaborn scheme 을 세팅하고, 일일이 graph 의 font size 를
# 지정할 필요 없이 seaborn 의 font_scale 을 사용하면 편합니다.
import missingno as msno
import warnings # ignore warnings
warnings.filterwarnings('ignore')
# %matplotlib inline