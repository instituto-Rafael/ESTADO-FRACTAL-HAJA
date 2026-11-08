# HAJA Ω — Estado de Direito, tratados, promessas de não repetição e jurisprudência comparada | V1

**Tipo:** Dossiê técnico-jurídico de pesquisa + registro verificável de fontes.  
**Estado:** RESEARCH_DRAFT / CLAIM_ALLOWED=false / REVIEW_BY_QUALIFIED_COUNSEL=TOKEN_VAZIO.  
**Emissão:** 2026-11-08. **Produtor:** instituto-Rafael/ESTADO-FRACTAL-HAJA.  
**Antecessor de metodologia:** [Estado de Direito e Ilha das Rosas](HAJA_ESTADO_DIREITO_ILHA_DAS_ROSAS_V1.md).  
**Corpus legível por máquina:** [33 instrumentos](../../data/legal/estado_direito_instruments.v1.jsonl) e [14 decisões](../../data/legal/estado_direito_cases.v1.jsonl). Cada entrada contém fonte, alcance e gaps.  
**IMPORTANTE:** 33 instrumentos ≠ total mundial de tratados; 14 casos ≠ total mundial de jurisprudência. É a **primeira amostra tipada**, a expandir por famílias normativas e jurisdição, sem alegação de exaustividade.

## 1. Fronteira semântica: jurisprudência real versus tese do HAJA

- **TRATADO**: exige texto autêntico, partes, entrada em vigor, reservas, denúncias, cláusulas facultativas, vigência temporal/territorial e competência do órgão. A adoção pelo HAJA não se confunde com ratificação.
- **CONSTITUIÇÃO/NORMA INTERNA**: exige edição vigente, hierarquia, competência e controle de constitucionalidade. Constituição brasileira obriga dentro de sua ordem jurídica; uma pessoa ou associação não funda soberania ao reproduzir artigos.
- **DECLARAÇÃO, RESOLUÇÃO E SOFT LAW**: autoridade normativa/persuasiva variável; não transformá-las sem fundamento em tratados vinculantes.
- **COSTUME INTERNACIONAL/JUS COGENS**: reconhecimento depende de critérios próprios, prática e opinio juris, fontes qualificadas e desenvolvimento jurisprudencial; não presumir universalidade de toda tese.
- **SENTENÇA CONTENCIOSA**: provar o dispositivo, ratio, fatos determinantes, jurisdição e força obrigatória para as partes.
- **OPINIÃO CONSULTIVA**: orientação jurídica, com regime próprio; não equivaler indiscriminadamente a sentença contenciosa.
- **ÓRGÃO QUASE JUDICIAL**: separar achado da Comissão Africana e comunicações de comitês de sentença estatal ou internacional.
- **TESE INTERPRETATIVA HAJA**: proposta autoral baseada em diálogo entre fontes, identificada `NON_BINDING_SYNTHESIS`, sem autorizar jurisdição, coerção, imunidade ou personalidade internacional.

**SOURCE ≠ ARTIFACT ≠ EXECUTION ≠ EVIDENCE ≠ CLAIM.** Nenhum precedente criado nesta pesquisa adquire força jurisprudencial por estar neste repositório.

## 2. Premissas necessárias do Estado de Direito (checklist operacional)

A ONU descreve accountability universal, inclusive do próprio Estado, perante leis públicas, executadas de modo igualitário e julgadas independentemente. A Comissão de Veneza (CDL-AD(2016)007) destaca seis núcleos: legalidade; segurança jurídica; proibição da arbitrariedade; acesso à justiça independente e imparcial; direitos humanos; não discriminação/igualdade.

