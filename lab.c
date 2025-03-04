/* Tentativa em C de criar o Labirinto
    - Possui melhor controle de memória
    - Melhor manipulação de arquivos
    - Servirá como base para posteriormente implementar novas soluções de IA
*/

//Bibliotecas
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "tad.h"

//Variáveis globais
char** mapa; /* Varável global que armazenará o mapa do labirinto, para ser utilizada por todas as funções
                char** os dois * siginifica ponteiro de ponteiros */

//Assinatura das Funções
void le_mapa();
void aloca_mapa(int linhas, int colunas);
void gera_posicao(int *vetor);
int calcula_heuristica(int *inicio, int *fim);
void ia_jogando(Caminhos *inicio, int *fim);

//Função Main
int main(){
    int posicao_inicial[2], posicao_final[2];
    Caminhos inicio;

    printf("Lê mapa!\n");
    le_mapa();

    gera_posicao(posicao_inicial);
    gera_posicao(posicao_final);

    inicio.heuristc = calcula_heuristica(posicao_inicial, posicao_final);
    inicio.position[0] = posicao_inicial[0];
    inicio.position[1] = posicao_inicial[1];
    inicio.ja_visto = 1;

    ia_jogando(&inicio, posicao_final);

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

    x = rand() % 8; //Gera linha da posição na matriz
    y = rand() % 8; //Gera coluna da posição na matriz

    if(x >= 1 && x <= 6){
        if(y >= 1 && y <= 3){
            y = 0;
        }else if(y >= 4 && y <= 6){
            y = 7;
        }
    }

    vetor[0] = x;
    vetor[1] = y;
}
int calcula_heuristica(int *inicio, int *fim){
    return abs(inicio[0] - fim[0]) + abs(inicio[1] - fim[1]);
}
void ia_jogando(Caminhos *inicio, int *fim){

}