let currentAccount = null;

const ethereumButton = document.querySelector('.enableEthereumButton');
const showAccount = document.querySelector('.showAccount');
const getreceipt = document.querySelector('.getreceipt');
const txnhash = document.querySelector('.txnhash').value;
ethereumButton.addEventListener('click', () => {
    getAccount();
  });

  async function getAccount() {
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' })
      .catch((err) => {
        if (err.code === 4001) {
          // EIP-1193 userRejectedRequest error
          // If this happens, the user rejected the connection request.
          console.log('Please connect to MetaMask.');
        } else {
          console.error(err);
        }
      });
    const account = accounts[0];
    showAccount.innerHTML = account;
    ethereumButton.innerHTML = "connected!"
    currentAccount = account;
  }
  window.ethereum.request({ method: 'eth_accounts' })
  .then(handleAccountsChanged)
  .catch((err) => {
    // Some unexpected error.
    // For backwards compatibility reasons, if no accounts are available,
    // eth_accounts returns an empty array.
    console.error(err);
  });
  window.ethereum.on('accountsChanged', handleAccountsChanged);

// eth_accounts always returns an array.
function handleAccountsChanged(accounts) {
  if (accounts.length === 0) {
    // MetaMask is locked or the user has not connected any accounts.
    console.log('Please connect to MetaMask.');
    currentAccount = null;
  } else if (accounts[0] !== currentAccount) {
    // Reload your interface with accounts[0].
    currentAccount = accounts[0];
    // Update the account displayed (see the HTML for the connect button)
    showAccount.innerHTML = currentAccount;
  }
}
const chainId = await window.ethereum.request({ method: 'eth_chainId' });

window.ethereum.on('chainChanged', handleChainChanged);

function handleChainChanged(chainId) {
  // We recommend reloading the page, unless you must do otherwise.
  window.location.reload();
}

getreceipt.addEventListener('click', () => {
  getReceipt(txnhash);
});

async function getReceipt(txnhash){
  receipt = await window.ethereum.request({
    "method": "eth_getTransactionReceipt",
    "params": [
      txnhash
    ]
  });
}