| Gate | Pergunta falsificável | Evidência exigida | Estado |
| --- | --- | --- | --- |
| ED-01 | A autoridade que edita a regra foi constituída legalmente? | norma constitutiva/competência/publicação | TOKEN_VAZIO |
| ED-02 | Texto é geral, anterior, público, claro e acessível? | publicação, versão, entrada em vigor, linguagem acessível | TOKEN_VAZIO |
| ED-03 | Existe separação e limitação de poderes? | competências independentes, impedimentos, accountability | TOKEN_VAZIO |
| ED-04 | Existe tribunal imparcial e acesso efetivo a remédios? | designação legal, contraditório, defesa, recurso externo | TOKEN_VAZIO |
| ED-05 | Existe igualdade efetiva e vedação de discriminação? | critérios, medidas de inclusão, exame adversarial | TOKEN_VAZIO |
| ED-06 | Direitos não-derrogáveis seguem preservados em emergência? | base legal, limites temporais e materiais, controles | TOKEN_VAZIO |
| ED-07 | Tortura, desaparecimento, escravidão e genocídio são prevenidos? | mecanismos lícitos de prevenção, investigação e responsabilização | TOKEN_VAZIO |
| ED-08 | Crianças e vítimas têm proteção e não revitimização? | salvaguardas, confidencialidade, interesse superior, reparação | TOKEN_VAZIO |
| ED-09 | Há rastreio das obrigações e suas reservas/vigência? | UNTC/autoridade depositária, data, jurisdição, tradução | TOKEN_VAZIO |
| ED-10 | Há regime de recursos, reparação e não repetição? | ação disponível, garantias institucionais, verificação | TOKEN_VAZIO |
| ED-11 | Estados, ONG, associação e ficção cívica estão distinguidos? | documentação de personalidade real e jurisdição real | DOC_SCOPE_ONLY |
| ED-12 | Toda decisão distingue fatos, ratio e dispositivo? | URL oficial; tribunal; data; parágrafos; divergência | PARTIAL_SEED |
| ED-13 | Normas, doutrina, tratados e casos mantêm pesos diferentes? | coluna kind + gate por fonte | DATASET_CREATED_NOT_LEGAL_AUDITED |
| ED-14 | Dados pessoais e históricos das vítimas estão minimizados? | base legal; necessidade; segurança; consentimento se pertinente | TOKEN_VAZIO |
| ED-15 | Há contraditório independente e mecanismo contra abuso interno? | veto/reserva, revisão externa, auditoria, remédio humano | TOKEN_VAZIO |
| ED-16 | Regulamento cívico evita simular autoridade pública? | vedação expressa de coerção, tributos, polícia e passaporte soberano | DOC_SCOPE_ONLY |

A existência desta tabela só documenta critérios. **ED-01..ED-16 não recebem PASS fático de implementação** sem evidência material.

Fontes estruturantes: https://www.un.org/ruleoflaw/en/what-is-the-rule-of-law-archived ; https://www.coe.int/en/web/venice-commission/-/CDL-ad%282016%29007-e ; https://www4.planalto.gov.br/legislacao/legis-federal/constituicao .

## 3. Carta global e regional de obrigações: matriz de instrumentos

A família normativa foi **catalogada**, não ratificada nem integralmente auditada pelo HAJA. No arquivo JSONL estão tipo normativo, fonte oficial disponível, recorte de artigos e pendências.

| Família | Instrumentos no corpus | Compromissos essenciais | Advertência |
| --- | --- | --- | --- |
| Paz e Direito Internacional | N001;N010;N025 | paz; boa-fé; irretroatividade; critérios clássicos de Estado | Carta ONU não cria soberania para organização privada; Montevidéu não basta por autodeclaração |
| Dignidade e garantias | N002;N005;N008;N011;N013;N023;N033 | igualdade; juiz independente; devido processo; remédio eficaz | DUDH é declaração; tutela regional difere |
| Prevenção de atrocidades | N003;N004;N014;N019;N020;N024 | impedir/punir genocídio; guerra; tortura; impunidade | responsabilidade internacional/penal depende de tipos e competência |
| Discriminação e inclusão | N007;N012;N017;N028 | combater racismo; sexismo; capacitismo; proteger direitos indígenas | reserva, obrigação e remédios variam por Estado |
| Infância e pessoas vulneráveis | N006;N015;N016;N018;N029 | refugiados; criança; migrante; vítima de desaparecimento | jurisdição, tratados e protocolos não são universais |
| Trabalho e escravidão | N026;N027;N030 | proibir trabalho forçado e escravidão | N030 tem fonte contextual, texto do tratado pendente |
| Verdade e reparação | N021;N031;N032 | reparação integral; políticas de não repetição; parâmetros institucionais | resolução ONU não é idêntica a obrigação convencional |

