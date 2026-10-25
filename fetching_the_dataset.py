import requests
import pandas as pd
import math

def air_density(temp_c, rh, pressure=101325):
    """Calculate air density (kg/m³) using Ideal Gas Law with humidity adjustment."""
    temp_k = temp_c + 273.15
    es = 6.112 * math.exp((17.67 * temp_c) / (temp_c + 243.5)) * 100  # saturation vapor pressure (Pa)
    e = rh / 100.0 * es  # actual vapor pressure
    rv = 461.495
    rd = 287.058
    rho = ((pressure - e) / (rd * temp_k)) + (e / (rv * temp_k))
    return rho

def fetch_dataset(lat, lon, start="2013", end="2023", output_file="wind_dataset.csv"):
    """Fetch wind speed, temp, humidity for a location and compute power output."""
    url = (
        f"https://power.larc.nasa.gov/api/temporal/daily/point"
        f"?parameters=WS10M,T2M,RH2M"
        f"&community=RE"
        f"&longitude={lon}"
        f"&latitude={lat}"
        f"&start={start}0101"
        f"&end={end}1231"
        f"&format=JSON"
    )

    response = requests.get(url)
    data = response.json()

    if "properties" not in data or "parameter" not in data["properties"]:
        raise ValueError("No parameter data returned. Check API response.")

    params = data["properties"]["parameter"]

    # 🔑 Convert nested dict → DataFrame
    df = pd.DataFrame(params)
    df.index.name = "Date"
    df.reset_index(inplace=True)

    # Convert YYYYMMDD → YYYY-MM-DD
    df["Date"] = pd.to_datetime(df["Date"], format="%Y%m%d")

    # Ensure numeric
    df = df.astype({"WS10M": float, "T2M": float, "RH2M": float})

    # Air density
    df["Air_Density"] = df.apply(lambda row: air_density(row["T2M"], row["RH2M"]), axis=1)

    # Turbine parameters (example: 2 MW, rotor diameter 80m)
    R = 40
    A = math.pi * R**2
    Cp = 0.45
    eta = 0.9

    df["Power_Output_kW"] = 0.5 * df["Air_Density"] * A * (df["WS10M"]**3) * Cp * eta / 1000

    # Keep only needed columns
    df = df[["Date", "WS10M", "T2M", "RH2M", "Power_Output_kW"]]
    df.rename(columns={
        "WS10M": "Wind_Speed(m/s)",
        "T2M": "Temperature(C)",
        "RH2M": "Humidity(%)",
        "Power_Output_kW": "Power_Output(kW)"
    }, inplace=True)

    # Save CSV
    df.to_csv(output_file, index=False)
    print(f"✅ Dataset saved to {output_file} with {len(df)} rows.")
    return df


# Example run (Bangalore, Karnataka)
dataset = fetch_dataset(12.9716, 77.5946, "2013", "2023")
print(dataset.head())