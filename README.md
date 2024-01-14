# StellarLedger
Record transactions, split bills, simplify and repay debts with ease.\
[Demo Video](https://youtu.be/boo4ZobXwfg?feature=shared)
## Tech Stack
### Backend
1. Django
2. SQLite
3. Celery
### APIs
1. Metamask
2. Google Cloud API
3. Chart.js
### Frontend
1. Javascript
2. HTML
3. CSS
4. Bootstrap
## Features
Stellar Ledger has multiple features that users require to maintain their finances.\
**1. Record Transactions:** Stellar Ledger provides a user-friendly interface for effortlessly logging, updating, and removing transactions into categories. It also offers breakdowns of savings and expenses on a daily, weekly, monthly, and yearly basis.\
**2. Custom Categories:** Users can add and delete categories for transactions, and can view the graphical reports for the savings and expenses in different categories in the form of pie-charts.\
**3. Track Ethereum:** Ethereum users can connect to their Ethereum wallet, and send transactions to settle the bills with friends. Download transaction receipts in PDF format using the unique transaction hash for added convenience.\
**4. Split with friends:** Users can record debits and credits with friends, and receive timely email notifications for due dates, simplifying financial interactions within their social circle.\
**5. Simplify debts in groups:** Users can form groups, record transactions within the group, and obtain simplified debt summaries among members.\
**6. Split equally using broadcasts:** A user can equally split debts among multiple users without disclosing individual details. Also, secure the settlement process with debtor confirmation.\
**7. Recurring debts:** Users get weekly notifications about their recurring bills before their due dates.\

## Guide to use the project
1. Install python and pip.
2. First, fork and clone the repository.\
    `https://github.com/<username>/StellarLedger.git`
3. Set up the virtual environment.\
    `python3 -m venv <env_name>`
4. Start the virtual environment.\
    `source .<env_name>/bin/activate`
5. Step into the newly created stellarledger directory.\
   `cd stellarledger`
6.  Install the requirements.\
   `pip install -r requirements.txt`
7.  Run the migration into database schema.\
   `python3 manage.py migrate`
8.  Set the Google All-Auth API key in settings.py.\
    `EMAIL_HOST_PASSWORD = <your_password>`
9. Start the django server.\
    `python3 manage.py runserver`
