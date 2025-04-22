# 📱 L10n-Auto: Detecção Automatizada de Falhas de Localização em Aplicativos Android

Este projeto propõe uma ferramenta automatizada capaz de identificar falhas de localização (L10N) em aplicativos Android. Ele foi desenvolvido como Trabalho de Conclusão de Curso no Centro de Informática da UFPE.

## 🧠 Sobre o Projeto

A internacionalização (I18N) e a localização (L10N) são fundamentais para adaptar aplicativos a diferentes idiomas e culturas. No entanto, falhas como traduções ausentes, truncamentos e elipses podem prejudicar seriamente a experiência do usuário.

O **L10n-Auto** integra o **DroidBot** (navegação automatizada em apps Android) com uma ferramenta de análise baseada em **OCR (Tesseract)** para detectar automaticamente:

- Palavras não traduzidas ou traduzidas incorretamente;
- Elipses decorrentes de traduções mal encaixadas;
- (E com possibilidades futuras para detectar truncamentos e sobreposições).

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **PyTesseract** – Reconhecimento Óptico de Caracteres
- **Pillow (PIL)** – Manipulação de imagens
- **Argparse** – Interface de linha de comando
- **DroidBot** – Navegação automatizada no app e coleta de screenshots + hierarquia

## 🔧 Melhorias Implementadas

- 🔁 **Automação da coleta de dados** com DroidBot (sem necessidade de extração manual de arquivos XML/JSON).
- 📸 **Análise OCR de mais de 100 imagens em menos de 1 minuto**.
- ⚠️ **Detecção de elipses** como possíveis falhas de L10N.
- 📄 **Geração de relatório em texto simples + imagens destacadas**, otimizando performance e leitura.
- 📂 **Suporte a lista personalizada de palavras ignoradas**, como nomes de marcas.

## 📌 Parâmetros da Ferramenta

```bash
python main.py --apk-path caminho/apk \
               --exploration-time 60 \
               --lang pt-br \
               --custom-ignore palavras.txt \
               --output-directory resultados/
```

- `--apk-path`: Caminho para o APK a ser testado.
- `--exploration-time`: Tempo em segundos de exploração do app.
- `--lang`: Idioma (ex: `pt-br`, `es`).
- `--custom-ignore`: Lista de termos ignorados durante a análise.
- `--output-directory`: Pasta onde os resultados serão armazenados.

## 📊 Avaliação

A ferramenta foi testada com 8 aplicativos Android, incluindo:

- MoneyManagerEx
- Microsoft 365 Copilot
- Kahoot!
- VLC Media Player
- IMDb
- Sofascore
- KitchenOwl
- Blood Pressure Monitor

Resultados mostraram grande eficácia na detecção de erros de tradução e elipses. O repositório inclui todos os dados, arquivos ignore e imagens geradas.
