#  Copyright (c) 2023. 秋城落叶, Inc. All Rights Reserved
#  @作者         : 秋城落叶(QiuChenly)
#  @邮件         : qiuchenly@outlook.com
#  @文件         : 项目 [qqmusic] - qq.py
#  @修改时间    : 2023-03-14 02:55:44
#  @上次修改    : 2023/3/14 下午2:55

from flaskSystem.src.Api.QQMusic import QQMusicApi
from flaskSystem.App import app
from flask_caching import Cache

# 配置缓存
app.config['CACHE_TYPE'] = 'simple'  # 使用简单的内存缓存，你可以选择其他后端
cache = Cache(app)

QQApi = QQMusicApi()


@app.get("/qq/search/<searchKey>/<page>/<size>")
def search(searchKey: str, page=1, size=30):
    # 检查前缀
    prefix = searchKey.split(":")

    size = 30 if int(size) > 30 else int(size)  # 这里强制让qq音乐指定为30一页 因为qq服务器现在禁止超过30一页拉取数据
    if len(prefix) == 2:
        # 尝试从缓存中获取数据
        cached_data = cache.get(f'{prefix}')
        if cached_data:
            lst = cached_data
        else:
            command = prefix[0]
            _id = prefix[1]
            # 高级指令
            if command == 'p':
                # 加载歌单
                lst = QQApi.parseQQMusicPlaylist(_id)
            elif command == 'b':
                # 加载专辑
                lst = QQApi.parseQQMusicAlbum(_id)
            elif command == 'id':
                # 指定单曲id
                lst = QQApi.getSingleMusicInfo(_id)
            elif command == 't':
                # 加载排行版
                lst = QQApi.parseQQMusicToplist(_id)
            else:
                lst = {}
            # 将数据存入缓存，有效期为 300 秒
            cache.set(f'{prefix}', lst, timeout=300)
        pages = lst.get('page')
        # 当前
        pages['cur'] = int(page)
        # 下一页 int(size)
        tmp_num = int(int(pages.get('size'))/(int(page)*int(size)))
        pages['next'] = -1 if tmp_num == 0 else int(page) + tmp_num
        lst = QQApi.formatList(lst['data'])
        # 分页获取
        data = lst[(int(page) - 1) * int(size):int(page) * int(size)]
    else:
        lst = QQApi.getQQMusicSearch(searchKey, int(page), int(size))
        pages = lst['page']
        data = QQApi.formatList(lst['data'])

    return {
        'code': 200,
        'list': data,
        'page': pages
    }


def init():
    pass
