class Car:
    def __init__(self,model, year, color, for_sale):   #Usado para iniciar a construção de um objeto, (self) significa agora,                                            # model,year,color são os atributos e for_sale é um metodo que pode ser true ou false
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale


    def drive(self):
        print(f"You drive the {self.color} {self.model}")
    def stop(self):
        print(f"You stop the {self.color} {self.model}")
    def describe(self):
        print(f"{self.model} {self.color} {self.year}")
