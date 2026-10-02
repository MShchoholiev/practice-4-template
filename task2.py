capacity = 20
n = 5
bikes_list = [0, 4, 10, 18, 20]

# Write your code here
status_list = []
for i in range(len(bikes_list)):
    if bikes_list[i] == 0:
        status_list.append("EMPTY")
    elif bikes_list[i] == capacity:
        status_list.append("FULL")
    elif 4 * bikes_list[i] <= capacity:
        status_list.append("LOW")
    elif 4 * (capacity - bikes_list[i]) <= capacity:
        status_list.append("HIGH")
    else:
        status_list.append("OK")

k = 0
for i, elem in enumerate(status_list):
    print("OBSERVATION", i + 1, ":", elem)
    if elem in ("EMPTY", "LOW", "HIGH", "FULL"):
        k += 1

print("SERVICE REQUIRED:", k)
