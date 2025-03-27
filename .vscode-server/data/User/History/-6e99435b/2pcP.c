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
    char input[4096];
    pid_t pid;
    int status;
    size_t input_len;

    while (1) {
        if (isatty(STDIN_FILENO))
            printf("cisfun$ ");

        if (fgets(input, sizeof(input), stdin) == NULL) {
            printf("Error reading input\n");
            exit(EXIT_FAILURE);
        }
        input_len = strlen(input);
        if (input[input_len - 1] == '\n')
            input[input_len - 1] = '\0';

        pid = fork();
        if (pid == -1) {
            perror("fork");
            exit(EXIT_FAILURE);
        }

        if (pid == 0) {
            execlp("sh", "sh", "-c", input, NULL);
            perror("execlp");
            exit(EXIT_FAILURE);
        } else {
            waitpid(pid, &status, 0);
        }
    }
}

