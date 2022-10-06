import "../App.css";
import image from "../assets/Next steps-pana.png";
import Button from "../components/Button";
import { Link } from "react-router-dom";

function Home() {
  return (
    <div className="home">
      <div className="home-container">
        <h1>
          Be the change by creating the{" "}
          <span className="highlight">digital certificate</span> using{" "}
          <span className="highlight">Blockchain</span>
        </h1>
        <Link to="/upload">
          <Button text="Explore" />
        </Link>
      </div>

      {/* <div className="home-feature">
        <div className="home-feature-section">
          <div className="home-feature-image">
            <img src={image} />
          </div>
          <span>feature1</span>
        </div>
        <div className="home-feature-section">
          <div className="home-feature-image">
            <img src={image} />
          </div>
          <span>feature1</span>
        </div>
      </div> */}
    </div>
  );
}

export default Home;
