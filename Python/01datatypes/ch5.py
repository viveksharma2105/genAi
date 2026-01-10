import arrow

time = arrow.utcnow()
time = time.to("US/Pacific")  # Capture the returned value
print(time.format("YYYY-MM-DD HH:mm:ss ZZ"))