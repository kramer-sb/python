
contacts = { #this is our primary dictionary
    'number': 4, #this is the key number which means we have 4 folx
    'folx':
        [ #this is the beginning of our next dictionary list
            {'name':'Bruce Wayne', 'email':'batman@gotham.com.invalid'},
            {'name':'Jack Napier', 'email':'joker@gotham.com.invalid'},
            {'name':'Comish Gordon', 'email':'gordon@gotham.com.invalid'},
            {'name':'Vicki Vale', 'email':'vicky@gotham.com.invalid'}
        ]
}

print('Folx emails:') #we only want the emails
for folx in contacts['folx']: #and we're looping through the list
    print(folx['email']) #this prints only the email addresses of the "folx" in our contacts
