import pandas as pd
import matplotlib.pyplot as plt

# Load the uploaded CSV file
file_path = '~/Desktop/solar panel/solar-panel/data/solar_data.csv' # Change the path if needed
solar_data = pd.read_csv(file_path)

def plot_data(site_num, date):

    # Filter the data for site_id = 1
    site_data = solar_data[solar_data['site_id'] == site_num]

    # Convert timestamp_utc to datetime
    site_data['timestamp_utc'] = pd.to_datetime(site_data['timestamp_utc'])

    # Filter the data for the date 2019-03-01
    site_data_date = site_data[site_data['timestamp_utc'].dt.date == pd.to_datetime(date).date()]

    plt.figure(figsize=(12, 6))
    plt.plot(site_data_date['timestamp_utc'], site_data_date['solar_gen_kwh'], label=f'Solar Generation (kWh) on {date}')

    # Set plot labels and title
    plt.xlabel('Time (UTC)')
    plt.ylabel('Solar Generation (kWh)')
    plt.title(f'Solar Generation Over Time for Site {site_num}')
    plt.legend()
    plt.grid(True)
    plt.show()

    return site_data_date


def plot_multi_data(site_num, date_list):

    # Filter the data for site_id = 1
    site_data = solar_data[solar_data['site_id'] == site_num]

    # Convert timestamp_utc to datetime
    site_data['timestamp_utc'] = pd.to_datetime(site_data['timestamp_utc'])

    # Create a plot for each date in the date list
    plt.figure(figsize=(12, 6))
    for date in date_list:
        # Filter the data for the specific date
        site_data_date = site_data[site_data['timestamp_utc'].dt.date == pd.to_datetime(date).date()]
        if not site_data_date.empty:
            plt.plot(site_data_date['timestamp_utc'], site_data_date['solar_gen_kwh'], label=f'Solar Generation (kWh) on {date}')

    # Set plot labels and title
    plt.xlabel('Time (UTC)')
    plt.ylabel('Solar Generation (kWh)')
    plt.title(f'Solar Generation Over Time for Site {site_num}')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_site_data(site_num):

    # Filter the data for site_id = 1
    site_data = solar_data[solar_data['site_id'] == site_num]

    # Convert timestamp_utc to datetime
    site_data['timestamp_utc'] = pd.to_datetime(site_data['timestamp_utc'])

    # Plot solar generation over time for site 1
    plt.figure(figsize=(12, 6))
    plt.plot(site_data['timestamp_utc'], site_data['solar_gen_kwh'], label='Solar Generation (kWh)')
    plt.xlabel('Time (UTC)')
    plt.ylabel('Solar Generation (kWh)')
    plt.title(f'Solar Generation Over Time for Site {site_num}')
    plt.legend()
    plt.grid(True)
    plt.show()
