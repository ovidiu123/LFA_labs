### Formal Languages & Finite Automata

### Course Overview by [Your Name]

### Objectives:

1. Understand the fundamentals of formal languages and their characteristics.
2. Establish the initial setup for the semester project, including GitHub repository setup and language selection.
3. Implement variant-specific tasks such as grammar definition, string generation, grammar to finite automaton conversion, and finite automaton testing.

### Implementation Description

### Part 1: Grammar Definition and Grammar Class

### Grammar Definition for Variant 16
VN = {"S", "A", "B"}
VT = {"a", "b", "c", "d"}
P = {
    "S": ["aS", "bS", "cA"],
    "A": ["dA", "bB", "a"],
    "B": ["bS", "a"]
}

### Grammar Class
class Grammar:
    def __init__(self, vn, vt, p):
        self.vn = vn
        self.vt = vt
        self.p = p

    def generate_string(self, symbol):
        if symbol in self.vt:
            return symbol
        else:
            options = self.p[symbol]
            chosen_option = random.choice(options)
            generated_string = ""
            for char in chosen_option:
                generated_string += self.generate_string(char)
            return generated_string

 
 Here we define the grammar for Variant 16, consisting of non-terminal symbols (VN), terminal symbols (VT), and production rules (P). 
 We also define a Grammar class with a method to generate strings based on the grammar rules.

### Part 2: Grammar to Finite Automaton Conversion

### Function to convert grammar to finite automaton
def grammar_to_finite_automaton(grammar):
    states = grammar.vn
    alphabet = grammar.vt
    start_state = "S"
    accept_states = {
        state for state, rules in grammar.p.items() if any(r in rules for r in grammar.vt)
    }

    transitions = {}
    for state, rules in grammar.p.items():
        for rule in rules:
            if len(rule) == 2:
                transitions[(state, rule[0])] = rule[1]
            elif len(rule) == 1:
                if rule[0] in grammar.vt:
                    transitions[(state, rule[0])] = rule[0]
                else:
                    transitions[(state, rule[0])] = next(iter(grammar.p[rule[0]]))[0]

    return FiniteAutomaton(states, alphabet, transitions, start_state, accept_states)

### Define the Finite Automaton class
class FiniteAutomaton:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def accepts(self, string):
        current_state = self.start_state
        for char in string:
            if (current_state, char) not in self.transitions:
                return False
            current_state = self.transitions[(current_state, char)]
        return current_state in self.accept_states


 We define a function to convert the grammar into a finite automaton (FA). 
 The function constructs states, alphabet, transitions, start state, and accept states based on the grammar rules.
 We also define a Finite Automaton class with a method to check if a given string is accepted by the FA.

### Part 3: Testing Strings with the Finite Automaton

### Test strings
test_strings = ["aabbc", "ac", "abba", "acaaaabba", "aab"]
print("\nTesting strings:")
for string in test_strings:
    fa = grammar_to_finite_automaton(grammar_variant_16)
    if fa.accepts(string):
        print(f"String '{string}' is accepted by the FA")
    else:
        print(f"String '{string}' is not accepted by the FA")

Here we test several strings using the finite automaton generated from the grammar.
For each test string, we convert the grammar to a finite automaton and check if the automaton accepts the string.

### Conclusions and Results

This project provided an overview of formal languages and finite automata. By implementing grammar definition, conversion to finite automata, and testing strings, we gained insights into language structure and validation mechanisms. This foundational knowledge can be extended to tackle more complex language-related projects in the future.
