# coding: utf-8

class Generic(object):

    @staticmethod
    def get_params(template,kwargs):
        for key in kwargs:
            if key in template:
                if isinstance(template[key], (list,dict)):
                    if isinstance(template[key], list) and isinstance(kwargs[key], list):
                        template[key] = []
                        template[key].extend(kwargs[key])
                    elif isinstance(template[key], list) and isinstance(kwargs[key], (int, float,str)):
                        template[key] = []
                        template[key].append(kwargs[key])
                    elif isinstance(template[key], dict) and isinstance(kwargs[key], dict):
                        template[key].clear()
                        template[key].update(kwargs[key])
                    else:
                        raise AssertionError("参数%s值%s错误" %(key,kwargs[key]))
                else:
                    template[key] = kwargs[key]
            else:
                raise AssertionError("参数名不存在!:%s" % key)
        return template