/**
 *  @file file_utils.h
 *  @author Ariel Leonardo Fideleff
 */

#ifndef __FILE_UTILS_H__

#include <stddef.h>

/**
 *  Maximum buffer size used in the program.
 */
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
 *  Concatenates two paths into a <b>new</b> string.
 *  For example, given the paths, \"/hello/world\" and \"/bye/world\", the function would return
 *  \"/hello/world/bye/world\".
 *
 *  @param path1 The first path to concatenate.
 *  @param path2 The second path to concatenate.
 */
char* concatenate_paths(char *path1, char *path2);

/**
 *  Counts the lines in the file at @p path.
 *  Lines are considered as consecutive amounts of characters separated within @c \n (newline)
 *  characters or the beginning / end of the file.
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

#endif
