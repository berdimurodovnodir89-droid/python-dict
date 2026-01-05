def show_menu() -> None:
    print("\n====== 📱 Contact Book v2.2 ======")
    print("1. + Yangi kontakt qoshish")
    print("2. 📄 Barcha kontaktlarni korish")
    print("3. 🔍 Kontaktni ism boyicha qidirish")
    print("4. 📧 Faqat @gmail.com kontaktlarni korish")
    print("5. 🚪 Dasturni yakunlash")


def is_valid_contact(contact: list) -> bool:
    if type(contact[0]) != str:
        return False
    elif type(contact[1]) != str:
        return False
    elif type(contact[2]) != str:
        return False
    else:
        return True


def add_contact(contact_list: list[list]) -> None:
    name = input('Name: ').strip().title()
    phone = input('Phone: ').strip()
    email = input('Email: ').strip()

    contact = [name, phone, email]
    if is_valid_contact(contact):
        contact_list.append(contact)
        print('contact muvvaffaqiyatli qoshildi')
    else:
        print('contact xato')


def list_contacts(contact_list: list[list]) -> None:
    for contact in contact_list:
        print(contact)


def search_contact(contact_list: list[list]) -> None:
    search = input("Search: ").strip()

    for contact in contact_list:
        if search.lower() in contact[0].lower():
            print(contact)


def filter_gmail_contacts(contact_list: list[list]) -> None:
    for contact in contact_list:
        if contact[2].endswith('@gmail.com'):
            print(contact)


def main() -> None:
    contacts: list[list] = [
        ['Ali', '99123123123', 'ali@gmail.com'],
        ['Vali', '881231231231', 'vali@yandex.ru']
    ]

    while True:
        show_menu()
        choice = input("Tanlov (1-5): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            list_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            filter_gmail_contacts(contacts)
        elif choice == "5":
            print("👋 Dasturni yakunlayapmiz. Xayr!")
            break
        else:
            print("Notogri tanlov. Iltimos, 1 dan 5 gacha son kiriting.")

main()