def prepare_data(item):
    for key_i in item:
        if item[key_i] is not None:
            if key_i != 'components':
                item[key_i] = item[key_i].strip()
            else:
                for component in item['components']:
                    for key_c in component:
                        if key_i != 'location':
                            item[key_i] = item[key_c].strip()
                        else:
                            for key_l in component['location']:
                                item[key_i] = item[key_l].strip()
    return item
