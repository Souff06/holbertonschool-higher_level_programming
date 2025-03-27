#include "shell.h"
/**
 * execute_command - executes a command provided by the user
 * @argv: main program arguments
 * @command: array of string as command and its arguments
 * @env: environment
 * Return: 0 on success, otherwise 1
 */
void execute_command(char **argv, char **command, char **env) {
    pid_t child;
    int status;

    (void)argv;
    (void)env;

    printf("Executing command: %s\n", command[0]);

    child = fork();
    if (child < 0) {
        perror("Failed to fork");
    } else if (child == 0) {
        if (execvp(command[0], command) == -1) {
            perror("Failed to execute command");
            exit(EXIT_FAILURE);
        }
    } else {
        waitpid(child, &status, 0);
    }
}
