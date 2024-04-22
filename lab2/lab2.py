import random

class FiniteAutomaton:
    def __init__(self, Q, Sigma, delta, q0, F):
        self.Q = Q
        self.Sigma = Sigma
        self.delta = delta
        self.q0 = q0
        self.F = F

    def is_deterministic(self):
        for state in self.Q:
            for symbol in self.Sigma:
                next_states = {next_state for (_, input_symbol, next_state) in self.delta
                               if _ == state and input_symbol == symbol}
                if len(next_states) > 1:
                    return False
        return True

    def to_regular_grammar(self):
        regular_grammar = {}
        for state in self.Q:
            regular_grammar[state] = [input_symbol + next_state for (_, input_symbol, next_state) in self.delta
                                      if _ == state and next_state != 'X']
        return regular_grammar

    def to_deterministic_finite_automaton(self):
        dfa = FiniteAutomaton(self.Q, self.Sigma, set(), frozenset([self.q0]), set())

        def epsilon_closure(state):
            closure = set(state)
            stack = list(state)
            while stack:
                currentState = stack.pop()
                for (_, input_symbol, nextState) in self.delta:
                    if currentState == nextState and input_symbol == 'ε' and nextState not in closure:
                        closure.add(nextState)
                        stack.append(nextState)
            return frozenset(closure)

        unprocessed_states = [dfa.q0]
        dfa.delta = set()
        dfa.F = set()

        while unprocessed_states:
            current_state = unprocessed_states.pop(0)
            for symbol in dfa.Sigma:
                next_state = set()
                for state in current_state:
                    next_state |= {next_state for (_, input_symbol, next_state) in self.delta
                                   if state in current_state and input_symbol == symbol}
                next_state_closure = epsilon_closure(next_state)
                if next_state_closure:
                    dfa.delta.add((current_state, symbol, next_state_closure))
                    if next_state_closure not in dfa.Q:
                        dfa.Q.add(next_state_closure)
                        unprocessed_states.append(next_state_closure)
                    if any(state in self.F for state in next_state_closure):
                        dfa.F.add(next_state_closure)

        return dfa


# Define the finite automaton variant
Q = {'q0', 'q1', 'q2', 'q3'}
Sigma = {'a', 'b'}
delta = {('q0', 'a', 'q1'), ('q1', 'b', 'q1'), ('q1', 'b', 'q2'),
         ('q2', 'a', 'q2'), ('q2', 'b', 'q3'), ('q0', 'b', 'q0')}
q0 = 'q0'
F = {'q3'}

# Create the finite automaton instance
finite_automaton = FiniteAutomaton(Q, Sigma, delta, q0, F)

# Check if the finite automaton is deterministic
if finite_automaton.is_deterministic():
    print("The finite automaton is deterministic.")
else:
    print("The finite automaton is non-deterministic.")

# Convert finite automaton to regular grammar
regular_grammar = finite_automaton.to_regular_grammar()

# Print the regular grammar productions
print("Conversion to grammar:")
for state, productions in regular_grammar.items():
    for production in productions:
        print(state, "->", production)

# Convert finite automaton to deterministic finite automaton
dfa = finite_automaton.to_deterministic_finite_automaton()

# Check if the resulting DFA is deterministic
if dfa.is_deterministic():
    print("The converted DFA is deterministic.")
else:
    print("The converted DFA is non-deterministic.")

# Print the states and transitions of the DFA
print("States and transitions of the DFA:")
for state, symbol, next_state in dfa.delta:
    print(state, "--", symbol, "-->", next_state)
