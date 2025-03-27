#include "shell.h"
/**
 * execute_command - executes a command provided by the user
 * @argv: main program arguments
 * @command: array of string as command and its arguments
 * @env: environment
 * Return: 0 on success, otherwise 1
 */
void execute_command(char **argv, char **command, char **env) {
    (void)argv;
    pid_t child;
    int status;

    char *cmd = find_command(command[0]);
    if (cmd == NULL) {
        printf("%s: command not found\n", command[0]);
        return;
    }

    child = fork();
    if (child < 0) {
        perror("fork");
        free(cmd);
        return;
    } else if (child == 0) {
        execve(cmd, command, env);
        perror("execve");
        exit(EXIT_FAILURE);
    } else {
        waitpid(child, &status, 0);
        free(cmd);
    }
}
