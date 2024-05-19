from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AssistenciaTecnica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    razao_social = db.Column(db.String(100), nullable=False)
    nome_fantasia = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(18), nullable=False)
    inscricao_estadual = db.Column(db.String(20))
    email = db.Column(db.String(100))
    telefone = db.Column(db.String(20))
    celular = db.Column(db.String(20))
    endereco = db.Column(db.String(200))
    observacao = db.Column(db.Text)
    clientes = db.relationship('Cliente', backref='assistencia', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'razao_social': self.razao_social,
            'nome_fantasia': self.nome_fantasia,
            'cnpj': self.cnpj,
            'inscricao_estadual': self.inscricao_estadual,
            'email': self.email,
            'telefone': self.telefone,
            'celular': self.celular,
            'endereco': self.endereco,
            'observacao': self.observacao
        }

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    documento = db.Column(db.String(20), nullable=False)  # CPF ou RG
    email = db.Column(db.String(100))
    telefone = db.Column(db.String(20))
    celular = db.Column(db.String(20))
    endereco = db.Column(db.String(200))
    observacao = db.Column(db.Text)
    assistencia_id = db.Column(db.Integer, db.ForeignKey('assistencia_tecnica.id'))
    oficina = db.relationship('Oficina', backref='cliente', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'documento': self.documento,
            'email': self.email,
            'telefone': self.telefone,
            'celular': self.celular,
            'endereco': self.endereco,
            'observacao': self.observacao,
            'assistencia_id': self.assistencia_id
        }

class Oficina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aparelho = db.Column(db.String(50), nullable=False)
    marca = db.Column(db.String(50))
    modelo = db.Column(db.String(50))
    numero_serie = db.Column(db.String(50))
    data_entrada = db.Column(db.Date)
    data_saida = db.Column(db.Date)
    garantia = db.Column(db.String(50))
    observacao = db.Column(db.Text)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    estoques = db.relationship('Estoque', backref='oficina', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'aparelho': self.aparelho,
            'marca': self.marca,
            'modelo': self.modelo,
            'numero_serie': self.numero_serie,
            'data_entrada': self.data_entrada,
            'data_saida': self.data_saida,
            'garantia': self.garantia,
            'observacao': self.observacao,
            'cliente_id': self.cliente_id
        }

class Estoque(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    componente = db.Column(db.String(100), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.Text)
    preco = db.Column(db.Float)
    observacao = db.Column(db.Text)
    oficina_id = db.Column(db.Integer, db.ForeignKey('oficina.id'))

    def to_dict(self):
        return {
            'id': self.id,
            'componente': self.componente,
            'quantidade': self.quantidade,
            'descricao': self.descricao,
            'preco': self.preco,
            'observacao': self.observacao,
            'oficina_id': self.oficina_id
        }

