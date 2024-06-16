#!/bin/bash
export DBUS_SESSION_BUS_ADDRESS=$(sudo -u binaily dbus-launch | grep "DBUS_SESSION_BUS_ADDRESS" | cut -d '=' -f 2-)
export PULSE_SERVER=$(sudo -u binaily pulseaudio --start)
sudo -u binaily cvlc --play-and-exit voice/electro_out.mp3