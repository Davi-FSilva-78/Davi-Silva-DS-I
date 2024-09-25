import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017/")

db = cliente["mongoDavi"]

coleção = db["produtos"]

produtos1 = {"nome": "Detergente", "tipo": "Limpeza", "Validade": "sem validade"}
resultado1 = coleção.insert_one(produtos1)

produtos2 = {"nome": "Sabão em Pó", "tipo": "Limpeza", "Validade": "12 meses"}
resultado2 = coleção.insert_one(produtos2)

produtos3 = {"nome": "Desinfetante", "tipo": "Limpeza", "Validade": "24 meses"}
resultado3 = coleção.insert_one(produtos3)

produtos4 = {"nome": "Limpador Multiuso", "tipo": "Limpeza", "Validade": "18 meses"}
resultado4 = coleção.insert_one(produtos4)

produtos5 = {"nome": "Esponja", "tipo": "Limpeza", "Validade": "12 meses"}
resultado5 = coleção.insert_one(produtos5)

produtos6 = {"nome": "Água Sanitária", "tipo": "Limpeza", "Validade": "18 meses"}
resultado6 = coleção.insert_one(produtos6)

produtos7 = {"nome": "Amaciante", "tipo": "Limpeza", "Validade": "24 meses"}
resultado7 = coleção.insert_one(produtos7)

produtos8 = {"nome": "Sabão Líquido", "tipo": "Limpeza", "Validade": "12 meses"}
resultado8 = coleção.insert_one(produtos8)

produtos9 = {"nome": "Pano de Limpeza", "tipo": "Limpeza", "Validade": "6 meses"}
resultado9 = coleção.insert_one(produtos9)

produtos10 = {"nome": "Desengordurante", "tipo": "Limpeza", "Validade": "18 meses"}
resultado10 = coleção.insert_one(produtos10)

produtos11 = {"nome": "Detergente Lava Louças", "tipo": "Limpeza", "Validade": "12 meses"}
resultado11 = coleção.insert_one(produtos11)

produtos12 = {"nome": "Limpa Vidros", "tipo": "Limpeza", "Validade": "18 meses"}
resultado12 = coleção.insert_one(produtos12)

produtos13 = {"nome": "Inseticida", "tipo": "Limpeza", "Validade": "36 meses"}
resultado13 = coleção.insert_one(produtos13)

produtos14 = {"nome": "Desodorizante", "tipo": "Limpeza", "Validade": "12 meses"}
resultado14 = coleção.insert_one(produtos14)

produtos15 = {"nome": "Limpador de Piso", "tipo": "Limpeza", "Validade": "24 meses"}
resultado15 = coleção.insert_one(produtos15)

produtos16 = {"nome": "Removedor de Manchas", "tipo": "Limpeza", "Validade": "18 meses"}
resultado16 = coleção.insert_one(produtos16)

produtos17 = {"nome": "Limpador de Banheiro", "tipo": "Limpeza", "Validade": "12 meses"}
resultado17 = coleção.insert_one(produtos17)

produtos18 = {"nome": "Limpa Fogão", "tipo": "Limpeza", "Validade": "6 meses"}
resultado18 = coleção.insert_one(produtos18)

produtos19 = {"nome": "Borrifador", "tipo": "Limpeza", "Validade": "sem validade"}
resultado19 = coleção.insert_one(produtos19)

produtos20 = {"nome": "Pó de Limpeza", "tipo": "Limpeza", "Validade": "12 meses"}
resultado20 = coleção.insert_one(produtos20)

produtos21 = {"nome": "Limpador de Carpete", "tipo": "Limpeza", "Validade": "24 meses"}
resultado21 = coleção.insert_one(produtos21)

produtos22 = {"nome": "Limpador de Teto", "tipo": "Limpeza", "Validade": "18 meses"}
resultado22 = coleção.insert_one(produtos22)

produtos23 = {"nome": "Solução de Limpeza", "tipo": "Limpeza", "Validade": "12 meses"}
resultado23 = coleção.insert_one(produtos23)

produtos24 = {"nome": "Cloro", "tipo": "Limpeza", "Validade": "18 meses"}
resultado24 = coleção.insert_one(produtos24)

