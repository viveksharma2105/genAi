import threading
import  requests
import time

def download(url):
    print(f"Starting download from {url}")
    res = requests.get(url)
    print(f"Finished download from {url}, size: {len(res.content)} bytes")
    
urls = [
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/svg",
]

start = time.time()
threads = []

for url in urls:
    t = threading.Thread(target=download, args=(url,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
    
end = time.time()
print(f"Total download time: {end - start:.2f} seconds")