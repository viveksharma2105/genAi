import asyncio
import time
from  concurrent.futures import ThreadPoolExecutor

def stock_check(item):
    print(f"Checking stock for  {item}...")
    time.sleep(2) # Simulating blocking I/O operation
    print(f"{item} stock: 42")
    
async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        await loop.run_in_executor(pool,stock_check, 'Masala chai')
        
asyncio.run(main())