produtos25 = {"nome": "Removedor de Ferrugem", "tipo": "Limpeza", "Validade": "24 meses"}
resultado25 = coleção.insert_one(produtos25)

produtos26 = {"nome": "Limpa Pratos", "tipo": "Limpeza", "Validade": "12 meses"}
resultado26 = coleção.insert_one(produtos26)

produtos27 = {"nome": "Limpador de Janelas", "tipo": "Limpeza", "Validade": "18 meses"}
resultado27 = coleção.insert_one(produtos27)

produtos28 = {"nome": "Detergente para Roupas", "tipo": "Limpeza", "Validade": "12 meses"}
resultado28 = coleção.insert_one(produtos28)

produtos29 = {"nome": "Limpa Cimento", "tipo": "Limpeza", "Validade": "6 meses"}
resultado29 = coleção.insert_one(produtos29)

produtos30 = {"nome": "Mr. Musculo", "tipo": "Limpeza", "Validade": "6 meses"}
resultado29 = coleção.insert_one(produtos30)



produtos31 = {"nome": "Arroz Tipo 1", "tipo": "Comida", "Validade": "12 meses"}
resultado31 = coleção.insert_one(produtos31)

produtos32 = {"nome": "Feijão Preto", "tipo": "Comida", "Validade": "10 meses"}
resultado32 = coleção.insert_one(produtos32)

produtos33 = {"nome": "Açúcar Cristal", "tipo": "Comida", "Validade": "24 meses"}
resultado33 = coleção.insert_one(produtos33)

produtos34 = {"nome": "Sal Refinado", "tipo": "Comida", "Validade": "36 meses"}
resultado34 = coleção.insert_one(produtos34)

produtos35 = {"nome": "Macarrão Espaguete", "tipo": "Comida", "Validade": "18 meses"}
resultado35 = coleção.insert_one(produtos35)

produtos36 = {"nome": "Bife de Alcatra", "tipo": "Comida", "Validade": "5 dias"}
resultado36 = coleção.insert_one(produtos36)

produtos37 = {"nome": "Queijo Prato", "tipo": "Comida", "Validade": "30 dias"}
resultado37 = coleção.insert_one(produtos37)

produtos38 = {"nome": "Pão Francês", "tipo": "Comida", "Validade": "3 dias"}
resultado38 = coleção.insert_one(produtos38)

produtos39 = {"nome": "Iogurte Natural", "tipo": "Comida", "Validade": "15 dias"}
resultado39 = coleção.insert_one(produtos39)

produtos40 = {"nome": "Margarina", "tipo": "Comida", "Validade": "90 dias"}
resultado40 = coleção.insert_one(produtos40)

produtos41 = {"nome": "Frango Congelado", "tipo": "Comida", "Validade": "6 meses"}
resultado41 = coleção.insert_one(produtos41)

produtos42 = {"nome": "Sardinha em Lata", "tipo": "Comida", "Validade": "24 meses"}
resultado42 = coleção.insert_one(produtos42)

produtos43 = {"nome": "Bacon", "tipo": "Comida", "Validade": "90 dias"}
resultado43 = coleção.insert_one(produtos43)

produtos44 = {"nome": "Pizza Congelada", "tipo": "Comida", "Validade": "12 meses"}
resultado44 = coleção.insert_one(produtos44)

produtos45 = {"nome": "Mousse de Chocolate", "tipo": "Comida", "Validade": "30 dias"}
resultado45 = coleção.insert_one(produtos45)

produtos46 = {"nome": "Maçã", "tipo": "Comida", "Validade": "30 dias"}
resultado46 = coleção.insert_one(produtos46)

produtos47 = {"nome": "Banana", "tipo": "Comida", "Validade": "7 dias"}
resultado47 = coleção.insert_one(produtos47)

produtos48 = {"nome": "Uva", "tipo": "Comida", "Validade": "14 dias"}
resultado48 = coleção.insert_one(produtos48)

produtos49 = {"nome": "Tomate", "tipo": "Comida", "Validade": "10 dias"}
resultado49 = coleção.insert_one(produtos49)

produtos50 = {"nome": "Batata", "tipo": "Comida", "Validade": "90 dias"}
resultado50 = coleção.insert_one(produtos50)

