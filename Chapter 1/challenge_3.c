// Crafting Interpreters Chapter 1 - Challenge 3
// Fabrice Bokovi

/*
Do the same thing for C. To get some practice with pointers, define a doubly
linked list of heap-allocated strings. Write functions to insert, find, and
delete items from it. Test them.
*/

#include <locale.h>
#include <stdint.h>
#include <stdio.h>

typedef struct Node {
  struct Node *next; /* A reference to the next node */
  struct Node *prev; /* A reference to the previous node */
  char *data;        /* Data or reference to the data */
} Node;

struct Node newNode(uint8_t *prev, char *data) {
  /* init a new Node struct */
  Node n = {.prev = NULL, .data = data, .next = NULL};

  return n;
}

int main() {
  Node head = {.prev = NULL, .data = "A", .next = NULL};

  Node tail = {.prev = head.next, .data = "B", .next = NULL};
}