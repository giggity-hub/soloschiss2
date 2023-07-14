import re
from stuttbard.domains.dataframes import load
from argparse import Namespace

domains = load()

class Chat():
    def __init__(self) -> None:
        self.history = [] 



    def start(self):
        domains = load()
        

        while True:
            # Get Model Output for User Input
            user_in = input()
            user_in_prefixed = f'user : {user_in}'
            self.history.append(user_in_prefixed)

            raw_output = sample([user_in_prefixed])[0]

            split_at = raw_output.find('system : ')
            system_response = raw_output[split_at:]
            belief_string = raw_output[:split_at]

            res = "I sorry i did not understand that"
            try:
                for code in belief_string.split(";"):
                    exec(code.strip())
                res = eval("f'" + belief_string.strip() + "'")
            except:
                pass
    

            self.history.append(system_response)

            print(raw_output)
            print(res)

def do_shit(belief_string, system_response, prev={'df': 'sheesh'}):
    ns = Namespace(**prev)

    # print(domains)
    res = "Sorry i nix understando"
    code_blocks = belief_string.split(";")
    code_blocks = [cb.strip() for cb in code_blocks]


    try:
        for cb in code_blocks:
            exec(cb)
        print(ns.df)
        eval_string = system_response.strip()
        print(eval_string)
        res = eval('f"' + eval_string + '"')
    except Exception as e:
        print(e)
        print("Oh boiiii something really bad happened")
    
    return res, locals()


if __name__ == "__main__":
    
    # print(domains)
    # print("sheeeeeeesh")
    x, y = do_shit("ns.df = domains['restaurant']", "give me your wallet {ns.df['name'].iloc[0]}")
    print(x)
    # print(df)
    # chat = Chat()
    # chat.start()