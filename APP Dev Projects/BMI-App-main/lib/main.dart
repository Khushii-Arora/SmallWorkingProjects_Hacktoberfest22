import 'package:flutter/material.dart';
import 'input_page.dart';
import 'welcome.dart';

void main() => runApp(BMICalculator());

class BMICalculator extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Welcome(),
      theme: ThemeData(
          //colorScheme: ColorScheme.fromSwatch().copyWith(secondary: Colors.red),
          scaffoldBackgroundColor: Color(0xFF1D2136),
          colorScheme: ColorScheme.fromSwatch()
              .copyWith(primary: Color(0xFF1D2136))
              .copyWith(secondary: Colors.purple),
          textTheme: TextTheme(
            bodyText1: TextStyle(
              color: Colors.white,
            ),
            bodyText2: TextStyle(
            color: Colors.white,
          ),
          )),
    );
  }
}
