#include "main.h"
/**
 * main - copy file_from to file_to
 * @argc: number of argument
 * @argv: la chaine d'argument
 * Return: always 0;
 */
int main(int argc, char **argv)
{
int file_from, file_to, fd_from = 0, fd_to = 0;
char buf[1024];
ssize_t bytes_readed, bytes_written;
if (argc != 3)
{
dprintf(STDERR_FILENO, "Usage: cp file_from file_to\n"), exit(97);
}
file_from = open(argv[1], O_RDONLY);
if (file_from == -1)
{
dprintf(STDERR_FILENO, "Error: Can't read from file %s\n", argv[1]), exit(98);
}
file_to = open(argv[2], O_WRONLY | O_CREAT | O_TRUNC, 0664);
if (file_to == -1)
{
dprintf(STDERR_FILENO, "Error: Can't write to %s\n", argv[2]), exit(99);
}
while ((bytes_readed = read(file_from, buf, 1024)) > 0)
{
bytes_written = write(file_to, buf, bytes_readed);
if (bytes_written == -1 || bytes_written != bytes_readed)
{
dprintf(STDERR_FILENO, "Error: Can't write to %s\n", argv[2]), exit(99);
}
}
if (bytes_readed == -1)
{
dprintf(STDERR_FILENO, "Error: Can't read from file %s\n", argv[1]), exit(98);
}
fd_from = close(file_from);
fd_to = close(file_to);
if (fd_from == -1)
{
dprintf(STDERR_FILENO, "Error: Can't close fd %d\n", fd_from), exit(100);
}
if (fd_to == -1)
{
dprintf(STDERR_FILENO, "Error: Can't close fd %d\n", fd_to), exit(100);
}
return (0);
}