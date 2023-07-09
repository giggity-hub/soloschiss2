from selection import Selection
import re

class Actions():
    def __init__(self) -> None:
        pass

    def list_entity_names_of_type(self, belief_state_dict, selection: Selection):
        return selection.df['name'].tolist()

    def query_attribute(self, belief_state_dict, selection: Selection):
        attribute = belief_state_dict['attribute']
        return selection.entity[attribute]
    
    
    









    def do(self, action_name, belief_state_dict, selection: Selection):
        action_func = self.__getattribute__(action_name)
        return action_func(belief_state_dict, selection)
    
    def find_action(self, string):
        action_regexp = 'action_[a-z_]+'
        found_actions = re.findall(action_regexp, string)

        print(f'found actions {found_actions}')
        if len(found_actions) == 0:
            return None
        
        action_name = found_actions[0].replace('action_', '')
        return action_name