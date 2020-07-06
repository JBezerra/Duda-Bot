# DudaBot | Sua Mensageira de Bolso - 2020
### Equipe EDUCA² - Educação
![duda-logo](https://i.imgur.com/NNhfmzs.png)
## 🥵 Nossos Perrengues
#### ⚠️ O Nosso Desafio 

    **DESAFIO 3:** “Existem milhares de conteúdos gratuitos de educação abertos na internet, como podem criar uma forma de busca e curadoria ágil para que próprios alunos, que estão em casa sem acesso, possam criar sua trilha personalizada e continuar seu processo de aprendizado?

#### 🌨 O que resolvemos?
>Como brasileiro não desiste nunca

Para agregar ao nosso desafio, ainda decidimos resolver o problema da falta de acessibilidade enfrentado por uma massa gigantesca de alunos nesse período.

Principalmente para os que mais precisam nesse momento, os pré-vestibulandos, já que o ENEM ~~está~~ estava batendo na porta (6 meses) e muitos alunos não tem nenhum tipo de acesso a aulas EaD.

#### 🕯 A primeiríssima idea:
Logo de primeira, pensamos em transmitir audios de aulas preparatórias ENEM via **rádio** para as comunidades e estudantes de escolas públicas. Certo... mas para isso é necessário uma movimentação de recursos e pessoas fora de nosso escopo de concretização. Além de nada escalonável, é pouco prático tanto para o professor quanto para o aluno... **MAAS** isso nos leva a outra ideia..

## 💡A Nossa Solução
>A ideia de transmitir o áudio das aulas era boa. O fato dela resolver o problema de 58% dos estudantes da rede pública que não tem acesso a internet nos animava, mas como poderíamos escalonar isso para o nosso querido Brasil? 🤔

**E daí nasceu a Duda!**

A **DudaBot** é uma sistema de stream de aulas via sinal de telefone, que:

---
 - 👩‍🏫 **Para o Professor:** Através da Chatbot, instruí o envio das aulas, de forma simples, no próprio chat.
 - 🙎‍♂️**Para o Aluno:** Disponibiliza as aula em um número de telefone, de forma gratuita, que pode ser acessado a qualquer momento.

#### 🎩 Como funciona isso tudo?
![esquema](https://i.imgur.com/mu97rDL.png)

Em um bom resumo de como nossa infraestrutura está funcionando, há **2 servidores**, `1 Webhook da DudaBot`, e `1 Webhook para o Twilio`, 
> **Twilio:** serviço de chamadas telefônicas/SMS acionado via internet

Sucintamente, a nossa Chatbot faz toda comunicação necessária entre o professor e o Twilio. Após o envio do nome e do arquivo da aula, a Duda gerará um número de celular, que armazenará este audio de maneira permanente.

*Ao final*, solicitará os números dos alunos para que ela possa enviar os SMS's a eles, informando o número da aula e o assunto trabalhado nela.

#### 🎯 E qual impacto causa?
🎖 **Um gargalo muito grande que vem sendo enfrentado principalmente pela rede pública, é a falta de familiaridade dos funcionários com tecnologias,** tendo isso em mente a Duda contorna isso de forma visual e empática.

🎖**Como a Duda pode resolver a falta de acessibilidade dos alunos da rede pública à internet?** Tornando todo o processo de aprendizado deles *offline*, é isso que fazemos, os códigos de aula são enviados via SMS, com o número, sem nenhum tipo de cobrança.

#### ⚠️  Área de Testes:
✈️ Como achar no a Duda **Telegram:**
	![telegram](https://i.imgur.com/VwAbQcr.png)

### 🍾 Muito Obrigado Equipe HH!
