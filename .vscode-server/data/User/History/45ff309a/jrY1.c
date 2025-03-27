#include "shell.h"

/**
 * split_string - Splits an input string into an array of arguments
 * @input: The user input string to split
 * @command: the command to split
 * Return: An array of split arguments, or NULL on failure
 */
char **split_string(char *input, char **command)
{
    char **args = NULL;
    char *delim = " \n\t", *token;
    size_t i = 0, buffer = 2;

    token = strtok(input, delim);
    if (!token) {
        return NULL;
    }
    *command = strdup(token);
    if (!(*command)) {
        perror("Failed to allocate command");
        exit(EXIT_FAILURE);
    }
    args = malloc(buffer * sizeof(char *));
    if (!args) {
        perror("Failed to allocate args");
        free(*command);
        exit(EXIT_FAILURE);
    }
    while (token) {
        if (i >= buffer - 1) {
            buffer *= 2;
            args = realloc(args, buffer * sizeof(char *));
            if (!args) {
                perror("Failed to reallocate args");
                free(*command);
                exit(EXIT_FAILURE);
            }
        }
        token = strtok(NULL, delim);
        args[i] = token ? strdup(token) : NULL;
        if (!args[i++]) {
            perror("Failed to duplicate token");
            while (i--) {
                free(args[i]);
            }
            free(args);
            free(*command);
            exit(EXIT_FAILURE);
        }
    }
    args[i] = NULL;
    return args;
}
