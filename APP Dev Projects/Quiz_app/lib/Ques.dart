import 'package:flutter/rendering.dart';

class Question {
  Question(this.question);
  final String question;
}

class Answer {
  Answer(this.answer);
  final String answer;
}

class Wrong {
  Wrong(this.wrong);
  final List<String> wrong;
}
