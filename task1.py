train_number = input("Enter the train number: ")
hour_of_departure = int(input("Enter the hour of departure: "))
minute_of_departure = int(input("Enter the minute of departure: "))
trip_duration = int(input("Enter the duration of the trip in minutes: "))

departure_time_minutes = hour_of_departure * 60 + minute_of_departure
minutes_in_day = 1440
day_shift = (departure_time_minutes + trip_duration) // minutes_in_day
arrival_time_minutes_total = (departure_time_minutes + trip_duration) % minutes_in_day
arrival_time_hours = arrival_time_minutes_total // 60
arrival_time_minutes = arrival_time_minutes_total % 60

print("TRAIN:", train_number)
print("DAY SHIFT:", day_shift)
print("ARRIVAL TIME:", arrival_time_hours, arrival_time_minutes)