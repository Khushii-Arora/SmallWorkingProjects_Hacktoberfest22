import 'package:flutter/material.dart';
import 'package:quiz_app/Scoreboard.dart';
import 'package:quiz_view/quiz_view.dart';
import 'QNA_Data/QuesBank.dart';
import 'QNA_Data/AnsBank.dart';
import 'QNA_Data/WrongAns.dart';
import 'package:flutter_timer_countdown/flutter_timer_countdown.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'GDSC',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: MyHomePage('GDSC Quiz App'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage(this.title);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int index = 0;
  int qno = 1;
  int score = 0;
  DateTime date1 = DateTime.now();
  @override
  Widget build(BuildContext context) {
    return index < 10
        ? Scaffold(
            backgroundColor: Colors.blue,
            appBar: AppBar(
              centerTitle: true,
              title: ListTile(
                trailing: TimerCountdown(
                  timeTextStyle: TextStyle(color: Colors.white, fontSize: 15),
                  colonsTextStyle: TextStyle(color: Colors.white),
                  descriptionTextStyle: TextStyle(color: Colors.white),
                  format: CountDownTimerFormat.minutesSeconds,
                  endTime: DateTime.now().add(
                    Duration(
                      minutes: 1,
                    ),
                  ),
                  onEnd: () {
                    Navigator.push(
                        context,
                        MaterialPageRoute(
                            builder: (context) => Score(
                                score, DateTime.now().difference(date1))));
                  },
                ),
                title: Text(
                  widget.title,
                  style: TextStyle(color: Colors.white, fontSize: 18),
                ),
              ),
            ),
            body: QuizView(
              image: Container(
                height: 150,
                child: Image.asset("images/flutter.webp"),
              ),
              showCorrect: false,
              tagBackgroundColor: Colors.blue,
              tagColor: Colors.white,
              questionTag: "Question: $qno",
              answerColor: Colors.blue,
              answerBackgroundColor: Colors.white,
              questionColor: Colors.white,
              backgroundColor: Colors.blue,
              width: MediaQuery.of(context).size.width,
              height: 600,
              question: QuesBank().questionBank[index].question,
              rightAnswer: AnsBank().answerBank[index].answer,
              wrongAnswers: Incorrect().wrongAnswers[index].wrong,
              onRightAnswer: () {
                setState(() {
                  index++;
                  qno++;
                  score++;
                });
              },
              onWrongAnswer: () {
                setState(() {
                  index++;
                  qno++;
                });
              },
            ),
          )
        : Score(score, DateTime.now().difference(date1));
  }
}
