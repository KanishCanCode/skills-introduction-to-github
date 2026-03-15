# Non-preemptive SJF Scheduling

n = int(input("Enter number of processes: "))

processes = []
for i in range(n):
    at = int(input(f"Arrival Time of P{i+1}: "))
    bt = int(input(f"Burst Time of P{i+1}: "))
    processes.append([i+1, at, bt])

# sort by arrival time first
processes.sort(key=lambda x: x[1])

time = 0
completed = []
waiting_time = 0
turnaround_time = 0

while processes:
    ready = [p for p in processes if p[1] <= time]

    if not ready:
        time += 1
        continue

    ready.sort(key=lambda x: x[2])  # sort by burst time
    p = ready[0]

    processes.remove(p)

    pid, at, bt = p
    start = time
    finish = time + bt

    wt = start - at
    tat = finish - at

    waiting_time += wt
    turnaround_time += tat

    time = finish

    completed.append([pid, at, bt, wt, tat])

print("\nPID  AT  BT  WT  TAT")
for p in completed:
    print(*p)

print("\nAverage Waiting Time:", waiting_time/n)
print("Average Turnaround Time:", turnaround_time/n)