produtos51 = {"nome": "Bife de Frango", "tipo": "Comida", "Validade": "5 dias"}
resultado51 = coleção.insert_one(produtos51)

produtos52 = {"nome": "Salame", "tipo": "Comida", "Validade": "60 dias"}
resultado52 = coleção.insert_one(produtos52)

produtos53 = {"nome": "Cenoura", "tipo": "Comida", "Validade": "30 dias"}
resultado53 = coleção.insert_one(produtos53)

produtos54 = {"nome": "Pimentão", "tipo": "Comida", "Validade": "10 dias"}
resultado54 = coleção.insert_one(produtos54)

produtos55 = {"nome": "Brócolis", "tipo": "Comida", "Validade": "7 dias"}
resultado55 = coleção.insert_one(produtos55)

produtos56 = {"nome": "Pepino", "tipo": "Comida", "Validade": "14 dias"}
resultado56 = coleção.insert_one(produtos56)

produtos57 = {"nome": "Batata Doce", "tipo": "Comida", "Validade": "90 dias"}
resultado57 = coleção.insert_one(produtos57)

produtos58 = {"nome": "Chá Verde", "tipo": "Comida", "Validade": "24 meses"}
resultado58 = coleção.insert_one(produtos58)

produtos59 = {"nome": "Café Solúvel", "tipo": "Comida", "Validade": "24 meses"}
resultado59 = coleção.insert_one(produtos59)

produtos60 = {"nome": "Chocolate em Barra", "tipo": "Comida", "Validade": "12 meses"}
resultado60 = coleção.insert_one(produtos60)



produtos61 = {"nome": "Água Mineral", "tipo": "Bebidas", "Validade": "Indefinida"}
resultado61 = coleção.insert_one(produtos61)

produtos62 = {"nome": "Refrigerante Lata", "tipo": "Bebidas", "Validade": "6 meses"}
resultado62 = coleção.insert_one(produtos62)

produtos63 = {"nome": "Suco de Laranja", "tipo": "Bebidas", "Validade": "90 dias"}
resultado63 = coleção.insert_one(produtos63)

produtos64 = {"nome": "Cerveja Lata", "tipo": "Bebidas", "Validade": "12 meses"}
resultado64 = coleção.insert_one(produtos64)

produtos65 = {"nome": "Vinho Tinto", "tipo": "Bebidas", "Validade": "24 meses"}
resultado65 = coleção.insert_one(produtos65)

produtos66 = {"nome": "Água com Gás", "tipo": "Bebidas", "Validade": "Indefinida"}
resultado66 = coleção.insert_one(produtos66)

produtos67 = {"nome": "Isotônico", "tipo": "Bebidas", "Validade": "12 meses"}
resultado67 = coleção.insert_one(produtos67)

produtos68 = {"nome": "Chá Gelado", "tipo": "Bebidas", "Validade": "90 dias"}
resultado68 = coleção.insert_one(produtos68)

produtos69 = {"nome": "Leite Longa Vida", "tipo": "Bebidas", "Validade": "12 meses"}
resultado69 = coleção.insert_one(produtos69)

produtos70 = {"nome": "Cachaça", "tipo": "Bebidas", "Validade": "Indefinida"}
resultado70 = coleção.insert_one(produtos70)

produtos71 = {"nome": "Suco de Uva", "tipo": "Bebidas", "Validade": "90 dias"}
resultado71 = coleção.insert_one(produtos71)

produtos72 = {"nome": "Refrigerante 2L", "tipo": "Bebidas", "Validade": "6 meses"}
resultado72 = coleção.insert_one(produtos72)

produtos73 = {"nome": "Água de Coco", "tipo": "Bebidas", "Validade": "60 dias"}
resultado73 = coleção.insert_one(produtos73)

produtos74 = {"nome": "Smoothie de Frutas", "tipo": "Bebidas", "Validade": "30 dias"}
resultado74 = coleção.insert_one(produtos74)

produtos75 = {"nome": "Energético", "tipo": "Bebidas", "Validade": "12 meses"}
resultado75 = coleção.insert_one(produtos75)

produtos76 = {"nome": "Suco de Abacaxi", "tipo": "Bebidas", "Validade": "90 dias"}
resultado76 = coleção.insert_one(produtos76)

