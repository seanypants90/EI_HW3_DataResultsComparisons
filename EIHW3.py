# Homework 3 Model Comparisons
# Sean Thatcher
# Environmental Informatics
# Instructor Dr. Rodger Wang

# Install packages

import matplotlib # Data Visualizations
import matplotlib.pyplot as plt
matplotlib.rc_params().update({'font.size': 22})

# Data being used
# Values being hard coded because there is only 1 model value
# and 1 observation value from the gage at each stage.
# The model values were computed in a spreadsheet from model outputs.
# The values and calculations can be found in the HAND Data for Stations spreadshet.
# Values from gauges were obtained from the USGS and a stage of the same/similar
# stage event modeled were selected for comparison.

# Green Brook at Burnt Mills NJ
# Station number 1403400

green_brook_1m_gauge = 0.427078125
green_brook_1m_model = 2.030675754
green_brook_3m_gauge = 91.414
green_brook_3m_model = 37.71595379

# Green Brook at Seeley Mills NJ
# Station number 1401650

pike_run_3m_gauge = 2.126028046
pike_run_3m_model = 62.01765657
pike_run_6m_gauge = 324.7777778
pike_run_6m_model = 379.969509

# Middle Brook at Burnt Mills NJ
# Station number 139910

middle_brook_6m_gauge = 2.60965818
middle_brook_6m_model = 184.7060298
middle_brook_8m_gauge = 394.9545455
middle_brook_8m_model = 395.7144673

# Bar graph visualizations
# These graphs compare the model results to the gauge observations

# 1 meter Green Brook at Burnt Mills NJ
plt.bar(0,green_brook_1m_gauge, label = 'Gauge', color = 'r')
plt.bar(1,green_brook_1m_model, label = 'Model', color = 'b')
plt.xticks([],[])
plt.xlabel('Stage Event')
plt.ylabel('Discharge Cubic ft/sec')
plt.legend()
plt.title('Green Brook Discharge for 3.28 ft (1 m) Stage')
plt.show()

plt.bar(0,green_brook_3m_gauge, label = 'Gauge', color = 'r')
plt.bar(1,green_brook_3m_model, label = 'Model', color = 'b')
plt.xticks([],[])
plt.xlabel('Stage Event')
plt.ylabel('Discharge Cubic ft/sec')
plt.legend()
plt.title('Green Brook Discharge for 9.84 ft (3 m) Stage')
plt.show()

plt.bar(0,pike_run_3m_gauge, label = 'Gauge', color = 'r')
plt.bar(1,pike_run_3m_model, label = 'Model', color = 'b')
plt.xticks([],[])
plt.xlabel('Stage Event')
plt.ylabel('Discharge Cubic ft/sec')
plt.legend()
plt.title('Pike Run Discharge for 9.84 ft (3 m) Stage')
plt.show()

plt.bar(0,pike_run_6m_gauge, label = 'Gauge', color = 'r')
plt.bar(1,pike_run_6m_model, label = 'Model', color = 'b')
plt.xticks([],[])
plt.xlabel('Stage Event')
plt.ylabel('Discharge Cubic ft/sec')
plt.legend()
plt.title('Pike Run Discharge for 19.7 ft (6 m) Stage')
plt.show()

plt.bar(0,middle_brook_6m_gauge, label = 'Gauge', color = 'r')
plt.bar(1,middle_brook_6m_model, label = 'Model', color = 'b')
plt.xticks([],[])
plt.xlabel('Stage Event')
plt.ylabel('Discharge Cubic ft/sec')
plt.legend()
plt.title('Middle Brook Discharge for 19.7 ft (6 m) Stage')
plt.show()

plt.bar(0,middle_brook_8m_gauge, label = 'Gauge', color = 'r')
plt.bar(1,middle_brook_8m_model, label = 'Model', color = 'b')
plt.xticks([],[])
plt.xlabel('Stage Event')
plt.ylabel('Discharge Cubic ft/sec')
plt.legend()
plt.title('Middle Brook Discharge for 26.2 ft (8 m) Stage')
plt.show()
