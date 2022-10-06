import 'package:flutter/cupertino.dart';
import 'dart:math';

class bigbrain{
  int height;
  int weight;

  double _bmi;

  bigbrain({@required int h,@required int w}){
    height=h;
    weight=w;
  }

  String calc()
  {
    _bmi= weight/pow(height/100, 2);
    return _bmi.toStringAsFixed(1);
  }


  String bmitext()
  {
    if(_bmi>=25)
      {
        return 'Overweight';
      }
    else if(_bmi>=18.5)
      {
        return 'Normal';
      }
    else
      {
        return 'Underweight';
      }
  }

  String bmimsg()
  {
    if(_bmi>=25)
    {
      return 'You need to do some exercise ! ';
    }
    else if(_bmi>=18.5)
    {
      return 'You are too good to go !';
    }
    else
    {
      return 'You need to eat more !';
    }
  }

}

