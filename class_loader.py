def get_class_dict():
    cls_dict = {}
    with open("classes.txt") as cls_file:
        for i, cls in enumerate(cls_file):
            cls_dict[i] = cls.strip()
    return cls_dict

cls_names = get_class_dict()

