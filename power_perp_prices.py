import inline as inline
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn
import pandas as pd
from matplotlib.pyplot import figure
from itertools import cycle, islice
from power_perp import everlasting_power_perp_price

vol = 1.5
drift = 0
funding_period = 1 / 365
spot = np.arange(1000., 4000., 50.)

power = 2
payoff = spot ** power / spot[0] ** (power - 1)
price = everlasting_power_perp_price(spot, funding_period, vol, drift, power) / spot[0] ** (power - 1)

data = pd.DataFrame({'Spot ETH': spot, f'ETH^{power}': payoff, f'Power perp price': price}).set_index('Spot ETH')
figure(figsize=(12, 9), dpi=80)
ax = sbn.lineplot(data=data, palette=['#4169e1', '#0ABAB5'], linewidth=2.5)
ax.set_ylabel("Value")
ax.set_title(f"Normalized ETH^{power} Perpetual Price vs. Spot Price ")

plt.show()
