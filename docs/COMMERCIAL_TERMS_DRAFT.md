# Minuta de termos comerciais e responsabilidade — NÃO ATIVA

```text
status = DRAFT_FOR_COUNSEL_REVIEW
claim_allowed = false
counsel_approval = TOKEN_VAZIO
binding_effect = NONE_UNTIL_SIGNED
```

Esta minuta não altera as licenças públicas do repositório e não constitui oferta automática. Serve para negociação B2B individualizada.

## 1. Objeto

Licença comercial limitada para software e materiais originais expressamente listados em anexo, por dispositivo, instância, usuário, organização ou finalidade definida.

## 2. Escopo mensurável

O contrato deve definir:

```text
licensed_artifacts
licensed_version
licensed_devices_or_instances
permitted_purposes
territory
term
support_level
security_profile
telemetry_profile
personal_data_roles
subprocessors
exit_and_deletion
```

## 3. Teto experimental por dispositivo

Para danos diretos ordinários decorrentes do software licenciado, a minuta admite, apenas onde legalmente permitido:

```text
ordinary_direct_damage_cap_usd = 1.00 per affected licensed device
aggregate_cap = sum of caps for affected licensed devices
```

O teto não se aplica, ou deve ser substituído pelo limite obrigatório da lei, em casos de:

- dolo, fraude ou declaração intencionalmente falsa;
- culpa grave quando não limitável;
- morte, lesão corporal ou risco à saúde;
- violação de confidencialidade ou segurança;
- tratamento ilícito de dados pessoais;
- dano ou exploração de crianças e adolescentes;
- discriminação;
- infração de propriedade intelectual de terceiros;
- obrigações que a lei, decisão judicial ou autoridade competente proíba limitar.

Nenhum teto cria imunidade. A validade depende da jurisdição, natureza das partes, equilíbrio contratual, transparência e normas obrigatórias.

## 4. Ausência de garantia

O produto não deve ser descrito como certificado, seguro para missão crítica, clinicamente validado ou adequado a infraestrutura crítica sem anexo técnico e evidência correspondente.

## 5. Usos de alto risco

Uso em ressonância magnética, equipamento médico, suporte à vida, aviação, nuclear, defesa, emergência, transporte, controle industrial, biometria coercitiva, justiça, policiamento ou perfilamento infantil exige:

```text
separate_high_risk_addendum
independent_validation
hazard_analysis
human_oversight
fail_safe
rollback
incident_plan
insurance_review
regulatory_review
```

Sem esses elementos:

```text
production_authorization = false
```

## 6. Dados, telemetria e atualizações

A coleta deve ser limitada ao necessário e documentada em tabela:

| Campo | Obrigatório |
|---|---|
| categoria de dado | sim |
| finalidade | sim |
| base legal | sim |
| retenção | sim |
| destinatários | sim |
| transferência internacional | quando houver |
| opção de desativação | quando tecnicamente e legalmente possível |
| impacto da desativação | sim |
| dados infantis | proibidos por padrão |

Atualização não autoriza finalidade nova de coleta. Mudança material exige aviso e, quando aplicável, novo consentimento ou outra base legal válida.

## 7. Obrigações do fornecedor

- manter inventário de componentes e versões;
- publicar vulnerabilidades conhecidas de modo responsável;
- preservar logs mínimos e íntegros;
- corrigir falhas conforme severidade e SLA;
- não ampliar telemetria silenciosamente;
- cooperar com titulares e autoridades dentro da lei;
- preservar capacidade de exportação e encerramento.

## 8. Obrigações do licenciado

- usar apenas no escopo contratado;
- não inserir dados sem base legal;
- proteger credenciais e chaves;
- manter ambiente, backups e dependências sob controle;
- comunicar incidentes relevantes;
- não remover avisos de autoria;
- não atribuir certificação ou endosso inexistente.

## 9. Indenização e custas

Indenização não é automática por mera acusação. Somente pode abranger valores:

```text
razoáveis
+ documentados
+ causalmente relacionados
+ permitidos pela lei
+ definidos por acordo, decisão ou procedimento com contraditório
```

A parte responsável por tratamento ilícito, uso comercial não autorizado, violação de direitos ou omissão contratual comprovada poderá responder por:

- contenção e investigação;
- notificação legalmente exigida;
- restauração e correção;
- auditoria independente proporcional;
- custas e honorários quando previstos em lei, contrato válido ou decisão.

## 10. Reparação técnica automática

O sistema pode executar medidas técnicas previamente autorizadas:

```text
suspender token
revogar chave
bloquear exportação
preservar evidência
parar job
restaurar versão segura
notificar responsáveis
abrir incidente
```

Não pode executar automaticamente:

- cobrança punitiva;
- exposição pública de acusado;
- destruição de dados sem política;
- comunicação falsa a autoridade;
- admissão de culpa;
- decisão sobre indenização.

## 11. Denúncia e auditoria

Toda denúncia recebe ID, timestamp, escopo, evidência, classificação de risco, responsável e decisão. A acusação e a resposta devem permanecer separadas.

```text
allegation != finding
finding != final_liability
```

## 12. Autoridades e cooperação

A mobilização de ANPD, autoridade de defesa do consumidor, Ministério Público, polícia, regulador setorial ou tribunal depende de competência, limiar legal, risco e dever de comunicação. O contrato não cria poderes públicos privados.

## 13. Lei aplicável e revisão

A lei aplicável, foro, arbitragem, proteção do consumidor, conflito de leis e idioma prevalente devem ser preenchidos por advogado habilitado antes da assinatura.

## 14. Variáveis abertas

```text
legal_entity_of_licensor = TOKEN_VAZIO
jurisdiction = TOKEN_VAZIO
commercial_price = TOKEN_VAZIO
insurance = TOKEN_VAZIO
counsel_review = TOKEN_VAZIO
regulatory_scope = TOKEN_VAZIO
```