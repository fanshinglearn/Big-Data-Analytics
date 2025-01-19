import json
from kafka import KafkaConsumer

with open("config.json", "r") as f:
    config:dict = json.load(f)

consumer = KafkaConsumer(config["topic"],
                         bootstrap_servers=config["server"],
                         consumer_timeout_ms=10000,
                         auto_offset_reset='earliest')

for msg in consumer:
    data = json.loads(msg.value)

sor = data["sor"]
rtns = data["rtns"]

with open("./data/route.json,", "w") as f:
    json.dump(sor, f)

with open("./data/location.json,", "w") as f:
    json.dump(rtns, f)

# B10802050
with open("./data/route.json", "r") as f:
    route_data = json.load(f)

with open("./data/location.json", "r") as f:
    location_data = json.load(f)


def print_route_stops(direction):
    for stop in route_data[direction]['Stops']:
        print(stop['StopName']['Zh_tw'], end=' -> ')

    print('\n\t目前公車停靠站：', end='')
    for stop in location_data:
        if stop['Direction'] == direction:
            print(stop['StopName']['Zh_tw'], end=', ')

forward = 0
backward = 1

# 順向
print('順向：')
print_route_stops(backward)

# 逆向
print('\n\n逆向：')
print_route_stops(forward)