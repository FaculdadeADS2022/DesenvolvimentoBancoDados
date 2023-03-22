from tipoMovimentacao import tipoMovimentacao

tableOption = int(input("""
Selecione uma das tabelas:
1 - tipoMovimentacao;
2 - saldoDiario;
3 - movimentacoes;
"""))

match tableOption:
   case 1:
      tableAction = int(input("""
         Selecione uma das ações:
            1 - Insert
            2 - Update
            3 - Select
            4 - Delete
      """))
      match tableAction:
         case 1:
            print('Informe os valores para:')
            tableDescricao = str(input("""
               Descrição do tipo de movimentação:
            """))
            tableTipo = str(input("""
               Tipo da movimentação[E - Entrada/S - Saída]:
            """))
            tipoMovimentacao = tipoMovimentacao()
            tipoMovimentacao.descricao = tableDescricao
            tipoMovimentacao.tipo = tableTipo
            result = tipoMovimentacao.inserir()
            print (f'inseriu {result}')

         case 2:
            print('Informe os valores para:')
            tableDescricao = str(input("""
               Descrição do tipo de movimentação:
            """))
            tableTipo = str(input("""
               Tipo da movimentação[E - Entrada/S - Saída]:
            """))
            tableId = int(input('O id do registro que deseja atualizar:'))
            tipoMovimentacao = tipoMovimentacao()
            tipoMovimentacao.id = tableId
            tipoMovimentacao.descricao = tableDescricao
            tipoMovimentacao.tipo = tableTipo
            result = tipoMovimentacao.update()
            print (f'Atualizou {result}')
         case 3:
            
   case 2:
      # tabela saldoDiario

   case 3:
      # tabela movimentacoes
