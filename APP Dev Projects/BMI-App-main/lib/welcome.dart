import 'package:bmi_calculator/input_page.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';

class Welcome extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Center(
              child: Container(
                height: 200,
                width: 200,
                decoration: BoxDecoration(
                  image: DecorationImage(
                    image: AssetImage('assets/wel.png'),
                    fit: BoxFit.fill,
                  ),
                ),
              ),
            ),
            SizedBox(
              height: 50,
            ),
            Text(
              "WELCOME ",
              style: TextStyle(
                fontSize: 40,
                fontWeight: FontWeight.w300,
              ),
            ),
            SizedBox(
              height: 20,
            ),
            
            GestureDetector(
              onTap: (){
                Navigator.pushReplacement(context,
                    MaterialPageRoute(builder: (context) => InputPage()));
              },
              child: Icon(
                FontAwesomeIcons.arrowCircleRight,
                color: Colors.red,
                size: 60,

              ),
            ),



          ],
        ),
      ),
    );
  }
}
