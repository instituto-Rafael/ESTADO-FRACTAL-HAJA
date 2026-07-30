# Perfil MPLS de segurança, privacidade e governança de dados

```text
version = MPLS_DATA_GOVERNANCE_PROFILE_V1
status = IMPLEMENTED_DOCUMENTARY_BASELINE
network_validation = TOKEN_VAZIO_REAL_MPLS_ENVIRONMENT
claim_allowed = false
```

## 1. Escopo

Este perfil governa redes que utilizem MPLS, BGP/MPLS IP VPN, VRF, route distinguishers, route targets e dispositivos CE/PE/P.

A invariante fundamental é:

```text
MPLS label switching != encryption
VRF separation != end-to-end confidentiality
private carrier network != zero trust
route target != authorization for data processing
```

MPLS organiza encaminhamento e separação lógica. Confidencialidade, integridade, autenticação, finalidade e direitos dos titulares exigem controles adicionais.

## 2. Inventário mínimo

Toda implantação deve possuir inventário versionado:

```yaml
service_id: ...
customer_or_domain: ...
ce_devices: []
pe_devices: []
p_devices: []
vrfs: []
route_distinguishers: []
import_route_targets: []
export_route_targets: []
address_families: []
control_plane_protocols: []
encryption_overlays: []
data_categories: []
children_in_scope: false
owners: []
rollback_ref: ...
```

## 3. Separação de rotas

Controles obrigatórios:

1. `RD` único conforme política documentada;
2. `RT import/export` mínimo e revisado;
3. proibição de wildcard ou importação ampla sem justificativa;
4. limites de prefixos por vizinho;
5. filtros de entrada e saída;
6. validação de origem quando aplicável;
7. isolamento de management plane;
8. revisão de extranet e shared-services;
9. detecção de route leak;
10. rollback testado para mudanças de RT/VRF.

## 4. Plano de controle

- autenticar sessões BGP/LDP quando suportado e coerente com a arquitetura;
- aplicar TTL security, ACLs e CoPP/CPPr quando disponíveis;
- restringir vizinhos e interfaces autorizadas;
- registrar alterações de política e adjacência;
- proteger chaves e senhas em cofre apropriado;
- desabilitar protocolos e serviços não utilizados;
- sincronizar tempo por fonte confiável e registrar incerteza;
- separar operador, aprovador e auditor para alterações críticas.

## 5. Confidencialidade e integridade

Quando o risco exigir proteção criptográfica, combinar MPLS com uma ou mais camadas:

```text
IPsec site-to-site or per-application
MACsec on eligible links
TLS/mTLS at application layer
object or field-level encryption
key rotation and revocation
```

A escolha deve documentar:

- fronteira criptográfica;
- algoritmo e versão;
- gestão de chaves;
- identidade de endpoints;
- tratamento de falha;
- impacto de rotação;
- recuperação e continuidade.

## 6. Metadados de rede

Logs MPLS/BGP/VRF podem revelar:

```text
organizações conectadas
localização e topologia
horários e hábitos
volume de tráfego
incidentes
identificadores de dispositivos
relações entre domínios
```

Logo, devem possuir:

- finalidade;
- base legal;
- retenção;
- acesso por função;
- minimização;
- pseudonimização quando possível;
- trilha de exportação;
- descarte verificável;
- proteção contra correlação indevida.

## 7. Crianças e adolescentes

Por padrão:

```text
child_personal_data_over_mpls = PROHIBITED_UNLESS_SPECIFICALLY_AUTHORIZED_AND_SAFEGUARDED
behavioral_advertising = false
profiling_for_remuneration = false
biometric_tracking = false
```

Se um serviço essencial exigir dados infantis, devem existir:

- avaliação de melhor interesse;
- minimização reforçada;
- segregação lógica e criptográfica;
- retenção mínima;
- supervisão humana;
- canal acessível de contestação;
- proibição de reutilização comercial;
- resposta acelerada a incidente.

## 8. Atualizações e telemetria

Atualização de roteador, controladora ou software de rede não autoriza coleta ilimitada.

Cada atualização deve registrar:

```text
vendor
version_before
version_after
hashes
release_notes
telemetry_delta
new_destinations
new_data_categories
rollback
maintenance_window
operator
approver
result
```

