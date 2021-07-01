from bson import ObjectId

from . import mongo


def get_items():
    result = []
    collection = mongo.get_conn()['main_item']
    items = collection.find()
    if collection:
        for document in items:
            document['_id'] = str(document['_id'])
            result.append(document)
    return result


def read_file(filename):
    lines = []
    f = open(filename)
    for line in f:
        if line.strip() != "":
            fields = line.split(" ")
            date = fields[2].split("-")
            data = {
                'inventory_n': fields[0][4:],
                'serial_n': fields[1][4:],
                'last_check': date[2] + '-' + date[1] + '-' + date[0],
                'object': fields[3][3:],
                'corpus': fields[4][5:],
                'cabinet': fields[5][4:],
            }
            lines += [data]
    return lines


def get_ids(filename):
    items = get_items()
    lines = read_file(filename)
    accordance = {}
    for item in items:
        accordance[item['_id']] = []
        for line in lines:
            if line['inventory_n'] == item['inventory_n'] and line['serial_n'] == item['serial_n']:
                accordance[item['_id']] += [line]
            else:
                for component in item['components']:
                    if item['inventory_n'] == line['inventory_n'] \
                            and component['serial_n'] == line['serial_n']:
                        accordance[item['_id']] += [line]
    return accordance


def prep_data(filename):
    accordance = get_ids(filename)
    items = get_items()
    for _id in accordance:
        for item in items:
            if _id != item['_id']:
                continue
            else:
                for line in accordance[_id]:
                    if item['inventory_n'] == line['inventory_n'] \
                            and item['serial_n'] == line['serial_n']:
                        item['last_check'] = line['last_check']
                        item['location_object'] = line['object']
                        item['location_corpus'] = line['corpus']
                        item['location_cabinet'] = line['cabinet']
                    else:
                        for component in item['components']:
                            if item['inventory_n'] == line['inventory_n'] \
                                    and component['serial_n'] == line['serial_n']:
                                item['last_check'] = line['last_check']
                                component['location']['object'] = line['object']
                                component['location']['corpus'] = line['corpus']
                                component['location']['cabinet'] = line['cabinet']
    return items


def update(filename):
    collection = mongo.get_conn()['main_item']
    if collection:
        items = prep_data(filename)
        for item in items:
            collection.update_one({
            "_id": ObjectId(item.pop('_id'))
            }, {
            "$set": item
            }, upsert=False)
    return True
