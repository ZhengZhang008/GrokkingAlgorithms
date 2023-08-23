if __name__ == "__main__":
    # You pass an array in, and it gets converted to a set.
    states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

    stations = {"kone": set(["id", "nv", "ut"]), "ktwo": set(["wa", "id", "mt"]), "kthree": set(["or", "nv", "ca"]),
                "kfour": set(["nv", "ut"]), "kfive": set(["ca", "az"])}

    final_stations = set()

    while states_needed:
        best_station = None
        states_covered = set()
        for station, states in stations.items():
            covered = states_needed & states
            if len(covered) > len(states_covered) and station not in final_stations:
                best_station = station
                states_covered = covered
        if best_station is not None:
            states_needed -= states_covered
            final_stations.add(best_station)
            stations.pop(best_station)

    print(final_stations)