Mudança de telemetria deve ser tratada como mudança de processamento de dados.

## 9. Incidentes

### Classes

```text
ROUTE_LEAK
VRF_CROSS_CONNECT
PREFIX_HIJACK
CONTROL_PLANE_COMPROMISE
KEY_OR_CREDENTIAL_EXPOSURE
UNAUTHORIZED_TELEMETRY
PERSONAL_DATA_EXPOSURE
CHILD_DATA_EXPOSURE
AVAILABILITY_FAILURE
CONFIGURATION_DRIFT
```

### Ciclo

```text
DETECT
→ VERIFY
→ CONTAIN
→ PRESERVE
→ REVOKE_OR_FILTER
→ RESTORE
→ ASSESS_DATA_RISK
→ NOTIFY_IF_REQUIRED
→ CORRECT
→ REVIEW
```

Nenhum evento deve ser classificado como violação confirmada apenas por alarme automático.

## 10. Reparação técnica

A automação pode:

- retirar rota;
- aplicar filtro previamente aprovado;
- revogar chave;
- colocar VRF em quarentena;
- congelar alteração;
- restaurar configuração conhecida;
- preservar snapshot e logs;
- abrir caso e notificar responsáveis.

A automação não pode:

- declarar culpado;
- impor multa;
- divulgar pessoa ou organização;
- destruir evidência;
- acionar autoridade com informação não verificada, salvo obrigação emergencial legalmente definida.

## 11. Auditoria de denúncia

Cada denúncia recebe:

```yaml
case_id: ...
allegation: ...
received_at: ...
reporter_protection: ...
scope: ...
evidence_refs: []
initial_risk: ...
preservation_actions: []
independent_reviewer: ...
finding: TOKEN_VAZIO
corrective_action: TOKEN_VAZIO
appeal_path: ...
```

A denúncia deve produzir auditoria proporcional, preservando contraditório, privacidade e proteção contra retaliação.

## 12. Gate de 20 controles

| ID | Controle | Estado inicial |
|---|---|---|
| M01 | inventário CE/PE/P | `TOKEN_VAZIO` |
| M02 | inventário VRF/RD/RT | `TOKEN_VAZIO` |
| M03 | proprietário do serviço | `TOKEN_VAZIO` |
| M04 | filtros e limites de prefixo | `TOKEN_VAZIO` |
| M05 | prevenção de route leak | `TOKEN_VAZIO` |
| M06 | autenticação do plano de controle | `TOKEN_VAZIO` |
| M07 | proteção do management plane | `TOKEN_VAZIO` |
| M08 | criptografia adicional | `TOKEN_VAZIO` |
| M09 | gestão de chaves | `TOKEN_VAZIO` |
| M10 | finalidade de logs | `TOKEN_VAZIO` |
| M11 | retenção de logs | `TOKEN_VAZIO` |
| M12 | minimização de telemetria | `TOKEN_VAZIO` |
| M13 | dados sensíveis mapeados | `TOKEN_VAZIO` |
| M14 | dados infantis excluídos ou protegidos | `TOKEN_VAZIO` |
| M15 | resposta a incidentes | `TOKEN_VAZIO` |
| M16 | rollback testado | `TOKEN_VAZIO` |
| M17 | segregação de funções | `TOKEN_VAZIO` |
| M18 | revisão independente | `TOKEN_VAZIO` |
| M19 | receipt de execução real | `TOKEN_VAZIO` |
| M20 | decisão de promoção | `BLOCKED` |

Nenhuma média compensa controle obrigatório ausente.

## 13. Referências técnicas primárias

- IETF RFC 3031 — MPLS Architecture.
- IETF RFC 4364 — BGP/MPLS IP VPNs.
- IETF RFC 5920 — Security Framework for MPLS and GMPLS Networks.
- IETF RFC 8964 — MPLS data-plane security observations.

## 14. Saída do `TOKEN_VAZIO`

O perfil só pode ser promovido após:

```text
configurações reais minimizadas
+ inventário completo
+ teste de route leak
+ teste de isolamento VRF
+ teste criptográfico
+ teste de rollback
+ exercício de incidente
+ receipt assinado
+ revisão independente
```
