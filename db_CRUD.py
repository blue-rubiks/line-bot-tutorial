from db_model import *


def create_demo(url):
    url_data = UrlData(url=url)
    db.session.add(url_data)
    db.session.commit()
    print('create done')


def read_demo():
    url_data = UrlData.query.all()

    # method_1
    data_dic = {}
    data_list = []
    for data in url_data:
        data_dic['id'] = data.id
        data_dic['url'] = data.url
        data_list.append(data_dic)
        data_dic = {}

    # method_2
    # data_list = [
    #     {
    #         "id": data.id,
    #         "url": data.url,
    #     }
    #     for data in url_data
    # ]
    return data_list


def update_demo(pk, new_url):
    url_data = UrlData.query.filter_by(id=pk).first()
    if url_data:
        url_data.url = new_url
        db.session.add(url_data)
        db.session.commit()
        print('update done')
    else:
        print('data not exist')


def delete_demo(pk):
    url_data = UrlData.query.filter_by(id=pk).first()
    if url_data:
        db.session.delete(url_data)
        db.session.commit()
        print('delete done')
    else:
        print('data not exist')


if __name__ == '__main__':
    # example url
    # https://imgur.com/NQyIaLp.jpg
    # https://imgur.com/EiE7Skk.jpg
    # https://imgur.com/soD0fPm.jpg
    # https://imgur.com/H4x2IkH.jpg
    # https://imgur.com/OTDI0e7.jpg

    all_data = read_demo()
    print('all_data', all_data)

    # create_demo('https://imgur.com/NQyIaLp.jpg')

    # update_demo(1, 'https://imgur.com/EiE7Skk.jpg')

    # delete_demo(2)
    pass
