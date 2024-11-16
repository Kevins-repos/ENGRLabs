import pandas as pd
import matplotlib.pyplot as plt

file_path = 'unit 12/WeatherDataCLL-1.csv'
weather_data = pd.read_csv(file_path)
weather_data.head(), weather_data.columns
weather_data['Date'] = pd.to_datetime(weather_data['Date'])
fig, ax1 = plt.subplots(figsize=(12, 6))
ax1.plot(weather_data['Date'], weather_data['Average Temperature (F)'], color='tab:red', label='Avg Temp (F)')
ax1.set_xlabel('Date')
ax1.set_ylabel('Avg Temperature (F)', color='tab:red')
ax1.tick_params(axis='y', labelcolor='tab:red')
ax2 = ax1.twinx()
ax2.plot(weather_data['Date'], weather_data['Average Daily Wind Speed (mph)'], color='tab:blue', label='Avg Wind Speed (mph)')
ax2.set_ylabel('Avg Wind Speed (mph)', color='tab:blue')
ax2.tick_params(axis='y', labelcolor='tab:blue')
plt.title('Average Temperature and Wind Speed Over Time')
fig.tight_layout()
plt.show()
# 1. Histogram of Average Wind Speed
plt.figure(figsize=(10, 6))
plt.hist(weather_data['Average Daily Wind Speed (mph)'], bins=15, color='skyblue', edgecolor='black')
plt.xlabel('Average Daily Wind Speed (mph)')
plt.ylabel('Number of Days')
plt.title('Distribution of Average Wind Speeds')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# 2. Scatterplot for Average Relative Humidity and Dew Point
plt.figure(figsize=(10, 6))
plt.scatter(weather_data['Average Relative Humidity (%)'], weather_data['Average Dew Point (F)'], 
            alpha=0.7, c='teal', edgecolors='black')
plt.xlabel('Average Relative Humidity (%)')
plt.ylabel('Average Dew Point (F)')
plt.title('Relationship Between Average Relative Humidity and Dew Point')
plt.grid(alpha=0.5)
plt.show()

# 3. Bar Chart for Calendar Month Statistics
weather_data['Month'] = weather_data['Date'].dt.month
weather_data['Year'] = weather_data['Date'].dt.year
monthly_stats = weather_data.groupby('Month').agg({
    'Average Temperature (F)': 'mean',
    'Maximum Temperature (F)': 'max',
    'Minimum Temperature (F)': 'min',
    'Precipitation (in)': 'mean'
}).reset_index()
fig, ax = plt.subplots(figsize=(12, 6))
bar_width = 0.6
ax.bar(monthly_stats['Month'], monthly_stats['Average Temperature (F)'], width=bar_width, color='orange', label='Mean Avg Temp (F)')
ax.plot(monthly_stats['Month'], monthly_stats['Maximum Temperature (F)'], color='red', marker='o', label='Max Temp (F)')
ax.plot(monthly_stats['Month'], monthly_stats['Minimum Temperature (F)'], color='blue', marker='o', label='Min Temp (F)')
ax.plot(monthly_stats['Month'], monthly_stats['Precipitation (in)'], color='green', marker='o', label='Mean Precipitation (in)')
ax.set_xticks(range(1, 13))
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ax.set_xlabel('Month')
ax.set_ylabel('Temperature (F) / Precipitation (in)')
ax.set_title('Monthly Weather Statistics')
ax.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
