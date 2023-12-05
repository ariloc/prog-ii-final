#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "files.h"

void list_files(const char *path, const char *filesListPath) {
    char command[MAX_BUF]; // TODO: snprintf?
    sprintf(command, "cd %s && ls > ../../%s", path, filesListPath);
    system(command);
}

char** read_n_lines(FILE *fp, int n, int *linesReturned) {
    char* linesBuf[n+1], buf[MAX_BUF];

    int linesRead = 0;
    while (linesRead < n && fgets(buf,MAX_BUF,fp)) {
        int lineLen = strlen(buf)-1;
        buf[lineLen] = '\0'; // remove \n at end of line
        
        char *line = malloc(sizeof(char)*(lineLen+1));
        strcpy(line,buf);
        linesBuf[linesRead] = line;

        linesRead++;
    }

    char **lines = malloc(sizeof(char*)*linesRead);
    for (int i = 0; i < linesRead; i++)
        lines[i] = linesBuf[i];

    *linesReturned = linesRead;
    return lines;
}

char** read_filenames(const char *filesListPath, int *fileCount) {
    FILE* filesList = fopen(filesListPath,"r");
    return read_n_lines(filesList, MAX_FILES, fileCount);
}

void delete_file(char *path) {
    char command[MAX_BUF];
    sprintf(command,"rm %s",path); // snprintf?
    system(command);
}

char** get_file_paths(char *path, int *pathsCount) {
    list_files(path, FILES_LIST_PATH);

    int fileCount;
    char **paths = read_filenames(FILES_LIST_PATH, &fileCount);

    char buf[MAX_BUF];
    for (int i = 0; i < fileCount; i++) { // Replace filenames with added folder paths
        sprintf(buf, "%s/%s", path, paths[i]); // TODO: snprintf?

        char *path = malloc(sizeof(char)*(strlen(buf)+1));
        strcpy(path,buf);

        free(paths[i]);
        paths[i] = path;
    }
    *pathsCount = fileCount;

    delete_file(FILES_LIST_PATH);

    return paths;
}

char** get_text_paths(char* personName, int *pathsCount) {
    char textsPath[MAX_BUF]; // TODO: snprintf?
    sprintf(textsPath, "%s/%s", TEXTS_PATH, personName);

    return get_file_paths(textsPath, pathsCount);
}
