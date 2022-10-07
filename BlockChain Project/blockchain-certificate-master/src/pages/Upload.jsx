import { ethers } from "ethers";
import React from "react";
import { useState } from "react";
import Button from "../components/Button";
import { CertificateContractAddress } from "../config.js";
import CertificateAbi from "../contracts/CertificateContract.json";
import Success from "../components/Success";

function Upload({ user }) {
  const [certHash, setCertHash] = useState("");
  const [studentWalletAddress, setStudentWalletAddress] = useState(null);
  const [studentName, setStudentName] = useState(null);
  const [issuerName, setIssuerName] = useState(null);
  const [stored, setStored] = useState(false);

  function handleUpload(e) {
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

      CertificateContract.addCertificate(
        certHash,
        user,
        studentWalletAddress,
        studentName,
        issuerName
      ).then((res) => {
        console.log(res);
        console.log("Stored");
        alert("Stored");
        setStored(true);
      });
    }
  }

  return (
    <div className="upload">
      <div className="upload-left-section">
        <h1>
          upload the certificate on{" "}
          <span className="highlight">blockchain</span>
        </h1>
      </div>
      <div className="upload-right-section">
        <div className="upload-right-heading">
          <h1>give the information</h1>
        </div>
        <div className="upload-right-input">
          <span>Student Name</span>
          <input
            type="text"
            placeholder="Type Here"
            onChange={(e) => {
              setStudentName(e.target.value);
            }}
          />
        </div>
        <div className="upload-right-input">
          <span>Student Wallet Address</span>
          <input
            type="text"
            placeholder="Type Here"
            onChange={(e) => {
              setStudentWalletAddress(e.target.value);
            }}
          />
        </div>
        <div className="upload-right-input">
          <span>Student Certificate Hash</span>
          <input
            type="text"
            placeholder="Type Here"
            onChange={(e) => {
              setCertHash(e.target.value);
            }}
          />
        </div>
        <div className="upload-right-input">
          <span>Issuer Name</span>
          <input
            type="text"
            placeholder="Type Here"
            onChange={(e) => {
              setIssuerName(e.target.value);
            }}
          />
        </div>
        <div className="upload-right-button">
          <Button text="upload" buttonAction={handleUpload} />
        </div>
      </div>
    </div>
  );
}

export default Upload;
