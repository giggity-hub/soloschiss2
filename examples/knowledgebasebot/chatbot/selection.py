class Selection():
    df = None
    object_type = None
    entity = None

    def __init__(self) -> None:
        pass

    def update(self, belief_state_dict, kb_df):
        if 'mention_id' in belief_state_dict:
            mention_id = int(belief_state_dict['mention_id'])
            self.entity = self.df.iloc[mention_id - 1]

        if 'mention_name' in belief_state_dict:
            mention_name = belief_state_dict['mention_name']
            self.entity = self.df[self.df['name'] == mention_name]


        if 'object_type' in belief_state_dict:
            object_type = belief_state_dict['object_type']
            
            self.entity = None
            self.df = kb_df[kb_df['object_type'] == object_type]