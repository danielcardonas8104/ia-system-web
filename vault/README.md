# Vault: cerebro digital de Daniel

Esta carpeta es el vault de Obsidian completo, listo para usar. Vive temporalmente aquí porque la integración no pudo crear el repo privado; el destino final es un repositorio privado propio.

## Cómo activarlo (5 minutos, en tu Mac)

1. Copia esta carpeta `vault/` a donde quieras tu cerebro, por ejemplo `~/Documents/ia-system-brain`
2. En Obsidian: Open folder as vault y selecciona esa carpeta
3. Crea el repo privado y sube el vault (en la terminal, dentro de la carpeta):

```bash
cd ~/Documents/ia-system-brain
git init
git add .
git commit -m "Cerebro digital inicial"
gh repo create ia-system-brain --private --source=. --push
```

Si no tienes `gh` instalado: crea el repo vacío y privado en github.com/new con el nombre `ia-system-brain` y luego:

```bash
git remote add origin git@github.com:danielcardonas8104/ia-system-brain.git
git branch -M main
git push -u origin main
```

4. Instala el plugin "Obsidian Git" en Obsidian para que haga commit y push automático cada 10 minutos
5. Borra esta carpeta `vault/` del repo del sitio web una vez migrada

## Punto de entrada

Todo LLM o persona empieza leyendo `00-INICIO.md`.
