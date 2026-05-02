#!/usr/bin/env bash
set -euo pipefail

readonly ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly SEED_FILE="SEMENTE_SUPRALEGAL.md"
readonly HASH_FILE="SEMENTE_SUPRALEGAL.sha256"
readonly GENERATED_AT="$(date -u +'%Y-%m-%dT%H:%M:%SZ')"
readonly REQUIRED_DOCS=(README.md Manifest.md preambulo.md Md.md Mp0001.md License.md)

log() { printf '%s\n' "$*"; }

validate_docs() {
  local missing=0
  for file in "${REQUIRED_DOCS[@]}"; do
    if [[ -f "$file" ]]; then
      log "[OK] Documento localizado: $file"
    else
      log "[ERRO] Documento obrigatório ausente: $file"
      missing=1
    fi
  done
  [[ $missing -eq 0 ]] || { log "Falha de integridade documental: interrompido."; exit 1; }
}

generate_seed() {
  cat > "$SEED_FILE" <<'SEED'
# Carta-Semente Supra Legal do Orquestrador Jurídico HAJA

**Data de emissão (UTC):** __GENERATED_AT__  
**Natureza:** Estrutura fundacional de direitos pétreos, devido processo e governança técnico-jurídica verificável.

## I. Cláusulas Essenciais Irrevogáveis
1. **Dignidade da pessoa humana** como norma matriz de interpretação e limite material de qualquer sistema.
2. **Proteção integral da criança e do adolescente** como prioridade absoluta e inderrogável.
3. **Liberdade de consciência, expressão e devido processo** como núcleo mínimo civilizatório.
4. **Legalidade, publicidade, auditabilidade e rastreabilidade** de atos digitais com prova criptográfica.
5. **Proporcionalidade e não discriminação algorítmica**, com dever de revisão humana em decisões sensíveis.

## II. Arquitetura Normativa por Analogia Constitucional
- **Brasil (Art. 5º, CF/1988):** garantias de liberdade, privacidade, contraditório e ampla defesa.
- **EUA (1ª Emenda):** tutela da expressão e da circulação de ideias.
- **EUA (5ª Emenda):** due process of law e proteção contra arbitrariedades estatais.
- **Cláusulas pétreas (teoria material):** núcleo essencial não pode ser reduzido por reforma ordinária.

## III. Eixos Internacionais e Regulatórios
- **ONU / Declaração Universal de Direitos Humanos** (dignidade, igualdade, liberdade).
- **UNICEF / UNESCO** (proteção de infância, educação, cultura e pluralidade linguística).
- **LGPD + princípios globais de proteção de dados** (finalidade, necessidade, transparência, segurança).
- **NIST / ISO / IEC / IEEE / RFC** como blocos técnicos de segurança, interoperabilidade e governança.

## IV. Doutrina de Integridade Probatória (cadeia de custódia)
- Documento público versionado.
- Hash SHA-256 para integridade.
- Registro temporal UTC.
- Critério de reprodutibilidade por execução local.

## V. Matriz Heurística de 9 Profundidades (rito de validação)
1. **Fundamento humano** (dignidade/vida).
2. **Fundamento constitucional** (garantias materiais).
3. **Fundamento convencional** (tratados internacionais).
4. **Fundamento probatório** (hash, logs, trilha de auditoria).
5. **Fundamento processual** (devido processo e contraditório).
6. **Fundamento tecnológico** (segurança e padrões técnicos).
7. **Fundamento de proporcionalidade** (balanço de direitos).
8. **Fundamento comparado** (casos exemplares globais).
9. **Fundamento de revisão contínua** (governança e accountability).

## VI. Geometria Institucional (hexagonal de possibilidades)
A governança é organizada em seis vértices acoplados:  
**Direitos Fundamentais ↔ Prova Técnica ↔ Processo ↔ Transparência ↔ Interoperabilidade ↔ Controle Social.**

## VII. Camada Matemática-Conceitual de Coerência
- \(\mathbb{T}^7=(\mathbb{R}/\mathbb{Z})^7\), \(\mathbf{s}=(u,v,\psi,\chi,\rho,\delta,\sigma)\in[0,1)^7\).
- \(\mathbf{s}=\mathrm{ToroidalMap}(x)\), com \(x=(\text{dados},\text{entropia},\text{hash},\text{estado})\).
- \(C_{t+1}=(1-\alpha)C_t+\alpha C_{in}\), \(H_{t+1}=(1-\alpha)H_t+\alpha H_{in}\), \(\alpha=0.25\).
- Integridade por hash/CRC/Merkle; convergência ética sob pluralidade linguística e semântica.

## VIII. Regra de Resposta a Objeções
Qualquer objeção normativa deve indicar:  
(a) qual cláusula essencial supostamente viola;  
(b) qual garantia constitucional internacional prevalece;  
(c) qual evidência técnica reproduzível sustenta a objeção.  
Sem os três elementos, a objeção é processualmente incompleta.

## IX. Execução
Executar `./HAJA.SH` para:
1. validar documentação base;
2. regenerar esta Carta-Semente;
3. atualizar hash de integridade.
SEED

  sed -i "s/__GENERATED_AT__/${GENERATED_AT}/g" "$SEED_FILE"
}

generate_hash() {
  sha256sum "$SEED_FILE" | tee "$HASH_FILE" >/dev/null
}

main() {
  cd "$ROOT_DIR"
  validate_docs
  generate_seed
  generate_hash
  log "Carta-semente gerada: $SEED_FILE"
  log "Hash de integridade salvo em: $HASH_FILE"
}

main "$@"
