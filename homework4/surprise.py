# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
for key in targets.keys():
    print(key)

# 2) Write a function that uses a loop to print the name of each star with its spectral type.
for name, spectral in targets.items():
    print(f"{name}'s spectral type is {spectral["Spectral Type"]}")
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def greater_than_mag(targets):
    for name, mag in targets.items():
        if mag["Magnitude"] > 0.1:
            print(f"{name}'s magnitude is greater than 0.1, it is {mag["Magnitude"]}")
print(greater_than_mag(targets))

# 4) Look up another target, add all the necessary information to the targets list. 
targets["Pollux"] = {
    "RA" : "07h 45m 18.9s",
    "Dec" : "+28° 01′ 34′′",
    "Magnitude" : 1.15,
    "Spectral Type" : "K0IIIb"
}
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
def dec_close_to_20(targets):
    starting_point = list(targets.keys())[0]
    largest = starting_point
    largest_val = targets[largest]["Magnitude"]
    for key in targets:
        current_val = targets[key]["Magnitude"]

        current_Dec = targets[key]["Dec"][1:2]
        dec_int = int(current_Dec)
        if current_val < largest_val and (dec_int - 20) < 5:
            largest = key
            largest_val = current_val
    print(f"{largest} is the brightest start that has a declination near 20 degrees,")
    print(f"It's magnitude is {largest_val}")

print(dec_close_to_20(targets))

# 6) What is your favorite constellation?
#Ursa Major
