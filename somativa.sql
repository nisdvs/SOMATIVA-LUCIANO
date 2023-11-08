create database ex1bd;
use ex1bd;

create table produtos(
	id bigint primary key auto_increment not null,
    discriminacao varchar(45) not null,
    p_unitario DECIMAL(10,2)
);

create table clientes(
	id bigint not null auto_increment primary key,
    nome varchar(45) not null,
    rua varchar(45) not null,
    bairro varchar(45) not null,
    cidade varchar(20) not null,
    estado varchar(2) not null,
    cep varchar(9) not null,
    cpf varchar(11) not null,
    fone varchar(13) not null
);

create table notas_fiscais(
	id bigint not null auto_increment primary key,
    data_emissao date not null default(now()),
    valor DECImal(10,2) not null,
    id_clientes bigint not null,
    foreign key (id_clientes) references clientes(id)
);

create table itens_nota_fiscal(
	id bigint not null auto_increment primary key,
    quant int not null,
    id_produtos bigint not null,
    id_nota_fiscal bigint not null,
    foreign key (id_produtos) references produtos(id),
    foreign key (id_nota_fiscal) references notas_fiscais(id)
);

insert into clientes (nome,rua,bairro,cidade,estado,cep,cpf,fone) values ('Fuzari','a','1','Sbo','SP','123456789','11111111111','19986124301'),('Henrique','b','2','Sbo','SP','987654321','22222222222','1234567890123'),('Kauan','c','3','Sbo','SP','432159876','33333333333','3210987654321');
insert into produtos (discriminacao,p_unitario) values ('notebook',5999.99),('laptop',7899.99),('mem ram',485.75),('celular',2525.99);
insert into notas_fiscais(data_emissao,valor,id_clientes) values ('2023-09-06',1000.00,1),('2023-08-31',23.89,1),('2022-01-01',10000.99,3);
insert into itens_nota_fiscal (quant,id_produtos,id_nota_fiscal) values (10,1,1),(1,2,1),(100,1,2),(1,3,2);

select *, (nf.valor+(p.p_unitario*inf.quant)) as valor_total from itens_nota_fiscal inf join produtos p on inf.id_produtos = p.id join notas_fiscais nf on inf.id_nota_fiscal = nf.id; # EX1
select *, (p.p_unitario*inf.quant) as sub_total, (nf.valor+(p.p_unitario*inf.quant)) as valor_total from itens_nota_fiscal inf join produtos p on inf.id_produtos = p.id join notas_fiscais nf on inf.id_nota_fiscal = nf.id join clientes c on c.id = nf.id_clientes where c.nome = "Fuzari"; # EX2

flush privileges;



-- Criando uma tabela pra testar a função do trigger
create table auditoria(
discrimicao varchar(50),
p_unitario_antigo decimal(10,2),
p_unitario_novo decimal(10,2),
data_trigger date
);

select * from produtos;
update produtos set p_unitario = 8999.99 where id = 1;
select * from auditoria;