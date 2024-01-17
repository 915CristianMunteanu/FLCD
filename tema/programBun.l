%{
#include <stdio.h>
#include <string.h>



typedef struct {
    char atom[100];
    int codAtom;
    int codTS;
} FIP;


FIP fip[300];

int fipIndex = 0;
int lineNumber = 1;


void addToFIP(char atom[], int codAtom, int codTS) {
    for (int i = 0; i < fipIndex; i++) {
        if (strcmp(fip[i].atom, atom) == 0) {
            return;
        }
    }

    if (fipIndex >= 300) {
        fprintf(stderr, "FIP array is full.\n");
        return;
    }

    if (strlen(atom) > 255) {
        fprintf(stderr, "Atom exceeds maximum length at line %d\n", lineNumber);
        return;
    }

    strncpy(fip[fipIndex].atom, atom, 99);
    fip[fipIndex].atom[99] = '\0';
    fip[fipIndex].codAtom = codAtom;
    fip[fipIndex].codTS = codTS;
    fipIndex++;
}



%}

/* Regular Definitions */
REAL_NUMBER  [+-]?(0|[1-9][0-9]*)(\.[0-9]+)?
IDENTIFIER   [a-z][a-z]*[0-9]*[a-z]*
CONSTANT     [A-Z][A-Z]*
STRING       \".*\"

%%
"int"      { addToFIP(yytext, 100, -1); }
"float"    { addToFIP(yytext, 101, -1); }
"if"       { addToFIP(yytext, 102, -1); }
"while"    { addToFIP(yytext, 103, -1); }
"cin"      { addToFIP(yytext, 104, -1); }
"cout"     { addToFIP(yytext, 105, -1); }
"daca"     { addToFIP(yytext, 106, -1); }
"atunci"   { addToFIP(yytext, 107, -1); }
"sfdaca"   { addToFIP(yytext, 108, -1); }
"+"        { addToFIP(yytext, 200, -1); }
"-"        { addToFIP(yytext, 201, -1); }
"*"        { addToFIP(yytext, 202, -1); }
"/"        { addToFIP(yytext, 203, -1); }
"<"        { addToFIP(yytext, 204, -1); }
"<="       { addToFIP(yytext, 205, -1); }
"="        { addToFIP(yytext, 206, -1); }
">="       { addToFIP(yytext, 207, -1); }
">"        { addToFIP(yytext, 208, -1); }
">>"       { addToFIP(yytext, 209, -1); }
"<<"       { addToFIP(yytext, 210, -1); }
"=="       { addToFIP(yytext, 211, -1); }
"&&"       { addToFIP(yytext, 212, -1); }
"!="       { addToFIP(yytext, 213, -1); }
"{"        { addToFIP(yytext, 300, -1); }
"}"        { addToFIP(yytext, 301, -1); }
"("        { addToFIP(yytext, 302, -1); }
")"        { addToFIP(yytext, 303, -1); }

[\n]         { ++lineNumber; }
[ \t\n]+     { /* Ignore whitespace */ }
.            { fprintf(stderr, "Illegal token %s at line %d\n", yytext, lineNumber); }

%%

int main(int argc, char** argv) {
    if (argc > 1) {
        FILE *file = fopen(argv[1], "r");
        if (!file) {
            fprintf(stderr, "Could not open file: %s\n", argv[1]);
            return 1;
        }

  	printf("Printing file contents:\n\n");
        char ch;
        while ((ch = fgetc(file)) != EOF) {
            putchar(ch);
        }
        printf("\n\nStarting lexical analysis...\n\n");
	    fseek(file, 0, SEEK_SET);
        yyin = file;
    }

    yylex();


    if (argc > 1) {
        fclose(yyin);
    }

    return 0;
}

int yywrap() {
    return 1;
}
