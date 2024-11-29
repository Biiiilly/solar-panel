import pandas as pd
import pvlib
from pvlib.location import Location
import matplotlib.pyplot as plt

# London latitude and longitude
latitude = 51.5074
longitude = -0.1278
tz = 'Europe/London'
location = Location(latitude, longitude, tz)

times = pd.date_range('2024-11-29', freq='1h', periods=24, tz=tz)
solar_position = location.get_solarposition(times)

# Assume the sunny day weather
weather = pd.DataFrame({
    'ghi': [200, 150, 100, 50, 0, 0, 0, 50, 150, 300, 500, 600, 650, 600, 500, 300, 200, 100, 50, 0, 0, 0, 0, 0],
    'dni': [100, 80, 50, 0, 0, 0, 0, 30, 80, 200, 400, 500, 550, 500, 400, 200, 100, 50, 0, 0, 0, 0, 0, 0],
    'dhi': [100, 70, 50, 50, 0, 0, 0, 20, 50, 100, 150, 200, 200, 200, 150, 100, 50, 50, 50, 0, 0, 0, 0, 0],
}, index=times)

# Solar Panel model
module_parameters = {
    'Name': 'Example_Module',
    'Pmax': 300,
    'gamma_pdc': -0.004,
}

# Tilt and oritentation
tilt = 35
azimuth = 180

# Environments Assumptions
poa_irradiance = pvlib.irradiance.get_total_irradiance(
    surface_tilt=tilt,
    surface_azimuth=azimuth,
    dni=weather['dni'],
    ghi=weather['ghi'],
    dhi=weather['dhi'],
    solar_zenith=solar_position['apparent_zenith'],
    solar_azimuth=solar_position['azimuth']
)

temperature_model_parameters = pvlib.temperature.TEMPERATURE_MODEL_PARAMETERS['sapm']['open_rack_glass_glass']
temperature_cell = pvlib.temperature.sapm_cell(
    poa_global=poa_irradiance['poa_global'],
    temp_air=10, 
    wind_speed=2.0,
    **temperature_model_parameters
)

# Output
effective_irradiance = poa_irradiance['poa_global']
power_output = effective_irradiance / 1000 * module_parameters['Pmax']

result = pd.DataFrame({
    'Time': times,
    'GHI (W/m^2)': weather['ghi'],
    'DNI (W/m^2)': weather['dni'],
    'DHI (W/m^2)': weather['dhi'],
    'Effective Irradiance (W/m^2)': effective_irradiance,
    'Power Output (W)': power_output
})

plt.figure(figsize=(10, 6))
plt.plot(result['Time'], result['Power Output (W)'], label='Power Output (W)')
plt.title('Daily Power Output for Solar Panel in London (2024-11-29)')
plt.xlabel('Time')
plt.ylabel('Power Output (W)')
plt.xticks(rotation=45)
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()

print(result)
