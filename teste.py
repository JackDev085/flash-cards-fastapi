import sqlite3 

cards = [
    {"question": "O que é uma lei ordinária e como é aprovada?", "answer": "Lei aprovada pela maioria simples no Congresso Nacional.", "theme_id": 5, "category_id": 2},
    {"question": "Qual a diferença entre lei complementar e lei ordinária?", "answer": "Lei complementar exige maioria absoluta; lei ordinária, maioria simples.", "theme_id": 5, "category_id": 2},
    {"question": "O que é um decreto e quem pode emitir?", "answer": "Ato normativo emitido pelo Presidente da República.", "theme_id": 5, "category_id": 2},
    {"question": "O que é uma medida provisória e seus prazos?", "answer": "Norma com força de lei, válida por 60 dias, prorrogável.", "theme_id": 5, "category_id": 2},
    {"question": "Quais são as etapas do processo legislativo?", "answer": "Iniciativa, discussão, votação, sanção ou veto, e promulgação.", "theme_id": 5, "category_id": 2},
    {"question": "O que é um veto presidencial e como pode ser derrubado?", "answer": "Rejeição de um projeto de lei; derrubado por maioria absoluta.", "theme_id": 5, "category_id": 2},
    {"question": "O que é uma emenda constitucional e como é aprovada?", "answer": "Alteração na Constituição, aprovada por 3/5 do Congresso.", "theme_id": 5, "category_id": 2},
    {"question": "O que é o quórum de aprovação para leis ordinárias?", "answer": "Maioria simples dos presentes no Congresso.", "theme_id": 5, "category_id": 2},
    {"question": "O que é uma lei delegada e como é criada?", "answer": "Lei elaborada pelo Executivo, com autorização do Legislativo.", "theme_id": 5, "category_id": 2},
    {"question": "O que é o controle de constitucionalidade e quem o faz?", "answer": "Verificação de leis com a Constituição; feito pelo STF.", "theme_id": 5, "category_id": 2},
    {"question": "O que é o princípio da legalidade na administração pública?", "answer": "Ninguém é obrigado a fazer algo sem lei.", "theme_id": 5, "category_id": 2},
    {"question": "Qual a função do poder legislativo no processo de criação de leis?", "answer": "Criar, discutir e aprovar leis para o país.", "theme_id": 5, "category_id": 2},
    {"question": "O que é uma súmula vinculante e qual seu efeito?", "answer": "Decisão do STF com efeito obrigatório para todos.", "theme_id": 5, "category_id": 2},
    {"question": "O que é uma lei orgânica e onde se aplica?", "answer": "Lei que regula a organização dos municípios.", "theme_id": 5, "category_id": 2},
    {"question": "O que é o trâmite legislativo de um projeto de lei?", "answer": "Caminho que um projeto percorre até virar lei.", "theme_id": 5, "category_id": 2},
    {"question": "O que é uma lei federal e qual seu alcance?", "answer": "Lei válida em todo o território nacional.", "theme_id": 5, "category_id": 2},
    {"question": "O que é uma lei estadual e quem a cria?", "answer": "Lei válida apenas em um estado; criada pela Assembleia Legislativa.", "theme_id": 5, "category_id": 2},
    {"question": "O que é uma lei municipal e quem a aprova?", "answer": "Lei válida apenas em um município; aprovada pela Câmara Municipal.", "theme_id": 5, "category_id": 2},
    {"question": "O que é o princípio da anterioridade na legislação tributária?", "answer": "Lei tributária não pode retroagir para prejudicar.", "theme_id": 5, "category_id": 2},
    {"question": "O que é o princípio da irretroatividade das leis?", "answer": "Lei não pode afetar fatos ocorridos antes de sua vigência.", "theme_id": 5, "category_id": 2},
    {"question": "O que é uma lei de iniciativa popular e como é proposta?", "answer": "Lei proposta por cidadãos, com assinaturas comprovadas.", "theme_id": 5, "category_id": 2},
    {"question": "O que é o plenário do Congresso e qual sua função?", "answer": "Reunião de todos os parlamentares para votar projetos.", "theme_id": 5, "category_id": 2},
    {"question": "O que é uma comissão parlamentar e qual seu papel?", "answer": "Grupo que analisa e emite parecer sobre projetos de lei.", "theme_id": 5, "category_id": 2},
    {"question": "O que é o regimento interno do Congresso?", "answer": "Conjunto de normas que regem o funcionamento do Legislativo.", "theme_id": 5, "category_id": 2},
    {"question": "O que é uma lei de diretrizes orçamentárias (LDO)?", "answer": "Lei que define as prioridades do orçamento anual.", "theme_id": 5, "category_id": 2},
    {"question": "O que é uma lei de efeitos concretos?", "answer": "Lei que resolve situações específicas e pontuais.", "theme_id": 5, "category_id": 2},
    {"question": "O que é uma lei de ordem pública?", "answer": "Lei que protege o interesse geral da sociedade.", "theme_id": 5, "category_id": 2},
    {"question": "O que é uma lei de caráter geral?", "answer": "Lei aplicável a todos os cidadãos de forma igual.", "theme_id": 5, "category_id": 2},
    {"question": "O que é uma lei de caráter especial?", "answer": "Lei aplicável a grupos ou situações específicas.", "theme_id": 5, "category_id": 2},
    {"question": "O que é uma lei de caráter temporário?", "answer": "Lei com prazo de validade definido.", "theme_id": 5, "category_id": 2}
]

conn = sqlite3.connect('db.db')
cursor = conn.cursor()

for i in range(len(cards)):
    cursor.execute("INSERT INTO cards (question, answer, theme_id, category_id) VALUES (?,?,?,?)", (cards[i]['question'], cards[i]['answer'], cards[i]['theme_id'], cards[i]['category_id']))

conn.commit()
