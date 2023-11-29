class Strategy:
    def execute(self):
        pass

class ConcreteStrategyA(Strategy):
    def execute(self):
        return "Executing Strategy A"

class ConcreteStrategyB(Strategy):
    def execute(self):
        return "Executing Strategy B"

class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def execute_strategy(self):
        return self._strategy.execute()

# Usage
strategy_a = ConcreteStrategyA()
context = Context(strategy_a)
print(context.execute_strategy())  # Outputs: Executing Strategy A
