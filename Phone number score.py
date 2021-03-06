"""
     # เลขผลรวมดีมาก ได้แก่ 9, 14, 15, 19, 23, 24, 32, 36, 40, 41, 42, 44, 45, 46, 50, 51, 54, 55, 56, 59, 63, 64, 65  ให้คุณระดับดีมาก
                                            69, 79 โอกาสประสบผลสำเร็จสูง อุปสรรคน้อย เจริญรุ่งเรือง ร่ำรวย รวดเร็ว และมีความสุข
     # เลขผลรวมดีปานกลาง ได้แก่ 10, 13, 16, 18, 20, 22, 25, 26, 28, 31, 35, 38, 39, 47, 49, 52, 53, 57, 58, 60, 61  ให้คุณระดับดีปานกลาง
                                           62, 66, 68, 74, 75 เหนื่อย มีอุปสรรค แต่ยังมีโอกาสประสบผลสำเร็จ หากมีความพยายาม
     # เลขผลรวมไม่ดี ได้แก่ 11, 12, 17, 21, 27, 29, 30, 33, 34, 37, 43, 48, 67, 70, 71, 72, 73, 76, 77, 78, 80  (ให้โทษ ใครได้ผลรวมเหล่านี้ควรเปลี่ยน)
                                            เหนื่อยมาก อุปสรรคมาก เจอปัญหารุมเร้า การงาน การเงิน ความรัก เกิดอุบัติเหตุชีวิตไม่จบไม่สิ้น

"""

def sum_phone_digit(x):
    total = 0
    for i in x:
        total += int(i)
    return total



def meaning(i):
    meaning=''
    if  i in (9,14,15,19,23,24,32,36,40,41,42,44,45,46,50,51,54,55,56,59,63,64,65):
        meaning='ระดับดีมาก'
    elif i in (69,79):
        meaning='โอกาสประสบผลสำเร็จสูง อุปสรรคน้อย เจริญรุ่งเรือง ร่ำรวย รวดเร็ว และมีความสุข'
    elif i in (10,13,16,18,20,22,25,26,28,31,35,38,39,47,49,52,53,57,58,60,61):
        meaning='ระดับปานกลาง'
    elif i in (62,66,68,74,75):
        meaning='เหนื่อย มีอุปสรรค แต่ยังมีโอกาสประสบผลสำเร็จ หากมีความพยายาม'
    else:
        meaning='ระดับแย่ เหนื่อยมาก อุปสรรคมาก เจอปัญหารุมเร้า การงาน การเงิน ความรัก เกิดอุบัติเหตุชีวิตไม่จบไม่สิ้น'
    return meaning

x= input('Enter phone number :')
ans = sum_phone_digit(x)
print(ans)
print(meaning(ans))
