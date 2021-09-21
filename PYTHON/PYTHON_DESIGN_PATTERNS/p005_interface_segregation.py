from abc import ABC, abstractmethod


# segregated interface
class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass


# segregated interface
class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass


# segregated interface
class FaxMachine(ABC):
    @abstractmethod
    def fax(self, document):
        pass

# can make combined interfaces from above and use them below


class MultiFunctionPrinter(Printer, Scanner, FaxMachine):
    def print(self, document):
        # do something
        pass

    def scan(self, document):
        # do something
        pass

    def fax(self, document):
        # do something
        pass


class OldFashionedPrinter(Printer):
    def print(self, document):
        pass


class MultiFunctionMachine(Printer, Scanner):
    def __init__(self, printer, scanner):
        self.printer = printer
        self.scanner = scanner

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)
