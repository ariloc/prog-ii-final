#ifndef __FILES_H__

#include <stddef.h>
#include <stdio.h>

#define FILES_LIST_PATH "archivos.txt"
#define TEXTS_PATH "Textos"

#define MAX_BUF 255
#define MAX_FILES 100

void list_files(const char *path, const char *filesListPath);

char** read_n_lines(FILE *fp, int n, int *linesReturned);

char** read_filenames(const char *filesListPath, int *fileCount);

void delete_file(char *path);

char** get_file_paths(char *path, int *pathsCount);

char** get_text_paths(char *personName, int *pathsCount);

char** read_filenames(const char *filesListPath, int *fileCount);

#endif
