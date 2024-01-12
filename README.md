# StellarLedger
Record transactions, split bills, simplify and repay debts with ease.
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
## Challenges I ran into
#### Graph Algorithm
 The group transactions are represented in the form of graphs and the graph edges are recorded into the database to use the algorithm to minimize cash flow between friends automatically when a transaction is recorded.

#### Generating receipts
Another challenge was getting the transaction receipt from the transaction in the form of a PDF.

## Future Scope
1. Automated Transaction Import.
2. Classification using Transaction IDs.
3. Predict trends in expenditure.
4. Multiple methods to repay debts.

## Guide to use the project
1. First, fork and clone the repository.
2. Step into the newly created stellarledger directory.
3.  Install the requirements.
4.  Run the migration into database schema.
5.  Set the Google All-Auth API key.
6.  Set up Celery API key.