produtos77 = {"nome": "Café", "tipo": "Bebidas", "Validade": "12 meses"}
resultado77 = coleção.insert_one(produtos77)

produtos78 = {"nome": "Chá Preto", "tipo": "Bebidas", "Validade": "24 meses"}
resultado78 = coleção.insert_one(produtos78)

produtos79 = {"nome": "Refrigerante Diet", "tipo": "Bebidas", "Validade": "6 meses"}
resultado79 = coleção.insert_one(produtos79)

produtos80 = {"nome": "Água Aromatizada", "tipo": "Bebidas", "Validade": "60 dias"}
resultado80 = coleção.insert_one(produtos80)

produtos81 = {"nome": "Limonada", "tipo": "Bebidas", "Validade": "30 dias"}
resultado81 = coleção.insert_one(produtos81)

produtos82 = {"nome": "Batida de Frutas", "tipo": "Bebidas", "Validade": "14 dias"}
resultado82 = coleção.insert_one(produtos82)

produtos83 = {"nome": "Refrigerante Sem Açúcar", "tipo": "Bebidas", "Validade": "6 meses"}
resultado83 = coleção.insert_one(produtos83)

produtos84 = {"nome": "Suco de Frutas Vermelhas", "tipo": "Bebidas", "Validade": "90 dias"}
resultado84 = coleção.insert_one(produtos84)

produtos85 = {"nome": "Cerveja Artesanal", "tipo": "Bebidas", "Validade": "12 meses"}
resultado85 = coleção.insert_one(produtos85)

produtos86 = {"nome": "Chá de Hibisco", "tipo": "Bebidas", "Validade": "12 meses"}
resultado86 = coleção.insert_one(produtos86)

produtos87 = {"nome": "Milkshake", "tipo": "Bebidas", "Validade": "3 dias"}
resultado87 = coleção.insert_one(produtos87)

produtos88 = {"nome": "Refrigerante de Guaraná", "tipo": "Bebidas", "Validade": "6 meses"}
resultado88 = coleção.insert_one(produtos88)

produtos89 = {"nome": "Suco de Manga", "tipo": "Bebidas", "Validade": "90 dias"}
resultado89 = coleção.insert_one(produtos89)

produtos90 = {"nome": "Água Tônica", "tipo": "Bebidas", "Validade": "12 meses"}
resultado90 = coleção.insert_one(produtos90)



produtos91 = {"nome": "Smartphone", "tipo": "Eletrônicos", "Validade": "Indefinida"}
resultado91 = coleção.insert_one(produtos91)

produtos92 = {"nome": "Notebook", "tipo": "Eletrônicos", "Validade": "Indefinida"}
resultado92 = coleção.insert_one(produtos92)

produtos93 = {"nome": "Tablet", "tipo": "Eletrônicos", "Validade": "Indefinida"}
resultado93 = coleção.insert_one(produtos93)

produtos94 = {"nome": "Fone de Ouvido", "tipo": "Eletrônicos", "Validade": "Indefinida"}
resultado94 = coleção.insert_one(produtos94)

produtos95 = {"nome": "Câmera Digital", "tipo": "Eletrônicos", "Validade": "Indefinida"}
resultado95 = coleção.insert_one(produtos95)

produtos96 = {"nome": "Televisor LED", "tipo": "Eletrônicos", "Validade": "Indefinida"}
resultado96 = coleção.insert_one(produtos96)

produtos97 = {"nome": "Console de Videogame", "tipo": "Eletrônicos", "Validade": "Indefinida"}
resultado97 = coleção.insert_one(produtos97)

produtos98 = {"nome": "Caixa de Som Bluetooth", "tipo": "Eletrônicos", "Validade": "Indefinida"}
resultado98 = coleção.insert_one(produtos98)

produtos99 = {"nome": "Smartwatch", "tipo": "Eletrônicos", "Validade": "Indefinida"}
resultado99 = coleção.insert_one(produtos99)

produtos100 = {"nome": "Roteador Wi-Fi", "tipo": "Eletrônicos", "Validade": "Indefinida"}
resultado100 = coleção.insert_one(produtos100)

produtos101 = {"nome": "Microfone", "tipo": "Eletrônicos", "Validade": "Indefinida"}
resultado101 = coleção.insert_one(produtos101)

