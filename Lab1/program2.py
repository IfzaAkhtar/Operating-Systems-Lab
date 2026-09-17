processes = []

while True:
    try:
        n = int(input("Enter number of processes: "))
        if n > 0:
            break
        print("Number of processes must be greater than 0.")
    except ValueError:
        print("Please enter a valid integer.")

for i in range(n):

    while True:
        pid = input(f"Enter Process ID for process {i + 1}: ").strip()

        if not pid:
            print("Process ID cannot be empty.")
        elif any(p["pid"] == pid for p in processes):
            print("Process ID must be unique.")
        else:
            break

    while True:
        try:
            arrival = int(input(f"Enter Arrival Time for {pid}: "))

            if arrival >= 0:
                break

            print("Arrival Time cannot be negative.")

        except ValueError:
            print("Please enter a valid integer.")

    while True:
        try:
            burst = int(input(f"Enter Burst Time for {pid}: "))

            if burst > 0:
                break

            print("Burst Time must be greater than 0.")

        except ValueError:
            print("Please enter a valid integer.")

    processes.append({
        "pid": pid,
        "arrival": arrival,
        "burst": burst
    })

def fcfs(process_list):
    current_time = 0
    intervals = []

    ordered = sorted(
        process_list,
        key=lambda p: (p["arrival"], p["pid"])
    )

    for process in ordered:
        if current_time < process["arrival"]:
            intervals.append(("IDLE", current_time, process["arrival"]))
            current_time = process["arrival"]

        start = current_time
        end = start + process["burst"]

        intervals.append((process["pid"], start, end))
        current_time = end

    return intervals

def sjf(process_list):
    remaining = process_list.copy()
    current_time = 0
    intervals = []

    while remaining:
        ready = [
            p for p in remaining
            if p["arrival"] <= current_time
        ]

        if not ready:
            next_arrival = min(
                p["arrival"] for p in remaining
            )
            intervals.append(
                ("IDLE", current_time, next_arrival)
            )
            current_time = next_arrival
            continue

        process = min(
            ready,
            key=lambda p: (
                p["burst"],
                p["arrival"],
                p["pid"]
            )
        )

        start = current_time
        end = start + process["burst"]

        intervals.append((process["pid"], start, end))
        current_time = end

        remaining.remove(process)

    return intervals

def show_result(title, intervals):
    print("\n" + title)
    print("Process Start End")

    sequence = []

    for pid, start, end in intervals:
        print(f"{pid:<9} {start:<7} {end}")

        if pid != "IDLE":
            sequence.append(pid)

    print("Sequence:", " -> ".join(sequence))

print("INPUT PROCESSES")
print("PID AT BT")

for p in processes:
    print(f'{p["pid"]:<5} {p["arrival"]:<4} {p["burst"]}')

show_result("FCFS SCHEDULING", fcfs(processes))
show_result("SJF SCHEDULING", sjf(processes))

