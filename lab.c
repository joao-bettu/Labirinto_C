/* Tentativa em C de criar o Labirinto
    - Possui melhor controle de memória
    - Melhor manipulação de arquivos */

//Bibliotecas
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//Variáveis globais
char** mapa; /* Varável global que armazenará o mapa do labirinto, para ser utilizada por todas as funções
                char** os dois * siginifica ponteiro de ponteiros */

//Assinatura das Funções
void le_mapa();
void aloca_mapa(int linhas, int colunas);
void gera_posicao(int *vetor);
int calcula_heuristica(int *inicio, int *fim);
void ia_jogando(int heuristica, int *inicio, int *fim);

//Função Main
int main(){
    int posicao_inicial[2], posicao_final[2], heuristica;
    printf("Lê mapa!\n");
    le_mapa();

    gera_posicao(posicao_inicial);
    gera_posicao(posicao_final);

    heuristica = calcula_heuristica(posicao_inicial, posicao_final);

    ia_jogando(heuristica, posicao_inicial, posicao_final);

    printf("\nFinalizado!\n");
    return 0;
}

//Funções
void le_mapa(){
    FILE *fp;
    int linhas, colunas;

    fp = fopen("/home/ixcsoft/Documentos/Meus Projetos/Labirinto_C/mapa.txt", "r");
    if(fp==NULL){
        printf("Erro na abertura do arquivo!\n");
        exit(1);
    }

    fscanf(fp, "%d;%d", &linhas, &colunas);
    printf("Linhas: %d e Colunas: %d\n", linhas, colunas);

    aloca_mapa(linhas, colunas);

    for(int i = 0; i < linhas; i++){
        fscanf(fp, "%s", mapa[i]);
    }
    
    fclose(fp);
    printf("Arquivo fechado!\n\n");
}
void aloca_mapa(int linhas, int colunas){
    mapa = malloc(sizeof(char*) * linhas);

    for(int i = 0; i < linhas; i++){
        mapa[i] = malloc(sizeof(char) * colunas + 1);
    }
    printf("Memória alocada!\n\n");
}
void gera_posicao(int *vetor){
    int x, y, min = 0, max = 7;
    srand(time(NULL));

    x = min + rand() % (max - min + 1);
    if(x == 1)
        x = 7;

    y = min + rand() % (max - min + 1);
    if(y == 1)
        y = 7;


    printf("X = %d e Y = %d\n", x, y);
    vetor[0] = x;
    vetor[1] = y;
}
int calcula_heuristica(int *inicio, int *fim){
    int heuristca, a , b;

    a = abs(inicio[0] - fim[0]);
    b = abs(inicio[1] - fim[1]);

    heuristca = a + b;

    return heuristca;
}
void ia_jogando(int heuristica, int *inicio, int *fim){
    char** copy = mapa;

    copy[inicio[0]][inicio[1]] = 'A';
    copy[fim[0]][fim[1]] = 'X';

    for(int i = 0; i < 8; i++)
        printf("%s\n", copy[i]);
}