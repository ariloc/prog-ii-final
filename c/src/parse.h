#ifndef __PARSE_H__

#include <stddef.h>
#include <stdio.h>

#define INPUTS_PATH "Entradas"

void parse_file (FILE* input, FILE* output);

void sanitize_files(int n, char **inputPaths, char *outputPath);

void sanitize_texts(char *personName);

#endif
