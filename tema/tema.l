%{
#include <stdio.h>
%}

%option noyywrap

%{
int left_bracket = 1;
int INT = 2;
int FLOAT = 2;
int VARIABILA = 3;
int CONSTANTA = 4;
int CIN = 5;
int COUT = 6;
int PLUS = 7;
int MINUS = 8;
int TIMES = 9;
int DIVIDE = 10;
int EQUALS = 11;
int IF = 12;
int WHILE = 13;
int EOL = 14;
%}

VAR [a-zA-Z][a-zA-Z0-9]*
CONST [A-Z][a-zA-Z0-9]*
DIGIT [0-9]

%%

"{"   printf("%d\n", left_bracket);
"}"   { return '}'; }
"int" printf("%d\n", INT);
"float" { return FLOAT; }

{VAR}+   { return VARIABILA; }
{CONST}+ { return CONSTANTA; }

"cin>>" { return CIN; }
"cout<<" { return COUT; }

"+" { return PLUS; }
"-" { return MINUS; }
"*" { return TIMES; }
"/" { return DIVIDE; }

"=" { return EQUALS; }

"if" { return IF; }
"while" { return WHILE; }

"(" { return '('; }
")" { return ')'; }
"\n" { return EOL; }

[<>{},;] { return yytext[0]; }

[ \t] { /* skip whitespace */ }

. { printf("Eroare la linia %d: Caracter neasteptat %s\n", yylineno, yytext); }

%%

int main() {
    yylex();
    return 0;
}
