import "./App.css";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Verify from "./pages/Verify";
import Upload from "./pages/Upload";
import ConnectWallet from "./pages/ConnectWallet";
import { useState } from "react";
import { ethers } from "ethers";
// import ethereum from "window";

function App() {
  const [user, setUser] = useState(null);

  async function connectwallet() {
    const { ethereum } = window;
    const accounts = await ethereum.request({
      method: "eth_requestAccounts",
    });

    setUser(accounts[0]);

    console.log(accounts[0]);
  }

  return (
    <div className="App">
      <BrowserRouter>
        <Navbar user={user} />
        <Routes>
          <Route
            path="/"
            element={
              user ? <Home /> : <ConnectWallet connectwallet={connectwallet} />
            }
          />
          <Route
            path="/verify"
            element={
              user ? (
                <Verify />
              ) : (
                <ConnectWallet connectwallet={connectwallet} />
              )
            }
          />
          <Route
            path="/upload"
            element={
              user ? (
                <Upload user={user} />
              ) : (
                <ConnectWallet connectwallet={connectwallet} />
              )
            }
          />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
