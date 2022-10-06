import "../App.css";

function Button({ text, buttonAction }) {
  return (
    <button className="button" onClick={buttonAction}>
      {text}
    </button>
  );
}

export default Button;
