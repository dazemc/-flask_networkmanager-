send and receive wifi credentials with flask,
apk is at this <a href="https://www.github.com/dazemc/wipi">repo</a>.

Using wpa_supplicant as the backend for NetworkManager creates a hotspot fine. 
However, not all my devices connect to the hotspot successfully when using WPA. 
When using iwd as the backend for NetworkManager, I run into frequent stability 
issues with a generic "802.1x supplicant failed". When it works, it works great.
I was able to trace it down to a generic kernel level error, "ieee80211 phy0: brcmf_vif_set_mgmt_ie: vndr ie set error : -52".
It appears, at least for the raspberry pi 3, that the built in wireless device is not getting stuck in "managed" mode and not switching over to "ap" mode. You can replicate this by toggling a hotspot off and on. I have a suspicion that iwd is not shutting the hotspot down cleanly. Toggling works fine with wpa_supplicant but the main device, my phone, that is project is intended for will not connect. So for now this will use an open wifi connection while I work on bluetooth serial. 