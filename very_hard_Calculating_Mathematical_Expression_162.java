//"""
//Calculating Mathematical Expression
//Create a function that takes a mathematical expression as a string, list of numbers on which the mathematical expression is to be calculated and return the result as a list of string.
//
//Examples
//mathematical("f(y)=y+1",[1,2]) ➞ ["f(1)=2","f(2)=3"]
//
//mathematical("f(y)=y^2",[1,2,3]) ➞ ["f(1)=1","f(2)=4","f(3)=9"]
//
//mathematical("f(y)=yx3",[1,2,3]) ➞ ["f(1)=3","f(2)=6","f(3)=9"]
//Notes
//List of numbers are positive integers.
//In the algebraic expression x = *
//"""

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class very_hard_Calculating_Mathematical_Expression_162 {
    public static List<String> mathematical(String exp, List<Integer> numbers) {
        String expression = exp.split("=")[1].replace("^", "**").replace("x", "*");
        List<String> total = new ArrayList<>();
        for (int y : numbers) {
            String replacedExpression = expression.replace("y", Integer.toString(y));
            double result = evaluateExpression(replacedExpression);
            total.add(String.format("f(%d)=%.1f", y, result));
        }
        return total;
    }

    // メインの数式評価メソッド
    public static double evaluateExpression(String expression) {
        char[] tokens = expression.toCharArray();
        Stack<Double> values = new Stack<>();
        Stack<Character> ops = new Stack<>();
        for (int i = 0; i < tokens.length; i++) {
            if (tokens[i] >= '0' && tokens[i] <= '9') {
                StringBuilder sbuf = new StringBuilder();
                while (i < tokens.length && (tokens[i] >= '0' && tokens[i] <= '9' || tokens[i] == '.')) {
                    sbuf.append(tokens[i++]);
                }
                values.push(Double.parseDouble(sbuf.toString()));
                i--;
            } else if (tokens[i] == '(') {
                ops.push(tokens[i]);
            } else if (tokens[i] == ')') {
                while (!ops.isEmpty() && ops.peek() != '(') {
                    values.push(applyOp(ops.pop(), values.pop(), values.pop()));
                }
                if (!ops.isEmpty() && ops.peek() == '(') {
                    ops.pop();
                } else {
                    throw new IllegalArgumentException("Invalid expression: Unmatched parentheses");
                }
            } else if (tokens[i] == '+' || tokens[i] == '-' || tokens[i] == '*' || tokens[i] == '/' || tokens[i] == '^') {
                while (!ops.isEmpty() && hasPrecedence(tokens[i], ops.peek())) {
                    values.push(applyOp(ops.pop(), values.pop(), values.pop()));
                }
                ops.push(tokens[i]);
            }
        }
        while (!ops.isEmpty()) {
            values.push(applyOp(ops.pop(), values.pop(), values.pop()));
        }
        if (values.size() != 1) {
            throw new IllegalArgumentException("Invalid expression");
        }
        return values.pop();
    }

    // 演算子の適用
    public static double applyOp(char op, double b, double a) {
        switch (op) {
            case '+':
                return a + b;
            case '-':
                return a - b;
            case '*':
                return a * b;
            case '/':
                if (b == 0) {
                    throw new UnsupportedOperationException("Cannot divide by zero");
                }
                return a / b;
            case '^':
                return Math.pow(a, b);
        }
        return 0;
    }

    // 演算子の優先順位を確認
    public static boolean hasPrecedence(char op1, char op2) {
        if (op2 == '(' || op2 == ')') {
            return false;
        }
        if ((op1 == '*' || op1 == '/' || op1 == '^') && (op2 == '+' || op2 == '-')) {
            return false;
        }
        return true;
    }

    public static void main(String[] args) {
        List<Integer> numbers1 = List.of(1, 2);
        List<Integer> numbers2 = List.of(1, 2, 3);
        List<Integer> numbers3 = List.of(3, 6, 9);
        System.out.println(mathematical("f(y)=y+1", numbers1));
        System.out.println(mathematical("f(y)=y^2", numbers2));
        System.out.println(mathematical("f(y)=y*3", numbers2));
        System.out.println(mathematical("f(y)=y-2", numbers2));
        System.out.println(mathematical("f(y)=y/3", numbers3));
    }
}

