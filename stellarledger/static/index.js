import "https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js";
let currentAccount = null;
const ethereumButton = document.querySelector('.enableEthereumButton');
const showAccount = document.querySelector('.showAccount');
const getreceipt = document.querySelector('.getreceipt');
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

document.getElementById("formid").addEventListener('submit', (e) => {
    e.preventDefault();
    let txnhash = document.getElementById("txnid").value;
    getReceipt(txnhash);
});

async function getReceipt(txnhash){
  var receipt = await window.ethereum.request({
    "method": "eth_getTransactionReceipt",
    "params": [
      txnhash
    ]
  });
  // console.log(receipt);
  let r = JSON.stringify(receipt).replace(/,/g, "\n").replace(/{/g, "").replace(/"/g, "\u0020");
  // console.log(r)
  window.jsPDF = window.jspdf.jsPDF
  const doc = new window.jsPDF({
    unit: "mm",
    orientation: "p",
    lineHeight: 2.0
  });
  // doc.addFont("Arimo-Regular.ttf", "Arimo", "normal");
  // doc.addFont("Arimo-Bold.ttf", "Arimo", "bold");
  doc.setFont("Times-Roman");
  // doc.setFontType("normal");
  doc.setFontSize(12);
  doc.text(r, 10, 10);
  doc.save('Receipt.pdf');
}