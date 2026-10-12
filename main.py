# getting datda from a textbox
from pyscript import display, document


def get_fullname(e):
    document.getElementById('div1').innerHTML = ' '
    book_clubf = ['bela', 'isabella', 'athena']
    book_clubl = ['esguerra', 'allas', 'athena']

    namef = document.getElementById('fname').value.lower().strip()
    name_checker = namef in book_clubf #true(1) or false(0)

    namel = document.getElementById('lname').value.lower().strip()
    name_checker = namel in book_clubl #true(1) or false(0)

    display_message = ('Sorry, your name is not in the list', f'{namef} {namel} is in the book club!')
    display(display_message[name_checker], target='div1') # displaying the message based on the result of name_checker
