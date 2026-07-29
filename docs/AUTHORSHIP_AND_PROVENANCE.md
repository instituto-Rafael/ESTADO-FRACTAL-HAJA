# Autoria, proveniência e diferenciação autoral

## Objetivo

Separar cinco perguntas que não podem ser respondidas por um único hash:

```text
quem criou?
quem possui direitos?
qual versão foi usada?
qual licença se aplica?
qual evidência sustenta a afirmação?
```

## Tipos de autoria

| Tipo | Campo canônico | Significado |
|---|---|---|
| autoria humana declarada | `declared_author` | pessoa que declara ter criado a expressão |
| titularidade | `rightsholder` | pessoa ou entidade que possui os direitos patrimoniais |
| contribuição | `contributors[]` | participantes com escopo delimitado |
| upstream | `upstream_source` | projeto anterior do qual parte do material deriva |
| assistência por ferramenta | `tool_assistance[]` | IA, editor, compilador ou gerador utilizado |
| curadoria | `curator` | quem selecionou, ordenou ou anotou materiais |
| execução | `executor` | quem executou o procedimento |
| revisão | `reviewer` | quem realizou análise independente |

Esses papéis podem pertencer a pessoas diferentes.

## Registro mínimo por artefato

```yaml
artifact_id: ART-...
title: ...
path: ...
revision: commit_sha
created_at: ...
declared_author: ...
rightsholder: ...
contributors: []
upstream_source: null
tool_assistance: []
license: ...
third_party_material: []
sha256: ...
claim_boundary: ...
```

## O que o Git demonstra

Um commit assinado ou identificado pode ajudar a demonstrar:

- que determinado conteúdo existia naquela revisão;
- que uma conta registrou uma alteração;
- relação cronológica entre versões;
- integridade relativa do objeto versionado.

Ele não demonstra sozinho:

- que a pessoa da conta é a única autora;
- que não existe anterioridade fora do repositório;
- que todo conteúdo é original;
- que direitos de terceiros foram liberados;
- que uma hipótese científica é verdadeira;
- que um contrato foi validamente aceito.

## Registro de software

O registro perante autoridade pública pode fortalecer prova de autoria ou titularidade. A ausência de registro não deve ser descrita como ausência automática de proteção autoral. O estado correto é:

```text
copyright_protection = GOVERNED_BY_APPLICABLE_LAW
public_registration = OPTIONAL_OR_CONTEXT_DEPENDENT
registration_observed = TOKEN_VAZIO
```

## Contribuições

Toda contribuição deve incluir declaração semelhante ao Developer Certificate of Origin:

> Declaro que tenho o direito de submeter esta contribuição sob a licença indicada, que identifiquei materiais de terceiros e que não inseri dados pessoais ou conteúdo confidencial sem autorização.

## IA e geração assistida

A utilização de IA deve ser registrada sem atribuir automaticamente autoria jurídica à ferramenta.

```text
prompt != autoria completa
saída gerada != originalidade garantida
revisão humana != titularidade automática de terceiros
```

O responsável pelo commit deve revisar:

- direitos;
- dados pessoais;
- segurança;
- atribuições;
- coerência factual;
- limites do claim.

## Metadados autorais

Metadados devem ser tratados como evidência de proveniência, não como conteúdo infalível. Eles podem ser alterados, removidos, copiados ou reconstruídos.

A confiança depende de:

```text
fonte
+ assinatura
+ timestamp
+ cadeia de custódia
+ consistência externa
+ possibilidade de contestação
```

## Política de atribuição

Uma atribuição adequada deve informar:

1. autor ou titular declarado;
2. título ou identificação do artefato;
3. revisão ou commit utilizado;
4. licença;
5. alterações efetuadas;
6. componentes de terceiros relevantes;
7. ausência de endosso.

## Correção e contestação

Qualquer pessoa pode apresentar evidência de autoria, titularidade, atribuição incorreta ou exposição indevida. A resposta deve:

```text
registrar alegação
→ preservar evidência
→ reduzir exposição quando necessário
→ ouvir partes relevantes
→ corrigir metadados
→ publicar decisão delimitada
```

Nenhuma contestação deve ser resolvida por intimidação, exposição de dados pessoais ou sanção automática.