**Fonte para 9 tratados centrais de direitos humanos:** lista ONU/OHCHR (https://www.un.org/en/node/143564). **A lista não equivale a ratificação por cada Estado.** A [Carta Democrática Interamericana de 2001](https://www.oas.org/en/iachr/mandate/Basics/democraticcharter.asp) está indexada em N033 como instrumento intergovernamental **não tratado**, distinta da Carta constitutiva da OEA (N032). Para cada tratado: consultar UN Treaty Collection + depositário + versão constitucional nacional antes de emitir afirmação aplicável a Brasil ou terceiro país.

### 3.1 Obrigações expressas, não simples intenções

- **Carta da ONU (1945):** preâmbulo de paz pós-guerras, dignidade, obrigações convencionais; arts.1 e 2 impedem usar o ideal humanitário como pretexto privado para intervenção coercitiva.
- **Convenção do Genocídio (1948), arts.I–V e IX:** Estado-parte se obriga a prevenir/punir o crime; tipo exige intenção específica; incitação direta e pública, tentativa e cumplicidade são contempladas; violações estatais discutíveis na CIJ quando presentes pressupostos de jurisdição.
- **Convenção contra Tortura (1984), arts.2–3 e 6–7:** emergência e ordens superiores não justificam tortura; non-refoulement; investigação e processar/extraditar dependem da relação com as cláusulas convencionais.
- **Convenção Americana (1969), arts.1,2,8,25:** dever de respeitar, garantir, adaptar direito interno e prover proteção judicial.
- **Convenção de Viena (1969), arts.26–28:** boa-fé no cumprimento; direito interno em regra não justifica descumprimento; regra de irretroatividade salvo condição prevista.
- **Estatuto de Roma (1998):** estatuto penal com competência complementar e limites; não abrange toda injustiça nem substitui apuração judicial.
- **Convenção de Montevidéu (1933), art.1:** população permanente; território definido; governo; capacidade para relações internacionais; art.3 não dispensa examinar fatos e prática do direito internacional. Não há demonstração desses elementos para o HAJA.
- **Constituição brasileira de 1988, arts.1,2,5 e 60§4:** Estado Democrático de Direito, dignidade, separação de poderes e cláusulas de proteção constitucional; normas privadas não fazem exceção à Constituição.

## 4. O “nunca mais” situado no tempo: episódios, compromissos e decisões

**Não há um único ato global de promessa de não repetição para cada tragédia.** O arquivo separa o evento, o compromisso ulterior, a norma e o pronunciamento judicial; algumas respostas surgiram *antes* de episódios posteriores e não podem ser artificialmente tratadas como reação causal.

| Episódio de referência | Resposta jurídico-institucional | Casos registráveis | Cautela |
| --- | --- | --- | --- |
| Segunda Guerra, Holocausto e extermínio de grupos | Carta ONU; Nürnberg; Genocídio; DUDH; Genebra 1949 | histórico N001–N004,N024; C001–C002 são casos posteriores | nunca equiparar direito internacional penal a vingança sem julgamento |
| Genocídio em Ruanda (1994) | julgamento do TPI-Ruanda; enquadramento da violência sexual como possível genocídio | C001 Akayesu | dolo específico e individualização probatória |
| Genocídio de Srebrenica (1995) | responsabilização internacional pelo dever de prevenir | C002 Bósnia v. Sérvia | CIJ não atribuiu diretamente os atos do VRS à Sérvia |
| Desaparecimentos na América Latina (ditaduras) | Convenção Americana; dever de investigar; direito à verdade e reparação | C003 Velásquez, C004 Barrios Altos, C005 Gomes Lund, C007 Gelman | controle de convencionalidade não é autoanistia nem poder de punição particular |
| Divergências entre ordens nacional e internacional | diálogo institucional, deveres internacionais, devido processo | C005 Gomes Lund vs C006 ADPF 153 | registrar conflito sem declarar “resolvido” por interpretação do HAJA |
| Tortura e repressão transnacional | Convenção CAT; julgamento CIJ Belgium v Senegal; TEDH Soering | C008,C009 | tempo, jurisdição e risco individual importam |
| Crianças usadas em guerras | Genebra; CRC e protocolo; Estatuto Roma | C010 Lubanga | culpa penal individual, não automaticamente estatal |
| Abuso ambiental, saúde e povos locais | Carta Africana; responsabilidade por violações em Ogoniland | C011 SERAC v Nigeria | decisão da Comissão, não de tribunal |
| Trabalho forçado e dívida servil no Brasil | OIT, Convenção Americana e deveres de prevenção | C012 Brasil Verde | tipificação depende de fatos e direito aplicável |
| Segurança nacional e restrições emergenciais | ECHR; controle jurisdicional de detenção | C013 A and Others v UK | exceções legítimas não eliminam due process |
| Operações policiais e investigação falha | Convenção Americana; garantia de investigação independente | C014 Favela Nova Brasília | distinguir violência, responsabilidade estatal e condenação individual |

A **ONU A/RES/60/147**, princípio 23, contém uma lista específica de garantias de não repetição: controle civil de forças militares e de segurança, devido processo, independência do Judiciário, proteção de defensores e profissões, educação em direitos humanos, padrões éticos para serviços públicos e outras salvaguardas institucionais. São recomendações e princípios que se articulam com obrigações extraídas de tratados e costumes; não convertem a resolução isoladamente em uma sentença. Fonte: https://mandates.un.org/mandate/A/RES/60/147.

## 5. Registro adversarial das decisões singulares

- **C001 Akayesu (TPI-Ruanda, 02/09/1998):** primeira condenação internacional por genocídio e reconhecimento de violência sexual como componente possível do crime; não há presunção de que qualquer agressão seja genocídio.
- **C002 Bósnia v Sérvia (CIJ, 26/02/2007):** provado genocídio em Srebrenica e descumprimento estatal do dever de prevenir; *não* provada atribuição dos atos materiais do VRS ao Estado sérvio. Duas proposições juridicamente diferentes.
- **C003 Velásquez Rodríguez (Corte IDH, 29/07/1988):** desaparecimento forçado e dever positivo de proteção/investigação estatal.
- **C004 Barrios Altos (Corte IDH, 14/03/2001):** leis específicas de autoanistia incompatíveis com a Convenção Americana; garantia de verdade, investigação e sanções nos limites da decisão.
- **C005 Gomes Lund (Corte IDH, 24/11/2010) + C006 ADPF 153 (STF, 29/04/2010):** **conflito de perspectivas internas e convencionais** sobre anistia e justiça de transição; comparar força obrigatória, hierarquia e efeitos sem simplificar a tensão.
- **C007 Gelman (Corte IDH, 24/02/2011):** obrigação de investigar graves violações apesar de obstáculos da Lei de Caducidade uruguaia.
- **C008 Bélgica v Senegal (CIJ, 20/07/2012):** obrigações convencionais de investigar e processar/extraditar sob arts.6(2),7(1) CAT; análise temporal impede universalizar sem restrições.
- **C009 Soering (TEDH, 07/07/1989):** risco concreto de tratamento degradante em eventual extradição pode violar art.3; **não é abolição judicial global da pena de morte**.
- **C010 Lubanga (TPI, 14/03/2012):** condenação penal individual pelo recrutamento/uso de crianças menores de 15 anos em hostilidades.
- **C011 SERAC/CESR v Nigéria (Comissão Africana, 2001):** proteção inter-relacionada de vida, saúde, ambiente e direitos de comunidade; não rotular parecer/comunicação de sentença de Corte.
- **C012 Brasil Verde (Corte IDH, 20/10/2016):** escravidão contemporânea, trabalho forçado e dever estatal de prevenção e resposta; fatos e obrigação são específicos.
- **C013 A and Others (TEDH, 19/02/2009):** limites de medidas excepcionais de detenção e controle judicial.
- **C014 Favela Nova Brasília (Corte IDH, 16/02/2017):** independência e imparcialidade da investigação de mortes e violência sexual.

**Alerta de fonte:** o JSONL contém `source_status`. Quando só há sinopse oficial, ficha do tribunal ou texto reproduzido em repositório institucional, a leitura do inteiro teor e a extração de parágrafos permanecem `TOKEN_VAZIO` até realização; não afirmar revisão integral.

## 6. Teses interpretativas comparadas — NÃO JURISPRUDÊNCIA EMITIDA PELO HAJA

Estas proposições são uma **síntese analítica não vinculante** (NON_BINDING_SYNTHESIS), destinada a avaliação independente. Nunca rotular como decisão judicial, súmula, parecer jurídico assinado, precedente obrigatório ou norma vigente.

**TJ-H01 — Legalidade de duplo limite:** poder e validade formal são necessários, não bastam se direitos fundamentais e proibição de arbitrariedade forem violados. Fundamentação: N001,N002,N022,N023,N033; limite: fontes formais e hierarquia própria.

**TJ-H02 — Dever de prevenir ≠ autoria do crime:** para genocídio, distinguir conhecimento/risco, meios razoáveis de prevenção e atribuição de atos; C002 é o principal teste de falsificação.

**TJ-H03 — A não repetição exige instituições:** memorial, símbolo, constituição nominal e manifesto não substituem investigação, juiz independente, reparação e controle civil. N021 princípio 23; C003–C007.

**TJ-H04 — Anistia não elimina automaticamente verdade:** examinar gravidade, jurisdição, tipo de anistia, direito nacional e decisões internacionais; C004/C005/C006/C007 formam um **nó de conflito**, não unanimidade.

**TJ-H05 — Ordem superior/emergência não licencia tortura:** N014 art.2; C008/C009, com análise de tempo e responsabilidade.

**TJ-H06 — O sofrimento de vulneráveis exige prevenção antes de algoritmo:** criança, refugiado, pessoa escravizada, vítima de violência e defensor de direitos têm proteção contra arbitrariedade, exposição e revitimização. N006,N015,N021; C010,C012.

**TJ-H07 — Compromisso político ≠ tratado vinculante:** N020 (R2P), N021 (resolução de reparações), N022 (checklist) têm pesos distintos. Cooperação multilateral não equivale a permissão de violência unilateral.

**TJ-H08 — Sem consentimento válido e jurisdição, não há poder estatal:** a denominação “Estado Fractal” e símbolos são expressão cívica; N025 art.1 e atos factuais exigem prova; qualquer pretensão de soberania, imunidade, cidadania vinculante ou polícia está BLOQUEADA.

**TJ-H09 — Ciência de redes organiza o conhecimento, não legitima soberania:** grafos tipo norma→fato→caso→holding→limite ajudam auditoria, não alteram fontes nem direito; [literatura de redes complexas 2026](../research/HENRIQUE_FERRAZ_DE_ARRUDA_REDES_COMPLEXAS_2026_V2.md).

**TJ-H10 — No caso singular, fatos adversos são parte do fundamento:** sem tribunal, data, competência, fatos, ratio, dispositivo e casos contraditórios, nenhum “precedente” pode ser promovido para CLAIM_ALLOWED.

## 7. Navegação sem fricção e expansão controlada

**Rota curta:** `001_PONTEIRO/START_HERE.md` → este dossiê → `data/legal/estado_direito_instruments.v1.jsonl` → `data/legal/estado_direito_cases.v1.jsonl` → URL oficial → revisão jurisdicional → receipt.

**Tipos de aresta do grafo:** `GROUNDED_IN`, `INTERPRETS`, `DECIDES`, `LIMITS`, `CONFLICTS_WITH`, `HISTORICAL_TRIGGER`, `PROTECTS`, `APPLIES_ONLY_IF`, `SUPERSEDES`. Cada edge exige `source_url` e, quando afirmada temporalidade causal, referência histórica específica. Proibido declarar uma ligação causal pelo mero fato de precedência cronológica.

**Expansão para “cada” norma exige lotes audíveis, sem fingir exaustão:**
1. Enumerar repositórios oficiais por família (ONU Treaty Collection, OHCHR, depositários, OEA, Conselho da Europa, União Africana, OIT, CICV, legislação e jurisprudência nacionais).
2. Para cada instrumento, criar entradas por artigo: `article_id`, texto oficial, edição, reserva, status de vigência, jurisdição, exceção, órgão monitor, link verificado, classificação de força, regra de admissibilidade.
3. Para cada caso, ler inteiro teor e anexar parágrafos exatos do holding, voto dissidente, status de cumprimento, decisão posterior e conflitos.
4. Fazer joins apenas por IDs tipados; toda relação inferida = `HYPOTHESIS`; lacunas = `TOKEN_VAZIO`.
5. Gate jurídico por Estado/época/órgão. Não mover de `INDEXED` para `LEGAL_VERIFIED` com CI de arquivos apenas.

**Escopo deste lote:** 33 instrumentos indexados, 14 decisões resumidas por fontes judiciais/institucionais, seis pilares e 16 gates. **Não** foram auditados todos os artigos, reservas, status de ratificação/denúncia de cada Estado, traduções, cumprimentos, opiniões separadas ou atualizações posteriores. Estes itens são lacunas materiais para expansão, não zero.

## 8. Segurança, direito e reversibilidade

Proibida coleta de dados pessoais de vítimas, nomes de crianças, dados de saúde ou relatos sensíveis como requisito para catalogação; usar somente informações públicas necessárias, e não expor pessoas vulneráveis. Não atribuir culpa criminal a não condenados. Não usar fontes acadêmicas como sentença; não automatizar coerção nem supostas sanções cívicas.

**Gate final:** `claim_allowed=false`, `recognized_state_claim=false`, `legal_adoption=TOKEN_VAZIO`, `counsel_review=TOKEN_VAZIO`, `merger_requires_human_decision=true`. No código, validadores só verificam consistência/forma e referência dos registros, **nunca certificam adequação ao Direito**.

**R3 = <primeiro corpus legal estruturado e teses comparativas identificadas, revisão artigo por artigo e aplicabilidade jurisdicional pendentes, ampliação sequencial guiada por evidências com parecer independente>.**
