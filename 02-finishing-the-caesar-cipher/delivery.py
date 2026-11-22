DAYS_IN_WEEK :int = 7

day: int = int(input("Day: "))
days_to_wait: int = int(input("Days_to_wait: "))

delivery_day = day + days_to_wait

if delivery_day > DAYS_IN_WEEK:
    delivery_day -= DAYS_IN_WEEK

print(delivery_day)
