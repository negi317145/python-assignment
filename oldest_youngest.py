age1=int(input('enter 1st person age'))
age2=int(input('enter 2nd person age'))
age3=int(input('enter 3rd person age'))
if age1>age2>age3:
    print('1st per is oldest and 3rd is yooungest')
elif age2>age1>age3:
    print('2nd is oldest and 3rd is youngest')
elif age1>age3>age2:
    print('1st is oldest and 2nd is youngest')
elif age2>age3>age1:
    print('3rd  is oldest and 1st is youngest')
elif age3>age2>age1:
    print('3rd is oldest and 1st is youngest')
else:
    print('3rd is oldest and 2nd is youngest')	