from collections import deque

n = int(input("Enter number of processes: "))

processes = []

print("\nEnter Process details:")

for i in range(n):
    print(f"\nProcess {i + 1}")

    pid = input("Process ID: ")
    at = int(input("Arrival Time: "))
    bt = int(input("Burst Time: "))
    priority = int(input("Priority: "))

    if at < 0 or bt <= 0 or priority < 0:
        print("Invalid input! Try again.")
        exit()

    processes.append({
        "pid": pid,
        "at": at,
        "bt": bt,
        "priority": priority
    })

print("\n======================================")
print("NON-PREEMPTIVE PRIORITY SCHEDULING")
print("======================================")

print("Priority Convention: Smaller number = Higher priority")

completed = []
remaining = processes.copy()
current_time = 0

while remaining:
    available = [p for p in remaining if p["at"] <= current_time]

    if not available:
        next_arrival = min(p["at"] for p in remaining)
        print(f"CPU Idle: {current_time} -> {next_arrival}")
        current_time = next_arrival
        continue

    selected = min(
        available,
        key=lambda p: (p["priority"], p["at"])
    )

    start = current_time
    end = current_time + selected["bt"]

    print(f"{selected['pid']}: {start} -> {end}")

    current_time = end
    completed.append(selected)
    remaining.remove(selected)

print("\nPriority Execution Sequence:")

for p in completed:
    print(p["pid"], end=" -> ")

print("END")

print("\n======================================")
print("ROUND ROBIN SCHEDULING")
print("======================================")

while True:
    quantum = int(input("Enter Round Robin Time Quantum: "))

    if quantum > 0:
        break

    print("Time Quantum must be greater than 0.")

print("Time Quantum:", quantum)

rr_processes = []

for p in processes:
    rr_processes.append({
        "pid": p["pid"],
        "at": p["at"],
        "bt": p["bt"],
        "remaining": p["bt"]
    })

rr_processes.sort(key=lambda p: p["at"])

queue = deque()
current_time = 0
index = 0

print("\nRound Robin Execution Slices:")

while index < n or queue:

    if not queue:

        if current_time < rr_processes[index]["at"]:
            print(
                f"CPU Idle: "
                f"{current_time} -> {rr_processes[index]['at']}"
            )

            current_time = rr_processes[index]["at"]

        while (
            index < n
            and rr_processes[index]["at"] <= current_time
        ):
            queue.append(rr_processes[index])
            index += 1

    current = queue.popleft()

    start = current_time

    execution = min(
        quantum,
        current["remaining"]
    )

    current["remaining"] -= execution
    current_time += execution

    print(f"{current['pid']}: {start} -> {current_time}")

    while (
        index < n
        and rr_processes[index]["at"] <= current_time
    ):
        queue.append(rr_processes[index])
        index += 1

    if current["remaining"] > 0:
        queue.append(current)

print("\n======================================")
print("SUMMARY")
print("======================================")

print("Priority Convention: Smaller number = Higher priority")
print("Round Robin Time Quantum:", quantum)

print("\nPriority Sequence:")

for p in completed:
    print(p["pid"], end=" -> ")

print("END")

print("\nRound Robin sequence is shown above as individual execution slices.")