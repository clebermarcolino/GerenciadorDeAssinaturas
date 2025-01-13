import templates.__init__
from models.database import engine
from models.model import Subscription, Payments
from sqlmodel import Session, select
from datetime import date, datetime

class SubscriptionService:
    def __init__(self, engine):
        self.engine = engine

    def create(self, subscription: Subscription):
        with Session(self.engine) as session: # Usa um Session como um gerenciador de contexto, o que garante que a sessão será fechada corretamente após o uso.
            session.add(subscription)
            session.commit() #  executa a query de inserção, efetivando as mudanças no banco de dados.
            return subscription
        
    def list_all(self):
        with Session(self.engine) as session:
            statement = select(Subscription) # select(Subscription): cria uma consulta SQL para selecionar todas as linhas da tabela Subscription.
            results = session.exec(statement).all() # executa a consulta e retorna todos os resultados como uma lista.
        return results
    
    def delete_payments(self, id):
        with Session(self.engine) as session:
            statement = select(Payments).where(Payments.subscription_id == id) # seleciona todos os pagamentos onde a coluna subscription_id é igual ao id recebido.
            results = session.exec(statement).all() # executa a consulta e pega todos os resultados.

            for payment in results:
                session.delete(payment) # adiciona o resultado à sessão, preparando uma query para deletar essa linha da tabela.

            session.commit() # executa todas as queries de deleção, efetivando as mudanças no banco de dados.

    def delete(self, id):
        with Session(self.engine) as session:
            self.delete_payments(id)
            statement = select(Subscription).where(Subscription.id == id)
            result = session.exec(statement).one() # executa a consulta e espera que um, e somente um, resultado seja encontrado.
            session.delete(result)
            session.commit()
    
    def _has_pay(self, results):
            for result in results:
                if result.date.month == date.today().month:
                    return True
                
                return False

    def pay(self, subscription: Subscription):
        with Session(self.engine) as session:
            statement = select(Payments).join(Subscription).where(Subscription.empresa==subscription.empresa)
            results = session.exec(statement).all()
            
            if self._has_pay(results):
                print('Essa assinatura já foi paga esse mês. Não é possível pagar a mesma assinatura mais de uma vez.')
                return

            pay = Payments(subscription_id=subscription.id, date=date.today())
            session.add(pay)
            session.commit()

    def total_value(self):
        with Session(self.engine) as session:
            statement = select(Subscription)
            results = session.exec(statement).all()

        total = 0

        for result in results:
            total += result.valor

        return float(total)
    
    def _get_last_12_months_native(self):
        today = datetime.now()
        year = today.year
        month = today.month
        last_12_month = []

        for i in range(12):
            last_12_month.append((month, year))
            month -= 1
            if month == 0:
                month = 12
                year -= 1

        return last_12_month[::-1] # Retorna uma lista de tuplas [(mes, ano), (mes, ano) ...] com os 12 últimos meses, ordenados do mais antigo para o mais atual.

    def _get_values_for_months(self, last_12_months):
        with Session(self.engine) as session:
            statement = select(Payments)
            results = session.exec(statement).all()

            value_for_months = []

            for i in last_12_months:
                value = 0
                for result in results:
                    if result.date.month == i[0] and result.date.year == i[1]:
                        value += float(result.subscription.valor)
                value_for_months.append(value)

            return value_for_months

    def gen_chart(self):
        last_12_months = self._get_last_12_months_native()
        values_for_months = self._get_values_for_months(last_12_months)
        last_12_months2 = []

        for i in last_12_months:
            last_12_months2.append(i[0])
            print(last_12_months2)
            
        import matplotlib.pyplot as plt

        plt.plot(last_12_months2, values_for_months)
        plt.show()