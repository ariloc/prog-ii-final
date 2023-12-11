#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "file_utils.h"
#include "files.h"

char* person_texts_path(char* personName) {
    return concatenate_paths(TEXTS_PATH, personName);
}

void reset_files_list(char *filesListPath) {
    FILE *fp = fopen(filesListPath, "w");
    if (fp == NULL)
        handle_file_open_error_rwa(filesListPath, 'w');
    fclose(fp);
}

void list_texts(char *textsPath, char *filesListPath) {
    char command[MAX_BUF];
    sprintf(command, "cd %s 2>/dev/null && ls > ../../%s 2>/dev/null", textsPath, filesListPath);
    system(command);
}

char** prepend_directory_to_filenames(char *directory, char **filenames, int n) {
    char **paths = malloc(sizeof(char*) * n);

    for (int i = 0; i < n; i++) 
        paths[i] = concatenate_paths(directory, filenames[i]);

    return paths;
}


char** get_text_paths(char* personName, int *pathsCount) {
    char *textsPath = person_texts_path(personName);

    // Overwrite files list as a blank file, erasing contents from previous runs if any.
    reset_files_list(FILES_LIST_PATH); 

    list_texts(textsPath, FILES_LIST_PATH);

    int fileCount;
    char **filenames = read_lines(FILES_LIST_PATH, &fileCount);

    if (fileCount == 0) {
        fprintf(stderr, "There are no files in \"%s\", the folder doesn't exist or you don't have permission to read from it.\n", textsPath);
        exit(1);
    }

    char **paths = prepend_directory_to_filenames(textsPath, filenames, fileCount);
    *pathsCount = fileCount;

    // Free filenames array and textsPath
    for (int i = 0; i < fileCount; i++)
        free(filenames[i]);
    free(filenames);
    free(textsPath);

    return paths;
}

char* sanitized_file_path(char *personName) {
    char filename[MAX_BUF];
    sprintf(filename, "%s.txt", personName);

    char *sanitizedFilePath = concatenate_paths(INPUTS_PATH, filename);

    return sanitizedFilePath;
}
