from datetime import datetime
from dateutil.relativedelta import relativedelta
fmt = '%d/%m/%Y, %H:%M:%S'
class Emprestimo:
    def __init__(self, data_inicial,valor, anos) -> None:  
        self.data_inicial = datetime.strptime (data_inicial, fmt) 
        self.valor = valor
        self.anos = anos
        self.valor_parcelas = self.valor/(12*self.anos)
        self.data_final = self.data_inicial + relativedelta(years=anos)
        self.parcelas  = [self.data_inicial + relativedelta(months=i) for i in range(1 , (self.anos*12))] 
    def __repr__(self):
        return f'{self.parcelas}, {self.valor_parcelas}'
    def mostra(self):
        for i in self.parcelas:
            print(f"{i}, {self.valor_parcelas:,.2f}")


if __name__=="__main__":
    empr_maria = Emprestimo('20/12/2020, 09:30:45', 1_000_000, 5)
    print(empr_maria.data_inicial)
    print(empr_maria.data_final- empr_maria.data_inicial)
    empr_maria.mostra()