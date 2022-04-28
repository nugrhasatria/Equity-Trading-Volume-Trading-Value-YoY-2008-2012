import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import pandas as pd

    # Volume Perdagangan Saham - Nilai Perdagangan Saham / Equity Trading Volume - Trading Value
        # YoY 2008-2012

# Data for Volume Perdagangan Saham
     #     Q1        Q2        Q3         Q4
vol12 = [196.021, 223.453, 170.515, 197.857,
        117.468, 656.727, 403.651, 289.813,
        262.328, 338.918, 317.981, 411.639,
        226.916, 348.312, 345.680, 282.642,
        255.561, 271.716, 215.890, 310.596]

# Data for Nilai Perdagangan Saham
     #     Q1        Q2        Q3         Q4
val12 = [317.446, 360.157, 240.865, 146.059,
        92.842, 337.197, 303.286, 241.810,
        246.704, 281.109, 267.186, 381.238,
        328.922, 290.219, 350.205, 254.095,
        278.401, 287.694, 252.992, 297.026]

# Year / Period(s)
    # X-Axis
yq12 = ['2008\nQ1', '2008\nQ2', '2008\nQ3', '2008\nQ4',
        '2009\nQ1', '2009\nQ2', '2009\nQ3', '2009\nQ4',
        '2010\nQ1', '2010\nQ2', '2010\nQ3', '2010\nQ4',
        '2011\nQ1', '2011\nQ2', '2011\nQ3', '2011\nQ4',
        '2012\nQ1', '2012\nQ2', '2012\nQ3', '2012\nQ4']
    #
# Merge Datasets into Dataframe
a_df = {'vol12': vol12, 'val12': val12, 'yq12': yq12}
alpha = pd.DataFrame(a_df)

# Axis for Volume Perdagangan Saham
fig, ax1 = plt.subplots(figsize = (10,6))
plt.ylim(50, 750)
color = 'Blue'
ax1.set_title('Perkembangan Volume dan Nilai Perdagangan Saham \n 2008-2012', fontsize = 15, pad = 15)
ax1.set_xlabel('Periode', fontsize = 13)
ax1.set_ylabel('Volume\n(Juta Lembar Saham)', fontsize=13, color=color)
ax1 = sns.lineplot(x='yq12', y='vol12', data=alpha, sort=False, marker='d', color=color)
ax1.tick_params(axis = 'y', color=color)

# Axis for Nilai Perdagangan Saham
ax2 = ax1.twinx()
color = 'Olive'
plt.ylim(30, 450)
ax2.set_ylabel('Nilai\n(Miliar Rupiah)', fontsize=13, color=color)
ax2 = sns.lineplot(x='yq12', y='val12', data=alpha, sort=False, color=color, marker='o') 
ax2.tick_params(axis ='y', color=color)

# Add Grid
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)

# Defining Legend Style and Data Index: 
Blue_line = mlines.Line2D([], [], color='Blue', label='Volume')
Olive_line = mlines.Line2D([], [], color='Olive', label='Nilai')
plt.legend(handles=[Blue_line, Olive_line], loc= 'upper left')

# Checkout
plt.show()