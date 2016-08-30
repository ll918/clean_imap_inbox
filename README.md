# clean_imap_inbox
Python 3 script that delete unnecessary messages in Inbox from imap server
according to a list of search criteria.

Only tested with outlook.com.

## How to run
1. Modify the search_criteria list so it's relevant to the Inbox cleaned.
2. Set the following environment variables:
    * OUTLOOK_USER (the whole email)
    * OUTLOOK_PASS
3. From the command line run: python3 clean_imap_inbox.py.

## N.B.
The double quotes used in search_criteria for the criteria string appear to be
necessary for the code to work.