class Checkbook:
    def __init__(self):
        """
        Initialise un nouveau compte avec un solde initial de 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Dépose un montant d'argent sur le compte.

        Parameters:
        amount (float): Le montant à déposer.

        Affiche le montant déposé et le solde actuel du compte.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Retire un montant d'argent du compte si le solde est suffisant.

        Parameters:
        amount (float): Le montant à retirer.

        Affiche un message d'erreur si les fonds sont insuffisants, 
        sinon affiche le montant retiré et le solde actuel du compte.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Affiche le solde actuel du compte.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Fonction principale pour interagir avec l'utilisateur et gérer les opérations du compte.
    Permet à l'utilisateur de choisir entre déposer, retirer, vérifier le solde ou quitter l'application.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            amount = float(input("Enter the amount to deposit: $"))
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            amount = float(input("Enter the amount to withdraw: $"))
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
