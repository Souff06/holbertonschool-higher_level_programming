#include "shell.h"
/**
 * main - The main function for a simple shell program
 * Description: this program create a basic shell
 * accepting and executing command entered by the user
 * Return: Always 0
 */

int main(int argc, char **argv, char **env) {
    char *input = NULL;
    char *line;
    char *command = NULL;
    char **args = NULL;
    size_t input_size = 0;
    ssize_t n_char = 0;

    (void)argc;

    while (1) {
        printf(isatty(STDIN_FILENO) ? "Cisfun$ " : "");
        if ((n_char = getline(&input, &input_size, stdin)) == -1) break;
        if (input[n_char - 1] == '\n') input[n_char - 1] = '\0';

        for (line = strtok(input, "\n"); line; line = strtok(NULL, "\n")) {
            if (check_spaces_tabs(line)) {
                args = split_string(line, &command);
                if (args == NULL) {
                    continue;
                }
                if (!strcmp(args[0], "exit")) {
                    free_resources(input, args, command);
                    exit(EXIT_SUCCESS);
                } else if (!strcmp(args[0], "env")) {
                    print_env();
                } else {
                    pid_t pid = fork();
                    if (pid == -1) {
                        perror("Failed to fork");
                    } else if (pid == 0) {
                        if (execvp(args[0], args) == -1) {
                            perror("Failed to execute command");
                            exit(EXIT_FAILURE);
                        }
                    } else {
                        int status;
                        waitpid(pid, &status, 0);
                    }
                }
                free_token_command(args);
                free(command);
            }
        }
        free(input);
        input = NULL;
        input_size = 0;
    }
    free(input);
    return 0;
}

void free_resources(char *input, char **args, char *command) {
    free_token_command(args);
    free(command);
    free(input);
}
