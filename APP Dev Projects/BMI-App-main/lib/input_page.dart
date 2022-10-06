import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'bottombar.dart';
import 'calculate.dart';
import 'reusecard.dart';
import 'iconcontent.dart';
import 'constants.dart';
import 'bigbrain.dart';

enum Gender {
  male,
  female,
}

class InputPage extends StatefulWidget {
  @override
  _InputPageState createState() => _InputPageState();
}

class _InputPageState extends State<InputPage> {

  int height = 180;
  int weight = 60;
  int age = 20;

Gender selectedGen;

  // Color malecard = DefaultCardColor;
  // Color femalecard = DefaultCardColor;

  // void Setcol(Gender selectedGen) {
  //   if (selectedGen == Gender.male) {
  //     if (malecard == DefaultCardColor) {
  //       malecard = ClickedCardColor;
  //       femalecard=DefaultCardColor;
  //     } else {
  //       malecard = DefaultCardColor;
  //     }
  //   }
  //   if (selectedGen == Gender.female) {
  //     if (femalecard == DefaultCardColor) {
  //       femalecard = ClickedCardColor;
  //       malecard=DefaultCardColor;
  //     } else {
  //       femalecard = DefaultCardColor;
  //     }
  //   }
  // }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('BMI CALCULATOR'),
        centerTitle: true,
      ),
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Expanded(
              child: Row(
            children: [
              Expanded(
                child: ReuseCard(
                  onPress: () {
                    setState(() {
                      selectedGen = Gender.male;
                    });
                  },
                  colour: selectedGen == Gender.male
                      ? ClickedCardColor
                      : DefaultCardColor,
                  cardchild: iconcontent(
                    icicon: FontAwesomeIcons.mars,
                    ictext: "MALE",
                  ),
                ),
              ),
              Expanded(
                child: ReuseCard(
                  onPress: () {
                    setState(() {
                      selectedGen = Gender.female;
                    });
                  },
                  colour: selectedGen == Gender.female
                      ? ClickedCardColor
                      : DefaultCardColor,
                  cardchild: iconcontent(
                    icicon: FontAwesomeIcons.venus,
                    ictext: "FEMALE",
                  ),
                ),
              ),
            ],
          )),
          Expanded(
            child: ReuseCard(
              colour: DefaultCardColor,
              cardchild: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: Text(
                        "HEIGHT",
                        style: TextStyle(
                          fontSize: 15,
                        ),
                      ),
                    ),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      crossAxisAlignment: CrossAxisAlignment.baseline,
                      textBaseline: TextBaseline.alphabetic,
                      children: [
                        Text(
                          height.toString(),
                          style: numtext,
                        ),
                        SizedBox(
                          width: 4,
                        ),
                        Text(
                          'CM',
                          style: TextStyle(
                            fontWeight: FontWeight.w400,
                            fontSize: 15,
                          ),
                        ),
                      ],
                    ),
                    Slider(
                        value: height.toDouble(),
                        min: 120.0,
                        max: 220.0,
                        activeColor: Colors.red,
                        inactiveColor: Colors.white70,
                        onChanged: (double val) {
                          setState(() {
                            height = val.round();
                            print("CHANGING: $val");
                          });
                        }),
                  ]),
            ),
          ),
          Expanded(
              child: Row(
            children: [
              Expanded(
                child: ReuseCard(
                  colour: DefaultCardColor,
                  cardchild: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Text('WEIGHT'),
                      Text(
                        weight.toString(),
                        style: numtext,
                      ),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          FloatingActionButton(
                            backgroundColor: Colors.red,
                            child: Icon(
                              FontAwesomeIcons.plus,
                            ),
                            onPressed: () {
                              setState(() {
                                weight++;
                              });
                            },
                          ),
                          SizedBox(
                            width: 20,
                          ),
                          FloatingActionButton(
                            backgroundColor: Colors.red,
                            child: Icon(
                              FontAwesomeIcons.minus,
                            ),
                            onPressed: () {
                              if (weight > 0) {
                                setState(() {
                                  weight--;
                                });
                              }
                            },
                          )
                        ],
                      )
                    ],
                  ),
                ),
              ),
              Expanded(
                child: ReuseCard(
                  colour: DefaultCardColor,
                  cardchild: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Text('AGE'),
                      Text(
                        age.toString(),
                        style: numtext,
                      ),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          FloatingActionButton(
                            backgroundColor: Colors.red,
                            child: Icon(
                              FontAwesomeIcons.plus,
                            ),
                            onPressed: () {
                              setState(() {
                                age++;
                              });
                            },
                          ),
                          SizedBox(
                            width: 20,
                          ),
                          FloatingActionButton(
                            backgroundColor: Colors.red,
                            child: Icon(
                              FontAwesomeIcons.minus,
                            ),
                            onPressed: () {
                              setState(() {
                                age--;
                              });
                            },
                          )
                        ],
                      )
                    ],
                  ),
                ),
              ),
            ],
          )),
          bottombuttonfunc(
            bartext: "CALCULATE",
            onTap: () {
              bigbrain b = bigbrain(h: height,w: weight);
              Navigator.push(context,
                  MaterialPageRoute(builder: (context) => calculate(
                    bm: b.calc(),
                    bmims: b.bmimsg(),
                    bmitex: b.bmitext(),
                  )));
            },
          ),
        ],
      ),
    );
  }
}
