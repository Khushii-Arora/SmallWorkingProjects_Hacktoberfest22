import "../App.css";
import { Link } from "react-router-dom";

function Navbar({ user }) {
  return (
    <div className="header">
      <div className="header-container">
        <div className="left-section">
          <Link to="/" className="heading">
            blockcert
          </Link>
        </div>

        <div className="middle-section">
          <Link to="/verify" className="links">
            <span>verify</span>
          </Link>

          <Link to="/upload" className="links">
            <span>upload</span>
          </Link>
        </div>

        <div className="right-section">
          <div className="account-section">
            <img src="https://img.freepik.com/free-vector/businessman-character-avatar-isolated_24877-60111.jpg?w=2000" />
          </div>
        </div>
      </div>
    </div>
  );
}

export default Navbar;
