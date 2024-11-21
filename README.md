# Automação Price&Quote


> Projeto para automação com Python utilizando Selenium e webdriver, consiste em extrair e baixar uma tabela de cotações seguindo uma série de passos (inclusive passar por pop-up de autenticação usando pyAutoGUI).

## 💻 Pré-requisitos

- Utilizei a versão mais recente do Python;
- Compatível com Windows;
- Documentação da utilização do Selenium no Python: `https://pypi.org/project/selenium/`.
- Importante citar que fiz a versão do Firefox, mas o Selenium também é compatível com Chrome, Edge e Safari.

## 🚀 Deixando tudo 0 bala

- No prompt do Windows:

```
py -m pip install pyautogui
py -m pip install selenium
```

- Adicione o caminho do geckodriver nas variáveis de ambiente do computador:

Necessário fazer a instalação do `geckodriver.exe` (https://github.com/mozilla/geckodriver/releases) e colocar em uma pasta, de preferência na do usuário da máquina. 

O meu está assim:
`C:\Users\PF6441\geckodriver.exe`

Caminho:
```Botão direito no nome da máquina > Properties > Advanced System settings > Environment Variables```

Em `System Variables`, procure o `Path`, clique `Edit`

Adicione o caminho do geckodriver na linha, clique `OK` para fechar.

OBS: relaxa isso não muda nada padrão do seu pc, é só pro python reconhecer o geckodriver.


## 📚 Bibliotecas

**Python:** Selenium/webdriver, pyAutoGUI


## 🤝 Contribuição
Se tiver alguma melhoria ou contribuição a fazer, por favor não exite em me chamar, estou aberta a sugestões. 
