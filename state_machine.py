import numpy as np

class StateMachine():

    def __init__(self, dict, num_states, init_state, receiving_states, cutoff):
        self.dict = dict #dictionary for letter:matrix
        self.num_states = num_states
        self.init_state = init_state
        self.receiving_states = receiving_states
        self.cutoff = cutoff

    def prep_run(self,word): #matrix list for word
        matrices = [self.dict[letter] for letter in word]
        return matrices

    def prep_machine(self,matrices): #flip matrix order for math..
        return matrices[::-1]

    def run_machine(self,matrices): #multiply matrices and get final state
        result = np.identity(2**self.num_states)
        matrices = self.prep_machine(matrices)
        for m in matrices:
            result = result @ m
        final_state = result @ self.init_state
        return final_state


    def check_final_state(self,final_state): #check if final state is accepted
        accept_prob = abs(np.dot(np.transpose(self.receiving_states), final_state)) ** 2
        return accept_prob

    def transfer(self,word):
        matrices = self.prep_run(word)
        machine = self.prep_machine(matrices)
        final_state = self.run_machine(machine)
        prob = self.check_final_state(final_state)
        if prob >= self.cutoff:
            return 1, prob
        else:
            return 0, prob










