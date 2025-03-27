#include "shell.h"

/**
 * split_string - split an input string into an array of arguments
 * @input: The user input string to split
 * @command: the command to split
 * Return: An array of split arguments, or NULL on failure.
 */
char **split_string(char *input, char **command) {
    char **args = NULL;
    char *delim = " \n\t", *token;
    size_t i = 0, buffer = 2;

    token = strtok(input, delim);
    if (!token) {
        return NULL; // Immediate return if no tokens found
    }
    *command = strdup(token);
    if (!(*command)) {
        perror("Failed to allocate command");
        return NULL;
    }
    args = malloc(buffer * sizeof(char *));
    if (!args) {
        perror("Failed to allocate args");
        free(*command);
        return NULL;
    }
    do {
        if (i >= buffer - 1) {
            buffer *= 2;
            char **new_args = realloc(args, buffer * sizeof(char *));
            if (!new_args) {
                perror("Failed to reallocate args");
                for (size_t j = 0; j < i; j++) free(args[j]);
                free(args);
                free(*command);
                return NULL;
            }
            args = new_args;
        }
        args[i++] = strdup(token);
        if (!args[i - 1]) {
            perror("Failed to duplicate token");
            for (size_t j = 0; j < i; j++) free(args[j]);
            free(args);
            free(*command);
            return NULL;
        }
    } while ((token = strtok(NULL, delim)));

    args[i] = NULL;
    return args;
}
