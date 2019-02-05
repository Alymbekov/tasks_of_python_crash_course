invite_best_guests = ['My Father','My Mother','Brother','small Brother']
message ='Приглашаю вас на обед дорогой(ая) мой(я)'
print(message , str(len(invite_best_guests)), invite_best_guests)
print(message + ' ' + invite_best_guests[0])
print(message + ' ' +  invite_best_guests[1])
print(message + ' ' + invite_best_guests[2])
print(message + ' ' + invite_best_guests[3])
print('К сожелению' + ' ' + invite_best_guests[0] + 'Не сможет прийти(((')

invite_best_guests[0] = 'Tuggan'

print(message + ' ' + invite_best_guests[0])
print(message + ' ' + invite_best_guests[1])
print(message + ' ' + invite_best_guests[2])
print(message + ' ' + invite_best_guests[3])
print('Список расширился')

invite_best_guests.insert(0, 'Rysya')
invite_best_guests.insert(2, 'Booki')
invite_best_guests.append('Asylbek')

print(message + ' ' + invite_best_guests[0])
print(message + ' ' + invite_best_guests[1])
print(message + ' ' + invite_best_guests[2])
print(message + ' ' + invite_best_guests[3])
print(message + ' ' + invite_best_guests[4])
print(message + ' ' + invite_best_guests[5])
print(message + ' ' + invite_best_guests[6])

message_two = 'sorry we do not have a chair )))'
print(message_two)

guest_one = invite_best_guests.pop()
print(guest_one + ' ' + message_two)
guest_two = invite_best_guests.pop()
print(guest_two + ' ' + message_two)
guest_three = invite_best_guests.pop()
print(guest_three + ' ' + message_two)
guest_four = invite_best_guests.pop()
print(guest_four + ' ' + message_two)
guest_fife = invite_best_guests.pop()
print(guest_fife + ' ' + message_two)

print(invite_best_guests)

message_three = ' Приложение еще в силе'
print(invite_best_guests[0] + ' ' + message_three)
print(invite_best_guests[1] + ' ' + message_three)

del invite_best_guests[0]
del invite_best_guests[0]

print(invite_best_guests)
