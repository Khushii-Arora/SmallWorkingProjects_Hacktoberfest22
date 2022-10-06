import { useState } from "react";
import "../App.css";
import Button from "../components/Button";
import { CertificateContractAddress } from "../config.js";
import CertificateAbi from "../contracts/CertificateContract.json";
import { ethers } from "ethers";

function Verify() {
  const [hash, setHash] = useState(null);
  const [issuerAddress, setIssuerAddress] = useState(null);

  function handleVerify(e) {
    e.preventDefault();
    const { ethereum } = window;
    if (ethereum) {
      const provider = new ethers.providers.Web3Provider(ethereum);
      const signer = provider.getSigner();
      const CertificateContract = new ethers.Contract(
        CertificateContractAddress,
        CertificateAbi.abi,
        signer
      );

      CertificateContract.verifyCerticate(hash, issuerAddress)
        .then((res) => {
          if (res != "") {
            alert(res);
          } else {
            alert("Document not found");
          }

          // !res ? alert(res) : alert("Document not found");
        })
        .catch((err) => {
          alert("Account is fake");
        });
    }
  }

  return (
    <div className="verify">
      <div className="verify-left-section">
        <h1>
          Verify the certificate is{" "}
          <span className="highlight">Real or not?</span>
        </h1>
      </div>
      <div className="verify-right-section">
        <div className="verify-right-heading">
          <h1>give the information</h1>
        </div>
        <div className="verify-right-input">
          <span>Certificate Hash</span>
          <input
            type="text"
            placeholder="Type Here"
            onChange={(e) => {
              setHash(e.target.value);
            }}
          />
        </div>
        <div className="verify-right-input">
          <span>Issuer Wallet Address</span>
          <input
            type="text"
            placeholder="Type Here"
            onChange={(e) => {
              setIssuerAddress(e.target.value);
            }}
          />
        </div>
        <div className="verify-right-button">
          <Button text="Verify" buttonAction={handleVerify} />
        </div>
      </div>
    </div>
  );
}

export default Verify;
