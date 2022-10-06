import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';

class iconcontent extends StatelessWidget {
  final IconData icicon;
  final String ictext;

  iconcontent({@required this.icicon, this.ictext});

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        Icon(
          icicon,
          size: 60,
          color: Colors.white,
        ),
        SizedBox(
          height: 20,
        ),
        Text(
          ictext,
          style: TextStyle(
            color: Colors.white,
            fontSize: 20,
          ),
        )
      ],
    );
  }
}