produtos102 = {"nome": "Projetor", "tipo": "Eletrônicos", "Validade": "Indefinida"}
resultado102 = coleção.insert_one(produtos102)

produtos103 = {"nome": "Baterias Externas", "tipo": "Eletrônicos", "Validade": "Indefinida"}
resultado103 = coleção.insert_one(produtos103)

produtos104 = {"nome": "Impressora", "tipo": "Eletrônicos", "Validade": "Indefinida"}
resultado104 = coleção.insert_one(produtos104)

produtos105 = {"nome": "Teclado Sem Fio", "tipo": "Eletrônicos", "Validade": "Indefinida"}
resultado105 = coleção.insert_one(produtos105)

produtos106 = {"nome": "Mouse Sem Fio", "tipo": "Eletrônicos", "Validade": "Indefinida"}
resultado106 = coleção.insert_one(produtos106)

produtos107 = {"nome": "Cabo HDMI", "tipo": "Eletrônicos", "Validade": "Indefinida"}
resultado107 = coleção.insert_one(produtos107)

produtos108 = {"nome": "Suporte para Celular", "tipo": "Eletrônicos", "Validade": "Indefinida"}
resultado108 = coleção.insert_one(produtos108)

produtos109 = {"nome": "Carregador Solar", "tipo": "Eletrônicos", "Validade": "Indefinida"}
resultado109 = coleção.insert_one(produtos109)

produtos110 = {"nome": "Drones", "tipo": "Eletrônicos", "Validade": "Indefinida"}
resultado110 = coleção.insert_one(produtos110)

produtos111 = {"nome": "Rádio", "tipo": "Eletrônicos", "Validade": "Indefinida"}
resultado111 = coleção.insert_one(produtos111)

produtos112 = {"nome": "Smart TV", "tipo": "Eletrônicos", "Validade": "Indefinida"}
resultado112 = coleção.insert_one(produtos112)

produtos113 = {"nome": "Aparelho de Som", "tipo": "Eletrônicos", "Validade": "Indefinida"}
resultado113 = coleção.insert_one(produtos113)

produtos114 = {"nome": "Assistente Virtual", "tipo": "Eletrônicos", "Validade": "Indefinida"}
resultado114 = coleção.insert_one(produtos114)

produtos115 = {"nome": "Controlador de Jogos", "tipo": "Eletrônicos", "Validade": "Indefinida"}
resultado115 = coleção.insert_one(produtos115)

produtos116 = {"nome": "Câmera de Segurança", "tipo": "Eletrônicos", "Validade": "Indefinida"}
resultado116 = coleção.insert_one(produtos116)

produtos117 = {"nome": "Scanner", "tipo": "Eletrônicos", "Validade": "Indefinida"}
resultado117 = coleção.insert_one(produtos117)

produtos118 = {"nome": "Monitor", "tipo": "Eletrônicos", "Validade": "Indefinida"}
resultado118 = coleção.insert_one(produtos118)

produtos119 = {"nome": "Cabo USB", "tipo": "Eletrônicos", "Validade": "Indefinida"}
resultado119 = coleção.insert_one(produtos119)

produtos120 = {"nome": "Smart Plug", "tipo": "Eletrônicos", "Validade": "Indefinida"}
resultado120 = coleção.insert_one(produtos120)

produtos121 = {"nome": "Cimento", "tipo": "Materiais de Construção", "Validade": "6 meses"}
resultado121 = coleção.insert_one(produtos121)

produtos122 = {"nome": "Areia", "tipo": "Materiais de Construção", "Validade": "Indefinida"}
resultado122 = coleção.insert_one(produtos122)

produtos123 = {"nome": "Brita", "tipo": "Materiais de Construção", "Validade": "Indefinida"}
resultado123 = coleção.insert_one(produtos123)

produtos124 = {"nome": "Tijolo", "tipo": "Materiais de Construção", "Validade": "Indefinida"}
resultado124 = coleção.insert_one(produtos124)

produtos125 = {"nome": "Bloco de Concreto", "tipo": "Materiais de Construção", "Validade": "Indefinida"}
resultado125 = coleção.insert_one(produtos125)

