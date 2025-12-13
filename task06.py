phone = input('phone: ')


if '90' <= phone[:2] <= '91':
    print('ucell')

elif '93' <= phone[:2] <= '94':
    print('beeline')

elif '95' <= phone[:2] <= '97':
    print('uzmobile')

elif phone[:2] == '88':
    print('mobiuz')
elif phone[:2] == '99':
    print('mobiuz')

else:
    print('noma’lum operator')  