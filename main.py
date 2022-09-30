import os

def get_lines(file_path):
    with open(file_path, 'r') as f:
        text = f.readlines()
    return text

def get_contacts(file_path):
    with open(file_path, 'r') as f:
        text = f.readlines()
        new_lst = []
        for i in text:
            new_lst.append("1" + i.rstrip())
    return new_lst #str(text)[2:-4]

def send_message(phone_number, message):
    os.system('osascript sendMessage.applescript {} "{}"'.format(phone_number, message))

if __name__ == '__main__':
    text = get_lines('message.txt')
    contact_text = get_contacts('contact.txt')

    for contact in contact_text:
        for line in text:
            send_message(str(contact)[1:], line)