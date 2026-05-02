#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"
DOCS=(README.md Manifest.md preambulo.md Md.md Mp0001.md License.md)
missing=0
for f in "${DOCS[@]}"; do
  if [[ -f "$f" ]]; then echo "[OK] Documento localizado: $f"; else echo "[ERRO] Documento obrigatório ausente: $f"; missing=1; fi
done
[[ $missing -eq 0 ]] || { echo "Falha de integridade documental."; exit 1; }
SEED_FILE="SEMENTE_SUPRALEGAL.md"
DATE_UTC="$(date -u +'%Y-%m-%dT%H:%M:%SZ')"
cat > "$SEED_FILE" <<'SEED'
# Semente Sólida do Direito Supra Legal — HAJA

Gerado por `HAJA.SH` em __DATE_UTC__.

## Núcleo Jurídico
1. Dignidade humana, proteção infantil e liberdade de consciência são cláusulas invioláveis.
2. Nenhum sistema técnico pode se sobrepor aos direitos fundamentais.
3. Todo ato digital relevante deve ser auditável, verificável e rastreável por hash.
4. Tratados digitais exigem texto público, consentimento explícito e integridade criptográfica.
5. O poder técnico deve obedecer à ética, ao devido processo e ao controle comunitário.

## Ponte Internacional
- Autodeterminação dos povos.
- Igualdade soberana entre entidades políticas.
- Boa-fé, publicidade e segurança jurídica em compromissos digitais.

## Estrutura Conceitual (resumo operacional)
- Espaço toroidal: \(\mathbb{T}^7=(\mathbb{R}/\mathbb{Z})^7\).
- Vetor: \(\mathbf{s}=(u,v,\psi,\chi,\rho,\delta,\sigma)\in[0,1)^7\).
- Atualização: \(C_{t+1}=(1-\alpha)C_t+\alpha C_{in}\), \(H_{t+1}=(1-\alpha)H_t+\alpha H_{in}\), com \(\alpha=0.25\).
- Integridade: hash, CRC e Merkle para cadeia de custódia.

## Execução
Rode `./HAJA.SH` para validar documentação e regenerar esta semente.
SEED
sed -i "s/__DATE_UTC__/${DATE_UTC}/g" "$SEED_FILE"
sha256sum "$SEED_FILE" | tee SEMENTE_SUPRALEGAL.sha256 >/dev/null
echo "Semente jurídica criada: $SEED_FILE"
echo "Hash de integridade salvo em: SEMENTE_SUPRALEGAL.sha256"
