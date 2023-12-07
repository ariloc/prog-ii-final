#ifndef __FILES_H__

#include <stddef.h>
#include <stdio.h>

#define FILES_LIST_PATH "archivos.txt"  // Must be a name for a new file infolder folder
#define TEXTS_PATH "Textos"             // Must be the name of a folder inside the same one as the program is in

#define MAX_BUF 255

/**
 *  Function to be called when fopen returns NULL. Prints an error message to the user according
 *  to the mode in which the file was attempted to be opened, given as an argument.
 *
 *  @param path Path of the file that failed to be opened.
 *  @param mode The file access mode with which the file was attempted to be opened.
 */
void handle_file_open_error_rwa(char *path, char mode);

/**
 *  Overwrites a file list stored at @p filesListPath with a blank file. 
 *  Creates a new file at this path if it doesn't exist.
 *
 *  @param filesListPath Path of a file that contains a filename list of a folder.
 */
void reset_files_list(char *filesListPath);

/**
 *  Given the name of a person, returns the path to the folder that contains all of this person's
 *  texts.
 *  This folder should be named after the person, inside the directory located at #TEXTS_PATH.
 *
 *  @param personName The name of the person (without spaces).
 *  @return A file path where the person's texts should be located in.
 */
char* person_texts_path(char* personName);

/**
 *  Writes a list of the filenames in @p textsPath, to the file located at @p filesListPath.
 *  For this purpose, runs the commands 'cd' and 'ls' typically present in the host's command
 *  processor, under a Linux environment.
 *  As such, no file may be written to @p filesListPath in case of failure of the commands
 *  aforementioned (i.e. any of the paths isn't accessible or doesn't exist).
 *
 *  @param textsPath Path for a directory whose filenames within it will be listed.
 *  @param filesListPath Path of a file where the filnames of @p textsPath will be written.
 */
void list_texts(char *textsPath, char *filesListPath);

/**
 *  Counts the lines in the file at @p path.
 *  Lines are considered as any amount of text separated with \n (endline) characters or, of 
 *  course, the beginning / end of the file.
 *
 *  @param path Path of the file for which to count its lines.
 *  @return The amount of lines contained in the file at @path.
 */
int count_lines(char *path);

/**
 *  Reads all of the lines inside the file at @p path.
 *  <b>The length of each line stored is capped at #MAX_BUF.</b>
 *
 *  @param path Path to the file from which its lines will be read.
 *  @param lineCount A pointer to an integer where the amount of lines read will be stored.
 *  @return An array of pointers, each holding a reference to a string for each of the lines read
 *          from the file.
 */
char** read_lines(char *path, int *lineCount);

/**
 *  Given a path to a directory, prepends its path to each of the @p n filenames listed in 
 *  @p filenames.
 *
 *  @param directory Path of a directory which will be appended to the beginning of the filenames.
 *  @param filenames An array of pointers, each holding a reference to a string with a filename.
 *  @param n The amount of filenames provided.
 *  @return An array of pointers, each holding a reference to a new string containing the result
 *          of the concatenation of the directory path and each of the filenames given.
 */
char** append_directory_to_filenames(char *directory, char **filenames, int n);

/**
 *  Returns a list of paths with each of the texts written by @p personName.
 *  These texts should be contained in a folder named after the person, inside the directory 
 *  located at #TEXTS_PATH.
 *
 *  @param personName The name of the person (without spaces).
 *  @param pathsCount A pointer to an integer where the amount of paths returned will be stored.
 *  @return An array of pointers, each holding a reference to the path of a text written by the
 *          person, represented as a string.
 */
char** get_text_paths(char *personName, int *pathsCount);

#endif
