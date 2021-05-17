def prepare_data(item):
    for key_i in item:
        if key_i != 'components':
            str(item[key_i]).strip()
        else:
            for component in item['components']:
                for key_c in component:
                    if key_i != 'location':
                        str(item[key_c]).strip()
                    else:
                        for key_l in component['location']:
                            str(item[key_l]).strip()
    return item
