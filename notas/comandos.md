# Comandos de Git y Guía de Solución de Problemas



## Comandos Principales



|Comando|Para qué|

|-|-|

|`git init`|Convierte la carpeta en repositorio|

|`git config user.name "..."`|Tu nombre en los commits (también `user.email`)|

|`git status`|Qué cambió y qué está preparado|

|`git add archivo`|Prepara un cambio|

|`git commit -m "mensaje"`|Guarda la foto|

|`git diff`|Lo que cambió y no has preparado|

|`git restore archivo`|Deshace los cambios desde el último commit|

|`git log --oneline`|La historia, un commit por renglón|

|`git branch -M main`|Renombra la rama a main|

|`explorer .`|Abre la carpeta actual en el Explorador|

|`notepad archivo`|Abre el archivo en el Bloc de notas|



\\---



\## Errores Comunes y Soluciones



|Ves esto|Por qué|Qué hacer|

|-|-|-|

|`bash: git: command not found`|Git no está instalado o Git Bash no es la terminal abierta.|Abrir Git Bash (no PowerShell ni CMD). Si sigue, usar PortableGit.|

|`fatal: not a git repository`|Están fuera de la carpeta del repositorio o no hicieron `git init`.|`pwd` para ver dónde están; `cd \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\~/portafolio-herramientas-ia`.|

|`Author identity unknown ... unable to auto-detect email address`|Faltó configurar nombre y correo.|Los dos `git config` dentro del repositorio, y repetir el commit.|

|`warning: LF will be replaced by CRLF`|Git en Windows ajusta los finales de línea.|Es un aviso, no un error. Seguir.|

|`fatal: pathspec 'readme.md' did not match any files`|El nombre está mal escrito.|Usar Tab para autocompletar; `ls` para ver el nombre exacto.|

|`nothing added to commit`|Hicieron commit sin `git add` antes.|`git add archivo` y después el commit.|

|La pantalla muestra `(END)` o `:` y no responde|Git abrió el paginador para una salida larga.|Presionar `q`.|

|Se abre un editor raro al hacer commit|Olvidaron `-m "mensaje"`; Git abre su editor (a veces Vim).|En Vim: Esc, escribir `:q!` y Enter. Repetir con `-m`.|

|`cp: cannot stat '.../Downloads/README.md'`|El README no está en Descargas o se llama distinto.|`ls \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\~/Downloads`; si se llama `README (1).md`, usar comillas o renombrarlo.|

|`comandos.md` no aparece en `git status`|El `.gitignore` ignora toda la carpeta `notas/`.|Dejar en `.gitignore` solo `notas/borrador.txt`.|

