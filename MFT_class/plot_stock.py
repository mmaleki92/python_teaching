import requests
import json
import matplotlib.pyplot as plt

response = requests.get("https://api.nobitex.ir/v2/trades/BTCIRT")

c = json.loads(response.content)

if c["status"] == "ok":
    trades = c["trades"]
    print("its Ok!")
else:
    exit()
time_list = []
price_list = []
volume_list = []
type_list = []

for trade in trades:
    time_list.append(trade["time"])
    price_list.append(trade["price"])
    volume_list.append(float(trade["volume"])*100000)

    if trade["type"] == "sell":
        type_list.append("red")
    else:
        type_list.append("green")

fig, axs = plt.subplots(2, 2)


# print(type_list)
axs[0, 0].plot(time_list, price_list, label="Price") # line plot
# plt.show()
# # plt.scatter(time_list, price_list, s=volume_list, c = type_list) # scatter plot
# plt.plot(time_list, volume_list, label="Volume") # line plot
# plt.xlabel("Time")
# plt.ylabel("Price")
# plt.legend()
plt.show()
