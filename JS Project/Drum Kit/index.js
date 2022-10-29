for (var i = 0; i < document.getElementsByClassName("drum").length; i++) {
    document
        .getElementsByClassName("drum")[i].addEventListener("click", function (){
            var alpha = this.innerHTML;
            handleClick(alpha);
            btnam(alpha);
        });
}

// function Audio(loc){
//     this.loc = loc;
//     this.play = function(){ 
//     }
// }

addEventListener("keydown", function (event){
    handleClick(event.key);
    btnam(event.key);
})

function handleClick(alpha) {
    switch (alpha) {
        case "w":
            var audio = new Audio("sounds/tom-1.mp3");
            audio.play();
            break;

        case "a":
            var audio = new Audio("sounds/tom-2.mp3");
            audio.play();
            break;

        case "s":
            var audio = new Audio("sounds/tom-3.mp3");
            audio.play();
            break;

        case "d":
            var audio = new Audio("sounds/tom-4.mp3");
            audio.play();
            break;

        case "j":
            var audio = new Audio("sounds/snare.mp3");
            audio.play();
            break;

        case "l":
            var audio = new Audio("sounds/kick-bass.mp3");
            audio.play();
            break;

        case "k":
            var audio = new Audio("sounds/crash.mp3");
            audio.play();
            break;

        default:
            console.log("wrong button");
    }
}

function btnam(btn){
    var active = document.querySelector("."+btn);
    console.log(active);
    document.getElementById(btn).classList.add("pressed");
    setTimeout(function(){
        document.getElementById(btn).classList.remove("pressed");
    });
}
