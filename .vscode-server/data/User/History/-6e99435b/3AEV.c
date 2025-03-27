#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>
#include "shell.h"
/**
 * read_input - Function that read the input line
 * entred by the user
 * @av: the string to read
 * @env: environment variable
 *
 */

void read_input() {
    char *input = NULL;
    size_t input_size = 0;
    ssize_t n_char;
    pid_t child_pid;
    int status;

    while (1) {
        if (isatty(STDIN_FILENO))
            printf("cisfun$ ");

        n_char = getline(&input, &input_size, stdin);
        if (n_char == -1) {
            free(input);
            exit(EXIT_FAILURE);
        }

        if (input[n_char - 1] == '\n')
            input[n_char - 1] = '\0';

        child_pid = fork();
        if (child_pid == -1) {
            free(input);
            exit(EXIT_FAILURE);
        }
        

        if (child_pid == 0) {

            execlp("sh", "sh", "-c", input, NULL);
            
            perror("execlp");
            exit(EXIT_FAILURE);
        } else {

            waitpid(child_pid, &status, 0);
        }
    }
}
