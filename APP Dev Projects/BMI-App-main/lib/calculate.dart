import 'package:bmi_calculator/bottombar.dart';
import 'package:bmi_calculator/constants.dart';
import 'package:bmi_calculator/reusecard.dart';
import 'package:flutter/material.dart';

class calculate extends StatelessWidget {

  calculate({@required String bmims,@required String bmitex,@required String bm})
  {
    bmimsg=bmims;
    bmitext=bmitex;
    bmi=bm;
  }

  String bmimsg='';
  String bmitext='';
  String bmi='';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text('BMI CALCULATOR'),
          centerTitle: true,
        ),
        body: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Expanded(
              child: Container(
                alignment: Alignment.center,
                child: Text(
                  "YOUR RESULT",
                  style: TextStyle(
                    fontSize: 40,
                    fontWeight: FontWeight.w300,
                  ),
                ),
              ),
            ),
            Expanded(

                flex: 5,
                child: ReuseCard(
                    colour: DefaultCardColor,
                    cardchild: Column(
                      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                      crossAxisAlignment: CrossAxisAlignment.center,
                      children: [
                        Text(bmitext,
                        style: ansstyle,
                        ),
                        Text(bmi,
                        style: TextStyle(
                            color: Colors.yellow,
                            fontSize: 70
                        )),
                        Text(bmimsg,style: TextStyle(
                          color: Colors.greenAccent,
                          fontSize: 20
                        ),)
                      ],
                    ))),
            bottombuttonfunc(
                bartext: "RE-CALCULATE",
                onTap: () {
                  Navigator.pop(context);
                })
          ],
        ));
  }
}
