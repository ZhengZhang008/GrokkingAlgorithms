if __name__ == "__main__":
    # You pass an array in, and it gets converted to a set.
    states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

    # Define the stations and the states they cover
    stations = {"kone": set(["id", "nv", "ut"]), "ktwo": set(["wa", "id", "mt"]), "kthree": set(["or", "nv", "ca"]),
                "kfour": set(["nv", "ut"]), "kfive": set(["ca", "az"])}

    # Initialize the set of final stations
    final_stations = set()

    while states_needed:
        # Initialize the best station and the states it covers
        best_station = None
        states_covered = set()
        for station, states in stations.items():
            # Find the states covered by both the station and the states needed
            covered = states_needed & states
            # If the station covers more states than the current best station and it's not in the final stations
            if len(covered) > len(states_covered) and station not in final_stations:
                # Update the best station and the states it covers
                best_station = station
                states_covered = covered
        if best_station is not None:
            # Remove the states covered by the best station from the states needed
            states_needed -= states_covered
            # Add the best station to the final stations
            final_stations.add(best_station)
            # Remove the best station from the stations
            stations.pop(best_station)

    print(final_stations)
