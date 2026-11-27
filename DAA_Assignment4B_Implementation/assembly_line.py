def assembly_line(a1, a2, t1, t2, entry, exit_time, show=False):
    n = len(a1)
    if n == 0 or len(a2) != n or len(t1) != n-1 or len(t2) != n-1:
        raise ValueError("Invalid input lengths")
    f1, f2, p1, p2 = [0]*n, [0]*n, [0]*n, [0]*n
    f1[0], f2[0] = entry[0] + a1[0], entry[1] + a2[0]
    for j in range(1, n):
        s1, x1 = f1[j-1] + a1[j], f2[j-1] + t2[j-1] + a1[j]
        f1[j], p1[j] = (s1, 1) if s1 <= x1 else (x1, 2)
        s2, x2 = f2[j-1] + a2[j], f1[j-1] + t1[j-1] + a2[j]
        f2[j], p2[j] = (s2, 2) if s2 <= x2 else (x2, 1)
        if show:
            print("Station", j+1, "line1 stay/transfer:", s1, x1,
                  "line2 stay/transfer:", s2, x2)
    end1, end2 = f1[-1] + exit_time[0], f2[-1] + exit_time[1]
    line, best = (1, end1) if end1 <= end2 else (2, end2)
    route = [0] * n
    route[-1] = line
    for j in range(n-1, 0, -1):
        route[j-1] = p1[j] if route[j] == 1 else p2[j]
    return best, route, f1, f2

def run():
    a1, a2 = [7,9,3,4,8,4], [8,5,6,4,5,7]
    t1, t2, entry, exits = [2,3,1,3,4], [2,1,2,2,1], [2,4], [3,2]
    result = assembly_line(a1, a2, t1, t2, entry, exits, True)
    print("Minimum time:", result[0], "line route:", result[1])
    print("DP line 1:", result[2], "DP line 2:", result[3])
    changed = t1.copy(); changed[2] = 20
    print("Changed transfer time result:", assembly_line(a1,a2,changed,t2,entry,exits)[:2])
    changed_a1 = a1.copy(); changed_a1[2] = 30
    print("Changed station time result:", assembly_line(changed_a1,a2,t1,t2,entry,exits)[:2])
