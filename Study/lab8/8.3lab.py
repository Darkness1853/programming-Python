emails = {
    'gryffindor.com': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'k_stepanov'],
    'hufflepuff.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
    'hogwarts.com': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
    'slytherin.com': ['ekaterina_ivanova', 'glebova_nastya'],
    'ravenclaw.com': ['john.doe', 'mark.zuckerberg', 'helen_hunt']
}

print("Программа выводит почту при вводе имени пользователя и домена.")

def get_emails(name):
    user_emails = []
    for domain, users in emails.items():
        if name in users:
            user_emails.append(f"{name}@{domain}")
    return user_emails

while True:
    name = input("Введите имя пользователя: ")
    address_list = get_emails(name)

    if address_list:
        print("Адреса электронной почты:", ", ".join(address_list))
    else:
        print("Ошибка, ключ не найден в словаре.")

    repeat = int(input("Введите 0/1\n Если хотите продолжить программу (0) иначе (1): "))
    if repeat == 1:
        print("Спасибо вам за то, что запустили программу.")
        break



