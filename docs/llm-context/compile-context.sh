#!/usr/bin/env bash
# compile-context.sh
# Compila un vault de Obsidian en un pack de contexto para LLMs.
#
# Uso:
#   ./compile-context.sh <ruta-vault> [ruta-salida]
#
# Ejemplo:
#   ./compile-context.sh ~/Obsidian/EVIA-Brain ~/Desktop/evia-context
#
# Salida:
#   EVIA-CORE.md    borrador del nucleo, editar a mano antes de usar
#   INDEX.md        mapa de todas las notas con ruta y primera linea
#   pack/parte-NN.md  contenido troceado por tamano

set -euo pipefail

VAULT="${1:-}"
OUT="${2:-$HOME/Desktop/evia-context}"

# Tamano maximo por archivo del pack, en KB.
MAX_KB="${MAX_KB:-180}"

# Carpetas excluidas. Ajustar segun el vault.
EXCLUDES=(
  ".obsidian"
  ".trash"
  ".git"
  ".smart-env"
  "Templates"
  "Plantillas"
  "Attachments"
  "Adjuntos"
  "99-Confidencial"
)

if [[ -z "$VAULT" ]]; then
  echo "Uso: $0 <ruta-vault> [ruta-salida]" >&2
  exit 1
fi

if [[ ! -d "$VAULT" ]]; then
  echo "Error: no existe el directorio '$VAULT'" >&2
  exit 1
fi

VAULT="$(cd "$VAULT" && pwd)"
FECHA="$(date +%Y-%m-%d)"

rm -rf "$OUT"
mkdir -p "$OUT/pack"

# Construye los predicados de exclusion para find.
PRUNE_ARGS=()
for dir in "${EXCLUDES[@]}"; do
  PRUNE_ARGS+=( -name "$dir" -o )
done
unset 'PRUNE_ARGS[${#PRUNE_ARGS[@]}-1]'

# Lista de notas, ordenada.
NOTES_LIST="$(mktemp)"
trap 'rm -f "$NOTES_LIST"' EXIT

find "$VAULT" \( "${PRUNE_ARGS[@]}" \) -prune -o -type f -name '*.md' -print \
  | LC_ALL=C sort > "$NOTES_LIST"

TOTAL="$(wc -l < "$NOTES_LIST" | tr -d ' ')"

if [[ "$TOTAL" -eq 0 ]]; then
  echo "Error: no se encontraron archivos .md en '$VAULT'" >&2
  exit 1
fi

echo "Vault:  $VAULT"
echo "Notas:  $TOTAL"
echo "Salida: $OUT"
echo

# ---------------------------------------------------------------------------
# INDEX.md
# ---------------------------------------------------------------------------
{
  echo "# Indice del vault"
  echo
  echo "Fuente: \`$VAULT\`"
  echo "Compilado: $FECHA"
  echo "Notas: $TOTAL"
  echo
  echo "Este indice lista cada nota con su ruta relativa y su primer encabezado."
  echo "Usalo para ubicar de que archivo pedir el contenido completo."
  echo
  echo "| Ruta | Titulo |"
  echo "|---|---|"
  while IFS= read -r file; do
    rel="${file#"$VAULT"/}"
    titulo="$(grep -m1 -E '^#{1,3} ' "$file" 2>/dev/null | sed -E 's/^#+ //' || true)"
    [[ -z "$titulo" ]] && titulo="$(basename "$file" .md)"
    titulo="${titulo//|/ }"
    echo "| \`$rel\` | ${titulo} |"
  done < "$NOTES_LIST"
} > "$OUT/INDEX.md"

echo "Generado: INDEX.md"

# ---------------------------------------------------------------------------
# pack/parte-NN.md
# ---------------------------------------------------------------------------
PART=1
CURRENT="$OUT/pack/parte-$(printf '%02d' $PART).md"
MAX_BYTES=$(( MAX_KB * 1024 ))

start_part() {
  {
    echo "# Pack de contexto EVIA - parte $(printf '%02d' $PART)"
    echo
    echo "Compilado: $FECHA"
    echo "Fuente: vault Obsidian EVIA-Brain"
    echo
    echo "---"
    echo
  } > "$CURRENT"
}

start_part

while IFS= read -r file; do
  rel="${file#"$VAULT"/}"
  size_current=$(wc -c < "$CURRENT" | tr -d ' ')
  size_file=$(wc -c < "$file" | tr -d ' ')

  if (( size_current + size_file > MAX_BYTES )) && (( size_current > 512 )); then
    PART=$(( PART + 1 ))
    CURRENT="$OUT/pack/parte-$(printf '%02d' $PART).md"
    start_part
  fi

  {
    echo "## NOTA: $rel"
    echo
    cat "$file"
    echo
    echo "---"
    echo
  } >> "$CURRENT"
done < "$NOTES_LIST"

echo "Generado: pack/ con $PART archivo(s)"

# ---------------------------------------------------------------------------
# EVIA-CORE.md, borrador del nucleo
# ---------------------------------------------------------------------------
{
  echo "# EVIA-CORE, borrador automatico"
  echo
  echo "ATENCION: este archivo es un borrador. Editarlo a mano usando"
  echo "CONTEXT-PACK.template.md antes de pegarlo en ningun LLM."
  echo "Objetivo: entre 2000 y 4000 palabras, solo informacion estable."
  echo
  echo "Compilado: $FECHA"
  echo
  echo "## Estructura detectada del vault"
  echo
  find "$VAULT" \( "${PRUNE_ARGS[@]}" \) -prune -o -type d -print \
    | LC_ALL=C sort \
    | sed "s|^$VAULT|.|" \
    | sed 's/^/- /'
  echo
  echo "## Notas raiz y notas MOC candidatas a nucleo"
  echo
  grep -iE '/(00|01|MOC|Index|Home|Dashboard|README|Perfil|Negocio|Oferta|Servicios|Pricing|ICP)' "$NOTES_LIST" \
    | sed "s|^$VAULT/|- |" || echo "- (ninguna detectada, revisar manualmente)"
  echo
  echo "## Siguiente accion"
  echo
  echo "1. Abrir CONTEXT-PACK.template.md"
  echo "2. Llenar cada seccion con contenido de las notas listadas arriba"
  echo "3. Guardar el resultado como EVIA-CORE.md definitivo"
  echo "4. Pegar en instrucciones del Project de ChatGPT y de Claude"
} > "$OUT/EVIA-CORE.md"

echo "Generado: EVIA-CORE.md (borrador)"
echo
echo "Listo. Revisa: $OUT"
