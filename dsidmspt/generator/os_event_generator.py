from dsidmspt.utils import common


class OSEventGenerator(object):
    def __init__(self):
        self.src = common.url_join(common.TEMPLATE_DIR, 'os_event')
        self.schema = {}
        self.load_schema_from_folder(self.src)

    def load_schema_from_folder(self, src):
        files = common.get_files_in_dir(src)
        for file in files:
            self.schema[file] = common.load_file_as_dict(
                common.url_join(src, file))

    def generate_uuid(self):
        return common.generat_uuid()

    def generate_data(self,
                      user_num,
                      project_per_user,
                      instance_per_project,
                      event_type):
        data = []
        for user in range(0, user_num):
            item = common.deepcopy(self.schema[event_type])
            item['']
            for project in range(0, project_per_user):
                for instance in range(0, instance_per_project):


osevent = OSEventGenerator()
print(osevent.schema)
