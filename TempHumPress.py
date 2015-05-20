#!/usr/bin/python
from astro_pi import AstroPi
import time

ap = AstroPi()
temp = ap.get_temperature()
humidity = ap.get_humidity()
pressure = ap.get_pressure()

while True:
    ap.set_rotation(180)

    print("Temperature: %s C" % temp)
    ap.show_message("Temperature: %.1f C" % temp, scroll_speed=0.1, text_colour$
    time.sleep(1)

    print("Humidity: %.2f %%rH" % humidity)
    ap.show_message("Humidity: %.1f %%rH" % humidity, scroll_speed=0.1, text_co$
    time.sleep(1)

    print("Pressure: %.2f mb" % pressure)
    ap.show_message("Pressure: %.1f mb" % pressure, scroll_speed=0.1, text_colo$
    time.sleep(1)

ap.clear()
