import myService as ms
import myClass as mc

if __name__ == '__main__':
    param = mc.Param()
    param.path = './PluginsQbit'
    param.url = 'https://github.com/qbittorrent/search-plugins/wiki/Unofficial-search-plugins'

    ms.main(param)
