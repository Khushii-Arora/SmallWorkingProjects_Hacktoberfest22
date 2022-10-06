import 'package:flutter/material.dart';
import 'package:quiz_app/main.dart';

class Score extends StatelessWidget {
  Score(this.score, this.time);
  final int score;
  final Duration time;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        width: double.infinity,
        decoration: BoxDecoration(
          gradient: LinearGradient(colors: [
            Colors.blueAccent,
            Colors.indigo,
            Colors.purple,
          ], begin: Alignment.topCenter, end: Alignment.bottomCenter),
        ),
        child: SafeArea(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(
                'End of the Quiz!',
                style: TextStyle(
                    fontSize: 40, color: Colors.white, fontFamily: 'Lobster'),
              ),
              SizedBox(height: 15),
              Text(
                'RESULT',
                style: TextStyle(
                    fontSize: 80,
                    color: Colors.white,
                    fontFamily: 'Bebas_Neue'),
              ),
              SizedBox(height: 15),
              Text(
                'Your Score is ${(score * (600 - time.inSeconds)).floorToDouble()} ',
                style: TextStyle(fontSize: 30, color: Colors.white),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
