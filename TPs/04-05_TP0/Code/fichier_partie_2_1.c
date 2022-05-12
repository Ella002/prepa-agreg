#include <stdio.h>
#include <stdlib.h>

struct a {
    struct a **f;
    int n;
    int e;
};

int f(struct a *a) {
    int s = a->e;
    for (int i=0; i<a->n; i++)
        s += f(a->f[i]);
    return s;
}

struct a* cree(struct a **f, int n, int e)
{
    struct a* a= malloc(sizeof(struct a));
    a->f = f;
    a->n = n;
    a->e = e;
    return a;
}

void supprime(struct a *a)
{
    if (a->f) {
        for(int i = 0; i < a->n; i++)
            supprime(a->f[i]);
        free(a->f);
    }

    free(a);
}

int main(int argc, char **argv)
{
    struct a *a = cree(NULL, 0, 1);
    struct a *b = cree(malloc(sizeof(struct a) * 2), 2, 1);

    b->f[0] = a;
    b->f[1] = a;

    printf("%d\n", f(b));
    supprime(b);

    return 0;
}
