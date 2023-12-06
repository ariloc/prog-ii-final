#ifndef __FILES_H__

#include <stddef.h>
#include <stdio.h>

#define FILES_LIST_PATH "archivos.txt"
#define TEXTS_PATH "Textos"

#define MAX_BUF 255

char* person_texts_path(char* personName);

void list_texts(char *personName, char *filesListPath);

int count_lines(char *path);

char** read_lines(char *path, int *lineCount);

char** append_directory_to_filenames(char *directory, char **filenames, int n);

char** get_text_paths(char *personName, int *pathsCount);

#endif
