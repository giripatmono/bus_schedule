def bus_schedule(m, n, k, bus_lines=[]):
    """
    :m number of buses (1 <= m <= 106)
    :n number of stations (2 <= n <= 106)
    :k time by which we must arrive at the airport (1 <= k <= 1018)
    :bus_lines list of bus schedule which is a tuple of
        (start_station a, destination_station b, departure time s, arrival time t, probability p)
        where (0 <= a, b < n, a 6 = b) and (0 <= s < t <= k)  and (0 <= p <= 1)
    :return: probability value (float)
    """

    print('Number of bus:{}, Number of station:{}'.format(m, n))
    print('Arrival Time:{}'.format(k))

    probability = 0
    route_counter = 0
    # calculate direct route to airport
    for key, row in enumerate(bus_lines):
        if row[0] == 0 and row[1] == 1:
            # time arrival valid
            if row[3] <= k:
                print('using route-{}, start_station:{}, dest_station:{}'.format(key, row[0], row[1]))
                route_counter += 1
                probability += row[4]

    # calculate probability value
    print(probability, route_counter)
    return round(probability / route_counter, 10)  # 10 digits decimal precision


num_bus = 8
num_station = 4
arrival_time = 1000
bus_lines = [
    (0, 1, 0, 900, 0.2),
    (0, 2, 100, 500, 1),
    (2, 1, 500, 700, 1),
    (2, 1, 501, 701, 0.1),
    (0, 3, 200, 701, 0.5),
    (3, 1, 500, 701, 0.1),
    (3, 0, 550, 701, 0.9),
    (0, 1, 700, 900, 0.1)
]

print('\n --- Calculating Probability ---')
result = bus_schedule(num_bus, num_station, arrival_time, bus_lines)
print('Probability Value', result)
# result = 0.319


num_bus = 4
num_station = 2
arrival_time = 2
bus_lines = [
    (0, 1, 0, 1, 0.5),
    (0, 1, 0, 1, 0.5),
    (0, 1, 1, 2, 0.4),
    (0, 1, 1, 2, 0.2)
]

print('\n --- Calculating Probability ---')
result = bus_schedule(num_bus, num_station, arrival_time, bus_lines)
print('Probability Value', result)
# result = 0.7
