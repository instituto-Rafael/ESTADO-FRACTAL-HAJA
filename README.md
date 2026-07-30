# ∆ ESTADO-FRACTAL-HAJA ∞

**Projeto de pesquisa, cidadania digital, governança de dados e expressão cultural.**

```text
status_juridico = PROJETO_DECLARATORIO_E_CIVIC_TECH
estado_reconhecido = false
personalidade_internacional_demonstrada = false
certificacao_juridica = false
claim_allowed = false
```

O projeto preserva uma linguagem constitucional, espiritual e artística, mas não declara que um repositório, hash, script, blockchain, domínio, endereço IP ou MPLS produza por si só soberania estatal, tratado internacional, personalidade jurídica, cidadania, certificação, autoria exclusiva ou verdade material.

A versão declaratória anterior permanece rastreável no histórico Git, especialmente no commit `590df75f0b51c25580410cb82d468195f26fdb2b`. Ela deve ser lida como manifesto histórico, não como parecer jurídico vinculante.

## Missão

Organizar, de forma auditável e não coercitiva:

- dignidade humana;
- proteção integral de crianças e adolescentes;
- liberdade de pensamento, consciência, religião e não religião;
- igualdade e não discriminação, inclusive por orientação sexual e identidade de gênero;
- privacidade, autodeterminação informativa e governança de dados;
- autoria, proveniência, atribuição e licenciamento;
- pesquisa científica e educação não comercial;
- incidentes, reparação técnica, prestação de contas e direito de contestação;
- redes MPLS com separação lógica, segurança criptográfica adicional e rastreabilidade.

## Invariantes

```text
manifesto != Estado reconhecido
hash != verdade jurídica
assinatura != consentimento para toda finalidade
repositório público != domínio público
acesso público != licença comercial
licença != registro de software
MPLS/VPN != criptografia
metadado != dado sem risco
crença != coerção
proteção infantil != vigilância infantil
referência constitucional != conformidade automática
```

## Licenciamento por camada

| Material | Regra padrão | Uso comercial |
|---|---|---|
| textos, documentação, diagramas e arte original do projeto | `CC BY-NC-SA 4.0` | exige autorização separada |
| software original identificável | `PolyForm Noncommercial 1.0.0` | exige licença comercial escrita |
| dados e bases | somente quando o manifesto do conjunto declarar titularidade e licença | não presumido |
| componentes de terceiros | licença original do componente | conforme a licença original |
| nomes, selos, símbolos e marcas | nenhum direito marcário é concedido automaticamente | autorização expressa |
| patentes e segredos industriais | nenhuma licença implícita | instrumento específico |

Consulte [`LICENSE.md`](LICENSE.md), [`docs/AUTHORSHIP_AND_PROVENANCE.md`](docs/AUTHORSHIP_AND_PROVENANCE.md) e [`docs/COMMERCIAL_TERMS_DRAFT.md`](docs/COMMERCIAL_TERMS_DRAFT.md).

## Pesquisa e ensino não comercial

O código original pode ser estudado, testado, modificado e redistribuído para finalidades não comerciais conforme a PolyForm Noncommercial 1.0.0. Textos e materiais autorais podem ser compartilhados e adaptados, com atribuição, sem finalidade comercial e sob a mesma licença, conforme CC BY-NC-SA 4.0.

Isto não autoriza automaticamente:

- redistribuir dados de terceiros;
- usar imagem, voz, biografia ou dados pessoais sem base legal;
- oferecer treinamento pago, consultoria, produto, serviço hospedado ou publicidade usando o material;
- afirmar endosso do autor ou do Instituto Rafael;
- usar o projeto como dispositivo médico, sistema de suporte à vida ou controle de infraestrutura crítica sem validação e contrato próprios.

## Limitação de responsabilidade e usos de alto risco

Os artefatos públicos são fornecidos para pesquisa e avaliação, sem garantia de adequação a finalidade específica. Não há autorização operacional, certificação ou validação para:

