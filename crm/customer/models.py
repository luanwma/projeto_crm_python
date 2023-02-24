from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    email = models.EmailField() # no bd vira um charfield mas aqui é melhor usar emailfield 
    birth_date = models.DateField()
    area_code = models.CharField(max_length=3) # codigo de area de tel
    phone_number = models.CharField(max_length=9)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True) # data e hora automatico da criação do objeto
    updated_date = models.DateTimeField(auto_now=True) # sempre que houver atualização no objeto o django atualiza a data automaticamente
    active = models.BooleanField(default=True)

    def __str__(self): ## sempre que retornar um objeto de customer e nao definir o campo desejado
            # essa função irá retornar o primeiro e ultimo nome
        return f"{self.first_name} {self.last_name}"
    
    class Meta: # metadados -> identifica o nome da tabela no banco de dados, se não for definido aqui
        # a tabela fica definida como customer_customer o banco de dado define como 
        # nome do app_nome da tabela 
        db_table = "customer"
