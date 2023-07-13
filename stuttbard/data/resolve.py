def main(domain_sampler, parametrize):
    repeat_mention_name = parametrize({
        "belief": "row = df.query('name == \"%(name)s\"').iloc[0] ; response = repeat_response(row)",
        "samplers": {"name": domain_sampler['name']},
        "user_system": [
            ("and what about the %(name)s?", "{response}"),
            ("How is that for the %(name)s?", "{response}"),
            ("What about the %(name)s?", "{response}")
        ]
    })

    repeat_mention_index = parametrize({
        "belief": "row = df.iloc[%(index_int)s] ; response = repeat_response(row)",
        "samplers": {"index_str, index_int": domain_sampler['index']},
        "user_system": [
            ("Does that also hold for the %(index_str)s one?", "{response}"),
            ("and the %(index_str)s one?", "{response}"),
            ("How about the %(index_str)s of them?", "{response}")
        ]
    })

    return [*repeat_mention_name, *repeat_mention_index]