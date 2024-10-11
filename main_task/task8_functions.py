def check_speed():
    speed = float(input("enter the speed of bthe car: "))
    speed_limit = 70
    demerit_points = 0
    if speed <= speed_limit:
        print("ok")
    elif speed > speed_limit and speed <= 75:
        demerit_points += 1
    else:
        demerit_points = 1
        demerit_points += round((speed-75)/5)
        if demerit_points > 12:
            print("license suspended")
        else:
            demerit_points = demerit_points

    print(f"demerit points {demerit_points}")
    
check_speed()
