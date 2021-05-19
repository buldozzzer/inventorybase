def prepare_data(item):
    for key_i in item:
        if item[key_i] is not None:
            if key_i != 'components':
                item[key_i] = item[key_i].strip()
            else:
                for component in item['components']:
                    print(component)
                    for key_c in component:
                        if component[key_c] is not None:
                            if key_c == 'id':
                                continue
                            if key_c != 'location':
                                component[key_c] = component[key_c].strip()
                            else:
                                for key_l in component['location']:
                                    component['location'][key_l] = component['location'][key_l].strip()
    return item
