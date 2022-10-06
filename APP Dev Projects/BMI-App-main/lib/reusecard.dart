import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';

class ReuseCard extends StatelessWidget {
  Color colour;
  Widget cardchild;
  Function onPress;

  ReuseCard({@required this.colour, this.cardchild, this.onPress});

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onPress,
      child: Container(
        margin: EdgeInsets.all(10),
        child: cardchild,
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(20),
          color: colour,
        ),
      ),
    );
  }
}