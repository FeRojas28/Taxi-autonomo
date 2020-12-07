#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from agente import Agente
from labirinto import Labirinto
from turtle import *
from time import sleep

def main():
    """ Basta ativar uma das simulações para rodar o código """
    # Simulação 1
    #um_agente_percorre_tudo()

    # Simulação 2
    #um_agente_vagueia()

    # Simulação 3
    #todos_vagueiam()

    # Simulação 4
    #agente_com_um_destino()

    # Simulação 5
    #n_agentes_percorrendo()

    # Simulação 6
    #agente_com_n_destinos()

    done()

""" Simulações """

def um_agente_percorre_tudo():
    """ Simulação 1: Agente percorre todo o labirinto """
    dimensao_da_matriz = 20
    lab = Labirinto(dimensao_da_matriz)
    id = 0
    agente = lab.add_pacman(id)

    intervalo_entre_frames = 0.1

    chegou_ao_fim = False
    while (not chegou_ao_fim):
        chegou_ao_fim = agente.percorrer()
        # Atualiza "frame"
        update()
        sleep(intervalo_entre_frames)

def um_agente_vagueia():
    """ Simulação 2: O único agente vagueia """

    dimensao_da_matriz = 20
    lab = Labirinto(dimensao_da_matriz)
    id = 0
    pacman = lab.add_pacman(id)

    n_frames = 500
    intervalo_entre_frames = 0.1
    for _ in range(n_frames):
        pacman.vaguear()
        update()
        sleep(intervalo_entre_frames)

def todos_vagueiam():
    """ Simulação 3: Todos os agentes vagueiam, sem 'colisões' """

    dimensao_da_matriz = 20
    lab = Labirinto(dimensao_da_matriz)
    id = 0
    pacman = lab.add_pacman(id)

    n_fantasmas = 60
    for id in range(1, n_fantasmas):
        f = lab.add_fantasma(id)

    n_frames = 10000
    intervalo_entre_frames = 0.1

    agentes = lab.agentes
    for _ in range(n_frames):
        for id in agentes.keys():
            agentes[id].vaguear()
        # Atualiza "frame"
        update()
        sleep(intervalo_entre_frames)


def agente_com_um_destino():
    """ Simulação 4: Agente caminha para um destino aleatoriamente sorteado """

    dimensao_da_matriz = 20
    lab = Labirinto(dimensao_da_matriz)
    id = 0
    agente = lab.add_pacman(id)

    origem = agente._posicao
    destino = lab.cel_aleatoria()

    lab.desenhar_celula(origem, 'red')
    lab.desenhar_celula(destino, 'red')

    intervalo_entre_frames = 0.1

    chegou_ao_destino = False
    while (not chegou_ao_destino):
        chegou_ao_destino = agente.ir_a(destino)
        # Atualiza "frame"
        update()
        sleep(intervalo_entre_frames)


def n_agentes_percorrendo():
    """ Simulação 5: n agentes percorrem, com 'colisões' """
    n_agentes = 10
    dimensao_da_matriz = 20
    lab = Labirinto(dimensao_da_matriz)
    id = 0
    agente = lab.add_pacman(id)

    intervalo_entre_frames = 0.1
    agentes = lab.agentes
    chegou_ao_fim = False
    for id in range(0, n_agentes):
        lab.add_fantasma(id)

    while (not chegou_ao_fim):

        for id in agentes.keys():
            agentes[id].percorrer()

        chegou_ao_fim = agente.percorrer()
        # Atualiza "frame"
        update()
        sleep(intervalo_entre_frames)

def agente_com_n_destinos():
    """ Agente caminha para n destinos aleatoriamente sorteados """
    n = 10
    dimensao_da_matriz = 20
    lab = Labirinto(dimensao_da_matriz)
    id = 0
    agente = lab.add_pacman(id)
    origem = agente._posicao
    destino = lab.cel_aleatoria()
    chegou_ao_destino = False
    for i in range(n):
        lab.desenhar_celula(origem, 'red')
        lab.desenhar_celula(destino, 'red')
        intervalo_entre_frames = 0.1
        while (not chegou_ao_destino):
            chegou_ao_destino = agente.ir_a(destino)
            # Atualiza "frame"
            update()
            sleep(intervalo_entre_frames)
        lab.desenhar_celula(origem, 'black')
        lab.desenhar_divisoria_horizontal(origem, 'yellow')
        lab.desenhar_divisoria_vertical(origem, 'yellow')
        origem = destino
        destino = lab.cel_aleatoria()
        chegou_ao_destino = False
        agente._waze.add_destino(destino)
        agente._waze.gerar_rota(origem)

main()
