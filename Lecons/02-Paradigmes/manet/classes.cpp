#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

class Message {
  int dateCreation;

public:
  Message() : dateCreation(time(NULL)) {}

  // non implémenté dans la classe Message
  virtual const char* valeur() = 0;

  void afficherLog() {
    const char* texte = this->valeur();
    printf("[créé à %d] %s", this->dateCreation, texte);
    free((void*)texte);
  }

};

class MessageTexte : public Message {
  char* texte;

public:
  MessageTexte(const char* texteParam) : Message(), texte(strdup(texteParam)) {}
  ~MessageTexte() {
    free(texte);
  }

  virtual const char* valeur() {
    return strdup(texte);
  }
};

class MessageErreur : public MessageTexte {
public:
  MessageErreur() : MessageTexte("ERREUR INCONNUE") {}
};

class MessageNombre : public Message {
  float nombre;

public:
  MessageNombre(float valeur) : Message(), nombre(valeur) {}

  virtual const char* valeur() {
    char* texte = (char*) malloc(sizeof(char)*40);
    sprintf(texte, "nombre : %f", this->nombre);
    return texte;
  }
};

