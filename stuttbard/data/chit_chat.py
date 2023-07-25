def main(parametrize):
    greet = parametrize({
        "belief": "",
        "user_system": [
            ("", "Hello I am Stuttbard. How can i help you?"),
            ("", "My name is Stuttbard. What can i do for you?"),
            ("", "I am Stuttbard. How can i assist you?")
        ]
    })

    inform_domains = parametrize({
        "belief": "domain_keys = domains.keys()",
        "user_system": [
            ("What can i talk to you about?", 
                "I can talk to you about cool things to do in and around Stuttgart, like {templates.list(domain_keys}"),
            ("What can you tell me about Stuttgart?",
                "I can tell you something about these domains {templates.list(domain_keys)}"),
            ("What domains can you inform me about?",
                "I can inform you about the following domains {templates.list(domain_keys)}"),
            ("What is there to do in Stuttgart?",
                "In Stuttgart there are lots of things to do. These are the topics i can tell you about {templates.list(domain_keys)}"),
            ("What is your purpose?",
                "My purpose is to give you information about things in Stuttgart, like {templates.list(domain_keys)}")
        ]
    })

    hello = parametrize({
        "belief": "",
        "user_system": [
            ("Hi", "Hello"),
            ("Hello there", "Hello to you"),
            ("Hello", "Hello")
        ]
    })

    return [*greet, *inform_domains, *hello]