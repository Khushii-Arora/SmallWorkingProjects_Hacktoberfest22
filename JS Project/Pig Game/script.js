'use strict';

//Selecting elements
const player0El = document.querySelector('.player--0');
const player1El = document.querySelector('.player--1');
const score0El = document.querySelector('#score--0');
const score1El = document.getElementById('score--1');
const current0El = document.getElementById('current--0');
const current1El = document.getElementById('current--1');
const diceEl = document.querySelector('.dice');
const btnNew = document.querySelector('.btn--new');
const btnRoll = document.querySelector('.btn--roll');
const btnHold = document.querySelector('.btn--hold');

// setting global scope
let scores, currentScore, activePlayer, playing;

const init = function () {
  // current score variable
  currentScore = 0;
  activePlayer = 0;
  scores = [0, 0];
  playing = true;

  // starting conditions
  score0El.textContent = 0;
  score1El.textContent = 0;
  current0El.textContent = 0;
  current1El.textContent = 0;
  diceEl.classList.add('hidden');
  player0El.classList.remove('player--winner');
  player1El.classList.remove('player--winner');
  player1El.classList.add('player--active');
  player1El.classList.remove('player--active');
};

// calling the initialise function
init();

const switchPlayer = function () {
  //  set current score of the person to 0
  currentScore = 0;
  document.getElementById(`current--${activePlayer}`).textContent =
    currentScore;
  // switch to next player
  activePlayer = activePlayer === 0 ? 1 : 0;
  player0El.classList.toggle('player--active');
  player1El.classList.toggle('player--active');
};

//rolling dice
btnRoll.addEventListener('click', function () {
  if (playing) {
    //generate random number
    const dice = Math.trunc(Math.random() * 6) + 1;
    // const dice = Math.trunc(Math.random() * 7);

    //display dice
    diceEl.classList.remove('hidden');
    //retrieve the image with the number of dice
    diceEl.src = `dice-${dice}.png`;

    //check for rolled dice if it's one

    if (dice !== 1) {
      //add dice number to current score
      currentScore += dice;
      document.getElementById(`current--${activePlayer}`).textContent =
        currentScore;
    } else {
      switchPlayer();
    }
  }
});

btnHold.addEventListener('click', function () {
  if (playing) {
    // add current score to score of active player
    scores[activePlayer] += currentScore;
    // ie.. scores[1]= scores[1]+currentScore
    document.getElementById(`score--${activePlayer}`).textContent =
      scores[activePlayer];

    // check if score is 100
    if (scores[activePlayer] >= 100) {
      // if true then finish game
      playing = false;
      // hide the dice
      diceEl.classList.add('hidden');
      document
        .querySelector(`.player--${activePlayer}`)
        .classList.add('player--winner');
      document
        .querySelector(`.player--${activePlayer}`)
        .classList.remove('player--active');
    }

    // else switch to next player
    else {
      switchPlayer();
    }
  }
});

btnNew.addEventListener('click', init);
