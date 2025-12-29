import datetime

first_date = datetime.datetime(1970, 1, 1)
now = datetime.datetime.now()
seconds = (now - first_date).total_seconds()

print(
    f"Seconds since January 1, 1970:"
    f" {seconds:,.4f} or {seconds:.2e} in scientific notation"
)
print(now.strftime("%b %d %Y"))
