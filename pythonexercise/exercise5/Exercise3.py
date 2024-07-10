def towerhanoi(disks,source,auxiliary,target):
    if (disks == 1):
        print("Move disk 1 from rod {} to rod {}.".format(source,target))
        return
    towerhanoi(disks-1,source,target,auxiliary)
    print("Move disk {} from rod {} to rod {}.".format(disks,source,target))
    towerhanoi(disks-1,auxiliary,source,target)
disks =4
towerhanoi(disks,"a","b","c")