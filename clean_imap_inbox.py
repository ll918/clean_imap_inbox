#!/usr/bin/env python3.5
""" Delete unnecessary messages in Inbox from imap server.

Only tested with outlook.com.
"""
from imaplib import IMAP4_SSL
import os

imap_server = 'imap-mail.outlook.com'
port = 993
user = os.environ['OUTLOOK_USER']
pwd = os.environ['OUTLOOK_PASS']
folder = 'Inbox'
search_criteria = ['(FROM "Netflix")', '(FROM "eBay")', '(FROM "Popular")',
                   '(FROM "Skype")', '(FROM "Twitter")',
                   '(SUBJECT "Microsoft")'
                   ]


def delete_msg():
    """Delete messages in Inbox according to a list of search criteria."""
    count = 0
    with IMAP4_SSL(imap_server, port) as i:
        i.login(user, pwd)
        i.select(folder, readonly=False)
        for criteria in search_criteria:
            status, msg_uids = i.uid('search', None, criteria)
            if status != 'OK':
                print('Status:', status)
            for uid in msg_uids[0].split():
                typ, data = i.uid('store', uid, '+FLAGS', '\\Deleted')
                if typ != 'OK':
                    print('Status:', typ)
                else:
                    count += 1
        i.expunge()
    print('Deleted a total of', count, 'messages from', folder)


delete_msg()
