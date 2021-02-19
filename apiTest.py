import datetime as dt
import time
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')
start = dt.datetime(2021,2,19)
end = dt.datetime(2021,2,19)

while(1):

    df = web.DataReader('SNC.TO', 'yahoo', start, end)
    print(df.head())
    time.sleep(60)

