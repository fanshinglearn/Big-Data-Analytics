from data import Data
import json, time
from kafka import KafkaProducer

data = Data()
sor = data.get_stop_of_route("Taoyuan", "715")
rtns = data.get_real_time_near_stop("Taoyuan", "715")

with open("config.json", "r") as f:
    config = json.load(f)

producer = KafkaProducer(bootstrap_servers=config["server"],
                         value_serializer=lambda m: json.dumps(m).encode())

msg = {"sor": sor, "rtns": rtns}
producer.send(config["topic"], msg)

time.sleep(5)