from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)

    list_severe_towns = []
    list_high_towns = []
    list_mod_towns = []
    list_low_towns = []

    for station in stations:
        if station.relative_water_level() != None:
            if station.relative_water_level() > 1.25:
                list_severe_towns.append(station.town)
            if 1 < station.relative_water_level() < 1.25:
                list_high_towns.append(station.town)
            if 0.75 < station.relative_water_level() < 1:
                list_mod_towns.append(station.town)
            if station.relative_water_level() < 0.75:
                list_low_towns.append(station.town)

    print(f"Towns with severe flood risk: {list_severe_towns}")
    print("\n")
    print(f"Towns with high flood risk: {list_high_towns}")
    print("\n")
    print(f"Towns with moderate flood risk: {list_mod_towns}")
    print("\n")
    print(f"Towns with low flood risk: {list_low_towns}")

if __name__ == "__main__":
    run()