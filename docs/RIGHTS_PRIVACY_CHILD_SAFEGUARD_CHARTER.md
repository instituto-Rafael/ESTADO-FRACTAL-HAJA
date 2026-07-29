# Carta de direitos, privacidade, dignidade e proteção infantil

```text
status = GOVERNANCE_BASELINE_DRAFT
legal_compliance_claim = false
certification_claim = false
```

## 1. Princípio de não coerção

A liberdade de pensamento, consciência, religião, espiritualidade e não religião deve coexistir com igualdade, segurança e dignidade.

```text
crença protegida != imposição de crença
liberdade de expressão != licença para discriminar
proteção contra ódio != censura de doutrina pacífica
```

## 2. Dignidade humana

Nenhuma pessoa deve ser reduzida a:

- perfil comercial;
- rótulo algorítmico;
- biometria reutilizável sem controle;
- objeto de experimentação não consentida;
- instrumento de propaganda;
- fonte de dados indefinida;
- categoria inferior por raça, origem, sexo, gênero, orientação sexual, identidade de gênero, deficiência, idade, religião ou não religião.

## 3. Proteção integral de crianças e adolescentes

O melhor interesse da criança é gate prioritário.

### Proibições padrão

- publicidade comportamental baseada em perfil infantil;
- venda ou aluguel de dados infantis;
- desenho manipulativo e compulsivo;
- reconhecimento emocional ou biométrico sem necessidade e base legal;
- treinamento de IA com dados infantis sem direitos verificados;
- exploração de imagem, voz, localização, saúde, escola ou relações familiares;
- contato não supervisionado que aumente risco de aliciamento;
- decisão exclusivamente automatizada com efeito relevante.

### Requisitos mínimos

```text
age_appropriate_design
best_interest_assessment
data_minimization
purpose_limitation
verified_guardian_flow_when_required
child_accessible_notice
human_oversight
reporting_channel
rapid_containment
retention_limit
```

Consentimento do responsável não transforma qualquer prática em legítima. Necessidade, proporcionalidade, segurança e interesse da criança continuam obrigatórios.

## 4. Privacidade e autodeterminação informativa

Todo tratamento deve possuir registro:

```yaml
purpose: ...
legal_basis: ...
data_categories: ...
subjects: ...
children_in_scope: false
recipients: []
retention: ...
security_controls: []
international_transfer: ...
human_contact: ...
```

### Direitos operacionais

Quando aplicável, o sistema deve suportar:

- confirmação de tratamento;
- acesso;
- correção;
- explicação de finalidade e compartilhamentos;
- portabilidade;
- oposição;
- revisão humana;
- revogação de consentimento;
- eliminação ou anonimização;
- contestação de decisões.

## 5. Não discriminação e diversidade

Testes devem incluir grupos e condições relevantes sem coletar dados sensíveis além do necessário.

```text
fairness_metric != ausência de discriminação provada
paridade estatística != justiça universal
boa intenção != impacto seguro
```

A proteção inclui orientação sexual e identidade de gênero, sem prejudicar a liberdade religiosa pacífica. Expressão religiosa não pode incitar hostilidade, violência ou discriminação contra pessoas.

## 6. Dados sensíveis

Biometria, saúde, genética, religião, orientação sexual, identidade de gênero e outros dados sensíveis exigem controles reforçados.

- não inferir crença ou sexualidade por comportamento;
- não usar biometria como identificador universal;
- separar autenticação de vigilância;
- preferir processamento local e templates revogáveis;
- documentar falsos positivos e possibilidade de recurso;
- restringir acesso por função;
- registrar exportações e consultas privilegiadas.

## 7. Metadados

Metadados podem revelar localização, relações, hábitos, identidade, crenças e saúde. Não devem ser classificados como inofensivos apenas por não conterem o conteúdo principal.

O inventário deve abranger:

```text
timestamps
IP and device identifiers
routing labels and VRFs
location
contact graphs
access logs
update telemetry
model prompts and outputs
file hashes linked to persons
```

## 8. Incidentes

Fluxo mínimo:

```text
DETECT
→ CONFIRM
→ CLASSIFY
→ CONTAIN
→ PRESERVE
→ MITIGATE
→ NOTIFY_IF_REQUIRED
→ REPAIR
→ REVIEW
```

O registro deve separar:

```text
vulnerability
suspected_event
confirmed_incident
relevant_harm_threshold
regulatory_notification
final_finding
```

## 9. Reparação

Reparação técnica pode incluir:

- restaurar disponibilidade;
- corrigir dado incorreto;
- apagar cópia indevida quando permitido;
- revogar credenciais;
- cessar finalidade incompatível;
- fornecer exportação;
- comunicar titulares;
- custear medidas razoáveis definidas por lei, acordo ou decisão.

Reparação financeira automática sem processo, base legal ou acordo é proibida.

## 10. Transparência de atualizações

Atualização de software deve informar, de forma proporcional:

- componentes alterados;
- dados novos coletados;
- finalidade;
- impacto de segurança;
- compatibilidade;
- rollback;
- período de suporte;
- mudanças de licença.

## 11. Fiscalização e denúncia

Canais de denúncia não podem ser usados para assédio ou exposição de dados.

Toda denúncia deve receber:

```text
case_id
received_at
scope
risk
preservation_action
owner
status
appeal_path
closure_reason
```

## 12. Fontes de referência

O repositório jurídico federado mantém as fontes primárias, decisões e datas. Esta Carta é uma política interna e não substitui LGPD, GDPR, ECA, Constituição, decisões judiciais, regras setoriais ou aconselhamento profissional.