```text
ressonância magnética e outros equipamentos médicos
suporte à vida
aviação, nuclear, ferroviário ou emergência
controle industrial e infraestrutura crítica
armazenamento ou perfilamento de dados infantis
identificação biométrica coercitiva
decisões jurídicas, clínicas, financeiras ou policiais automatizadas
```

A minuta B2B contém um teto experimental de `US$ 1,00` por dispositivo licenciado para danos diretos ordinários, mas permanece `TOKEN_VAZIO_COUNSEL_APPROVAL`, não integra a licença pública e não alcança situações em que a lei impeça limitação, incluindo dolo, fraude, culpa grave, morte ou lesão corporal, violação de dados, confidencialidade, propriedade intelectual, discriminação ou dano a crianças.

## Privacidade, dignidade e proteção infantil

A governança local adota como gates:

1. finalidade específica e documentada;
2. minimização de dados;
3. base legal e consentimento quando aplicável;
4. melhor interesse de crianças e adolescentes;
5. proibição de exploração comercial infantil, manipulação e perfilamento abusivo;
6. transparência e explicação acessível;
7. acesso, correção, portabilidade, oposição e eliminação quando cabíveis;
8. não discriminação;
9. revisão humana e contestação;
10. registro de incidentes e medidas de mitigação;
11. preservação de evidência sem exposição desnecessária;
12. comunicação a titulares e autoridades quando o limiar legal for atingido.

Consulte [`docs/RIGHTS_PRIVACY_CHILD_SAFEGUARD_CHARTER.md`](docs/RIGHTS_PRIVACY_CHILD_SAFEGUARD_CHARTER.md).

## MPLS

O projeto trata a rede como **MPLS/BGP IP VPN**, quando aplicável. MPLS organiza encaminhamento por rótulos e pode oferecer separação lógica por VRF e políticas de rotas. Ele não fornece, por si só, confidencialidade criptográfica ou integridade ponta a ponta.

A implantação deve combinar, conforme o risco:

```text
MPLS + VRF/RT controlados
+ autenticação do plano de controle
+ IPsec/MACsec ou criptografia de aplicação
+ inventário CE/PE
+ prevenção de route leak
+ logs minimizados e selados
+ resposta a incidentes
```

Consulte [`docs/MPLS_DATA_GOVERNANCE_PROFILE.md`](docs/MPLS_DATA_GOVERNANCE_PROFILE.md).

## Reparação e resposta a incidentes

A resposta automática permitida é técnica e reversível:

```text
conter
→ revogar credenciais
→ preservar evidência
→ interromper tratamento indevido
→ restaurar estado verificado
→ avaliar risco
→ comunicar quando exigido
→ corrigir
→ revisar controles
```

Compensação monetária, multas, custas, indenização, comunicação compulsória a órgãos públicos ou atribuição de culpa dependem da lei aplicável, nexo causal, contraditório e instrumento válido. Não se cria sanção privada automática por simples acusação.

## Jurisprudência e fontes

O projeto mantém um registro separado de fontes primárias e decisões relevantes, sem transformar precedentes estrangeiros em regra universal. Consulte o repositório jurídico federado:

`instituto-Rafael/LGPD-Constituicoes-planetaria-paises-onu-direitos-humanos-e-fundamentais-de-cada-continents-geologic`

## Estado da evidência

```text
estrutura_documental = IMPLEMENTED_DRAFT
licencas_separadas = IMPLEMENTED_DRAFT
uso_cientifico_nao_comercial = DEFINED
uso_comercial = REQUIRES_SEPARATE_AGREEMENT
revisao_juridica_independente = TOKEN_VAZIO
validacao_mpls_em_rede_real = TOKEN_VAZIO
registro_INPI = OPTIONAL_NOT_OBSERVED
claim_allowed = false
```

## Autoria

Obra original declarada por **Rafael Melo Reis — ∆RafaelVerboΩ**, sem prejuízo de direitos de terceiros, colaboradores, fontes citadas e componentes upstream.

A atribuição deve apontar para o arquivo, revisão ou commit utilizado. Hashes e commits ajudam a demonstrar integridade e cronologia; não substituem análise de titularidade, contrato, registro público ou decisão judicial.