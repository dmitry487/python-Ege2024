from string import digits

alph = digits[:9]

def f(num):
    if (
        ( 
            ('0' in num)
        ) and
        (
            ('11' in num) or ('22' in num) or ('33' in num) or\
            ('44' in num) or ('55' in num) or ('66' in num) or\
            ('77' in num) or ('88' in num) or ('99' in num) or\
            ('13' in num) or ('15' in num) or ('17' in num) or ('19' in num) or\
                  ('31' in num) or ('35' in num) or ('37' in num) or ('39' in num) or\
                  ('51' in num) or ('53' in num) or ('57' in num) or ('59' in num) or\
                  ('71' in num) or ('73' in num) or ('75' in num) or ('79' in num) or\
                  ('91' in num) or ('93' in num) or ('95' in num) or ('97' in num) or\
                  ('24' in num) or ('26' in num) or ('28' in num) or ('32' in num) or\
                  ('34' in num) or ('36' in num) or ('38' in num) or ('42' in num) or\
                  ('46' in num) or ('48' in num) or ('62' in num) or ('64' in num) or\
                  ('68' in num) or ('82' in num) or ('84' in num) or ('86' in num)
        ) and
        (
            (num.count('1') > 4) or (num.count('2') > 4) or (num.count('3') > 4) or\
            (num.count('4') > 4) or (num.count('5') > 4) or (num.count('6') > 4) or\
            (num.count('7') > 4) or (num.count('8') > 4) or (num.count('9') > 4)         
        )
    ):return False
    return True

kolichestvo = 0

for a1 in alph:
    for a2 in alph:
        for a3 in alph:
            for a4 in alph:
                for a5 in alph:
                    for a6 in alph:
                        for a7 in alph:
                            for a8 in alph:
                                for a9 in alph:
                                    for a10 in alph:
                                        for a11 in alph:
                                            num1 = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 + a11
                                            if f(num1):
                                                kolichestvo += 1

print(kolichestvo)