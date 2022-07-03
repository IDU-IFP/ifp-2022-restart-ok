for r in range(int(input())):
    cls_info = list(map(int,input().split()))[1:]
    cls_info.sort()

    mns_list = []

    for i in range(len(cls_info)):
        try:
            mns_list.append(cls_info[i+1] - cls_info[i])
        except IndexError:
            pass
    lgap = max(mns_list)

    print(f"Class {r+1}")
    print(f'Max {max(cls_info)}, Min {min(cls_info)}, Largest gap {lgap}')
