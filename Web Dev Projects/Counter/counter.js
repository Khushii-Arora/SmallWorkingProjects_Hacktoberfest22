const counter = document.querySelector("#counter");
const btns = document.querySelectorAll(".btn");

let count = 0;

btns.forEach((btn) => {
  btn.addEventListener("click", (e) => {
    const ups = e.currentTarget.classList;

    if (ups.contains("increase")) 
    {
      count++;
      counter.classList.add("up");

      setTimeout(() => {
        counter.classList.remove("up");
      }, 500);
    } 
    else if (ups.contains("decrease")) 
    {
      count--;
      counter.classList.add("down");

      setTimeout(() => {
        counter.classList.remove("down");
      }, 500);
    } 
    else 
    {
      count = 0;
    }

    counter.textContent = count;
  });
});