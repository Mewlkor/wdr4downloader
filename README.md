# WDR Radio Downloader

Use install.sh to get dependencies

Downloads these WDR streams:

- 1Live : https://wdr-1live-live.icecastssl.wdr.de/wdr/1live/live/mp3/128/stream.mp3
- WDR2 : https://wdr-wdr2-ostwestfalenlippe.icecastssl.wdr.de/wdr/wdr2/ostwestfalenlippe/mp3/128/stream.mp3
- WDR3 : https://wdr-wdr3-live.icecastssl.wdr.de/wdr/wdr3/live/mp3/128/stream.mp3
- WDR4 : https://wdr-wdr4-live.icecastssl.wdr.de/wdr/wdr4/live/mp3/128/stream.mp3
- WDR5 : https://wdr-wdr5-live.icecastssl.wdr.de/wdr/wdr5/live/mp3/128/stream.mp3
___
Accepts three arguments:
- --stream (-s) : Name of Radiochanel form list above. Default: WDR4
- --duraton (-d) : Duration of recording in minutes. Default: 1
- --filename (-f) : Desired filename. The script will add the current date. Default: download
___
Example: 
~~~ 
python downloader.py -s WDR2 -d 5 -f test
~~~
___
Made for my father

