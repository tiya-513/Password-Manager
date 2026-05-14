Project: Password manager
-needs to have a master password 
-user should be able to change the master password
-user should be able to c.r.u.d. username and password
-password should be stored encrypted and decrypted while reading
-user should be able to copy the password





New usage detected, create a master password
Create Master Password: myPass@69069710

Welcome to the password manager
-created by 

~$ list
Listing existing users: 
ID_3u2i  google.com      rudrapd2005@gmail.com
ID_i2o0  spotify.com     eepy@gmail.com
ID_ai42  twitter.com     2328039@gmail.com

~$ mstr_pswd
Enter current master password   : whatever@513
Enter new master password       : new_whatever@513

~$ entry
Enter website: meesho.in
Enter username: tiya_513
Enter password: meesho@513

New entry created

~$ show ID_3u2i

Website : google.com
Username: rudrapd2005@gmail.com
Password (Do you want to copy? (y/n)): y

Copied!

~$ update ID_j322
Leave empty for no change
Website name    (netflix.com)       : reddit.com
Username        (rudrapd2005@gmail.com) :
Password        (********)          : my_newpass@1234

Updated entry ID_j322!

~$ delete ID_i2o0
Deleting the following entry

Website : google.com
Username: rudrapd2005@gmail.com

type the word DELETE for confirmation: DELETE

Deleted ID_i2o0 successfully!

~$ help

list
    Lists all the users

mstr_pswd
    Change master password

entry
    New entry, takes in website name, username,
    and password and stores it encrypted

show <ID_xxxx>
    displays an entry of the corresponding ID

update <ID_xxxx>
    updates the entry of the corresponding ID

delete <ID_xxxx>
    deletes a specific entry

help
    displays this message

~$ about
