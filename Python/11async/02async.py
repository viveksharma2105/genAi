import asyncio

async def brew(name):
    print(f"Brewing  {name}  Chai...")
    await  asyncio.sleep(2)
    print(f'{name} is ready...')


async def  main():
    await asyncio.gather(
        brew("Masala Chai"),
        brew("Ginnger Chai"),
        brew("leamon Chai"),
    )
    
asyncio.run(main())