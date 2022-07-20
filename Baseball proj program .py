position = input("Position: ")

total_pts = 0

if position == "Pitcher":
    ERA = float(input("\nERA: "))
    WHIP = float(input("WHIP: "))
    K9 = float(input("K/9: "))
    KBB = float(input("K/BB: "))
    FIP = float(input("FIP: "))
    if ERA <= 2.92:
        total_pts += 3
    elif 2.92 < ERA <= 3.32:
        total_pts += 2
    elif 3.32 < ERA <= 3.71:
        total_pts += 1
    elif 3.71 < ERA <= 4.1:
        total_pts += -1
    elif 4.1 < ERA <= 4.55:
        total_pts += -2
    else:
        total_pts += -3
    if WHIP <= 1.06:
        total_pts += 3
    elif 1.06 < WHIP <= 1.14:
        total_pts += 2
    elif 1.14 < WHIP <= 1.21:
        total_pts += 1
    elif 1.21 < WHIP <= 1.29:
        total_pts += -1
    elif 1.29 < WHIP <= 1.36:
        total_pts += -2
    else:
        total_pts += -3
    if K9 >= 10.46:
        total_pts += 3
    elif 9.35 <= K9 < 10.46:
        total_pts += 2
    elif 8.51 <= K9 < 9.35:
        total_pts += 1
    elif 7.64 <= K9 < 8.51:
        total_pts += -1
    elif 6.76 <= K9 < 7.64:
        total_pts += -2
    else:
        total_pts += -3
    if KBB >= 4.8:
        total_pts += 3
    elif 3.8 <= KBB < 4.8:
        total_pts += 2
    elif 3.25 <= KBB < 3.8:
        total_pts += 1
    elif 2.82 <= KBB < 3.25:
        total_pts += -1
    elif 2.35 <= KBB < 2.82:
        total_pts += -2
    else:
        total_pts += -3
    if FIP <= 3.12:
        total_pts += 3
    elif 3.12 < FIP <= 3.58:
        total_pts += 2
    elif 3.58 < FIP <= 3.88:
        total_pts += 1
    elif 3.88 < FIP <= 4.15:
        total_pts += -1
    elif 4.15 < FIP <= 4.58:
        total_pts += -2
    else:
        total_pts += -3
    if total_pts == 15:
        print("should be paid $18,714,286 or more")
    elif total_pts == 14:
        print("should be paid $18,714,286 to $12,500,000")
    elif total_pts == 13:
        print("should be paid $12,500,000 to $9,000,000")
    elif total_pts == 12:
        print("should be paid $9,000,000 to $7,450,000")
    elif total_pts == 11:
        print("should be paid $7,450,000 to $5,700,000")
    elif total_pts == 10:
        print("should be paid $5,700,000 to $4,750,000")
    elif total_pts == 9:
        print("should be paid $4,750,000 to $3,687,500")
    elif total_pts == 8:
        print("should be paid $3,687,500 to $2,875,000")
    elif total_pts == 7:
        print("should be paid $2,875,000 to $2,500,000")
    elif total_pts == 6:
        print("should be paid $2,500,000 to $2,000,000")
    elif total_pts == 5:
        print("should be paid $2,000,000 to $1,700,000")
    elif total_pts == 4:
        print("should be paid $1,700,000 to $1,175,000")
    elif total_pts == 3:
        print("should be paid $1,175,000 to $900,000")
    elif total_pts == 2:
        print("should be paid $900,000 to $749,100")
    elif total_pts == 1:
        print("should be paid $749,100 to $725,900")
    elif total_pts == -1:
        print("should be paid $725,900 to $720,000")
    elif total_pts == -2:
        print("should be paid $720,000 to $716,900")
    elif total_pts == -3:
        print("should be paid $716,900 to $713,000")
    elif total_pts == -4:
        print("should be paid $713,000 to $710,000")
    elif total_pts == -5:
        print("should be paid $710,000 to $706,000")
    elif total_pts == -6:
        print("should be paid $706,000 to $704,000")
    elif total_pts == -7:
        print("should be paid $704,000 to $702,000")
    elif total_pts == -8:
        print("should be paid $702,000 to $700,000")
    elif total_pts == -9:
        print("should be paid $700,000 to $670,000")
    elif total_pts == -10:
        print("should be paid $670,000 to $640,000")
    elif total_pts == -11:
        print("should be paid $640,000 to $610,000")
    elif total_pts == -12:
        print("should be paid $610,000 to $580,000")
    elif total_pts == -13:
        print("should be paid $580,000 to $550,000")
    elif total_pts == -14:
        print("should be paid $550,000 to $500,000")
    else:
        print("should be paid $500,000 or less")
    print(total_pts)
    
