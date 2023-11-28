#include <stdio.h>
#include <stdlib.h>
struct node 
{
int info;
struct node* link;
};
struct node* start = NULL;
void createList()
{
if (start == NULL) 
{
int n;
printf("\nEnter the number of nodes: ");
scanf("%d", &n);
if (n != 0) 
{
int data;
struct node* newnode;
struct node* temp;
newnode = malloc(sizeof(struct node));
start = newnode;
temp = start;
printf("\nEnter number to"
" be inserted : ");
scanf("%d", &data);
start->info = data;
for(int i = 2; i <= n; i++) 
newnode=malloc(sizeof(struct node));
temp->link=newnode;
printf("\nenter number to be inserted');
scanf("%d",&data);

