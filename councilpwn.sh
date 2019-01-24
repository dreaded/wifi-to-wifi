#!/bin/bash
sudo sh -c "echo namesever 8.8.8.8 >> /etc/resolv.conf"
/bin/sleep 10
curl -k -d email=oopa@loompa.co.uk https://captive.rochdale.gov.uk/cgi-bin/login?cmd=login
/bin/sleep 5
/bin/bash /home/pi/bashtest.sh
sudo /home/pi/create_ap/create_ap wlan0 wlan1 HH HeritageHackers


