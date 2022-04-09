class Payroll:
    Employee = str
    Payment = float
    '''
    The default payroll. It hold an employee:payment dictionary.

    Obs: I'm using simple builtin types for employee and payment as custom classes are not necessary to the problem.
    '''
    def __init__(self):
        self.payroll = {}

    def register_pay(self, employee : Employee, payment : Payment ):
        self.payroll[employee] = payment


    def __str__(self):
        str_rpr = ''
        for employee in self.payroll:
            str_rpr += f'The amount to pay {employee} is: {self.payroll[employee]} USD\n'

        return str_rpr


