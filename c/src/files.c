#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "files.h"

void handle_file_open_error_rwa(char *path, char mode) {
    switch(mode) {
        case 'r':
            fprintf(stderr, "There was an error reading from %s.\nFile may not exist or you may not have permission to read it.\n", path);
            break;
        case 'w':
        case 'a':
            fprintf(stderr, "There was an error writing to %s.\nCheck path exists and you have permission to write in it.\n", path);
            break;
    }
    exit(1);
}

void reset_files_list(char *filesListPath) {
    FILE *fp = fopen(filesListPath, "w");
    if (fp == NULL)
        handle_file_open_error_rwa(filesListPath, 'w');
    fclose(fp);
}

char* person_texts_path(char* personName) {
    char* path = malloc(sizeof(char) * (strlen(TEXTS_PATH) + strlen(personName) + 2));
    sprintf(path, "%s/%s", TEXTS_PATH, personName);
    return path;
}

void list_texts(char *textsPath, char *filesListPath) {
    char command[MAX_BUF];
    sprintf(command, "cd %s 2>/dev/null && ls > ../../%s 2>/dev/null", textsPath, filesListPath);
    system(command);
}

int count_lines(char *path) {
    FILE *fp = fopen(path,"r");
    if (fp == NULL)
        handle_file_open_error_rwa(path, 'r');

    char c, prev = -1;
    int lines = 0;
    while ((c = (char)fgetc(fp)) != EOF) {
        if (c == '\n') {
            ++lines;
        }
        prev = c;
    }
    // Count last line if it doesn't end with '\n'
    // If prev == -1, the file is empty, therefore no lines should be counted.
    if (prev != '\n' && prev != -1) {
        ++lines;
    }

    fclose(fp);

    return lines;
}

char** read_lines(char *path, int *lineCount) {
    char buf[MAX_BUF];
    
    *lineCount = count_lines(path);
    char **lines = malloc(sizeof(char*) * (*lineCount));

    FILE *fp = fopen(path, "r");
    if (fp == NULL)
        handle_file_open_error_rwa(path, 'r');

    for (int i = 0; i < *lineCount; i++) {
        fgets(buf, MAX_BUF, fp);
        
        // Count characters before \n. Note that buf may not have \n if fgets encountered EOF.
        int lineLen = strcspn(buf, "\n");
        buf[lineLen] = '\0'; // Remove \n

        char *line = malloc(sizeof(char) * (lineLen+1));
        strcpy(line,buf);

        lines[i] = line;
    }

    fclose(fp);

    return lines;
}

char** append_directory_to_filenames(char *directory, char **filenames, int n) {
    char buf[MAX_BUF];
    char **paths = malloc(sizeof(char*) * n);

    for (int i = 0; i < n; i++) {
        sprintf(buf, "%s/%s", directory, filenames[i]);

        char *path = malloc(sizeof(char) * (strlen(buf)+1));
        strcpy(path,buf);

        paths[i] = path;
    }

    return paths;
}

char** get_text_paths(char* personName, int *pathsCount) {
    char *textsPath = person_texts_path(personName);

    // Overwrite files list as a blank file, possibly erasing contents from previous runs.
    reset_files_list(FILES_LIST_PATH); 

    list_texts(textsPath, FILES_LIST_PATH);

    int fileCount;
    char **filenames = read_lines(FILES_LIST_PATH, &fileCount);

    if (fileCount == 0) {
        fprintf(stderr, "There are no files in \"%s\" or the folder doesn't exist.\n", textsPath);
        exit(1);
    }

    char **paths = append_directory_to_filenames(textsPath, filenames, fileCount);
    *pathsCount = fileCount;

    // Free filenames array and textsPath
    for (int i = 0; i < fileCount; i++)
        free(filenames[i]);
    free(filenames);
    free(textsPath);

    return paths;
}
