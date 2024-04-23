def check_overlap(start1, end1, start2, end2):
    # 開始時刻が終了時刻より後の場合、重複していないと判定
    if start1 >= end1 or start2 >= end2:
        return False
    
    # 重複している場合、重複していることを返す
    if start1 < end2 and start2 < end1:
        return True
    
    return False

def main():
    schedules = [
        ("2022-10-15T09:30:00", "2022-10-15T11:00:00"),
        ("2022-10-15T10:30:00", "2022-10-15T12:00:00"),
        ("2022-10-15T12:30:00", "2022-10-15T13:30:00"),
        ("2022-10-15T15:30:00", "2022-10-15T16:30:00"),
        ("2022-10-15T16:00:00", "2022-10-15T17:00:00"),
        ("2022-10-16T10:00:00", "2022-10-16T11:00:00"),
        ("2022-10-16T10:30:00", "2022-10-16T11:30:00")
    ]
    
    inputs = [
        ("2022-10-15T09:30:00", "2022-10-15T12:00:00"),
        ("2022-10-15T14:00:00", "2022-10-15T15:00:00"),
        ("2022-10-15T17:00:00", "2022-10-15T17:30:00"),
        ("2022-10-15T12:00:00", "2022-10-15T12:30:00"),
        ("2022-10-15T09:00:00", "2022-10-15T10:00:00")
    ]
    
    for start, end in inputs:
        overlap = False
        for schedule_start, schedule_end in schedules:
            if check_overlap(start, end, schedule_start, schedule_end):
                overlap = True
                print(f"{start} - {end} は重複しています")
                break
        if not overlap:
            print(f"{start} - {end} は重複しません")

if __name__ == "__main__":
    main()