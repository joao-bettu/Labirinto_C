/* Tentativa em C de criar o Labirinto
    - Possui melhor controle de memória
    - Melhor manipulação de arquivos */

//Bibliotecas
#include <stdio.h>
#include <stdlib.h>

//Variáveis globais
char** mapa; /* Varável global que armazenará o mapa do labirinto, para ser utilizada por todas as funções
                char** os dois * siginifica ponteiro de ponteiros */

//Assinatura das Funções
void le_mapa();
void aloca_mapa(int linhas, int colunas);

//Função Main
int main(){
    printf("Lê mapa!\n");
    le_mapa();

    printf("Finalizado!\n");

    return 0;
}

//Funções
void le_mapa(){
    FILE *fp;
    int linhas, colunas;

    fp = fopen("/home/ixcsoft/Documentos/Códigos/Python/Labirinto/mapa.txt", "r");
    if(fp==NULL){
        printf("Erro na abertura do arquivo!\n");
        exit(1);
    }

    fscanf(fp, "%d %d", &linhas, &colunas);
    printf("Linhas: %d e Colunsa: %d\n", linhas, colunas);

    aloca_mapa(linhas, colunas);
    
    fclose(fp);
    printf("Arquivo fechado!\n");
}
void aloca_mapa(int linhas, int colunas){
    mapa = malloc(sizeof(char*) * linhas);

    for(int i = 0; i < linhas; i++){
        mapa[i] = malloc(sizeof(char) * colunas + 1);
    }
    printf("Memória alocada!\n");
}