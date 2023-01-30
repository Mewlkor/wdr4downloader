import requests
import datetime
import multiprocessing
import time
import sys

wdr_streams = {'1Live': 'http://wdr-1live-live.icecast.wdr.de/wdr/1live/live/mp3/128/stream.mp3',
                'WDR2': 'http://wdr-wdr2-ostwestfalenlippe.icecast.wdr.de/wdr/wdr2/ostwestfalenlippe/mp3/128/stream.mp3',
                'WDR3': 'http://wdr-wdr3-live.icecast.wdr.de/wdr/wdr3/live/mp3/128/stream.mp3',
                'WDR4': 'http://wdr-wdr4-live.icecast.wdr.de/wdr/wdr4/live/mp3/128/stream.mp3',
                'WDR5': 'http://wdr-wdr5-live.icecast.wdr.de/wdr/wdr5/live/mp3/128/stream.mp3'}

def download(stream_url=wdr_streams['1Live'] , filename='download'):
    stream_request = requests.get(stream_url, stream=True)
    with open(f'{filename}_{datetime.date.today()}.mp3', 'wb') as f:
        try:
            for block in stream_request.iter_content(1024):
                f.write(block)
        except KeyboardInterrupt:
            pass



if __name__ == '__main__':
    t1 = multiprocessing.Process(target=download, args=(wdr_streams[sys.argv[1]], sys.argv[3]))
    print('Starting download')
    t1.start()
    wait_time = int(sys.argv[2])*60
    time.sleep(wait_time)
    print('Stopping download')
    t1.terminate()
    t1.join()
