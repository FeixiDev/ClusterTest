import action

class CreateResource(object):
    def __init__(self):
        self.linstor_cmd = action.Linstor

    def create_diskful(self, resource_name, resource_size, host_name, pool_name, ssh_conn):
        self.linstor_cmd.create_rd(resource_name, ssh_conn)
        self.linstor_cmd.create_vd(resource_name, resource_size, ssh_conn)
        self.linstor_cmd.create_diskful_resource(host_name, resource_name, pool_name, ssh_conn)

    def create_diskless(self, resource_name, resource_size, host_name, ssh_conn):
        self.linstor_cmd.create_rd(resource_name, ssh_conn)
        self.linstor_cmd.create_vd(resource_name, resource_size, ssh_conn)
        self.linstor_cmd.create_diskless_resource(host_name, resource_name, ssh_conn)
