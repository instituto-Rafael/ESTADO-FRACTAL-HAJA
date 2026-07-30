# Registro de fontes jurídicas e decisões de alto impacto

```text
version = LEGAL_SOURCE_REGISTER_V1
status = CURATED_PRIMARY_SOURCES
legal_advice = false
universal_precedent_claim = false
claim_allowed = false
```

Este registro orienta pesquisa e desenho de controles. Uma decisão vale dentro de sua jurisdição, competência, fatos, pedidos e período. Citação não transforma precedente estrangeiro em regra universal.

## 1. Direitos fundamentais e constitucionais

| ID | Fonte | Tema | Uso seguro |
|---|---|---|---|
| CON-BR-001 | Constituição Federal do Brasil | dignidade, igualdade, intimidade, proteção de dados, devido processo, prioridade infantil | parâmetro constitucional brasileiro |
| CON-US-001 | First Amendment | religião, expressão, associação e limites estatais | parâmetro constitucional dos EUA, não regra privada universal |
| CON-US-005 | Fifth Amendment | devido processo e garantias federais | parâmetro contra ação federal |
| CON-US-014 | Fourteenth Amendment | devido processo e igual proteção nos Estados | parâmetro contra ação estatal |
| HR-UDHR | Declaração Universal dos Direitos Humanos | dignidade, igualdade, crença, expressão e remédio efetivo | referência internacional de direitos humanos |
| HR-ICCPR | Pacto Internacional sobre Direitos Civis e Políticos | consciência, religião, expressão, privacidade e devido processo | obrigação dos Estados-partes conforme internalização |
| CHILD-CRC | Convenção sobre os Direitos da Criança | melhor interesse, privacidade, proteção e participação | gate internacional de proteção infantil |

## 2. Proteção de dados

| ID | Fonte | Tema | Fronteira |
|---|---|---|---|
| DATA-BR-LGPD | Lei 13.709/2018 | princípios, bases legais, direitos, segurança e responsabilização | aplicação depende de escopo e papéis reais |
| DATA-BR-ANPD-INC | Regulamento de comunicação de incidente de segurança | limiar, comunicação e registro de incidentes | observar edição vigente e fatos do incidente |
| DATA-EU-GDPR | Regulation (EU) 2016/679 | proteção de dados, direitos, transferências, accountability | aplicação territorial deve ser analisada |

## 3. Decisões de alto impacto

### CASE-US-GOOGLE-ORACLE — Google LLC v. Oracle America, Inc. (2021)

**Tribunal:** Suprema Corte dos Estados Unidos.

**Tema:** uso de declarações de API Java e fair use.

**Regra de uso:** não declarar que APIs são sempre livres ou sempre protegidas. A decisão foi contextual, analisando natureza funcional, propósito transformativo, quantidade e efeito de mercado.

**Fonte primária:** https://www.supremecourt.gov/opinions/20pdf/18-956_d18f.pdf

### CASE-US-CARPENTER — Carpenter v. United States (2018)

**Tribunal:** Suprema Corte dos Estados Unidos.

**Tema:** aquisição governamental de histórico de localização por torres celulares.

**Valor para metadados:** metadados extensivos e retrospectivos podem revelar profundamente a vida de uma pessoa. `metadata != harmless`.

**Fonte primária:** https://www.supremecourt.gov/opinions/17pdf/16-402_h315.pdf

### CASE-EU-SCHREMS-II — Data Protection Commissioner v. Facebook Ireland and Maximillian Schrems, C-311/18 (2020)

**Tribunal:** Tribunal de Justiça da União Europeia.

**Tema:** transferência internacional, salvaguardas e invalidação do Privacy Shield.

**Uso seguro:** transferir dados exige analisar proteção efetiva no destino e medidas suplementares; cláusula contratual não resolve toda incompatibilidade por si só.

**Fonte primária:** https://curia.europa.eu/juris/liste.jsf?num=C-311/18

### CASE-EU-META-BKA — Meta Platforms v. Bundeskartellamt, C-252/21 (2023)

**Tribunal:** Tribunal de Justiça da União Europeia.

**Tema:** interação entre concorrência, consentimento, posição dominante e GDPR.

**Uso seguro:** governança de dados não deve ser isolada de poder de mercado, escolha real e combinação entre serviços.

**Fonte primária:** https://curia.europa.eu/juris/liste.jsf?num=C-252/21

### CASE-EU-GOOGLE-SPAIN — Google Spain, C-131/12 (2014)

**Tribunal:** Tribunal de Justiça da União Europeia.

**Tema:** responsabilidade de mecanismo de busca e desindexação em determinadas condições.

**Uso seguro:** não prometer apagamento universal da fonte; distinguir remoção da origem, desindexação, jurisdição e equilíbrio com interesse público.

**Fonte primária:** https://curia.europa.eu/juris/liste.jsf?num=C-131/12

### CASE-EU-DIGITAL-RIGHTS — Digital Rights Ireland, C-293/12 e C-594/12 (2014)

**Tribunal:** Tribunal de Justiça da União Europeia.

**Tema:** retenção generalizada e indiscriminada de metadados.

**Uso seguro:** retenção preventiva ampla exige necessidade, proporcionalidade e salvaguardas fortes.

**Fonte primária:** https://curia.europa.eu/juris/liste.jsf?num=C-293/12

### CASE-BR-ADI-6387 — STF, compartilhamento de dados de telecomunicações com o IBGE

**Tribunal:** Supremo Tribunal Federal.

**Tema:** privacidade, autodeterminação informativa, necessidade e proporcionalidade no compartilhamento em massa.

**Uso seguro:** finalidade pública não elimina minimização, segurança e demonstração de necessidade.

**Fonte primária:** https://portal.stf.jus.br/processos/detalhe.asp?incidente=5895165

### CASE-BR-ADO-26-MI-4733 — STF, homotransfobia

**Tribunal:** Supremo Tribunal Federal.

**Tema:** proteção contra discriminação por orientação sexual e identidade de gênero; liberdade religiosa pacífica preservada, sem proteção para incitação discriminatória.

**Uso seguro:** combinar não discriminação e liberdade de crença sem transformar nenhuma delas em licença para hostilidade ou coerção.

**Fonte primária:** https://portal.stf.jus.br/processos/detalhe.asp?incidente=4515053

## 4. Jurisprudência de software, privacidade e mercado

O registro deve distinguir:

```text
copyright
patent
contract
antitrust
privacy
consumer protection
computer misuse
trade secret
```

Uma decisão de copyright não resolve automaticamente privacidade; uma decisão antitruste não concede licença de software; uma cláusula contratual não elimina dever regulatório.

## 5. Limitação de responsabilidade

Cláusulas de produtos comerciais frequentemente excluem danos indiretos e limitam danos diretos. A validade varia por jurisdição, relação de consumo, transparência e natureza do dano.

A política HAJA exige carve-outs para, no mínimo:

```text
fraud
intentional misconduct
gross negligence where non-waivable
personal injury or death
privacy and security violations
child harm
confidentiality
third-party intellectual property
mandatory statutory liability
```

## 6. Registro de atualização

Toda fonte deve carregar:

```yaml
source_id: ...
jurisdiction: ...
authority: ...
decision_or_instrument_date: ...
official_url: ...
verified_at: ...
current_status: ...
supports: []
does_not_support: []
```

## 7. Estados abertos

```text
independent_legal_review = TOKEN_VAZIO
complete_global_constitutional_comparison = TOKEN_VAZIO
binding_effect_for_HAJA = NONE
case_specific_application = REQUIRES_FACTS_AND_COUNSEL
```