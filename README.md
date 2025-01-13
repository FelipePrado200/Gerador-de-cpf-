# Gerador de CPF 🧮

Este é um simples gerador de CPFs válidos implementado em Python. Ele utiliza cálculos baseados no algoritmo oficial para criar CPFs que passam na validação do dígito verificador.

## 🚀 Funcionalidades

- Geração de 100 CPFs válidos a cada execução.
- Simplicidade no código para fácil entendimento e aprendizado.
- Algoritmo fiel à validação oficial dos dígitos verificadores.

## 🛠️ Como funciona

O gerador segue o seguinte fluxo:

1. Gera 9 dígitos aleatórios iniciais.
2. Calcula o **primeiro dígito verificador** com base nos 9 dígitos.
3. Calcula o **segundo dígito verificador** com base nos 9 dígitos mais o primeiro dígito verificador.
4. Combina os 9 dígitos e os dois dígitos verificadores para formar o CPF completo.

## 📋 Pré-requisitos

Antes de executar o projeto, você precisará de:

- Python 3.x instalado na sua máquina.

### Instalação do Python
Faça o download e a instalação do Python através do site oficial: [Python.org](https://www.python.org/).

## 🖥️ Como usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/gerador-de-cpf.git
   cd gerador-de-cpf
