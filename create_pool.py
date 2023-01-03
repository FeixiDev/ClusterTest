import action


class CreateStoragePool(object):
    def __init__(self):
        self.lvm_cmd = action.LVM()
        self.linstor_cmd = action.Linstor
    def create_pv(self, device, ssh_conn):
        self.lvm_cmd.create_pv(device, ssh_conn)
    def create_vg(self, device, vg_name, ssh_conn):
        self.lvm_cmd.create_vg(device, vg_name, ssh_conn)
    def create_thin_pool(self, pool_size, pool_name, vg_name, ssh_conn):
        self.lvm_cmd.create_thin_pool(pool_size, pool_name, vg_name, ssh_conn)
    def create_thick_pool(self, node_name, pool_name, vg_name, ssh_conn):
        self.linstor_cmd.create_sp(node_name, pool_name, vg_name, ssh_conn)
