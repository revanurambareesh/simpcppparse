%{

/*Simple C++ Parser*/

#include <stdio.h>
#include <stdlib.h>
int scope=0;
int recordNum=0;
int linenum=1;

FILE *outfile;

void debugInfo()
{
	printf("\n\n====Line num: %d=====\n", linenum);
}

void declareFound(char* yytext)
{
	printf("Declaration statement found: %s\n", yytext);
	fprintf(outfile, "%s", "dec ");
	debugInfo();
}

void classFound(char* yytext)
{
	printf("Class found: %s\n", yytext);
	fprintf(outfile, "%s", "cla ");
	debugInfo();
}

void functionDecFound(char* yytext)
{
	printf("Function statement found: %s\n", yytext);
	fprintf(outfile, "%s", "fid ");
	debugInfo();
}

void verifyID(char* yytext)
{
	fprintf(outfile, "%s", "id ");
	debugInfo();
}

%}

num [0-9]+
validvar [a-zA-Z][0-9a-zA-Z]*
validmem [a-zA-Z][\.0-9a-zA-Z]*
arr \[[0-9]*\]
init [ ]*"="[ ]*[a-zA-Z0-9]+
normal ("int "|"float "|"char "|"double "|({validvar}" "))({validvar}({arr}?|{init}?),[ ]*)*{validvar}({arr}?|{init}?);
op "+"|"-"|"*"|"/"|"=="|"="|"!="|">"|">="|"<"|"<="|"+="|"-="|"*="|"/="
uop "++"|"--"

%%
[/][/][^\n]*[\n] {printf("Comment found:%s\n", yytext);}
"/*"[^("*/")]*"*/" {printf("Comment found\n");}
"\"".*"\"" {printf("literal found");fprintf(outfile, "%s", "id ");}
"#include"((" ")?)("<".*">")|("\"".*"\"") {printf("Found #include\n");fprintf(outfile, "%s", "i ");}
{normal} {declareFound(yytext);} /*verify_if_the_variable_is_classMem_or_Duplicate*/
"class "{validvar}(":"{validvar}(","{validvar})*)? {classFound(yytext);}
"if" {fprintf(outfile, "%s", "f ");}
"for" {fprintf(outfile, "%s", "for ");}
{op} {fprintf(outfile, "%s", "op ");}
"(" {fprintf(outfile, "%s", "( ");}
")" {fprintf(outfile, "%s", ") ");}
("int "|"float "|"char "|"double "){validvar}\([^(")")]*\);? {functionDecFound(yytext);}
"return "({validvar}|([0-9]*))";" {printf("Return found\n");fprintf(outfile, "%s", "ret ");}
["{"] {scope++;fprintf(outfile, "%s", "{ ");}
["}"] {scope--;fprintf(outfile, "%s", "} ");}
"cin" {fprintf(outfile, "%s", "cin ");}
"cout" {fprintf(outfile, "%s", "cout ");}
"<<" {fprintf(outfile, "%s", "< < ");}
">>" {fprintf(outfile, "%s", "> > ");}
"else" {fprintf(outfile, "%s", "el ");}
(" ")+|[\t]+ ;
[";"] fprintf(outfile, "%s", "; ");
"\n" {linenum++;fprintf(outfile, "%d ", linenum);}
{validmem} {printf("\n%s\n", yytext);verifyID(yytext);}
{num} {printf("\n%s\n", yytext);verifyID(yytext);}
. {printf("\nfailed: %s\n", yytext);}
%%

int yywrap()
{return 1;}

int main()
{
	yyin=fopen("sample.cpp", "r");
	outfile=fopen("output.txt", "w+");
	fprintf(outfile, "%s", "1 ");
	yylex();
	return 1;
}
