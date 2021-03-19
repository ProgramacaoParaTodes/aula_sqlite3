import sqlite3

# cria o banco de dados
conexao = sqlite3.connect("meu_banco.db")

# cria o cursor que executa as consultas
cursor = conexao.cursor()

# consulta para criar tabela
criar_tabela = """CREATE TABLE IF NOT EXISTS t_clientes (
  cpf TEXT,
  nome TEXT,
  email TEXT,
  mobile TEXT,
  renda REAL,
  nascimento DATE,
  PRIMARY KEY (cpf)  
)"""

# executar a consulta criar_tabela
cursor.execute(criar_tabela)

# consulta para inserir dados na tabela
inserir_dados = """INSERT INTO t_clientes VALUES
    ('709.688.737-74', 'Márcio Benedito Julio', 'marciobene@terra.com.br', '(21) 99888-7611', 95900.0, '1979-12-19'),
    ('025.819.062-00', 'Erick Giovanni da Silva Jr.', 'erick1234@gmail.com', '(62) 98852-3498', 8000.0, '1965-10-12'),
    ('458.081.579-35', 'Beatriz da Conceição', 'biaconceicao@uol.com.br', '(51) 99585-4539', 11000.0, '1981-11-12'),
    ('320.755.040-16', 'Rafael Jorge Anderson', 'rafajorge@protonmail.com', '(21) 99978-3334', 10000.0, '1942-05-12'),
    ('564.329.869-40', 'Antonella Carolina Assunção', 'assuncao1990@yahoo.com', '(68) 98157-8607', 4800.0, '1990-12-12'),
    ('070.659.356-12', 'Henry Miguel Corte Real', 'henrycortereal@gmail.com', '(11) 92991-0987', 4000.0, '1974-04-12'),
    ('720.395.977-51', 'Nicolas Alexandre Freitas', 'nickyfreitas@uol.com.br', '(31) 99712-7743', 3000.0, '1983-01-12'),
    ('787.440.220-00', 'Stella Aparício', 'stellaaparicio@hotmail.com', '(21) 99954-3544', 5000.0, '1982-03-12'),
    ('123.054.040-11', 'Calebe Davi Osvaldo', 'calebedavi@outlook.com', '(21) 99912-9553', 8000.0, '1957-11-12'),
    ('704.210.461-71', 'Marlene Carolina Araújo', 'marlenecarol@yahoo.com.br', '(21) 99914-1290', 5700.0, '1989-08-12'),
    ('949.886.998-70', 'Cecília Heloise Jesus', 'cecigzuis@gmail.com', '(21) 99123-3321', 9800.0, '1974-04-12'),
    ('928.667.263-24', 'Francisca Mariane Moraes', 'franmoraes@gmail.com', '(21) 99091-0905', 3200.0, '1983-01-12'),
    ('908.974.188-75', 'Raimundo Fernando Melo', 'raimundomelo@gmail.com', '(21) 97812-4008', 12000.0, '1982-03-12'),
    ('610.249.078-99', 'Jennifer Aragão', 'jenniferaragao@gmail.com', '(21) 99124-3437', 20000.0, '1957-11-12')"""

# executa a consulta inserir_dados
cursor.execute(inserir_dados) # ATENÇÃO: ao rodar o código pela 2a vez, comente esta linha!
conexao.commit()

# consulta para visualizar os dados da tabela
select_tabela = """SELECT nome FROM t_clientes"""
resultados = cursor.execute(select_tabela)
for resultado in resultados:
    print(resultado[0])

# selecionando uma pessoa com CPF específico
cpf = ("787.440.220-00",)
resultados2 = cursor.execute("SELECT nome FROM t_clientes WHERE cpf = (?)", cpf)
for resultado in resultados2:
  print(resultado[0])