produtos126 = {"nome": "Argamassa", "tipo": "Materiais de Construção", "Validade": "6 meses"}
resultado126 = coleção.insert_one(produtos126)

produtos127 = {"nome": "Gesso", "tipo": "Materiais de Construção", "Validade": "Indefinida"}
resultado127 = coleção.insert_one(produtos127)

produtos128 = {"nome": "Cal", "tipo": "Materiais de Construção", "Validade": "Indefinida"}
resultado128 = coleção.insert_one(produtos128)

produtos129 = {"nome": "Prego", "tipo": "Materiais de Construção", "Validade": "Indefinida"}
resultado129 = coleção.insert_one(produtos129)

produtos130 = {"nome": "Parafuso", "tipo": "Materiais de Construção", "Validade": "Indefinida"}
resultado130 = coleção.insert_one(produtos130)

produtos131 = {"nome": "Porcelanato", "tipo": "Materiais de Construção", "Validade": "Indefinida"}
resultado131 = coleção.insert_one(produtos131)

produtos132 = {"nome": "Piso Laminado", "tipo": "Materiais de Construção", "Validade": "Indefinida"}
resultado132 = coleção.insert_one(produtos132)

produtos133 = {"nome": "Lâmina de Madeira", "tipo": "Materiais de Construção", "Validade": "Indefinida"}
resultado133 = coleção.insert_one(produtos133)

produtos134 = {"nome": "Tubulação de PVC", "tipo": "Materiais de Construção", "Validade": "Indefinida"}
resultado134 = coleção.insert_one(produtos134)

produtos135 = {"nome": "Ferro", "tipo": "Materiais de Construção", "Validade": "Indefinida"}
resultado135 = coleção.insert_one(produtos135)

produtos136 = {"nome": "Telha", "tipo": "Materiais de Construção", "Validade": "Indefinida"}
resultado136 = coleção.insert_one(produtos136)

produtos137 = {"nome": "Cimento Queimado", "tipo": "Materiais de Construção", "Validade": "Indefinida"}
resultado137 = coleção.insert_one(produtos137)

produtos138 = {"nome": "Tinta Acrílica", "tipo": "Materiais de Construção", "Validade": "1 ano"}
resultado138 = coleção.insert_one(produtos138)

produtos139 = {"nome": "Massa Corrida", "tipo": "Materiais de Construção", "Validade": "6 meses"}
resultado139 = coleção.insert_one(produtos139)

produtos140 = {"nome": "Cola para Madeira", "tipo": "Materiais de Construção", "Validade": "1 ano"}
resultado140 = coleção.insert_one(produtos140)

produtos141 = {"nome": "Espuma Expansiva", "tipo": "Materiais de Construção", "Validade": "1 ano"}
resultado141 = coleção.insert_one(produtos141)

produtos142 = {"nome": "Silicone", "tipo": "Materiais de Construção", "Validade": "1 ano"}
resultado142 = coleção.insert_one(produtos142)

produtos143 = {"nome": "Régua de Alumínio", "tipo": "Materiais de Construção", "Validade": "Indefinida"}
resultado143 = coleção.insert_one(produtos143)

produtos144 = {"nome": "Serra Circular", "tipo": "Materiais de Construção", "Validade": "Indefinida"}
resultado144 = coleção.insert_one(produtos144)

produtos145 = {"nome": "Martelo", "tipo": "Materiais de Construção", "Validade": "Indefinida"}
resultado145 = coleção.insert_one(produtos145)

produtos146 = {"nome": "Pá", "tipo": "Materiais de Construção", "Validade": "Indefinida"}
resultado146 = coleção.insert_one(produtos146)

produtos147 = {"nome": "Enxada", "tipo": "Materiais de Construção", "Validade": "Indefinida"}
resultado147 = coleção.insert_one(produtos147)

produtos148 = {"nome": "Escada", "tipo": "Materiais de Construção", "Validade": "Indefinida"}
resultado148 = coleção.insert_one(produtos148)

produtos149 = {"nome": "Pincel", "tipo": "Materiais de Construção", "Validade": "Indefinida"}
resultado149 = coleção.insert_one(produtos149)

produtos150 = {"nome": "Lixa", "tipo": "Materiais de Construção", "Validade": "Indefinida"}
resultado150 = coleção.insert_one(produtos150)

