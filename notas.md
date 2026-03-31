Ejercicio práctico de control de versiones utilizando branches en Git.

```
mkdir "Semana 12" && cd "Semana 12"
git init
git remote add origin https://github.com/mlopezc/programacion-1.git
git sparse-checkout init --cone
git sparse-checkout set "clase-12"
git pull origin main
```