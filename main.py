import requests
import datetime
import multiprocessing
import time


def download():
    stream_url = 'http://wdr-wdr4-live.icecast.wdr.de/wdr/wdr4/live/mp3/128/stream.mp3'
    stream_request = requests.get(stream_url, stream=True)
    with open(f'WDR4_Klassik_populaer_{datetime.date.today()}.mp3', 'wb') as f:
        try:
            for block in stream_request.iter_content(1024):
                f.write(block)
        except KeyboardInterrupt:
            pass

if __name__ == '__main__':
    t1 = multiprocessing.Process(target=download)
    print('Starting download')
    t1.start()
    time.sleep(10860)
    print('Stopping download')
    t1.terminate()
    t1.join()
