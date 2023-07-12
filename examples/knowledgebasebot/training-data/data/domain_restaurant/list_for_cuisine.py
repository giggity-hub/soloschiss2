def main(domain_sampler, parametrize):
    res = []

    res += parametrize(2, {"cuisine": domain_sampler['restaurant']['cuisine']}, [
    {
        "user": "I want to eat %(cuisine)s food",
        "belief": "df = domains['restaurant'].query('cuisine == \"%(cuisine)s\"') ; names = df['name'].tolist()",
        "system": "Here are some %(cuisine)s restaurants {templates.list(names)}"
    },
    {
        "user": "I'd like to get a %(cuisine)s meal",
        "belief": "df = domains['restaurant'].query('cuisine == \"%(cuisine)s\"') ; names = df['name'].tolist()",
        "system": "These restaurants serve sugondese meals {templates.list(names)}"
    },
    {
        "user": "Where can i get some %(cuisine)s food?",
        "belief": "df = domains['restaurant'].query('cuisine == \"%(cuisine)s\"') ; names = df['name'].tolist()",
        "system": "You can get %(cuisine)s food at these restaurants {templates.list(names)}"
    },
    {
        "user": "I want to eat %(cuisine)s",
        "belief": "df = domains['restaurant'].query('cuisine == \"%(cuisine)s\"') ; names = df['name'].tolist()",
        "system": "Here are some %(cuisine)s restaurants {templates.list(names)}"
    },
    {
        "user": "give me %(cuisine)s restaurants",
        "belief": "df = domains['restaurant'].query('cuisine == \"%(cuisine)s\"') ; names = df['name'].tolist()",
        "system": "Here are %(cuisine)s restaurants {templates.list(names)}"
    },
    {
        "user": "List %(cuisine)s restaurants",
        "belief": "df = domains['restaurant'].query('cuisine == \"%(cuisine)s\"') ; names = df['name'].tolist()",
        "system": "Here is a list of %(cuisine)s restaurants {templates.list(names)}"
    }])

    options = {
        "cuisine1": domain_sampler['restaurant']['cuisine'],
        "cuisine2": domain_sampler['restaurant']['cuisine']
    }

    res += parametrize(2, options, [
    {
        "user": "Do you know any restaurants that are either %(cuisine)s or %(cuisine)s",
        "belief": "df = domains['restaurant'].query('cuisine == \"%(cuisine)s\" | cuisine == \"%(cuisine)s\"') ; names = df['name'].tolist()",
        "system": "Here are restaurants that fit your description {templates.list(names)}"
    },
    {
        "user": "I like %(cuisine)s and %(cuisine)s food",
        "belief": "df = domains['restaurant'].query('cuisine == \"%(cuisine)s\" | cuisine == \"%(cuisine)s\"') ; names = df['name'].tolist()",
        "system": "Then you should like these restaurants {templates.list(names)}"
    },
    {
        "user": "I want food that is  %(cuisine)s or %(cuisine)s",
        "belief": "df = domains['restaurant'].query('cuisine == \"%(cuisine)s\" | cuisine == \"%(cuisine)s\"') ; names = df['name'].tolist()",
        "system": "Then you should like these restaurants {templates.list(names)}"
    }])

    return res
