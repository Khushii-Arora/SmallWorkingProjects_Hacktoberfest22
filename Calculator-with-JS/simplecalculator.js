var input = document.getElementById("screen");
var operator = ['+','-','x','/'];
var decimalAdded = false;

function Stack() {
    this.datastore = [];
    this.tos = 0;
    this.push = function (element) {
        this.datastore[this.tos++] = element;
    }
    this.pop = function () {
        return this.datastore[--this.tos];
    }
    this.peek = function () {
        return this.datastore[this.tos-1];
    }
    this.length = function () {
        return this.tos;
    }
}

function processResetButton()
{
    input.value = "0";
    decimalAdded = false;
}

function processEqualsButton()
{
    var equation = input.value;
    var lastChar = equation.substring(equation.length - 1);
    equation = equation.replace(/x/g,'*');

    if(equation.indexOf("%") > -1)
    {
        var res = equation.split('%');
        input.value = (res[0]/100)*res[1];
    }
    else
    {
        if(operator.indexOf(lastChar) > -1)
        {
            equation = equation.substring(0, equation.length - 1);
        }
        if(equation != '')
        {
            if(checkParentheses(equation) == true)
            {
                var postfix = shuntingYardAlgorithm(equation);
                var result = evaluatePostfixExpression(postfix);
                input.value = result;
            }
            else
                input.value = "Unmatched Parentheses";
        }
           
    }

    if(input.value.indexOf('.') > -1)
        decimalAdded = true;
    else
        decimalAdded = false;

}

function processOperatorButton(btnValue)
{
    var inputVal = input.value;
    var lastChar = inputVal.substring(inputVal.length - 1);
    var btnVal = btnValue;

    if(inputVal!='' && operator.indexOf(lastChar) == -1)
    {
        input.value += " " + btnVal + " ";
    }
    else if(inputVal == '' && btnVal == '-')
    {
        input.value += " " + btnVal + " ";
    }

    if(operator.indexOf(lastChar) > -1 && inputVal.length > 1)
    {
       
        input.value = inputVal.substring(0, inputVal.length - 1) + btnVal;
    }

    decimalAdded = false;

}

function processDecimalButton(btnValue)
{
    var btnVal = btnValue;

    if(!decimalAdded)
    {
        input.value += btnVal;
        decimalAdded = true;
    }
}

function processNumberButton(btnValue)
{
    if(input.value == '0')
        input.value="";

    var btnVal = btnValue;
    input.value += btnVal;
  

}

function processPercentageButton(btnValue)
{
    var inputVal = input.value;
    var btnVal = btnValue;

    if(inputVal!='' && inputVal.indexOf('-') == -1 && inputVal.indexOf('+') == -1
        && inputVal.indexOf('/') == -1 && inputVal.indexOf('x') == -1 && inputVal.indexOf('^') == -1
        && inputVal.indexOf('(') == -1 && inputVal.indexOf(')') == -1
        && inputVal.indexOf('%') == -1)
    {
        input.value += btnVal;
    }
}

function processParenthesesButton(btnValue)
{
    if(input.value == '0')
        input.value="";

    var btnVal = btnValue;

    if(btnVal == '(')
        input.value += btnVal + " ";
    else
        input.value += " " + btnVal;

    decimalAdded = false;
}

function checkParentheses(expression)
{
    var s =  new Stack();

    for(var i=0; i<expression.length; i++)
    {
        if(expression[i] == '(')
            s.push(expression[i]);
        else if(expression[i] == ')')
            s.pop();
    }

    if(s.length() == 0)
    {
        console.log("balanced");
        return true;
    }
    else
    {
        console.log("unbalanced");
        return false;
    }

}



function shuntingYardAlgorithm(expression)
{
    var operators = '+-/*^';
    var precedence = {'^':4,'*':3,'/':3,'+':2,'-':2};
    var associative = {'^':'Right','*':'Left','/':'Left','+':'Left','-':'Left'};
    var postfix="";
    var s = new Stack();
    var token;
    var operator1;
    var operator2;

    var res1 = expression.split(" ");

    for(var i=0; i<res1.length; i++)
    {
        token = res1[i];

        if(operators.indexOf(token) == -1 && token != '(' && token != ')')
            postfix+=token + " ";
        else if(operators.indexOf(token) > -1)
        {
            operator1 = token;
            operator2 = s.peek();
            while(operators.indexOf(operator2) > -1 && ((associative[operator2] == 'Left' && precedence[operator1] <= precedence[operator2]) ||
                (associative[operator2] == 'Right' && precedence[operator1] < precedence[operator2])))
            {
                postfix+=operator2 + " ";
                s.pop();
                operator2 = s.peek();
            }
            s.push(operator1);
        }
        else if(token == '(')
        {
            s.push(token);
        }
        else if(token == ')')
        {
            while(s.peek() != '(')
            {
                postfix += s.pop() + " ";
            }
            s.pop();
        }
    }

    while (s.length()>0){
        postfix += s.pop() + " ";
    }

    console.log(postfix);
    return postfix;
}

function evaluatePostfixExpression(postfix)
{
    var operators = '+-/*^';
    var s = new Stack();
    var res2 = postfix.split(" ");

    for(var j=0; j<res2.length - 1; j++)
    {
        if(operators.indexOf(res2[j]) == -1)
        {
            s.push(res2[j]);
        }
        else
        {
            var op1 = s.pop();
            var op2 = s.pop();
            var interResult = processIntermediateResult(op1, op2, res2[j]);
            s.push(interResult);
        }
    }

    return s.pop();

}

function processIntermediateResult(operand1, operand2, operator)
{
    var interResult;

        switch (operator){
        case '+':
            interResult = Number(operand2) + Number(operand1);
            break;
        case '-':
            interResult = Number(operand2) - Number(operand1);
            break;
        case '*':
            interResult = Number(operand2) * Number(operand1);
            break;
        case '/':
            interResult = Number(operand2) / Number(operand1);
            break;
        case '^':
            interResult = Math.pow(Number(operand2), Number(operand1));
            break;
        default:
            console.log("could not be processed");
        }

    return interResult;
}
