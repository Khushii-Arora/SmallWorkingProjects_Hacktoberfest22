import 'package:flutter/material.dart';
import 'calculate.dart';

class bottombuttonfunc extends StatelessWidget {


  String bartext;
  Function onTap;

  bottombuttonfunc({@required this.bartext,@required this.onTap});



  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onTap,
      child: Container(
        alignment: Alignment.center,
        height: 70,
        child: Text(bartext,
          style: TextStyle(
            fontWeight: FontWeight.w300,
            fontSize: 30,


          ),),

        margin: EdgeInsets.only(top: 20),
        width: double.infinity,
        color: Colors.red,
      ),
    );
  }
}
