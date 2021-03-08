# Compost Temp
<img src="./docs/lora.png"  height="96" width="300"/>

This project uses an IOT Temperature Sensor
 [(The Thing Node)](https://www.thethingsnetwork.org/docs/devices/node/)
communicating via LoRaWAN to track the temperatures in my wife’s garden compost.
The compost box is pretty far back in the yard outside the reach of any WiFi.
So using LoRa is a practical solution for this problem.
(Given that I have a [LoRa Gateway](https://www.thethingsnetwork.org/docs/gateways/gateway/) to work with.)

The App creates a simple website, through a somewhat elaborate process,
to check on the temperature in the compost box deep in our backyard. If things are working correctly
with the compost the temps in the box should always be higher than the outside
temperatures.


###### A little background on LoRaWan
The LoRaWAN® specification is a Low Power, Wide Area (LPWA) networking
protocol designed to wirelessly connect battery operated ‘things’ to
the internet in regional, national or global networks, and targets key
Internet of Things (IoT) requirements such as bi-directional
communication, end-to-end security, mobility and localization services.


### Website View of Compost

<img src="./docs/Screen_Shot.png"  height="375" width="300"/>

## Atchitecture
LoRa example using The Things Network

<img src="./docs/Architecture.png" height="400" width="600"/>



## Note
A config.json file is require. The format is:

```
{
  "app_id":"dhiggs01-compost-temperature",
  "access_key":"ttn-account-v2.xxxxxxxxxxxxxxxxxx"
}
```

