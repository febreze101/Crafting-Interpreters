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
#include <stdlib.h>

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

void displayNode(Node *node) {
  Node* last;

  printf("The linked list elements are: \n");

  while (node != NULL) {
    printf("%s\n", node->data);
    last = node;

    node = node->next;
  }
}

void insertAfter(Node* currNode, Node* newNode) {
  newNode->prev = currNode;

  // if current node has no next
  if (currNode->next == NULL) {
    currNode->next = newNode;
  } else {
    newNode->next = currNode->next;
    currNode->next = newNode;
  }
}

void insertBefore(Node* currNode, Node* newNode) {
  newNode->next = currNode;

  if(currNode->prev == NULL) {
    currNode->prev = newNode;
  } else {
    newNode->prev = currNode->prev;
    currNode->prev = newNode;
  }
}

void deleteNode(Node* currNode) { 
  /* if no prev */
  if (currNode->prev == NULL) {
    currNode = NULL;
  } else if (currNode->next == NULL) {
    currNode = NULL;
  } else {
    currNode->prev->next = currNode->next;
  }

  free(currNode);
}

void findNode(char* data) {

}

void insertBeginning(Node* currNode) {

}


int main() {
  Node* head;
  Node* first = NULL;
  Node* second = NULL;
  Node* third = NULL;
  Node* fourth = NULL;

  first = (struct Node*)malloc(sizeof(struct Node));

  second = (struct Node*)malloc(sizeof(struct Node));

  third = (struct Node*)malloc(sizeof(struct Node));

  fourth = (struct Node*)malloc(sizeof(struct Node));

  /* init all nodes */
  first->data = "A";
  first->next = second;

  second->prev = first;
  second->data = "B";
  second->next = third;

  third->prev = second;
  third->data = "C";
  third->next = fourth;

  fourth->prev = third;
  fourth->data = "D";

  head = first;

  displayNode(first);

}