elif position == "Hitter":
    BA = float(input("\nAVG: "))
    OBP = float(input("OBP: "))
    HR = int(input("HR: "))
    SLUG = float(input("SLG: "))
    RBI = int(input("RBI: "))
    if BA >= .298:
        total_pts += 3
    elif .282 <= BA < .298:
        total_pts += 2
    elif .270 <= BA < .282:
        total_pts += 1
    elif .259 <= BA < .270:
        total_pts += -1
    elif .247 <= BA < .259:
        total_pts += -2
    else:
        total_pts += -3
    if OBP >= .370:
        total_pts += 3
    elif .355 <= OBP < .370:
        total_pts += 2
    elif .341 <= OBP < .355:
        total_pts += 1
    elif .326 <= OBP < .341:
        total_pts += -1
    elif .313 <= OBP < .326:
        total_pts += -2
    else:
        total_pts += -3
    if HR >= 30:
        total_pts += 3
    elif 25 <= HR < 30:
        total_pts += 2
    elif 20 <= HR < 25:
        total_pts += 1
    elif 17 <= HR < 20:
        total_pts += -1
    elif 10 <= HR < 17:
        total_pts += -2
    else:
        total_pts += -3
    if SLUG >= .527:
        total_pts += 3
    elif .487 <= SLUG < .527:
        total_pts += 2
    elif .457 <= SLUG < .487:
        total_pts += 1
    elif .430 <= SLUG < .457:
        total_pts += -1
    elif .404 <= SLUG < .430:
        total_pts += -2
    else:
        total_pts += -3
    if RBI >= 89:
        total_pts += 3
    elif 79 <= RBI < 89:
        total_pts += 2
    elif 70 <= RBI < 79:
        total_pts += 1
    elif 61 <= RBI < 70:
        total_pts += -1
    elif 54 <= RBI < 61:
        total_pts += -2
    else:
        total_pts += -3
    if total_pts == 15:
        print("should be paid $23,357,143 or more")
    elif total_pts == 14:
        print("should be paid $23,357,143 to 18,250,000")
    elif total_pts == 13:
        print("should be paid $18,250,000 to 15,000,000")
    elif total_pts == 12:
        print("should be paid $15,000,000 to 10,200,000")
    elif total_pts == 11:
        print("should be paid $10,200,000 to 8,500,000")
    elif total_pts == 10:
        print("should be paid $8,500,000 to 7,000,000")
    elif total_pts == 9:
        print("should be paid $7,000,000 to 5,200,000")
    elif total_pts == 8:
        print("should be paid $5,200,000 to 4,600,000")
    elif total_pts == 7:
        print("should be paid $4,600,000 to 4,000,000")
    elif total_pts == 6:
        print("should be paid $4,000,000 to 3,000,000")
    elif total_pts == 5:
        print("should be paid $3,000,000 to 2,250,000")
    elif total_pts == 4:
        print("should be paid $2,250,000 to 1,825,000")
    elif total_pts == 3:
        print("should be paid $1,825,000 to 1,400,000")
    elif total_pts == 2:
        print("should be paid $1,400,000 to 1,200,000")
    elif total_pts == 1:
        print("should be paid $1,200,000 to 1,000,000")
    elif total_pts == -1:
        print("should be paid $1,000,000 to 825,000")
    elif total_pts == -2:
        print("should be paid $825,000 to 730,900")
    elif total_pts == -3:
        print("should be paid $730,900 to 721,700")
    elif total_pts == -4:
        print("should be paid $721,700 to 714,000")
    elif total_pts == -5:
        print("should be paid $714,000 to 709,500")
    elif total_pts == -6:
        print("should be paid $709,500 to 704,500")
    elif total_pts == -7:
        print("should be paid $704,500 to 700,200")
    elif total_pts == -8:
        print("should be paid $700,200 to 700,000")
    elif total_pts == -9:
        print("should be paid $700,000 to 625,000")
    elif total_pts == -10:
        print("should be paid $625,000 to 600,000")
    elif total_pts == -11:
        print("should be paid $600,000 to 575,000")
    elif total_pts == -12:
        print("should be paid $575,000 to 550,000")
    elif total_pts == -13:
        print("should be paid $550,000 to 525,000")
    elif total_pts == -14:
        print("should be paid $525,000 to 500,000")
    else:
        print("should be paid $500,000 or less")
    print(total_pts)
else:
    print("invaild option")
    

               
    
          
