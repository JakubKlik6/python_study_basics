#Creating email adress
persons = ['Elizabeth', 'Steven@sales.mycompany.com','Sebastian','Margaret','Svetlana@mycompany.eu','Raphael']

domain = 'mycompany.com'

emails = []

#without continue

for person in persons:
    if '@' in person:
        emails.append(person)
    else:
        email = person +'@' + domain
        emails.append(email)

for email in emails:
    print(email)

#with continue

for person in persons:
    if '@' in person:
        emails.append(person)
        continue
    email = person + '@' + domain
    emails.append(email)

for email in emails:
    print(email)
